"""Command-level acceptance tests for the public-data benchmark."""
import ast
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent


class BenchmarkTests(unittest.TestCase):
    def test_all_predeclared_cases_are_measured_with_independent_labels(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'report.json'
            run = subprocess.run([sys.executable, '-B', str(HERE / 'run_benchmark.py'),
                                  '--output', str(output)], capture_output=True, timeout=120)
            self.assertEqual(run.returncode, 0, run.stderr)
            report = json.loads(output.read_text())
            self.assertEqual(report['invocation']['argv'],
                             [str(HERE / 'run_benchmark.py'), '--output', str(output)])
            self.assertEqual(report['invocation']['working_directory'], str(Path.cwd()))
            self.assertEqual(report['invocation']['executable'], sys.executable)
            self.assertTrue(report['invocation']['dont_write_bytecode'])
            self.assertEqual(report['selected'], 241)
            self.assertEqual(len(report['cases']), 241)
            self.assertEqual(report['excluded_in_vendored_files'], 273)
            self.assertEqual(sum(c['expected_valid'] for c in report['cases']), 107)
            self.assertTrue(report['controls_passed'])
            self.assertEqual(report['passed'] + report['failed'], 241)
            self.assertEqual(run.returncode, int(report['failed'] != 0))


    def test_corpus_drift_is_an_input_error_without_a_score(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(HERE, root / 'benchmarks')
            source = next((root / 'benchmarks/data').glob('*.json'))
            source.write_bytes(source.read_bytes() + b' ')
            output = root / 'benchmarks/results/report.json'
            run = subprocess.run([sys.executable, '-B', str(root / 'benchmarks/run_benchmark.py'),
                                  '--output', str(output)], capture_output=True, timeout=10)
            self.assertEqual(run.returncode, 2)
            self.assertIn(b'SHA-256 mismatch', run.stderr)
            self.assertFalse(output.exists())

    def test_selection_manifest_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(HERE, root / 'benchmarks')
            manifest = root / 'benchmarks/manifest.json'
            manifest.write_text(manifest.read_text() + ' ')
            run = subprocess.run([sys.executable, '-B', str(root / 'benchmarks/run_benchmark.py'),
                                  '--output', str(root / 'report.json')], capture_output=True, timeout=10)
            self.assertEqual(run.returncode, 2)
            self.assertIn(b'manifest SHA-256 mismatch', run.stderr)

    def test_degenerate_and_broken_candidates_cannot_earn_success(self):
        candidates = [('def json_schema_errors(data, schema, root):\n    return []\n', 107, 134, False), ('raise RuntimeError("candidate crash")\n', 0, 241, False)]
        for source, passed, failed, controls_passed in candidates:
            with self.subTest(source=source), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                shutil.copytree(HERE, root / 'benchmarks')
                candidate = root / 'bin/engineering-gate.py'
                candidate.parent.mkdir(parents=True, exist_ok=True)
                candidate.write_text(source)
                output = root / 'benchmarks/results/report.json'
                run = subprocess.run([sys.executable, '-B', str(root / 'benchmarks/run_benchmark.py'),
                                      '--output', str(output)], capture_output=True, timeout=120)
                self.assertEqual(run.returncode, 1, run.stderr)
                report = json.loads(output.read_text())
                self.assertEqual(report['passed'], passed)
                self.assertEqual(report['failed'], failed)
                self.assertEqual(report['controls_passed'], controls_passed)

    def test_one_timeout_remains_a_failed_case_in_the_denominator(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(HERE, root / 'benchmarks')
            candidate = root / 'bin/engineering-gate.py'
            candidate.parent.mkdir(parents=True, exist_ok=True)
            original = HERE.parent / 'bin/engineering-gate.py'
            source = original.read_text()
            tree = ast.parse(source)
            insertion = max((node.end_lineno for node in tree.body
                             if isinstance(node, ast.ImportFrom) and node.module == '__future__'), default=0)
            lines = source.splitlines(keepends=True)
            probe = ("import pathlib, time, sys\n"
                     "_counter = pathlib.Path(__file__).with_name('test-process-count')\n"
                     "_count = int(_counter.read_text()) if _counter.exists() else 0\n"
                     "_counter.write_text(str(_count + 1))\n"
                     "if _count == 2:\n"
                     "    print('partial stdout', flush=True)\n"
                     "    print('partial stderr', file=sys.stderr, flush=True)\n"
                     "    time.sleep(6)\n")
            candidate.write_text(''.join(lines[:insertion]) + probe + ''.join(lines[insertion:]))
            output = root / 'benchmarks/results/report.json'
            run = subprocess.run([sys.executable, '-B', str(root / 'benchmarks/run_benchmark.py'),
                                  '--output', str(output)], capture_output=True, timeout=120)
            self.assertEqual(run.returncode, 1, run.stderr)
            report = json.loads(output.read_text())
            timed_out = [c for c in report['cases'] if c['execution'] == 'timeout']
            self.assertEqual(len(timed_out), 1)
            self.assertFalse(timed_out[0]['passed'])
            self.assertEqual(timed_out[0]['stdout'], 'partial stdout\n')
            self.assertEqual(timed_out[0]['stderr'], 'partial stderr\n')
            self.assertEqual(report['passed'] + report['failed'], report['selected'])
            self.assertTrue(report['controls_passed'])

if __name__ == '__main__':
    unittest.main()
