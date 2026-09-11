# Historical DEGS core correction

This branch applies the already reviewed v2 comparator correction to the gate whose original bytes match the selected September 1 historical DEGS backup. The branch starts at the existing standalone draft baseline; it is a historical **core backport**, not a reconstructed complete system v1 distribution. Other retained files include later staging and the Sashiko-derived component.

The defect accepted nested booleans as numbers: a const requirement of `[false]` accepted `[0]`. The worklist comparator now rejects that input. It preserves equality between 1 and 1.0, unordered object members, ordered arrays with equal lengths, and deep decoded inputs without recursive comparison frames.

The original gate and schema hashes match the user-confirmed historical source. The [new provenance record](../provenance/v1-core-backport.json) records that identity separately from the unchanged original source manifest. DobeWorks's historical 224-line validator delegates to an external gate; it has no duplicate comparator to patch. Neither that validator nor the current frozen 792-line package was changed or repinned.

## Reproduce

```sh
python3 -B -m unittest discover -s tests -p test_json_equality.py -v
python3 -B -m unittest discover -s tests -v
```

The regression suite exercises the existing schema-validation seam through both const and enum. It includes all 14 formerly accepted invalid public cases, symmetric JSON comparisons, valid numerical equality, and 600-level array/object inputs. Original red results and all 14 canonical CLI observations remain in [the evidence directory](../provenance/v1-core-backport/).

Only two upstream JSON fixture files were copied, with the unchanged [MIT notice](../benchmarks/data/LICENSE). Credit Julian Berman and JSON Schema Test Suite contributors, pinned at f6fd52a0a95472e079cbfc6ef7f089702b80e045. Expected labels remain unchanged. These examples establish bounded helper behavior, not whole-system accuracy or full JSON Schema conformance.

The complete historical integrated Pickup/FigureMe identities and full system v1 release packaging remain unresolved. This correction does not activate governance, install into the running system, merge a PR, or publish a release.
