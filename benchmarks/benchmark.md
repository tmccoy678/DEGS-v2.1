# DEGS schema-helper benchmark

**241 of 241 cases matched. Zero false acceptances, false rejections, exceptions, or timeouts. Controls passed.**

This measures the existing schema helper against independently labeled JSON Schema examples. It does not measure the full DEGS gate, authority decisions, security effectiveness, or full draft2020-12 compliance.

The original run exposed one recursive JSON-equality defect across 14 cases: Python container equality accepted nested booleans as numbers. The corrected comparator rejects all 14 examples while preserving numerical equivalence such as 1 and 1.0, object member ordering independence, and array ordering. The original 227/241 result is retained unchanged; this is a new observation of corrected source. No canonical task authority bypass was demonstrated. All 14 fixture CLI invocations retain identical exits and diagnostics.

Selection was frozen before execution: 69 groups across 15 complete upstream files, comprising 107 valid and 134 invalid cases. Results: 107/107 valid cases correctly accepted; 134/134 invalid cases correctly rejected. Another 273 cases in those files were excluded for unsupported schema syntax. Other files and optional directories were outside scope; their inventory is recorded in the raw report. An omitted case is not a pass. See the [selection rationale](selection.md) for exact group indices and limitations.

## Reproduce on Apple silicon

From this repository root, with Python 3:

```bash
python3 -B benchmarks/run_benchmark.py --output benchmarks/results/rerun.json
python3 -B -m unittest discover -s benchmarks -p 'test_*.py' -v
```

Exit 0 is expected for the corrected candidate when all selected cases and controls pass. The original candidate exited 1 for fourteen failures and wrote a complete report. Harness exit 1 indicates measured mismatches or failed controls; exit 2 indicates input/configuration error. A failed control invalidates interpretation of the corpus score. Each candidate process has a five-second timeout. There are no automatic retries. Corpus and selection integrity must pass before scoring. The fixed selection manifest is hashed in the harness; changing it creates a new benchmark version and must be disclosed.

Recorded host: macOS 26.6.2, arm64, Python 3.9.6. Corrected run started 2026-09-11T20:04:22.516567+00:00 and ended 2026-09-11T20:04:29.978398+00:00. Other platforms were not tested. This is an observed result for these exact source bytes, not a performance leaderboard or certification.

## Inspect the evidence

- [Corrected machine-readable run](results/apple-silicon-v2.json): all case outcomes, stdout/stderr, exits, controls, identities, and environment.
- [Original observation, preserved unchanged](results/apple-silicon.json). Its command field was a hard-coded recipe; the new run records actual script arguments and interpreter state.
- [Before/after comparison](results/measurement-comparison.json): exact changed outcomes and run hashes.
- [Current tests and limitations](../docs/benchmark-correction.md).
- [Pinned input manifest](manifest.json): upstream commit and exact input SHA-256 hashes.
- [Selection and research](selection.md): source fit, exclusions, and license inspection.
- [Full upstream MIT notice](data/LICENSE): retained unchanged with the copied data.
- [Original APA reference collection](../references/dobeworks-apa-references.pdf): unchanged; benchmark sources supplement it.

Source: [json-schema-org/JSON-Schema-Test-Suite at the pinned commit](https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/f6fd52a0a95472e079cbfc6ef7f089702b80e045). Credit Julian Berman and JSON Schema Test Suite contributors. No endorsement is implied. Only selected data files and the license were copied; the report distinguishes local controls from public inputs. Repositories remain private drafts.

## Originally failed cases, now corrected

| Case ID (file:group:test) | Upstream expectation | Original result | Corrected result |
| --- | --- | --- | --- |
| `enum.json:6:1` | Invalid | Accepted | Rejected |
| `enum.json:6:2` | Invalid | Accepted | Rejected |
| `enum.json:8:1` | Invalid | Accepted | Rejected |
| `enum.json:8:2` | Invalid | Accepted | Rejected |
| `enum.json:10:0` | Invalid | Accepted | Rejected |
| `enum.json:12:0` | Invalid | Accepted | Rejected |
| `const.json:6:1` | Invalid | Accepted | Rejected |
| `const.json:6:2` | Invalid | Accepted | Rejected |
| `const.json:7:1` | Invalid | Accepted | Rejected |
| `const.json:7:2` | Invalid | Accepted | Rejected |
| `const.json:8:1` | Invalid | Accepted | Rejected |
| `const.json:8:2` | Invalid | Accepted | Rejected |
| `const.json:9:1` | Invalid | Accepted | Rejected |
| `const.json:9:2` | Invalid | Accepted | Rejected |

[Evidence contract and change controls](evidence.md).

Timeouts retain partial stdout and stderr. Stale controls require literal STALE freshness. Invocation provenance records executable, script arguments, working directory, and effective interpreter flags; original interpreter arguments are unavailable on Python 3.9. Corpus inputs and denominators are unchanged.
