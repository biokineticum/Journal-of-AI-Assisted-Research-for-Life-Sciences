# Peer review policy

**Journal of AI-Assisted Research for Life Sciences**

**Status:** draft for adoption (version 0.1, 14 November 2026).

**Language:** English · [Wersja polska](../pl/peer-review-policy.md)

## 1. Principles

The journal uses two review rounds with different jobs.

- **Round 1** is an AI preliminary review. It is done by a model, it is named as such, and it checks completeness, disclosure, consistency, citations, and red flags.
- **Round 2** is expert review by humans. Reviewers assess methodology, interpretation, and novelty, and they say whether the AI use and the human oversight look adequate.
- **The decision** is made by a human editor. A model does not accept, revise, or reject a manuscript.

Review is single-anonymised in this draft: reviewers know who the authors are, and authors are not told the reviewers' names. A reviewer may sign a review. The editor's name is on the decision letter.

The working targets, to be confirmed before launch, are: AI preliminary review within 10 days of a complete in-scope submission; reviewer reports within 21 days of accepting the invitation; first decision within 8 weeks. These are targets, not a promise of a particular outcome.

## 2. Confidentiality

The manuscript, the data supplied for review, the reviews, and the decision are confidential.

The editorial office, editors, and reviewers do not upload any of that material to a public consumer model (a service that may train on inputs, or that has no written no-training and limited-retention terms).

The AI preliminary review runs only on a **permitted deployment**: a local model, or an enterprise or API service under a written agreement that submissions are not used for training and are not retained beyond the review task. The same rule applies to any later AI-assisted check of a revision.

Staff and contractors who handle submissions work under that confidentiality rule. Authors do not post the confidential contents of reviews or decision letters in a public model.

## 3. Overview

1. **Triage** by a human editor: scope, file integrity, and obvious failure to meet the minimum requirements.
2. **Round 1 — AI preliminary review** of in-scope submissions, then a human check of the report before it is released.
3. **Repair**, if the editor asks the authors to fix completeness gaps before human review.
4. **Round 2 — at least two independent human reviewers.**
5. **Decision** by a human editor: accept, minor revision, major revision, or reject.
6. **Revision checks.** A permitted model may help compare the revision with the decision letter. The editor decides whether reviewers see it again.
7. **Acceptance** only when a human editor is satisfied on the science, the ethics, the data, and the disclosure.

Out-of-scope manuscripts are declined at triage and are not sent to a model.

## 4. Triage

A human editor or a delegated member of the editorial office checks that:

- the manuscript is within the [aims and scope](aims-and-scope.md);
- the files open and the required parts listed in the [Author guidelines](author-guidelines.md) are present;
- the authors are humans and no AI tool is listed as an author.

If the manuscript is outside the scope, the editor rejects it with a short reason. If required parts are missing, the office may return it for administrative correction once, or reject it. Triage is not peer review and is not a judgement of novelty.

## 5. Round 1 — AI preliminary review

### 5.1 What it is

The office runs a structured check with a named model and version on a permitted deployment. The check asks the questions in the report template at the end of this policy. It covers:

- completeness and structure of the manuscript;
- presence and adequacy of the AI disclosure, including the prompts supplement and the verification statement;
- consistency between the text, tables, figures, and the deposited data, as far as the files allow;
- citation checks (whether cited items appear to exist and, on a sampled or full check, to support the claims);
- plagiarism and other integrity red flags, together with the journal's similarity software when that service is in place;
- presence and specificity of ethics, consent, registration, and competing-interest statements.

### 5.2 What it is not

The preliminary review does not judge whether the study was worth doing, whether the design was the right one, or whether the interpretation is the best available. It does not confirm that the experiment happened. It does not authenticate images. It does not decide the manuscript.

Model output can be wrong. A citation flagged as fake, a plagiarism hint, or a numerical mismatch is a lead for a human, not a finding, until a person checks it.

