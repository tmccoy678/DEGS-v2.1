# DEGS historical core backport

**The historical gate now preserves nested boolean/number distinctions.** Read [the executable correction and exact scope](docs/v1-core-backport.md). This branch retains the standalone draft packaging below; it does not claim to reconstruct the complete historical system v1 release.

# DEGS — v2.1 development draft

DEGS evaluates engineering task records and explains whether their recorded evidence satisfies its rules. Missing recovery evidence or an agent's claimed human approval can block a task. A passing result does not prove the evidence true, approve the work, or execute it.

**Private development draft. No versioned public release.** This copy preserves the current standalone gate and adds a small, Sashiko-derived Python review-data component. It does not activate governance on your computer.

## Try the gate

Use an Apple-silicon Mac with Python 3.9 or later. Python 3.9.6 on macOS 26.6.2 was tested. No pip packages are needed for the gate or Python tests. Private repository access is currently required; run these commands from this checkout's root.

```sh
python3 -B bin/engineering-gate.py evaluate fixtures/tier2-complete-pass.json --json
python3 -B bin/engineering-gate.py evaluate fixtures/tier2-missing-rollback-blocked.json --json
python3 -B bin/engineering-gate.py evaluate fixtures/tier3-agent-self-approval-blocked.json --json
```

The examples are synthetic records. Their approval and evidence fields are examples, not authorization for real work.

| Example | Expected and observed | What it demonstrates |
| --- | --- | --- |
| Complete Tier 2 record | `PASS`, exit 0 | The supplied record meets the evaluated requirements. |
| Missing rollback evidence | `BLOCKED`, exit 2; `DEGS-CFG-004` | Recovery evidence is required for this task. |
| Agent self-approval | `BLOCKED`, exit 2; `DEGS-RISK-003` | An agent's claim does not satisfy the human-approval requirement. |

Each result lists the unmet fields and rule IDs. A blocked example is a successful demonstration when blocking is the expected result. Invalid JSON is a separate input failure (`FAIL`, exit 4), covered by the test suite.

## Try the Sashiko-derived component

```sh
python3 -B -m sashiko_derived.demo
```

This demonstration preserves a supplied concern and a supplied dismissed concern in separate collections, with the producing stage attached. It performs no LLM investigation and makes no decision about which claim is true. The later collections remain empty because deduplication, conflict resolution, and verification have not run.

The Python port retains Sashiko's selected state names, independent list defaults, deep-copy behavior, and stage stamping. Its object adapter distinguishes omitted arrays from explicit null. The original deduplication and conflict-resolution prompts are included as **unmodified reference text**, not an operating review service. See [source provenance](provenance/sashiko-source.json), [port boundaries](docs/port-boundaries.md), and [credits](THIRD_PARTY_NOTICES.md).

## Understand the tests

```sh
python3 -B -m unittest discover -s tests -v
```

The recorded run passed **64 tests**: 58 existing gate tests and 6 port tests. The tests exercise ordinary command input, valid and invalid records, required evidence, approval boundaries, and Python value semantics. A separate comparison passed **331 cases** against an executable harness containing the selected upstream Rust source. Instructions, raw outputs, source hashes, and exact environment are in [the test report](docs/test-report.md).

These results concern the recorded scenarios. They do not establish defect freedom, semantic truth, AI review accuracy, security certification, full-system integration, or support for other platforms. The copied core is identified in [the baseline manifest](provenance/degs-baseline.json). Local activation history, private audits, context-skill integration, and the Workbench adapter are excluded, along with tests requiring those dependencies. The core's existing rules are unchanged.

## Purpose, credit, and help

The goal is rigorous, understandable evidence with a clear explanation when something needs attention. Taylor welcomes questions, corrections, and suggestions and will respond as quickly as possible; no response-time guarantee is promised. Use this private repository's issues for non-sensitive questions. Follow [SECURITY.md](SECURITY.md) for vulnerability reports.

Muchun Song introduced Sashiko's dismissed-concern collection and concern/dismissed-concern conflict resolution. The implementation also credits the Sashiko contributors and Chris Mason's separate review-prompts foundation. [Exact contributions and licensing](THIRD_PARTY_NOTICES.md) distinguish those roles. [Citations](CITATIONS.md) explain the source and software-engineering literature behind the reporting format.

Existing DEGS material retains [MIT](LICENSE). Sashiko-derived files and reference prompts retain [Apache-2.0](LICENSES/Apache-2.0.txt), with notices and modifications identified separately. This is not a claim that every file has become Apache-2.0. Public v2.1 licensing, packaging, installation, and release acceptance remain unfinished.
