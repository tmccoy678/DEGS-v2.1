# Citations and source credit

## Original APA reference collection

[Read the complete APA references PDF](references/dobeworks-apa-references.pdf). This is the original seven-page document, reused byte-for-byte at Taylor's request. Its formatting, wording, order, and links are unchanged. SHA-256: `fc6f090f2f9a937f6ab6d62cc505611969a18e00dde1ef026f5f981ad150c557`. The sources below supplement that fixed reference collection; this copy does not update its retrieval dates or claim a new verification of every citation.


This list records the sources used for the private v2.1 draft and its documentation. Research informs how results are presented; none of these publications evaluates, certifies, or endorses DobeWorks or DEGS. PubMed is a biomedical citation index, not a software-engineering journal ranking. Sources were chosen for relevance, with publication types kept explicit.

## Source-derived engineering

- **Sashiko contributors.** [Sashiko source at 39f6ce95c797bb40023247916a8b16d0f4aaf0da](https://github.com/sashiko-dev/sashiko/tree/39f6ce95c797bb40023247916a8b16d0f4aaf0da). The selected Python value operations in the companion DEGS draft derive from `src/worker/kernel_workflow.rs`, including stage outputs, concern accumulation, and the six selected state collections. The reference prompts retain exact source wording. Apache-2.0; preserve source notices and identify modifications.
- **Muchun Song.** [Dismissed concerns, commit 39ff1c4](https://github.com/sashiko-dev/sashiko/commit/39ff1c4d4a9e6fef466dfade79d34617c28f6cda); [concern/dismissed-concern conflict resolution, commit 522c14b](https://github.com/sashiko-dev/sashiko/commit/522c14b7ac7461eecb2655c3d358afab4e5996b2). These commits substantiate credit for the mechanisms selected for reuse.
- **Chris Mason and review-prompts contributors.** [review-prompts](https://github.com/masoncl/review-prompts/tree/032284304f3bbad50e092fa870c5d810de324d9f), MIT; Copyright (c) 2025 Chris Mason. [Sashiko's own description](https://sashiko.dev/) credits these prompts as a foundation. This does not attribute every Sashiko Rust function to Chris Mason. The separate corpus is not vendored in these drafts.
- Additional Sashiko contributions include Roman Gushchin's declarative workflow, Fuad Tabba's restored review guidance, and Anders Heimer's location preservation. The companion DEGS draft records exact commits and license scope in its third-party notices.

## Software-engineering evidence and reporting

1. Barr, E. T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S. (2015). **The Oracle Problem in Software Testing: A Survey.** *IEEE Transactions on Software Engineering, 41*(5), 507–525. [DOI: 10.1109/TSE.2014.2372785](https://doi.org/10.1109/TSE.2014.2372785). [Author-hosted full paper](https://discovery.ucl.ac.uk/id/eprint/1471263/1/06963470.pdf). Application: state the expected decision and reason before judging the observed output. Running a command is not enough to establish correct behavior.

2. Timperley, C. S., Herckis, L., Le Goues, C., & Hilton, M. (2021). **Understanding and improving artifact sharing in software engineering research.** *Empirical Software Engineering, 26*, article 67. [DOI: 10.1007/s10664-021-09973-5](https://doi.org/10.1007/s10664-021-09973-5). [Author-hosted full paper](https://squareslab.github.io/materials/timperley21ese.pdf). Application: explain purpose, claims, limitations, dependencies, examples, and tests so that reproduction does not depend on hidden knowledge.

3. Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). **Good enough practices in scientific computing.** *PLOS Computational Biology, 13*(6), e1005510. Publisher type: Perspective. [DOI and full article](https://doi.org/10.1371/journal.pcbi.1005510). Application: provide small known-answer examples, understandable project overviews, requirements, and clear collaboration and citation guidance.

4. Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). **Ten Simple Rules for Reproducible Computational Research.** *PLOS Computational Biology, 9*(10), e1003285. Publisher type: Editorial. [DOI and full article](https://doi.org/10.1371/journal.pcbi.1003285). Application: retain exact software versions, commands, intermediate results, and the connection between a claim and its evidence. This is methodological guidance, not an empirical DW/DEGS study.

5. Inozemtseva, L., & Holmes, R. (2014). **Coverage Is Not Strongly Correlated with Test Suite Effectiveness.** *ICSE 2014*, research-track conference paper. [Author-hosted full paper](https://cs.uwaterloo.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf). The study examines Java projects and mutation-based effectiveness; its setting limits generalization. Application: do not equate coverage or a passing-test count with correctness or security. No coverage percentage or mutation-testing result is claimed for these drafts.

## License references and unresolved release work

The [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0), especially sections 2, 4, and 6, provides the terms for Sashiko-derived reuse. Keep the license, applicable notices, and prominent modification notices; do not imply transfer of copyright or endorsement. MIT source notices continue to apply to MIT material. Exact source ancestry is useful evidence but is not itself license compliance.

The DobeWorks snapshot contains historical private records and identity material. The DEGS draft retains MIT coverage for original code and Apache-2.0 coverage for the identified Sashiko-derived portions. A uniform public Apache-2.0 release has not been declared. Its exact file/asset rights and license coverage need a final review, and the inherited DobeWorks Phase 3 manifest mismatch remains unresolved. Citations expose uncertainty; they do not resolve rights or turn a failing test into a pass.

## Public benchmark data

- JSON Schema Test Suite contributors. (n.d.). *JSON Schema Test Suite* [Test data, commit `f6fd52a0a95472e079cbfc6ef7f089702b80e045`]. GitHub. [Pinned source](https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/f6fd52a0a95472e079cbfc6ef7f089702b80e045). MIT; original copyright and permission text retained in [the corpus license](benchmarks/data/LICENSE).
- [Benchmark selection research](benchmarks/selection.md) records the primary-source basis and scope. These supplemental references do not alter the fixed APA PDF or imply its citations were reverified.

## Revised reading edition

The dated [44-work APA edition](references/engineering-foundations-references.pdf), [HTML equivalent](references/engineering-foundations-references.html), and [verification audit](references/verification.md) apply supported corrections while retaining explicit access and metadata limits. The earlier `references/dobeworks-apa-references.pdf` remains byte-identical to the original. [Figure-specific citation notes](references/figure-citation-notes.md) document the additional source selections.
