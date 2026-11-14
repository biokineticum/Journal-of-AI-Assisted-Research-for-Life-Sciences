# AI Disclosure Statement

**Journal of AI-Assisted Research for Life Sciences**

**Status:** draft for adoption (version 0.1, 14 November 2026).

**Language:** English · [Wersja polska](../pl/ai-disclosure-statement.md)

This is the mandatory statement for every submission. Upload it as a supplementary file named `AI-disclosure-statement.md` (PDF is acceptable if the content is identical). Complete it in English. If no generative AI tool was used, say so in section 1 and complete sections 4, 6, and 7.

Policy: [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md).

Copy the template below. Replace every bracketed field. Tick the boxes that apply.

---

## Template

### Manuscript

- **Title:** [MANUSCRIPT TITLE]
- **Manuscript ID** (if assigned): [ID or "not yet assigned"]
- **Corresponding author:** [FULL NAME]
- **ORCID of the corresponding author:** [ORCID]
- **Date of this statement:** [YYYY-MM-DD]

### 1. Declaration

Tick one.

- [ ] **No AI tool was used** at any stage of the research, analysis, figures, code, transcription, translation, or writing. Grammar or spell-checkers that do not generate sentences are ignored for this question. Complete sections 4, 6, and 7 only.
- [ ] **One or more AI tools were used.** Complete every section.

### 2. Tools

One row per tool. Add rows as needed.

| # | Tool name | Provider | Model and version | Access mode | Dates of use | Use codes (section 3) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [e.g. a named model] | [provider] | [exact model and version] | [local / enterprise, no-training contract / other — describe] | [YYYY-MM-DD to YYYY-MM-DD] | [e.g. A, D, H] |
| 2 |  |  |  |  |  |  |

If the access mode is "other", state whether inputs may be retained or used for training: [yes / no / unknown]. "Unknown" is not accepted for identifiable participant data. See section 9 of the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md).

### 3. What the tools were used for

Tick every use that occurred. For each ticked item, name the tool number from section 2 and the part of the work (section, figure, file).

- [ ] **A.** Drafting text from the authors' data, analysis outputs, or notes. Detail: [ ]
- [ ] **B.** Drafting or revising these sections: [Introduction / Methods / Results / Discussion / other]. Detail: [ ]
- [ ] **C.** Abstract. Detail: [ ]
- [ ] **D.** Language editing (grammar, clarity, tone) of: [sections]. Detail: [ ]
- [ ] **E.** Translation. From [language] to [language]. Detail: [ ]
- [ ] **F.** Suggesting or formatting references. Detail: [ ]. Every reference was opened and checked by a human author (confirmed in section 6).
- [ ] **G.** Writing or debugging analysis code. Files: [ ]. The human author who reviewed and ran the code: [NAME].
- [ ] **H.** Creating plots or visualisations from the authors' data. Figure numbers: [ ].
- [ ] **I.** Formatting tables or the reference list. Detail: [ ]
- [ ] **J.** Assistance limited to literature-search queries. Humans designed the final search, screened records, and extracted data. Detail: [ ]
- [ ] **K.** Transcription of real recordings. A human corrected the transcript against the audio. Detail: [ ]
- [ ] **L.** Other. Detail: [ ]

### 4. Confirmations

Every box is required, including when section 1 states that no AI tool was used.

- [ ] Primary data were collected or produced by the human authors or their human team, or come from an existing dataset the authors had the right to analyse. Existing dataset (if any): [repository, identifier, licence, or "not applicable"].
- [ ] No AI tool generated primary data.
- [ ] No AI tool modified primary data: it did not create, impute, delete, replace, or selectively alter observations. Any cleaning or transformation was specified by the authors, is described in the Methods, and is in the deposited code.
- [ ] Primary-data images (microscopy, blots, gels, photographs of samples, scans, clinical or field images) are original captures and were not generated or generatively altered.
- [ ] Any AI-assisted plot uses only the real data, was checked against the analysis output, and can be rebuilt from the deposited data and code. Figure numbers, or "not applicable": [ ].
- [ ] No AI tool is listed as an author or credited as a person who carried out the study.
- [ ] No citation appears in the manuscript unless a human author opened the source and confirmed that it exists and supports the claim.

### 5. Prompts and workflow

Required when section 1 records that an AI tool was used.