### 5.3 Human check before the report is sent

A named member of the editorial office reads the model output before authors or reviewers see it.

- Allegations the staff member cannot reproduce are deleted or marked "not confirmed — not a query for the authors".
- The staff member does not add scientific praise or blame in the model's voice.
- The released report still states which model and version produced the draft, and who checked it.

Authors are not asked to answer an unsupported AI accusation.

### 5.4 Who receives the report

The checked report goes to the authors and to the handling editor. It goes to the Round 2 reviewers with the manuscript. It is kept in the editorial record, together with the model version, the date, the deployment type, and the office prompt.

Under this draft the report is not published with the article. The article states that an AI preliminary review took place. The board may later decide to publish reports. That choice is listed in the [launch roadmap](launch-roadmap.md).

### 5.5 Outcomes of Round 1

The model does not recommend accept or reject. The human editor chooses one administrative outcome:

- **Proceed to human peer review.**
- **Return for completeness.** The editor tells the authors what is missing (for example an unsigned verification, a dead data link, a missing ethics number). This is not a scientific revision.
- **Escalate.** The editor takes an integrity concern — such as a staff-confirmed fabricated citation, numbers that do not match the table, or a missing ethics statement for research that needs one — and handles it under the [Publication ethics](publication-ethics.md) policy. The AI report is a source of checks, not a verdict.

## 6. Between the rounds

Authors asked to repair completeness submit a tracked change and a short reply. The office confirms that the gaps named by the editor are closed. A permitted model may assist that confirmation. The editor releases the file to reviewers.

The manuscript is not sent to Round 2 while the AI disclosure is missing, the raw-data link does not resolve, or a required ethics or registration statement is absent without an accepted explanation.

## 7. Round 2 — human expert peer review

The handling editor invites at least two reviewers with relevant expertise who have no competing interest that would block them. Reviewers are human researchers or practitioners. A model is not invited as a reviewer.

The editor may invite an additional reviewer for statistics, methods, or a second discipline. If the two reports conflict, the editor may invite a third reviewer or decide on the basis of the reports, the manuscript, and the editor's own reading. The decision letter explains the basis.

Reviewers receive:

- the manuscript and the figures;
- the AI Disclosure Statement and the prompts supplement;
- access to the deposited data and code, or to the review-only access route;
- the checked AI preliminary report;
- this policy's questions.

Suggested reports are returned within 21 days. The office sends one reminder. A reviewer who cannot finish is replaced. The identity of a replacement is not shared with the authors if the review is anonymised.

A reviewer who completes a review receives a discount voucher toward the APC of their own future article. The discount is set by the editorial office and published on the site.

## 8. What human reviewers are asked

Reviewers comment on:

1. whether the design can answer the question, and whether the methods are reported in enough detail to repeat the study;
2. whether the analysis matches the design, and whether the numbers in the text match the tables and figures;
3. whether the interpretation stays within the data;
4. what the study adds, without mistaking novelty for a reason to ignore a sound null result;
5. whether ethics, consent, registration, and data availability are adequate for the design;
6. **whether the disclosed AI use is appropriate and whether human oversight looks adequate** for the text, the code, the figures, the numbers, and the citations;
7. any citation that does not exist or does not support the claim;
8. any sign that primary data or primary-data images were generated or altered by a model.

Reviewers are not asked to re-run every analysis. They are asked to say if the deposited material is insufficient to support the claims.

A reviewer who believes the disclosure is incomplete, or that oversight was inadequate, says so plainly. That comment is grounds for the editor to query the authors. It is not, by itself, a recommendation the editor must follow without reading the manuscript.

## 9. Reviewer conduct

Reviewers:

