# Dobeworks EGS Source Register

Policy ID: `dobeworks-egs`  
Policy version: `1.1.0`  
Policy status: `DRAFT`  
Date verified: `2026-08-31`

> The Dobeworks Engineering Governance System is a tailored local engineering-governance framework informed by selected authoritative standards, handbooks, primary literature and public industry practices. It does not by itself constitute certification, accreditation, formal regulatory compliance, equivalence to private internal procedures, or endorsement by MIT, NASA, NIST, INCOSE, ISO, OWASP, CISA, Lockheed Martin, NVIDIA, Apple, Microsoft, IBM, the U.S. Department of Defense, or any other referenced organization.

The machine-readable canonical source records are in [`source-register.json`](source-register.json). This human-readable register describes the same 41-source baseline: the preserved 23-source baseline plus the validated bounded 18-record expansion. A citation records evidence and scope; it does not prove conformity, implementation effectiveness, endorsement, or suitability by reputation.

## Selection method

DEGS uses this evidence hierarchy:

1. **Tier A — current normative or formal sources:** currently effective government requirements, current final standards, and current formal procedural requirements. A draft in this tier is advisory only.
2. **Tier B — authoritative handbooks:** official engineering handbooks, professional bodies of knowledge, official educational material, and authoritative government guidance.
3. **Tier C — foundational primary literature:** original publisher-hosted, author-hosted, or institutional-archive papers.
4. **Tier D — public industry practice:** first-party public descriptions, informative only and never represented as private internal procedure.

SEO articles, anonymous summaries, unsourced blogs, social-media claims, vendor marketing presented as normative evidence, inaccessible material that was not reviewed, and AI-generated summaries are excluded as evidence.

## Current-version conclusions

- NIST SP 800-218, SSDF v1.1, remains the current **FINAL STANDARD** baseline. NIST SP 800-218 Rev. 1, SSDF v1.2, remains an **Initial Public Draft** and is advisory only.
- ISO/IEC/IEEE 15288:2023 and ISO/IEC/IEEE 12207:2026 are the current published lifecycle standards identified by ISO. The full licensed standards were not reviewed, so mappings are limited to official scope and lifecycle metadata.
- NPR 7123.1D Change 2 and NPR 7150.2D are current NASA procedural requirements within their stated NASA scope. That applicability does not transfer to Dobeworks.
- OWASP ASVS 5.0.0 is the current stable release, and SLSA v1.2 is the current Approved specification reviewed here.
- INCOSE Systems Engineering Handbook Version 5 and SEBoK v2.14 are the current official versions reviewed.
- Lockheed Martin material is first-party public industry practice only. DEGS has no access to, and makes no claim about, private Lockheed Martin procedures.
- The 2026-08-31 expansion is exactly 18 logical records from NVIDIA, Apple, Microsoft, IBM, and DoD. Corporate records remain Tier D public industry practice; DoD sources retain only their stated government or contractual scope.
- Swift Evolution is Swift-project governance, Microsoft Responsible AI Standard v2 is a June 2022 public snapshot, NVIDIA's FY2025 report is a dated corporate self-report, and Apple PCC and IBM z/OS are specialized product or system evidence.
- Distribution Statement A and public availability are access statements, not blanket content licenses. Mutable pages are tied to the retrieval identities recorded in `source-register.json`; repository sources use the validated commit pins.

## Source records

### Systems engineering

#### DEGS-SRC-MIT-16842

