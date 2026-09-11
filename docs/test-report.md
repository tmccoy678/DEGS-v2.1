# Recorded tests and demonstration

Date: September 11, 2026. Environment: Apple silicon (`arm64`), macOS 26.6.2, Python 3.9.6. The standalone DEGS baseline and hashes are in `provenance/degs-baseline.json`. The Sashiko source pin and adaptation boundaries are in `provenance/sashiko-source.json`. Tested Python and oracle files have hashes in [raw evidence](test-evidence.json).

## Python tests

From the checkout root:

```sh
python3 -B -m unittest discover -s tests -v
```

Observed: 63 tests passed, zero failures or skips. This includes all 58 copied gate CLI tests and 5 new port tests. The port tests cover detached nested values, retained scalars and order, default-type rules, stage replacement, omitted versus null arrays, ignored extra fields, independent defaults, and source/destination alias rejection.

The implementation followed failing-test then passing-test slices. The result above is the final recorded suite, not the initial red runs. Existing source files listed in the baseline manifest remain byte-identical to their local canonical counterparts.

## Rust comparison

The reference harness contains the selected upstream structs and helpers, with a small JSON-line driver. Dependencies are pinned to the same serde 1.0.229 and serde_json 1.0.151 versions found in Sashiko's lockfile. The harness's own lockfile records resolved dependencies. It was compiled with rustc 1.98.1 for `aarch64-apple-darwin`.

With Rust/Cargo available, reproduce from the checkout root:

```sh
CARGO_TARGET_DIR=$(mktemp -d)
export CARGO_TARGET_DIR
cargo build --locked --manifest-path tests/rust_reference/Cargo.toml
python3 -B tools/check_rust_parity.py \
  --oracle "$CARGO_TARGET_DIR/debug/sashiko-parity-oracle"
```

Observed: **329 cases matched**, seed 20260911. Cases cover both append operations and three decoded-object output types. Numeric, boolean, string, null, nested-value, missing-field, wrong-type, and extra-field cases are included. This compares observable results with independently executed Rust source; it does not prove equivalence for every possible input or implement Sashiko's entire parser and review workflow. Rust is needed only for this optional comparison, not ordinary DEGS use.

## Demo observations

The README commands were executed from the draft root. Complete Tier 2 input returned PASS/0. Missing rollback returned BLOCKED/2 and named the rollback requirement. Agent self-approval returned BLOCKED/2 and named the human-approval requirement. The Sashiko-derived demo preserved both supplied collections without adjudicating their truth. Full stdout, stderr, and return codes appear in the raw evidence.

## Limits

This standalone package does not include private activation records, audit history, context-skill installation, or the Workbench adapter. Their dependent test suites were not imported or claimed as passing. This report does not replace full-system integration, fresh-user installation acceptance, public-license review, or semantic-review evaluation. No tests on other platforms were performed.