- declare competing interests before accepting, including recent collaboration, a shared institution where the conflict is real, or a financial interest in the intervention or tool under study;
- treat the files as confidential, including after a recommendation is filed;
- do not use a public consumer model on the manuscript, the data, the AI report, or the review;
- if they use a permitted deployment at all, tell the editor which tool and version, and confirm the no-training terms — the review they submit is still their own judgement;
- do not ask authors to cite the reviewer's work unless it is necessary for the science;
- do not contact the authors directly about the submission;
- notify the office if they recognise a manuscript they cannot assess fairly.

The editorial office does not use AI-generated reviewer suggestions from a public consumer model. Suggestions from a permitted tool, if any are used later, are checked by the editor against real publications and conflicts before an invitation is sent.

## 10. The decision

A human editor makes the decision and signs the letter. The editor reads the manuscript, the AI report, and the human reviews. The editor is not bound to follow a recommendation that is unreasoned, hostile, or at odds with the journal's policies. The editor does not follow a recommendation to accept a paper whose disclosure, data, or ethics statements fail the journal's minimum requirements.

| Decision | Meaning |
| --- | --- |
| Accept | The editor is satisfied. Remaining changes are limited to production queries. |
| Minor revision | Specified changes, usually checked by the editor. Human re-review is optional. |
| Major revision | Substantial changes. Human re-review is the default. Acceptance is not promised. |
| Reject | The manuscript will not proceed. A new submission of the same study is allowed only if the editor's letter says so. |

There is no paid fast track, and no decision is exchanged for a citation or a fee. A fixed article processing charge is billed only after acceptance. Editors and reviewers deciding on a paper do not see payment status.

An editor does not decide a manuscript they wrote, or one where a competing interest makes a fair decision unreasonable. Another editor handles that file. If every editor is conflicted, the journal asks a guest editor from outside the board and records the arrangement.

## 11. Revisions and later AI checks

Authors respond point by point. They update the AI Disclosure Statement if any new tool, or any new use, entered the revision. A quiet expansion of AI use at revision is undisclosed use.

The office may run a permitted model to list what changed against the decision letter and whether previously flagged numbers, links, and citations now match. A human editor reads that list. Where the revision changes the analysis, the sample, the interpretation, or the images, the editor sends it back to at least one human reviewer unless both reviewers had already confined their requests to items the editor can check directly.

## 12. Appeals

Authors may appeal a rejection once, in writing, to [EMAIL], within 30 days of the decision. The appeal states the factual or procedural error. It is not a resubmission.

A human editor who was not the deciding editor handles the appeal when the board has more than one editor. That editor may consult a new reviewer. The AI preliminary report is not an appealable decision, because it is not a decision. The outcome of the appeal is accept the appeal and obtain further review, invite a revision, or uphold the rejection. The appeal decision is final for that manuscript.

Complaints about conduct, bias, or undisclosed AI use follow the [Publication ethics](publication-ethics.md) policy.

## 13. What readers are told

The published article states that review comprised an AI preliminary review and human expert review, and that a human editor made the decision. It does not name the reviewers unless they have chosen to sign and the board has agreed to publish that signature.

The model name and version used for Round 1 are recorded in the editorial file. The board decides, before launch, whether the model name is also printed on the article. Until that decision, the public line does not invent a model name. See the [launch roadmap](launch-roadmap.md).

## 14. Related documents

- [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md)
- [Publication ethics](publication-ethics.md)
- [Author guidelines](author-guidelines.md)

---

## Appendix. AI preliminary review — report template

The office copies this template for each manuscript. Text in brackets is replaced. The released report keeps the notice at the top.

---

### AI PRELIMINARY REVIEW

**This report was drafted by an AI system and checked by a member of the editorial office. It is not peer review and it is not a decision.**

| Field | Entry |
| --- | --- |
| Journal | Journal of AI-Assisted Research for Life Sciences |
| Manuscript ID | [ID] |
| Title | [TITLE] |
| Date of the model run | [YYYY-MM-DD] |
| Model and version | [MODEL AND VERSION] |
| Deployment | [local / enterprise — provider]. No-training and limited retention: [yes, contract reference] |
| Office prompt version | [identifier of the internal prompt, kept on file] |
| Human checker | [ROLE, not a public reviewer name — e.g. Editorial office]. Date checked: [YYYY-MM-DD] |
| Similarity software | [TOOL NAME AND VERSION, or "not yet used"] |