- **Supplementary file name:** [e.g. AI-workflow.md]
- The file contains the key prompts or a faithful record of the workflow, the tool versions, the dates, what was given to the model, and what the authors kept, edited, or discarded.
- [ ] I confirm the file is attached.
- [ ] The public file is redacted to remove participant identifiers or third-party confidential material. The unredacted file has been provided to the editor. Tick only if this applies: [ ]

### 6. Human verification

- [ ] Human authors verified the facts, the numbers, the citations, and the interpretations in this manuscript.
- **Author responsible for the numerical check** (abstract, results, tables, figures against the analysis output and deposited data): [FULL NAME]
- **Author responsible for the citation check** (each reference opened and matched to the claim): [FULL NAME]
- **How the check was done:** [short description, e.g. comparison with the statistical software output dated YYYY-MM-DD, rebuild of figures from the deposited script, full-text check of references]
- [ ] Quotations, if any, were checked against the verified transcript or the cited source.
- [ ] All human authors have read the final manuscript and this statement and agree to be accountable for the work.

Verification was done by the authors. It was not delegated to the model that drafted the text.

### 7. Approval

- **Corresponding author (signature / typed name):** [FULL NAME]
- **Date:** [YYYY-MM-DD]
- **Email:** [CORRESPONDING AUTHOR EMAIL]

All authors approve this statement. Add named confirmations if the journal's submission system asks for them:

| Author (human) | ORCID | Approved the manuscript and this statement (yes/no) | Date |
| --- | --- | --- | --- |
| [FULL NAME] | [ORCID] | [yes] | [YYYY-MM-DD] |

---

## Example (fictional)

The following example shows the level of detail. It is not a real study and not a real author.

**Title:** Countermovement-jump height in university footballers during a four-week pre-season block: a cohort study

**Declaration:** One or more AI tools were used.

**Tools:**

| # | Tool name | Provider | Model and version | Access mode | Dates of use | Use codes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ExampleLLM | Example Provider | ExampleLLM-Large 2.1 | Enterprise, no-training contract dated 2026-03-01 | 2026-04-02 to 2026-04-09 | A, C, D, H |

**Uses:** A — drafted the Results and Discussion from the authors' analysis notes and the output of the deposited R script `cmj_analysis.R`. C — drafted the abstract from the same notes. D — language editing of the Introduction and Methods. H — drafted Figure 2 (jump height by week) from the deposited CSV; the author checked every point against `cmj_analysis.R`.

**Confirmations:** all ticked. Force-plate files and the session log are the primary data. No observation was imputed by the model. Figure 1 is a photograph of the force-plate setup taken by the authors.

**Workflow file:** `AI-workflow.md`, containing the Results prompt, the figure prompt, a representative language-editing prompt, and a note that a suggested citation to a non-existent paper was discarded after the citation check.

**Verification:** numerical check by [AUTHOR NAME]; citation check by [AUTHOR NAME]; values compared with the R output saved as `cmj_analysis_log.txt`.

---

## Appendix. Submission-system fields

The statement file is the full record. The submission form in Open Journal Systems (OJS) repeats the items below so an incomplete form cannot be sent. Wording may be shortened on screen; the meaning stays the same.

| Form field | Type | Required | Maps to |
| --- | --- | --- | --- |
| AI tools used? | yes / no | yes | Section 1 |
| Tools, versions, access mode, dates | long text | yes if tools were used | Section 2 |
| Use codes and where they apply | long text | yes if tools were used | Section 3 |
| AI did not generate or modify primary data | checkbox | yes | Section 4 |
| Primary-data images are original captures | checkbox | yes | Section 4 |
| AI is not an author | checkbox | yes | Section 4 |
| Every citation was opened and checked by a human author | checkbox | yes | Section 4 |
| Prompts and workflow file uploaded | checkbox | yes if tools were used | Section 5 |
| Facts, numbers, citations, and interpretations were human-verified | checkbox | yes | Section 6 |
| Names of the authors who did those checks | short text | yes | Section 6 |
| All human authors approve this statement | checkbox | yes | Section 7 |

Genre labels for supplementary files: `AI Disclosure Statement` and `AI prompts and workflow`.

The Data Availability Statement, ethics approvals, consent, registration, and competing interests are separate required fields. They are specified in the [Author guidelines](author-guidelines.md) and are not replaced by this statement.
