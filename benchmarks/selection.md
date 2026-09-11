# Public-data benchmark selection for current DW/DEGS

Date: 2026-09-11. Research and corpus inventory only; no benchmark implementation or execution. Public datasets do not authorize publication of project code or results. The project copies remain private unless Taylor authorizes otherwise.

## Recommended achievable benchmark

Use two separately reported, narrow evaluations:

1. **DEGS schema-keyword interoperability:** the existing custom JSON Schema helper against a predeclared subset of official JSON Schema Test Suite draft2020-12 examples. Upstream `valid` booleans supply independent expected outcomes.
2. **DobeWorks Observer rejection robustness:** all 318 JSONTestSuite parsing files through the actual Observer CLI, checking that inputs outside the Observer snapshot contract never produce usable telemetry. Native fresh/stale controls prevent an implementation that rejects everything from appearing correct.

Neither is a benchmark of general intelligence, vulnerability discovery, comprehensive governance quality, or source-code repair. The inspected software evaluates JSON evidence records and synthetic boundaries. A source-derived concern accumulator without an LLM review engine cannot honestly receive a Sashiko bug-finding score.

## DEGS: exact public source and license

Repository: [JSON Schema Test Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite). Pinned commit: [`f6fd52a0a95472e079cbfc6ef7f089702b80e045`](https://github.com/json-schema-org/JSON-Schema-Test-Suite/commit/f6fd52a0a95472e079cbfc6ef7f089702b80e045). [Immutable download](https://api.github.com/repos/json-schema-org/JSON-Schema-Test-Suite/tarball/f6fd52a0a95472e079cbfc6ef7f089702b80e045).

The inspected [pinned LICENSE](https://github.com/json-schema-org/JSON-Schema-Test-Suite/blob/f6fd52a0a95472e079cbfc6ef7f089702b80e045/LICENSE) is MIT, Copyright (c) 2012 Julian Berman. Preserve its copyright and complete permission notice with redistributed corpus material. LICENSE SHA-256: `837402bd25fad9b704265801ca3f92566a98157c1f9a7acd6f446299ba1c305a`. Credit the JSON Schema Test Suite contributors as the source of examples; do not imply they endorse DW/DEGS.

The [upstream README](https://github.com/json-schema-org/JSON-Schema-Test-Suite/blob/f6fd52a0a95472e079cbfc6ef7f089702b80e045/README.md) defines groups containing a schema and examples containing data and expected validity. It explicitly targets specification behavior, with versioned directories. Crashes or errors do not count as implementing an example correctly. The suite has its own stated coverage limits. Use draft2020-12 because the inspected canonical task schema declares that dialect, not because it produces a better score.

### Actual interface and restrictions

Inspected `engineering-gate.py` implements `json_schema_errors(value, schema, root_schema)`. Its docstring scopes it to keywords used by the canonical task schema. A benchmark adapter may call this existing helper with upstream data and schema, preserving the implementation bytes; this measures the helper, not the whole CLI. The CLI validates one fixed task schema and does not expose a general arbitrary-schema interface.

The source currently recognizes object/array/string/boolean/null types; const/enum; minLength; Python regular-expression patterns; minItems; object-form items; required/properties; additionalProperties false; allOf/oneOf; object-form not; an if/then path; and limited local JSON pointers. It does not implement full 2020-12. Unsupported or materially different features include numeric type validation, boolean schemas, anyOf, else, numeric bounds, maxLength/maxItems, patternProperties, schema-valued additionalProperties, prefixItems, contains, unevaluated keywords, dynamic/remote references, and full URI/anchor processing. `$ref` returns early, so sibling validation is not general 2020-12 behavior.

### Predeclared first subset: 241 examples

Selection below was made from schema syntax and implementation scope before any benchmark run. Preserve **every** example within the selected group, including cases expected to expose faults. Group numbers are zero-based indices in the pinned JSON file. Never remove an example because it fails. Exact descriptions and schema hashes should be emitted in the eventual machine-readable run manifest.

All paths below are under [`tests/draft2020-12/`](https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/f6fd52a0a95472e079cbfc6ef7f089702b80e045/tests/draft2020-12).

| File | Group indices | Examples | Upstream valid | Upstream invalid |
| --- | --- | ---: | ---: | ---: |
| type.json | 2,3,4,5,6,8,9,10 | 55 | 14 | 41 |
| minLength.json | all | 7 | 4 | 3 |
| minItems.json | all | 6 | 4 | 2 |
| required.json | all | 18 | 12 | 6 |
| enum.json | all | 53 | 23 | 30 |
| const.json | all | 54 | 22 | 32 |
| pattern.json | 0,1 | 9 | 8 | 1 |
| additionalProperties.json | 4 | 1 | 1 | 0 |
| properties.json | 4 | 1 | 1 | 0 |
| allOf.json | 6,7,10 | 4 | 3 | 1 |
| oneOf.json | 8,10 | 6 | 3 | 3 |
| not.json | 2,3,4,7 | 15 | 4 | 11 |
| if-then-else.json | 0,1 | 4 | 4 | 0 |
| ref.json | 7,8,14 | 7 | 3 | 4 |
| items.json | 9 | 1 | 1 | 0 |
| **Total** | **69 groups** | **241** | **107** | **134** |

There are 514 examples in these 15 complete upstream files: 241 selected and 273 outside this first subset. This is not a denominator for the entire upstream suite; other files and optional directories remain outside scope. Record their omission explicitly rather than calling them passed. Include the inventory beside any headline score.

Reasons for exclusions are structural: numeric types, unsupported keywords, boolean schema nodes, full reference-resolution requirements, or Python/ECMAScript regular-expression differences. The basic pattern groups use `^a*$` and `a+`; the Unicode-property-escape group is excluded because Python `re` does not implement that syntax. This does not establish general regex interoperability.

Some groups cover only narrow paths: the if/then selections check orphan-keyword behavior, the additionalProperties selection checks the default, and the items selection checks null elements. Do not advertise these as comprehensive coverage of those keywords. Native DEGS fixtures separately exercise the actual canonical combinations.

Keep numeric and nested-boolean const/enum examples. The source's equality helper distinguishes booleans at the top level but delegates nested equality to Python; this is an inspection-based reason to expect potentially useful failures, not permission to delete those examples. Report actual outcomes rather than predicting a perfect score.

### Scoring and controls

For each selected example, compare `not errors` with upstream `valid`. Report matched valid and matched invalid cases separately, false acceptance, false rejection, exceptions, timeouts, and total selected. Crashes/timeouts stay in the 241 denominator and are never converted into correct rejection. A useful result is an exact outcome list with file/group/test identifiers, not only a percentage.

Retain candidate/source hashes and upstream commit, the immutable selection, command, Python version, macOS version, architecture, run timestamp, stdout/stderr, and any limitations. Verify the adapter forwards inputs unchanged and interprets results correctly using known-valid and known-invalid controls. Keep fixture-based DEGS governance checks as a separate result; they are locally authored, not independent public benchmark labels.

## DobeWorks: exact public corpus and license

Repository: [Nicolas Seriot's JSONTestSuite](https://github.com/nst/JSONTestSuite). Pinned commit: [`1ef36fa01286573e846ac449e8683f8833c5b26a`](https://github.com/nst/JSONTestSuite/commit/1ef36fa01286573e846ac449e8683f8833c5b26a). [Immutable download](https://api.github.com/repos/nst/JSONTestSuite/tarball/1ef36fa01286573e846ac449e8683f8833c5b26a).

The inspected [LICENSE](https://github.com/nst/JSONTestSuite/blob/1ef36fa01286573e846ac449e8683f8833c5b26a/LICENSE) is MIT, Copyright (c) 2016 Nicolas Seriot. Preserve the full notice with reused data. LICENSE SHA-256: `8bd0e0578be788c617ea01d18b2a8146e3746ae50bddadc65a5f9d3aad08ad49`. Import the test data and license rather than bundling unrelated parser implementations, each of which may have additional licenses.

The [README](https://github.com/nst/JSONTestSuite/blob/1ef36fa01286573e846ac449e8683f8833c5b26a/README.md) defines `y_` as parser acceptance required, `n_` as rejection required, and `i_` as implementation-dependent. The pinned `test_parsing` directory has **318 files: 95 y_, 188 n_, 35 i_**, totaling 354,024 bytes. These are corpus counts, not successful execution results.

### Application-boundary oracle

The `observer_core.py` requires its own snapshot schema and exact policy. Inventory confirms none of the 318 files contains the Observer snapshot schema marker. Therefore the independently specified application property is: none may become validated, decision-usable telemetry.

Drive the actual CLI using the corpus file unchanged as `--snapshot`, a verified native policy, a bounded disposable input root, and a fixed `--now`. Report corpus groups separately. The public files are untrusted input data; do not execute anything contained in them.

The source deliberately permits schema-incompatible objects to return structured `UNKNOWN` with exit 0. Its controlled exceptions return structured `ERROR` with exit 2. Thus do not require all corpus files to return exit 2. Require one of those documented unavailable/error outcomes, no usable signals, consistent exit status, and parseable expected result structure. A traceback, crash, timeout, missing output, unexpected status, validated telemetry, or non-UNKNOWN signals is a failed robustness case.

For structured UNKNOWN results, verify all six signal values are UNKNOWN and the result marks schema incompatibility. For ERROR results, ensure an error code is present and no usable telemetry is emitted. Parser labels are descriptive strata, not the Observer's acceptance oracle: rejecting a syntactically valid `y_` array can be correct for an object-only application. Report this as **application rejection robustness**, never RFC 8259 conformance.

Run the native fresh snapshot control, which must produce expected validated values, and a stale-time control, which must suppress usable signals. Report these controls separately from the 318 public inputs. If fresh control fails, reject the benchmark run as invalid rather than rewarding an implementation that rejects everything. Snapshot freshness and field checking exercise DobeWorks application logic; raw malformed-input outcomes also reflect Python's parser. None measures Worker behavior automatically.

## Why not Juliet, SARD, or a repair leaderboard today

NIST describes Juliet as synthetic C/C++ and Java programs with known flaws for testing static analyzers. Its [C/C++ 1.3 suite record](https://samate.nist.gov/SARD/test-suites/112) identifies public-domain treatment under United States law and CC0 for applicable foreign rights, with NSA Center for Assured Software attribution. [NIST paper on the suite](https://www.nist.gov/publications/juliet-11-cc-and-java-test-suite)

These are valuable when the tested system actually analyzes that source and produces discriminating findings. The present gate and synthetic Observer do not. Feeding a file name or prewritten finding into a JSON record would evaluate record handling, not independent discovery of the labeled flaw. SARD is a collection containing many separately contributed suites; do not generalize one suite's license to all SARD data. No Juliet download or execution is necessary for the selected benchmark.

The same scope objection applies to claiming a SWE-bench repair score or CVE detection score: a task-evidence validator and concern collector are not a repair agent or implemented code-review engine. Benchmark the capability that exists and preserve stronger evaluation for an implemented future subsystem.

## Selection provenance
This selection was recorded on 2026-09-11 before the candidate benchmarks executed. The result reports are separate artifacts. Source archives were inspected as data; no third-party build or parser implementation was executed.