**Notice to authors and reviewers.** The model does not decide acceptance. It does not establish that the study took place. Flags below are queries only where the human checker has confirmed them. Items marked "not confirmed" require no response.

### Checklist

Use **Met**, **Gap**, or **Not assessed**. Every Gap has a one-sentence note. Every Not assessed states why (for example "full texts of citations were not available to the model").

| # | Question | Result | Note |
| --- | --- | --- | --- |
| 1 | Required sections are present for this article type (title, human authors and affiliations, structured abstract, keywords, introduction, methods, results, discussion, data availability, ethics, AI disclosure pointer, funding, competing interests, references). | | |
| 2 | The byline lists humans only. No model, company, or software product is an author. | | |
| 3 | The AI Disclosure Statement is present and names tools, versions, access mode, uses, the prompts file, and the human verifiers. | | |
| 4 | The statement matches the manuscript (tools mentioned in the text are disclosed; disclosed uses appear where claimed). | | |
| 5 | If no AI was declared, nothing in the file contradicts that declaration. | | |
| 6 | A data availability statement gives a repository and an identifier. The identifier resolves, or the failure is described. | | |
| 7 | Spot check: numbers in the abstract and results match the tables and figures. List each mismatch. | | |
| 8 | Spot check: a competent reader could connect the reported analyses to the deposited files. | | |
| 9 | Citations: state how many were checked and by which method. List items that do not appear to exist or do not support the claim, only if the human checker confirmed the list. | | |
| 10 | Similarity / plagiarism screen: tool, score if any, and what the human checker concluded. Overlap limited to methods boilerplate is described as such. | | |
| 11 | Ethics, consent, animal welfare, permits, and trial or protocol registration are present and specific, or a reasoned "not applicable" is present. | | |
| 12 | Competing interests and funding are stated, including "none" where that is the claim. | | |
| 13 | Figure rules: primary-data images are presented as original captures; AI-assisted plots are disclosed; no obvious generative artifact is left undescribed. The model cannot authenticate an image. | | |
| 14 | The relevant reporting guideline is named (CONSORT, STROBE, ARRIVE, PRISMA, or another from the author guidelines), and the checklist is present when the guideline expects one. | | |
| 15 | The study design is empirical work conducted by humans, as far as the text and files show. Simulations are labelled as simulations. | | |

### Red flags the human checker confirmed

[None / list, each with the location in the file and what was checked by hand.]

### Leads the human checker did not confirm

[None / list, marked not for the authors.]

### What this review did not assess

- scientific novelty and importance;
- whether the design was appropriate beyond obvious internal gaps;
- whether the data were really collected;
- the truth of unaudited image files;
- the correctness of analyses that were not recomputed.

### Administrative recommendation to the editor

Tick one. Do not tick an accept or reject decision.

- [ ] Proceed to human peer review
- [ ] Return to authors for completeness (list the gaps)
- [ ] Escalate to the handling editor as an integrity concern (list the confirmed flags)

**Human checker sign-off:** I read this report and removed or marked unconfirmed allegations. Signature / name and date: [NAME, ROLE, DATE]

---

### Internal prompt — minimum instructions

The office uses a written prompt that includes at least the following instructions, stored with a version identifier:

1. You are performing an AI preliminary review for the *Journal of AI-Assisted Research for Life Sciences*. You do not recommend acceptance or rejection.
2. Use only the files provided. Do not browse, and do not send the files to any other service.
3. Complete the checklist. Use Met, Gap, or Not assessed.
4. Do not invent citations, quotations, or numerical mismatches. If you cannot check an item, mark it Not assessed.
5. Do not rewrite the manuscript.
6. Treat the files as confidential.