- **Organization or author:** Massachusetts Institute of Technology OpenCourseWare; Prof. Olivier de Weck
- **Title:** *Fundamentals of Systems Engineering*
- **Edition, version, or revision:** Course 16.842, Fall 2015
- **Publication or effective date:** Fall 2015; exact web-publication date `UNKNOWN`
- **Current status:** `EDUCATIONAL`
- **Official source location:** [MIT OpenCourseWare](https://ocw.mit.edu/courses/16-842-fundamentals-of-systems-engineering-fall-2015/)
- **Scope and DEGS use:** Stakeholder analysis, requirements, architecture, trade spaces, integration, safety, V&V, operations, and lifecycle management; used as educational support for mission framing, alternatives, lifecycle thinking, and V&V separation.
- **Normative weight:** Tier B; informative, not binding
- **Limitations and access:** 2015 course material with some superseded references; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-NASA-SEH

- **Organization or author:** NASA; Steven R. Hirshorn, Linda D. Voss, and Linda K. Bromley
- **Title:** *NASA Systems Engineering Handbook*
- **Edition, version, or revision:** NASA/SP-2016-6105 Rev 2
- **Publication or effective date:** Document year 2016; NTRS publication date 2017-02-17
- **Current status:** `AUTHORITATIVE HANDBOOK`
- **Official source location:** [NTRS full text](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20170001761.pdf); [NASA web edition](https://www.nasa.gov/reference/systems-engineering-handbook/)
- **Scope and DEGS use:** Lifecycle, design, product realization, and technical management; used for tailoring, requirements, V&V, configuration, reviews, risk, and handoffs.
- **Normative weight:** Tier B
- **Limitations and access:** Guidance, not a directive; NASA applicability does not transfer; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-NASA-NPR7123

- **Organization or author:** NASA Office of the Chief Engineer
- **Title:** *NASA Systems Engineering Processes and Requirements*
- **Edition, version, or revision:** NPR 7123.1D, updated with Change 2
- **Publication or effective date:** Effective 2023-07-05; expires 2028-07-05
- **Current status:** `CURRENT REQUIREMENT`
- **Official source location:** [NASA NODIS](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_)
- **Scope and DEGS use:** NASA technical processes, lifecycle reviews, responsibilities, and planning; used as a source pattern for local tailoring, reviews, requirements management, and evidence.
- **Normative weight:** Tier A within NASA's stated scope
- **Limitations and access:** Does not bind Dobeworks; mapped without a compliance claim; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-INCOSE-SEH

- **Organization or author:** INCOSE; editors David D. Walden, Thomas M. Shortell, Garry J. Roedler, Bernardo A. Delicado, Odile Mornas, Yip Yew-Seng, and David Endler
- **Title:** *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- **Edition, version, or revision:** Fifth edition; INCOSE-TP-2003-002-05-2023
- **Publication or effective date:** E-book 2023-06; paperback 2023-07
- **Current status:** `AUTHORITATIVE HANDBOOK`
- **Official source location:** [INCOSE handbook page](https://www.incose.org/resources-publications/technical-publications/se-handbook/); [publisher sample](https://catalogimages.wiley.com/images/db/pdf/9781119814290.excerpt.pdf)
- **Scope and DEGS use:** Systems-engineering concepts, lifecycle processes, methods, tailoring, and practice; used for lifecycle, architecture, risk, V&V, and reviews.
- **Normative weight:** Tier B
- **Limitations and access:** Complete handbook not publicly accessible; no INCOSE certification is implied; `OFFICIAL OVERVIEW AND SAMPLE ONLY`.

#### DEGS-SRC-SEBOK

- **Organization or author:** SEBoK Editorial and Governing Boards
- **Title:** *Guide to the Systems Engineering Body of Knowledge*
- **Edition, version, or revision:** Version 2.14
- **Publication or effective date:** 2026-05-18
- **Current status:** `AUTHORITATIVE HANDBOOK`
- **Official source location:** [SEBoK](https://sebokwiki.org/wiki/Main_Page); [Version 2.14 release](https://sebokwiki.org/wiki/Version_2.14)
- **Scope and DEGS use:** Living systems-engineering guide; used to orient and cross-check lifecycle, governance, tailoring, and terminology.
- **Normative weight:** Tier B
- **Limitations and access:** Living body of knowledge, not a requirement or certification scheme; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-ISO-15288

- **Organization or author:** ISO, IEC, and IEEE
- **Title:** *Systems and software engineering — System life cycle processes*
- **Edition, version, or revision:** ISO/IEC/IEEE 15288:2023, Edition 2
- **Publication or effective date:** 2023-05; published 2023-05-16
- **Current status:** `FINAL STANDARD`
- **Official source location:** [ISO record and scope](https://www.iso.org/standard/81702.html)
- **Scope and DEGS use:** System lifecycle process framework; used only where the official scope supports lifecycle, stakeholder, tailoring, and improvement mappings.
- **Normative weight:** Tier A
- **Limitations and access:** Full standard not reviewed; mapping does not establish conformity; `OFFICIAL OVERVIEW ONLY`.

### Software engineering

#### DEGS-SRC-NASA-NPR7150

- **Organization or author:** NASA Office of the Chief Engineer
- **Title:** *NASA Software Engineering Requirements*
- **Edition, version, or revision:** NPR 7150.2D
- **Publication or effective date:** Effective 2022-03-08; expires 2027-03-08
- **Current status:** `CURRENT REQUIREMENT`
- **Official source location:** [NASA NODIS](https://nodis3.gsfc.nasa.gov/displayDir.cfm?c=7150&s=2D&t=NPR)
- **Scope and DEGS use:** NASA software lifecycle, planning, implementation, testing, assurance, traceability, and configuration; used as source patterns for local controls.
- **Normative weight:** Tier A within NASA's stated scope
- **Limitations and access:** Does not bind Dobeworks; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-NASA-SWEHB

- **Organization or author:** NASA Office of the Chief Engineer
- **Title:** *NASA Software Engineering Handbook*
- **Edition, version, or revision:** NASA-HDBK-2203, version d, change 0
- **Publication or effective date:** 2020-04-20
- **Current status:** `AUTHORITATIVE HANDBOOK`
- **Official source location:** [NASA Technical Standards System](https://standards.nasa.gov/standard/NASA/NASA-HDBK-2203)
- **Scope and DEGS use:** Implementation guidance for NPR 7150.2 and NASA software assurance and safety; used for requirements, assurance, planning, testing, and evidence.
- **Normative weight:** Tier B; active and endorsed, not mandatory
- **Limitations and access:** Listed review date 2025-04-20 has passed; refresh every 90 days; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-ISO-12207

- **Organization or author:** ISO, IEC, and IEEE
- **Title:** *Systems and software engineering — Software life cycle processes*
- **Edition, version, or revision:** ISO/IEC/IEEE 12207:2026, Edition 2
- **Publication or effective date:** 2026-04; published 2026-04-29
- **Current status:** `FINAL STANDARD`
- **Official source location:** [ISO record and scope](https://www.iso.org/standard/90219.html)
- **Scope and DEGS use:** Software lifecycle process framework; used only where the official scope supports software lifecycle and tailoring mappings.
- **Normative weight:** Tier A
- **Limitations and access:** Full standard not reviewed; 2017 edition withdrawn; mapping does not establish conformity; `OFFICIAL OVERVIEW ONLY`.

#### DEGS-SRC-CMU-SEI-QAW

- **Organization or author:** Carnegie Mellon University Software Engineering Institute; Mario R. Barbacci, Robert J. Ellison, Anthony J. Lattanze, Judith A. Stafford, Charles Weinstock, and William Wood
- **Title:** *Quality Attribute Workshops (QAWs), Third Edition*
- **Edition, version, or revision:** Third edition; CMU/SEI-2003-TR-016
- **Publication or effective date:** 2003-10-01
- **Current status:** `AUTHORITATIVE HANDBOOK`
- **Official source location:** [SEI report](https://www.sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/); [current collection](https://www.sei.cmu.edu/library/quality-attribute-workshop-collection/)
- **Scope and DEGS use:** Stakeholder-driven quality-attribute scenarios; used for measurable quality attributes, acceptance criteria, architecture trade-offs, assumptions, and early risk discovery.
- **Normative weight:** Tier B
- **Limitations and access:** Method rather than universal requirement; ceremony must be proportional; `FULL TEXT ACCESSIBLE`.

### Secure development

#### DEGS-SRC-NIST-SSDF

- **Organization or author:** NIST; Murugiah Souppaya, Karen Scarfone, and Donna Dodson
- **Title:** *Secure Software Development Framework Version 1.1*
- **Edition, version, or revision:** NIST SP 800-218; SSDF v1.1
- **Publication or effective date:** Final 2022-02-03
- **Current status:** `FINAL STANDARD`
- **Official source location:** [NIST final publication](https://csrc.nist.gov/pubs/sp/800/218/final)
- **Scope and DEGS use:** Secure-development practices across preparation, software protection, secure production, and vulnerability response; the current final normative SSDF baseline for DEGS.
- **Normative weight:** Tier A
- **Limitations and access:** Risk-based recommendations require local implementation and do not confer certification; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-NIST-SSDF12-DRAFT

- **Organization or author:** NIST; Harold Booth, Michael Ogata, Karen Kent, Murugiah Souppaya, and Donna Dodson
- **Title:** *Secure Software Development Framework Version 1.2*
- **Edition, version, or revision:** NIST SP 800-218 Rev. 1, Initial Public Draft
- **Publication or effective date:** 2025-12-17; comment period closed 2026-01-30
- **Current status:** `DRAFT`
- **Official source location:** [NIST Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd)
- **Scope and DEGS use:** Proposed SSDF changes; advisory horizon-scanning and refresh trigger only.
- **Normative weight:** Tier A candidate, **ADVISORY ONLY**
- **Limitations and access:** Not final and does not replace v1.1; `FULL DRAFT TEXT ACCESSIBLE`.

#### DEGS-SRC-NIST-SSDF-AI

- **Organization or author:** NIST; Harold Booth, Murugiah Souppaya, Apostol Vassilev, Michael Ogata, Martin Stanley, and Karen Scarfone
- **Title:** *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile*
- **Edition, version, or revision:** NIST SP 800-218A
- **Publication or effective date:** Final 2024-07-26
- **Current status:** `FINAL STANDARD`
- **Official source location:** [NIST final publication](https://csrc.nist.gov/pubs/sp/800/218/a/final)
- **Scope and DEGS use:** AI-model-development additions to SSDF v1.1; used for applicable AI secure-development and acquisition controls.
- **Normative weight:** Tier A
- **Limitations and access:** Supplements rather than replaces SSDF v1.1; scope is specific to generative AI and dual-use foundation models; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-CISA-SBD

- **Organization or author:** U.S. CISA with U.S. and international government partners
- **Title:** *Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design Software*
- **Edition, version, or revision:** Refined and expanded October 2023 edition; no formal version
- **Publication or effective date:** 2023-10; exact day `UNKNOWN`
- **Current status:** `AUTHORITATIVE HANDBOOK`
- **Official source location:** [CISA resource](https://www.cisa.gov/resources-tools/resources/secure-by-design); [official PDF](https://www.cisa.gov/sites/default/files/2023-10/Shifting-the-Balance-of-Cybersecurity-Risk-Principles-and-Approaches-for-Secure-by-Design-Software.pdf)
- **Scope and DEGS use:** Manufacturer ownership, transparency, leadership, and safe defaults; used for secure-by-design and customer-burden-reduction principles.
- **Normative weight:** Tier B
- **Limitations and access:** Voluntary guidance, not a certification or universal legal requirement; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-OWASP-ASVS

- **Organization or author:** OWASP Foundation, ASVS project
- **Title:** *OWASP Application Security Verification Standard*
- **Edition, version, or revision:** Version 5.0.0
- **Publication or effective date:** 2025-05-30
- **Current status:** `FINAL STANDARD`
- **Official source location:** [OWASP project](https://owasp.org/www-project-application-security-verification-standard/); [official repository](https://github.com/OWASP/ASVS)
- **Scope and DEGS use:** Testable web-application and service security requirements; used where applicable for security acceptance criteria and tests.
- **Normative weight:** Tier A
- **Limitations and access:** Applicability must be tailored and version-qualified; repository development output is not the stable release; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-SLSA

- **Organization or author:** SLSA Community
- **Title:** *SLSA specification*
- **Edition, version, or revision:** Version 1.2; Approved
- **Publication or effective date:** 2025-11-24
- **Current status:** `FINAL STANDARD`
- **Official source location:** [SLSA v1.2](https://slsa.dev/spec/v1.2/); [release announcement](https://slsa.dev/blog/2025/11/announce-slsa-v1.2)
- **Scope and DEGS use:** Build and Source tracks, levels, and attestation formats; used for proportional provenance and supply-chain controls.
- **Normative weight:** Tier A
- **Limitations and access:** Bounded guarantees, not a complete secure-development program; claims require evidence; `FULL TEXT ACCESSIBLE`.

### Mentorship and learning

#### DEGS-SRC-MIT-ELO-BP

- **Organization or author:** MIT Office of Experiential Learning
- **Title:** *Best Practices for Experiential Learning*
- **Edition, version, or revision:** Web resource; no formal version
- **Publication or effective date:** `UNKNOWN`
- **Current status:** `EDUCATIONAL`
- **Official source location:** [MIT ELO](https://elo.mit.edu/best-practices/)
- **Scope and DEGS use:** Mentoring, reflection, feedback, assessment, goal-setting, and scaffolded independence; adapted for Taylor's learning and ownership.
- **Normative weight:** Tier B
- **Limitations and access:** Educational rather than software-governance guidance; no MIT approval is implied; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-MIT-ELO-AFR

- **Organization or author:** MIT Office of Experiential Learning
- **Title:** *About the Office of Experiential Learning — What is Experiential Learning?*
- **Edition, version, or revision:** Web resource; no formal version
- **Publication or effective date:** `UNKNOWN`
- **Current status:** `EDUCATIONAL`
- **Official source location:** [MIT ELO method](https://elo.mit.edu/about/)
- **Scope and DEGS use:** Action-feedback-reflection cycles; locally adapted for authentic action, feedback, reflection, and next-phase learning.
- **Normative weight:** Tier B
- **Limitations and access:** Educational guidance, not an engineering mandate; `FULL TEXT ACCESSIBLE`.

### Foundational design and elegance

#### DEGS-SRC-DIJKSTRA-STRUCT

- **Organization or author:** Edsger W. Dijkstra; University of Texas institutional archive
- **Title:** *Notes on Structured Programming*
- **Edition, version, or revision:** EWD249; T.H. Report 70-WSK-03; second edition
- **Publication or effective date:** First text 1969-08; second edition 1970-04
- **Current status:** `FOUNDATIONAL`
- **Official source location:** [archive transcription](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html); [archival PDF](https://www.cs.utexas.edu/~EWD/ewd02xx/EWD249.PDF)
- **Scope and DEGS use:** Comprehensibility, correctness reasoning, abstraction, structured composition, and manageability; used for clarity and structured decomposition.
- **Normative weight:** Tier C
- **Limitations and access:** Historical and not a modern lifecycle or security standard; `FULL TEXT ACCESSIBLE`.

#### DEGS-SRC-PARNAS-MODULES

- **Organization or author:** David L. Parnas
- **Title:** *On the Criteria To Be Used in Decomposing Systems into Modules*
- **Edition, version, or revision:** Communications of the ACM 15(12), 1053–1058; DOI 10.1145/361598.361623
- **Publication or effective date:** 1972-12-01
- **Current status:** `FOUNDATIONAL`
- **Official source location:** [ACM publisher record](https://doi.org/10.1145/361598.361623)
- **Scope and DEGS use:** Modularization and information hiding; used for responsibility ownership, cohesion, coupling, and change isolation.
- **Normative weight:** Tier C
- **Limitations and access:** Historical design paper; publisher metadata and abstract only were reviewed; `OFFICIAL OVERVIEW ONLY`.

#### DEGS-SRC-SALTZER-E2E

- **Organization or author:** Jerome H. Saltzer, David P. Reed, and David D. Clark
- **Title:** *End-to-End Arguments in System Design*
- **Edition, version, or revision:** ACM TOCS 2(4), 277–288; DOI 10.1145/357401.357402
- **Publication or effective date:** 1984-11
- **Current status:** `FOUNDATIONAL`
- **Official source location:** [author-hosted full text](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf); [MIT publication record](https://web.mit.edu/Saltzer/www/publications/pubs.html)
- **Scope and DEGS use:** Responsibility placement and complete end-to-end correctness; used for actual user-path validation and avoiding misplaced controls.
- **Normative weight:** Tier C
- **Limitations and access:** A design argument rather than an absolute rule; `FULL TEXT ACCESSIBLE`.

### Public industry practice

#### DEGS-SRC-LM-SWFACTORY

- **Organization or author:** Lockheed Martin
- **Title:** *Lockheed Martin Software Factory Continues to Expand with Accelerated Software Development Capability*
- **Edition, version, or revision:** First-party web feature; no formal version
- **Publication or effective date:** 2020-08-24
- **Current status:** `PUBLIC INDUSTRY PRACTICE`
- **Official source location:** [Lockheed Martin public feature](https://www.lockheedmartin.com/en-us/news/features/2020/lockheed-martin-software-factory-continues-expand-company-accelerates-software-development-capabilities.html)
- **Scope and DEGS use:** Public description of integrated people, process, automation, security, testing, and delivery; informative example only.
- **Normative weight:** Tier D; informative only
- **Limitations and access:** First-party corporate communications may be selective; not an internal standard or independent evaluation; `FULL PUBLIC PAGE ACCESSIBLE`.

#### DEGS-SRC-LM-SKUNKWORKS

- **Organization or author:** Lockheed Martin Skunk Works
- **Title:** *The Skunk Works Legacy*
- **Edition, version, or revision:** First-party web page; no formal version
- **Publication or effective date:** `UNKNOWN`
- **Current status:** `PUBLIC INDUSTRY PRACTICE`
- **Official source location:** [Lockheed Martin public page](https://www.lockheedmartin.com/en-us/who-we-are/business-areas/aeronautics/skunkworks/skunk-works-origin-story.html)
- **Scope and DEGS use:** Public description of small teams, streamlined process, and rapid prototyping; informative example for bounded prototypes and learning cycles.
- **Normative weight:** Tier D; informative only
- **Limitations and access:** Self-reported corporate history, not private procedures or independently validated governance; `FULL PUBLIC PAGE ACCESSIBLE`.

### Validated 2026-08-31 primary-source expansion

The following records implement the bounded 18-record validation set. Each record separates what the source documents from the control or workflow that DEGS locally synthesizes from it.

#### DEGS-SRC-NVIDIA-SDL

- **Organization or author:** NVIDIA
- **Title:** *Security Development Lifecycle for NVIDIA AI Enterprise*
- **Identity/currentness:** Mutable official page reported last updated 2026-04-15; retrieved 2026-08-31; SHA-256 `c156a50ce61926f02bd7bf00b9a412bae57485d2c6dd123d5f445113adced73a`.
- **Current status and source:** `PUBLIC INDUSTRY PRACTICE`; [official product documentation](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-enterprise-security-white-paper/latest/security-lifecycle.html).
- **Documented practice:** Product-specific lifecycle description covering threat analysis, scanning, security testing, provenance, signing, and a publication-blocking readiness check.
- **DEGS synthesis:** Lifecycle-spanning checks, deterministic fail-closed gates, and artifact provenance are locally adapted control patterns.
- **Limitations:** Not an NVIDIA-wide standard, independent effectiveness evidence, or proof of equivalent DEGS security; Tier D and informative only.
- **Licensing:** Copyrighted NVIDIA documentation; no open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-NVIDIA-CUDA-BPG

- **Organization or author:** NVIDIA
- **Title:** *CUDA C++ Best Practices Guide*
- **Identity/currentness:** Release 13.3 live edition retrieved 2026-08-31; SHA-256 `adafb42af49413c1fd78cd657bcb3d2bc05d4255f10ad0d676b35d59dd515b47`.
- **Current status and source:** `PUBLIC INDUSTRY PRACTICE`; [official CUDA guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html).
- **Documented practice:** CUDA-specific Assess–Parallelize–Optimize–Deploy cycle, realistic workloads, known-good reference output, explicit tolerances, unit checks, and production error checking.
- **DEGS synthesis:** Representative baselines and measured correctness comparison are adapted beyond CUDA only as local engineering choices.
- **Limitations:** CUDA product guidance, not company-wide governance; no open-document reuse license identified; Tier D and informative only.
- **Licensing:** No open-document reuse license identified; cite and paraphrase.

#### DEGS-SRC-NVIDIA-TAI-FY25

- **Organization or author:** NVIDIA
- **Title:** *NVIDIA Sustainability Report Fiscal Year 2025 — Trustworthy AI*
- **Identity/currentness:** Dated corporate self-report covering the fiscal year ending 2025-01-26, with information approximately current to 2025-06-12.
- **Current status and source:** `PUBLIC INDUSTRY PRACTICE`; [official FY2025 report](https://images.nvidia.com/aem-dam/Solutions/documents/NVIDIA-Sustainability-Report-Fiscal-Year-2025.pdf).
- **Documented practice:** Public description of privacy, intended performance, limitations, bias work, lifecycle documentation, cross-functional review, model cards, validation, red teaming, and decommissioning.
- **DEGS synthesis:** Corroborates consequential-AI lifecycle assurance, limitations disclosure, and cross-functional accountability.
- **Limitations:** Dated self-report with aspirational and measurement caveats; never sole normative authority or proof of effectiveness; Tier D.
- **Licensing:** Copyright NVIDIA; no open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-APPLE-PRIV-GOV

- **Organization or author:** Apple
- **Title:** *Apple Privacy Governance*
- **Identity/currentness:** Mutable official page with no displayed stable version; retrieved 2026-08-31; SHA-256 `48e2ebf424f556c7c75c8f16c30603e5ff87a790fd68afcdd9525e1390414002`.
- **Current status and source:** `PUBLIC INDUSTRY PRACTICE`; [official governance page](https://www.apple.com/legal/privacy/en-ww/governance/).
- **Documented practice:** Public description of purpose limitation, minimum-necessary collection, bounded retention, business-need access, privacy impact assessment, and risk-based reassessment.
- **DEGS synthesis:** Data-purpose, minimization, retention, and reassessment fields and gate logic are local DEGS choices.
- **Limitations:** Company-authored living description, not a complete control specification or independent proof of effectiveness; Tier D.
- **Licensing:** No open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-APPLE-PCC

- **Organization or author:** Apple Security Research
- **Title:** *Private Cloud Compute architecture and expansion status*
- **Identity/currentness:** Declared composite of the [architecture introduction](https://security.apple.com/blog/private-cloud-compute/), [documentation entry point](https://security.apple.com/documentation/private-cloud-compute/), and [2026 expansion status](https://security.apple.com/blog/expanding-pcc/); ordered retrieval hashes are recorded in `source-register.json`.
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Specialized PCC requirements for stateless computation, technically enforceable guarantees, no privileged runtime access, non-targetability, verifiable transparency, purpose-limited processing, restricted logging, and inspectable signed artifacts.
- **DEGS synthesis:** Evidence identity, privilege separation, deletion-after-purpose, inspectability, and non-bypass patterns are locally adapted.
- **Limitations:** No equivalence to PCC hardware or guarantees. The 2026 Google Cloud deployment was described as preview ramping toward the full requirements, not already complete production equivalence; Tier D.
- **Licensing:** Limited-use licensing applies only to released PCC components; it is not a general open-content license.

#### DEGS-SRC-APPLE-SWIFT-EVOLUTION

- **Organization or author:** Swift project; swiftlang organization
- **Title:** *Swift Evolution Process*
- **Identity/currentness:** Commit `c8623621aacc8e3f364bb0f3cb07675177a1ec4e`; [pinned process](https://github.com/swiftlang/swift-evolution/blob/c8623621aacc8e3f364bb0f3cb07675177a1ec4e/process.md).
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Swift-project proposals, open review, accountable workgroup decisions, relevant prototypes, and bounded experimental-feature gates.
- **DEGS synthesis:** Proposal, review, decision-owner, prototype, and experiment-exit patterns are adapted to local governance.
- **Limitations:** Swift-project governance, not Apple-wide internal practice; repository licensing applies only to repository content; Tier D.
- **Licensing:** Apache-2.0 for the pinned Swift Evolution repository content only.

#### DEGS-SRC-MS-SDL

- **Organization or author:** Microsoft
- **Title:** *Microsoft Security Development Lifecycle*
- **Identity/currentness:** Official page updated 2025-09-29; retrieval identity recorded in `source-register.json`.
- **Current status and source:** `PUBLIC INDUSTRY PRACTICE`; [Microsoft Learn](https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle).
- **Documented practice:** Public description of lifecycle security, maintained threat models, non-author review, layered analysis and testing, remediation and resubmission, staged release, and monitoring.
- **DEGS synthesis:** Reviewer independence, threat-model currency, remediation-and-rerun, and monitoring requirements are local adaptations.
- **Limitations:** Microsoft-authored assurance description, not independent proof of uniform adherence or effectiveness; Tier D.
- **Licensing:** No per-page open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-MS-RAI-V2

- **Organization or author:** Microsoft
- **Title:** *Microsoft Responsible AI Standard v2 — General Requirements*
- **Identity/currentness:** June 2022 public external snapshot; [official PDF](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf).
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Dated public requirements for intended use, impact assessment, fit-for-purpose criteria, operational bounds, stakeholder impacts, human oversight and interruption, monitoring, and discontinuation.
- **DEGS synthesis:** Consequential-AI assurance fields and pass/fail decisions are local DEGS design.
- **Limitations:** Does not establish the unchanged content of a current private Microsoft standard or certify DEGS; Tier D.
- **Licensing:** Copyright Microsoft; no open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-MS-ISE-PLAYBOOK

- **Organization or author:** Microsoft Industry Solutions Engineering
- **Title:** *Code With Engineering Playbook*
- **Identity/currentness:** Commit `016770e43d8a75be87b98c000c049f07c4a6e6f8`; [pinned repository](https://github.com/microsoft/code-with-engineering-playbook/tree/016770e43d8a75be87b98c000c049f07c4a6e6f8).
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Guidance for ISE customer and partner work emphasizing focus, incremental delivery, scope discipline, shared context, testing, review, delivery automation, and observability.
- **DEGS synthesis:** Focused increments, automated verification, shared context, and observability are locally adapted.
- **Limitations:** Not a universal Microsoft mandate; repository licenses apply only to their respective content; Tier D.
- **Licensing:** CC BY 4.0 for repository documentation and the MIT license for repository code, each limited to its respective content.

#### DEGS-SRC-IBM-SEF

- **Organization or author:** IBM
- **Title:** *The IBM Secure Engineering Framework*
- **Identity/currentness:** IBM Redpaper REDP-4641-01, published 2018-12-17; [official PDF](https://www.redbooks.ibm.com/redpapers/pdfs/redp4641.pdf), [abstract](https://www.redbooks.ibm.com/abstracts/redp4641.html), and current-link corroboration recorded in the machine register.
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Dated framework for phase exits, open-issue disposition, threat modeling, layered testing, defect rework, retest, and stop authority.
- **DEGS synthesis:** Explicit phase exit, open-issue visibility, layered testing, and remediation-and-rerun are local adaptations.
- **Limitations:** Current IBM linking proves continued availability, not that every 2018 detail is unchanged or universally practiced; Tier D.
- **Licensing:** IBM copyright; no open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-IBM-TRUST

- **Organization or author:** IBM Policy
- **Title:** *IBM Principles for Trust and Transparency and Pillars of Trust for Artificial Intelligence*
- **Identity/currentness:** One declared composite of [Trust Principles](https://www.ibm.com/policy/blog/trust-principles) and [AI Pillars](https://www.ibm.com/policy/blog/ibm-artificial-intelligence-pillars); page-level retrieval identities are recorded in `source-register.json`.
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Page-specific principles covering human augmentation, creator control of data and insights, agreed purpose, explainability, fairness, robustness, transparency, privacy, and minimum-necessary data.
- **Claim-to-page mapping:** [Trust Principles](https://www.ibm.com/policy/blog/trust-principles) supports human augmentation, creator control of data and insights, agreed specific purpose, transparency, and explainability. [AI Pillars](https://www.ibm.com/policy/blog/ibm-artificial-intelligence-pillars) supports explainability, fairness, robustness, transparency, privacy, minimum-necessary data, explicit purpose, and resistance to repurposing.
- **DEGS synthesis:** Converting those principles into data-purpose and AI-assurance controls is local synthesis.
- **Limitations:** Two pages grouped as one logical record, not one versioned standard or complete executable assurance; Tier D.
- **Licensing:** No open-content reuse license identified for either page; cite and paraphrase.

#### DEGS-SRC-IBM-ZOS-INTEGRITY

- **Organization or author:** IBM
- **Title:** *z/OS 3.2 System Integrity*
- **Identity/currentness:** Versioned [z/OS 3.2 product documentation](https://www.ibm.com/docs/en/zos/3.2.0?topic=aapmss-system-integrity).
- **Current status:** `PUBLIC INDUSTRY PRACTICE`.
- **Documented practice:** Product-specific integrity guidance about preventing bypass or unauthorized state and preserving equivalent checks when privileged functions are added.
- **DEGS synthesis:** A local rule that integrations preserve gates and cannot create a bypass is a reasoned adaptation.
- **Limitations:** z/OS product guidance, not IBM-wide governance, direct macOS guidance, or proof that DEGS is secure; Tier D.
- **Licensing:** No open-content reuse license identified; cite and paraphrase.

#### DEGS-SRC-DOD-5000-88

- **Organization or author:** United States Department of Defense
- **Title:** *DoDI 5000.88, Engineering of Defense Systems*
- **Identity/currentness:** Effective 2020-11-18; [official instruction](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500088p.PDF); `CURRENT REQUIREMENT`.
- **Documented practice:** Within covered Defense systems, addresses technical baselines, configuration and risk management, traceability, independent technical review, decision audit trails, and system safety.
- **DEGS synthesis:** Traceable baselines, configuration control, review evidence, and risk ownership are locally tailored without acquisition-scale ceremony.
- **Limitations:** Authoritative only within stated DoD scope; not automatically binding on Dobeworks and not an open-content or compliance license.
- **Licensing:** Cleared for public release; public release is not an open-content license.

#### DEGS-SRC-DOD-5000-87

- **Organization or author:** United States Department of Defense
- **Title:** *DoDI 5000.87, Operation of the Software Acquisition Pathway*
- **Identity/currentness:** Effective 2020-10-02; [official instruction](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500087p.PDF); `CURRENT REQUIREMENT`.
- **Documented practice:** Within the Software Acquisition Pathway, describes iterative delivery, DevSecOps, human-centered design, end-user collaboration, cybersecurity from inception, automated testing, and monitoring.
- **DEGS synthesis:** Iterative, user-centered, security-integrated delivery is adapted while local approval gates remain intact.
- **Limitations:** Authoritative only within stated DoD scope; it does not make DoD roles, cadence, or terminology universal.
- **Licensing:** Cleared for public release; no open-content license established.

#### DEGS-SRC-DOD-5000-97

- **Organization or author:** United States Department of Defense
- **Title:** *DoDI 5000.97, Digital Engineering*
- **Identity/currentness:** Effective 2023-12-21; [official instruction](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500097p.pdf); `CURRENT REQUIREMENT`.
- **Documented practice:** Within its DoD scope, calls for verified, validated, curated, configuration-controlled authoritative digital sources and lifecycle traceability.
- **DEGS synthesis:** Controlled identity, validation, configuration control, source currency, and end-to-end traceability are local adaptations.
- **Limitations:** Does not govern DEGS; calling a folder canonical does not prove its contents authoritative.
- **Licensing:** Cleared for public release; no open-content license established.

#### DEGS-SRC-DOD-RAI

- **Organization or author:** DoD Chief Digital and Artificial Intelligence Office
- **Title:** *Responsible Artificial Intelligence Strategy and Implementation Pathway*
- **Identity/currentness:** June 2022; [official strategy](https://www.ai.mil/Portals/137/Documents/Resources%20Page/DoD%20Responsible%20AI%20Strategy%20and%20Implementation%20Pathway.pdf); `AUTHORITATIVE HANDBOOK`.
- **Documented practice:** Within DoD strategy scope, describes human responsibility, auditable sources and methods, explicit uses, lifecycle assurance, unintended-consequence controls, and disengagement.
- **DEGS synthesis:** Human accountability, intended-use, assurance, and safe-disengagement fields are local adaptations.
- **Limitations:** Strategy and guidance, not a generally binding instruction, certification, approval, or proof of DEGS compliance.
- **Licensing:** No explicit open-content license identified; cite and paraphrase.

#### DEGS-SRC-DOD-MILSTD-882E

- **Organization or author:** United States Department of Defense; DLA ASSIST
- **Title:** *MIL-STD-882E Change 1, System Safety*
- **Identity/currentness:** Revision E Change 1, dated 2023-09-27; [official ASSIST record](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36027); `FINAL STANDARD`.
- **Documented practice:** Within invoked government or contractual scope, prioritizes hazard elimination, mitigation and testing, cross-domain impacts, and explicit residual-risk management.
- **DEGS synthesis:** A lightweight hazard hierarchy, failure-path evidence, cross-domain check, and named human residual-risk owner are local adaptations.
- **Limitations:** DEGS is not a military system-safety program. Distribution Statement A is not an open-content license.
- **Licensing:** Distribution Statement A permits public distribution but is not an open-content license.

#### DEGS-SRC-DOD-5000-101

- **Organization or author:** United States Department of Defense
- **Title:** *DoDM 5000.101, Operational Test and Evaluation and Live Fire Test and Evaluation of Artificial Intelligence-Enabled and Autonomous Systems*
- **Identity/currentness:** Effective 2024-12-09; [official manual](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/5000101p.PDF); `CURRENT REQUIREMENT`.
- **Documented practice:** Within covered DoD systems, addresses independent test data, operationally representative and out-of-distribution conditions, adversarial and integrated human-machine tests, error consequences, drift, safer modes, and monitoring.
- **DEGS synthesis:** Proportional independent fixtures, adversarial and negative tests, integrated human-agent-tool paths, fallback modes, and monitoring are local adaptations.
- **Limitations:** Military operational-test scope and ceremony do not transfer automatically to low-consequence engineering, and no accreditation is implied.
- **Licensing:** Cleared for public release; no open-content license established.

## Deliberately excluded first-party candidates

These exclusions preserve the validated 18-record boundary. They are not silent judgments that the sources are false, and they must not be reintroduced merely to increase source count or brand coverage:

- **NVIDIA Skills pipeline:** living repository requiring a separate pin and redundant with controls already supported by the bounded set.
- **Apple Platform Security:** platform- and hardware-specific; the separate 2015 MacBook work remains deferred.
- **Apple third-generation foundation-model technical report/page:** beta or product evidence that does not close an additional governance gap.
- **Microsoft Secure Future Initiative:** useful but redundant once Microsoft SDL is retained.
- **IBM Well-Architected:** current corroboration for the IBM Secure Engineering Framework, not a separate record.
- **IBM product lifecycle traceability:** product-specific and substantially covered by DoDI 5000.97.
- **IBM Enterprise Design Thinking:** useful workflow guidance that does not close an uncovered control gap.
- **DoDI 5000.61:** intended-use discipline that would widen the fixed set and risk importing accreditation concepts.

The expansion does not support claims that DEGS is approved, endorsed, certified, accredited, compliant with, or equivalent to any listed company, product, project, government agency, or military program. Public availability, public release, and organizational reputation do not substitute for scope, identity, licensing, fit, or local evidence.

## Review and refresh policy

- Verify normative-source status at least every 90 days.
- Verify again before any major Tier 3 operation.
- Verify when a source announces a new revision.
- Never silently adopt a draft as normative.
- Update DEGS only through controlled change.
- Preserve superseded source records for historical traceability.

Unknown dates or values remain `UNKNOWN`; they are never guessed.
