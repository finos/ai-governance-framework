# Test plan — item reference checks (#426)

Validates the floor, cap and reverse-coverage checks for
`finos/ai-governance-framework`.

**Under test:** `scripts/validate-item-references.py`
**Dependencies:** Python 3, PyYAML (already required by `scripts/requirements.txt`)
**Fixtures:** each case builds a throwaway repo in a temp directory, so no test
depends on the real catalogue except the integration cases in section 5.

Legend: **P** = expected pass (no finding) · **F** = expected finding

---

## 1. Floor check — risks

| ID | Case | Fixture | Expected |
|---|---|---|---|
| F-01 | Risk cites a threat and an obligation | `owasp-llm` + `eu-ai-act` | **P** no finding |
| F-02 | Risk cites threat only | `owasp-llm` | **F** `missing obligation` |
| F-03 | Risk cites obligation only | `eu-ai-act` | **F** `missing threat` |
| F-04 | Risk cites nothing | no `*_references` keys | **F** `missing threat, obligation` |
| F-05 | Risk has a reference key with an empty list | `owasp-llm_references:` (empty) | **F** empty list is not a citation |
| F-06 | Risk cites a control only | `iso-42001` | **F** `missing threat, obligation` |
| F-07 | Risk cites two standards of the same lens | `owasp-llm` + `owasp-asi` | **F** `missing obligation` — one lens, not two |

## 2. Floor check — mitigations and the IOSCO switch

| ID | Case | Fixture | Expected |
|---|---|---|---|
| F-08 | Mitigation cites a control | `nist-sp-800-53r5` | **P** no finding |
| F-09 | Mitigation cites no control | `owasp-llm` only | **F** `missing control` |
| F-10 | Mitigation rule does not require threat/obligation | `iso-42001` only | **P** no finding |
| F-11 | Risk whose only obligation is IOSCO, `--lenient-iosco` | `owasp-llm` + `iosco` | **P** IOSCO counts |
| F-12 | Same fixture, default mode | `owasp-llm` + `iosco` | **F** `missing obligation` |
| F-13 | Risk with IOSCO **and** EU AI Act, default mode | both | **P** EU AI Act satisfies it |

## 3. Cap check

| ID | Case | Fixture | Expected |
|---|---|---|---|
| C-01 | Exactly 3 from one standard (boundary) | 3 keys | **P** not flagged |
| C-02 | Exactly 4 from one standard (boundary) | 4 keys | **F** 1 over cap |
| C-03 | Zero references | none | **P** not flagged |
| C-04 | Two standards both over cap on one item | 5 + 4 keys | **F** both reported |
| C-05 | 3 each from four standards (12 total) | 3×4 | **P** cap is per standard, not per item |
| C-06 | Cap check does not depend on lens | standard with no lens, 5 keys | **F** still flagged |

## 4. Reverse coverage

| ID | Case | Fixture | Expected |
|---|---|---|---|
| R-01 | Library entry cited by an item | 1 of 2 entries cited | used=1, unused=1 |
| R-02 | Library entry cited by nobody | no citations | unused = all |
| R-03 | Item cites a key absent from the library | `owasp-llm: [nope-99]` | **F** dangling citation |
| R-04 | Item cites an entry marked `superseded_by` | old key cited | **F** superseded still cited |
| R-05 | Superseded entry not cited by anyone | old key uncited | **P** not reported |
| R-06 | Citation comes from a use case, not a risk | `_usecases` only | counted as used |

## 5. Robustness

| ID | Case | Fixture | Expected |
|---|---|---|---|
| E-01 | Markdown file with no front matter | bare `# Heading` | skipped, no crash |
| E-02 | Non-conforming filename in a collection | `README.md` | skipped, no crash |
| E-03 | Reference file missing its `lens` | no `lens:` key | warning naming the file; no crash |
| E-04 | Item cites a dataset with no library file | `made-up_references:` | **F** reported, no crash |
| E-05 | Empty collection directory | no `.md` files | no crash, zero items |
| E-06 | Non-markdown file in a collection | `notes.txt` | ignored |
| E-07 | Numeric library key cited (`14:`) | int key both sides | resolves; **not** dangling |
| E-08 | Each finding reported once | broken page + 3 checks | one line, not one per pass |
| E-09 | Repeated key in one list | `llm01` ×4, cap 3 | counts 1 distinct; repeat reported separately |
| E-10 | `docs/_data/references` absent | directory removed | clear message, exit non-zero |

## 6. Integration — against the real repository

Run from a clean checkout of `main`. Record the commit SHA with the results.

| ID | Command | Expected at `67b8c32` |
|---|---|---|
| I-01 | floor, `--lenient-iosco` | exactly 1 risk below floor: `ri-30` |
| I-02 | floor, default (strict) | exactly 7: `ri-24`…`ri-30` |
| I-03 | floor, mitigations | 0 below floor |
| I-04 | reverse coverage | 0 dangling citations |
| I-05 | reverse coverage | 2 superseded cited, both `owasp-llm` on `ri-30` |
| I-06 | cap | 39 of 49 items over cap |
| I-07 | after `scripts/validate-references.py` passes | no `missing lens` warnings |
| I-08 | `--tables` | reproduces the counts in #426: owasp-llm 16/24, eu-ai-act 17/24, iso-42001 20/25, sr11-7 0/24 and 0/25 |
| I-09 | `--warn` with findings | exit 0 |

> I-01/I-02 reproduce the counts claimed in #426. Note the default is strict:
> #426 states IOSCO "supports but doesn't satisfy the floor on its own", so
> `--lenient-iosco` is the opt-out, not the other way round.
> I-05 is resolved by PR #428; re-baseline once it merges.

## 7. Out of scope

- Ranking rules — require human judgement, not mechanically testable.
- Whether exceeding the cap is a defect — depends on the open
  "separate data from display" decision in #426.
- Correctness of any individual mapping — this validates structure, not
  whether a cited clause is the right one.
