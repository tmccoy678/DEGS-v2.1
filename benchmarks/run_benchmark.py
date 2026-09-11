#!/usr/bin/env python3
"""Measure a fixed public JSON Schema subset against the DEGS helper."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CANDIDATE = ROOT / 'bin/engineering-gate.py'
MANIFEST_SHA256 = '00b74200d8fe5dedf994fd036110e63bfd75493d6d0ee49b21463147ce7a74fe'
TIMEOUT_SECONDS = 5


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_manifest():
    if digest(HERE / 'manifest.json') != MANIFEST_SHA256:
        raise ValueError('manifest SHA-256 mismatch')
    manifest = json.loads((HERE / 'manifest.json').read_text())
    actual = {p.name: digest(p) for p in (HERE / 'data').iterdir() if p.is_file()}
    if actual != manifest['files']:
        raise ValueError('corpus file inventory or SHA-256 mismatch')
    return manifest


def helper():
    spec = importlib.util.spec_from_file_location('engineering_gate', CANDIDATE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.json_schema_errors


def worker(case):
    validate = helper()
    if case == 'controls':
        results = [not validate('yes', {'type': 'string'}, {'type': 'string'}),
                   not validate(False, {'type': 'string'}, {'type': 'string'})]
        print(json.dumps({'valid': results == [True, False]}))
        return
    filename, group_index, test_index = case.split(':')
    group = json.loads((HERE / 'data' / filename).read_text())[int(group_index)]
    test = group['tests'][int(test_index)]
    errors = validate(test['data'], group['schema'], group['schema'])
    print(json.dumps({'valid': not errors, 'errors': errors}, ensure_ascii=True))


def invoke(case):
    command = [sys.executable, '-B', str(Path(__file__).resolve()), '--case', case]
    try:
        result = subprocess.run(command, capture_output=True, timeout=TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired as error:
        return {'execution': 'timeout', 'exit_code': None,
                'stdout': (error.stdout or b'').decode('utf-8', errors='replace'),
                'stderr': (error.stderr or b'').decode('utf-8', errors='replace')}
    record = {'execution': 'error', 'exit_code': result.returncode,
              'stdout': result.stdout.decode('utf-8', errors='replace'),
              'stderr': result.stderr.decode('utf-8', errors='replace')}
    if result.returncode != 0 or result.stderr:
        return record
    try:
        parsed = json.loads(result.stdout)
        if not isinstance(parsed, dict) or type(parsed.get('valid')) is not bool:
            return record
    except (ValueError, UnicodeError):
        return record
    record.update(execution='completed', actual_valid=parsed['valid'])
    return record


def inventory(manifest):
    selected, excluded = [], []
    for filename, indices in manifest['selection'].items():
        groups = json.loads((HERE / 'data' / filename).read_text())
        for gi, group in enumerate(groups):
            included = indices == 'all' or gi in indices
            for ti, test in enumerate(group['tests']):
                case = {'id': f'{filename}:{gi}:{ti}', 'group': group['description'],
                        'description': test['description'], 'expected_valid': test['valid'],
                        'schema_sha256': hashlib.sha256(json.dumps(group['schema'], sort_keys=True).encode()).hexdigest()}
                if not included:
                    case['reason'] = 'outside predeclared supported-syntax group selection; see selection.md'
                (selected if included else excluded).append(case)
    if len(selected) != 241 or len(excluded) != 273:
        raise ValueError('predeclared inventory count differs')
    return selected, excluded


def measure(manifest):
    cases, excluded = inventory(manifest)
    started = datetime.now(timezone.utc).isoformat()
    candidate_hash = digest(CANDIDATE)
    control = invoke('controls')
    for case in cases:
        result = invoke(case['id'])
        case.update(result)
        case['passed'] = (result['execution'] == 'completed' and
                          result['actual_valid'] == case['expected_valid'])
        case['outcome'] = ('match' if case['passed'] else result['execution'] if
                           result['execution'] != 'completed' else
                           'false_acceptance' if result['actual_valid'] else 'false_rejection')
    if digest(CANDIDATE) != candidate_hash:
        raise ValueError('candidate changed during measurement')
    return {'benchmark': 'degs-schema-subset-v1', 'started_at': started,
            'ended_at': datetime.now(timezone.utc).isoformat(),
            'python': platform.python_version(), 'macos': platform.mac_ver()[0],
            'architecture': platform.machine(), 'timeout_seconds_per_case': TIMEOUT_SECONDS,
            'invocation': {'executable': sys.executable, 'argv': sys.argv[:],
                           'working_directory': str(Path.cwd()),
                           'dont_write_bytecode': sys.dont_write_bytecode,
                           'interpreter_flags': str(sys.flags),
                           'original_argv': getattr(sys, 'orig_argv', None),
                           'note': 'argv records script arguments exactly; original interpreter argv is unavailable on Python 3.9'},
            'candidate_sha256': candidate_hash, 'harness_sha256': digest(Path(__file__)),
            'manifest_sha256': digest(HERE / 'manifest.json'), 'upstream_commit': manifest['commit'],
            'selected': len(cases), 'excluded_in_vendored_files': len(excluded),
            'excluded': excluded, 'outside_files': manifest['outside_files'],
            'outside_optional_directories': manifest['outside_optional_directories'],
            'controls': control, 'controls_passed': control.get('actual_valid') is True,
            'passed': sum(c['passed'] for c in cases), 'failed': sum(not c['passed'] for c in cases),
            'outcomes': dict(Counter(c['outcome'] for c in cases)), 'cases': cases}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--case', help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        if args.case:
            worker(args.case)
            return 0
        if args.output is None:
            parser.error('--output is required')
        manifest = checked_manifest()
        report = measure(manifest)
        checked_manifest()
        output = args.output.resolve()
        if ROOT in output.parents and HERE / 'results' not in output.parents:
            raise ValueError('repository output must be inside benchmarks/results')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=True) + '\n')
        print(json.dumps({k: report[k] for k in ('selected', 'passed', 'failed', 'controls_passed')}))
        return int(report['failed'] != 0 or not report['controls_passed'])
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({'status': 'ERROR', 'message': str(error)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
