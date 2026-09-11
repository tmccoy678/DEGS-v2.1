# Benchmark evidence record

- **Evidence ID:** draftdegs-public-benchmark-v1
- **Requirement/fault IDs:** Spec user stories 1–16; DEGS-NESTED-EQUALITY-001
- **Claim under test:** degs-schema-subset-v1
- **Acceptance method:** Pinned public-data execution and native controls
- **Exact source/configuration/role/device-safe identity/environment/target:** Pinned corpus and source/harness digests in results/apple-silicon.json; Apple silicon arm64, macOS 26.6.2, Python 3.9.6
- **Procedure or command identity:** python3 -B benchmarks/run_benchmark.py --output benchmarks/results/apple-silicon.json
- **Start time:** 2026-09-11T19:29:03.702631+00:00
- **End time:** 2026-09-11T19:29:11.157000+00:00
- **Clock-quality basis:** Host wall clock; UTC timestamps, independent synchronization not verified
- **Expected result:** Every selected case matches its stated oracle; controls pass
- **Actual result:** 227/241 cases matched; 14 mismatches; controls passed: True
- **Status:** FAIL
- **Discrepancy references:** DEGS-NESTED-EQUALITY-001; benchmark.md case table
- **Artifact paths:** benchmarks/results/apple-silicon.json; benchmarks/manifest.json
- **Cryptographic identities:** Exact hashes in the raw run and manifest; raw run SHA-256 2f0ab57eaa64d9172880ca05338d2bbc19aa906d7cae45288e34939b489e8e0f
- **Evidence owner:** Taylor; Codex prepared the measurement
- **Human/physical action owner:** Taylor retains release and acceptance decisions
- **Confidentiality classification:** Public-source test data and synthetic controls in a private draft
- **Recoverability classification:** Reproducible from pinned data; previous main commits retained
- **Limitations:** Narrow component benchmark; unsupported features excluded before execution; host-specific observation
- **Unsupported inferences:** Full-system assurance, full schema/parser conformance, security efficacy, release approval, or other-platform compatibility
- **Current freshness:** Fixed observation at recorded times; rerun after source or harness changes
- **Supersession:** NONE; first public-data benchmark generation

## Change controls

DEAS Strict; Python, Document, Evidence, Validator, AI-Assisted, Git overlays. Authorized surface: benchmark data, runners, tests, reports, citations, notices, and exact APA PDF copies in these private drafts. At this first observation, runtime sources remained unchanged. Rollback: revert the bounded benchmark commit; retained upstream main commits remain the source baseline. Runs are bounded by the pinned 241/318 inventories and five seconds per candidate invocation; no retries or network calls occur during measurement. Existing Phase 3 nonconformance is not waived by this record.

## Intermediate correction observation

The first observation above remains historical. The user authorized a bounded staged comparator correction and benchmark reliability fixes. The intermediate observation is in results/apple-silicon-v2.json; tests are in results/validation-v2.json, and exact before/after identities are in results/measurement-comparison.json. DEAS Strict and all six listed overlays continue to apply. The comparator descends only into smaller finite decoded JSON subtrees; cyclic or arbitrary Python objects are outside its contract. Existing input parsing and recursion limits are unchanged. The benchmark bounds each candidate process to five seconds and the same fixed corpus.

Intermediate result: 241/241; failures 0; controls passed True. Intermediate run SHA-256: 400c4efcd8207c20065047ed6b7e55ab92f9dd1cd5dec749ff7c945e6eb898cd. This supersedes the first run for current-source claims while retaining it as evidence. Historical package-test failures remain disclosed; release approval is not implied.

## Current correction observation (v3)

Independent review found a deep-container regression in the intermediate recursive generator. The final comparator uses an explicit worklist bounded by finite input tree size. New 600-level array/object const and enum regressions demonstrated eight failures before correction and now pass. All 67 core/port tests and five benchmark tests pass. All 14 canonical fixture commands retain identical output and exits.

Current run: results/apple-silicon-v3.json. Current tests: results/validation-v3.json. Before/after identities: results/measurement-comparison-v3.json. Result: 241/241, zero mismatches, controls pass. Run SHA-256: e2ffa330547ad9d4f469f287885d985727eef80e13c6b1ef1c46bb5c94ae74f7. Recorded time: 2026-09-11T20:10:59.022826+00:00 through 2026-09-11T20:11:06.193573+00:00. Effective environment and actual script arguments are in the raw record. This observation supersedes v2 for current-source claims. Both prior observations are retained. Release and acceptance decisions remain separate.
