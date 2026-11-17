# Peer review policy

**Journal of AI-Assisted Research for Life Sciences**

**Status:** draft for adoption (version 0.1, 14 November 2026).

**Language:** English · [Wersja polska](../pl/peer-review-policy.md)

## 1. Principles

The journal uses two review rounds with different jobs.

- **Round 1** is an AI preliminary review. It is a multi-agent check, named as such, inspired by the ScholarPeer design and adapted for this journal (section 5). It checks literature context, missed baselines and datasets, claims, the match between the manuscript and the deposited data, reporting and ethics, and citations. It does not decide.
- **Round 2** is expert review by humans. Reviewers assess methodology, interpretation, and novelty, and they say whether the AI use and the human oversight look adequate.
- **The decision** is made by a human editor. A model does not accept, revise, or reject a manuscript.

Review is single-anonymised in this draft: reviewers know who the authors are, and authors are not told the reviewers' names. A reviewer may sign a review. The editor's name is on the decision letter.

The working targets, to be confirmed before launch, are: AI preliminary review within 10 days of a complete in-scope submission; reviewer reports within 21 days of accepting the invitation; first decision within 8 weeks. These are targets, not a promise of a particular outcome.

## 2. Confidentiality

The manuscript, the data supplied for review, the code, the reviews, and the decision are confidential.

The AI preliminary review, and any later AI-assisted check of a revision, runs exclusively on **locally hosted models**. These are open-weight language models that the journal runs on infrastructure it controls. Manuscripts, datasets, analysis code, and reviewer materials are never sent to an external or third-party AI API. A written promise that the provider will not train on the files does not make an outside API acceptable. The files do not leave the journal's infrastructure.

Literature context and citation verification need lookups the local model cannot do from the files alone. Those lookups may use a literature database, a DOI resolver, Crossref, PubMed, or a web search. What leaves the infrastructure is a generic search query or a bibliographic identifier (a DOI, a PMID, a title, or an author-year string from a reference). Manuscript text, data, code, reviews, and anything that identifies the submitting authors do not leave. If a query cannot be written within that limit, the office supplies a literature pack and the report says the lookup was not run.

Staff, editors, and reviewers do not upload the manuscript, the data, the code, or the reviews to an external AI service. Authors do not post the confidential contents of reviews or decision letters in any AI tool.

## 3. Overview

1. **Triage** by a human editor: scope, file integrity, and obvious failure to meet the minimum requirements.
2. **Round 1 — AI preliminary review** of in-scope submissions, then a human check of the report before it is released.
3. **Repair**, if the editor asks the authors to fix completeness gaps before human review.
4. **Round 2 — at least two independent human reviewers.**
5. **Decision** by a human editor: accept, minor revision, major revision, or reject.
6. **Revision checks.** The same locally hosted models may help compare the revision with the decision letter. The revision is not sent to an external AI API. The editor decides whether reviewers see it again.
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

The office runs a structured, multi-agent preliminary review on infrastructure it controls, using open-weight models it hosts itself. No component calls an external or third-party AI API. The design is inspired by ScholarPeer, the reviewer agent described by Jinsung Yoon and Tomas Pfister in the Google Research blog post "Improving the academic workflow: introducing two AI agents for better figures and peer review" (8 April 2026): [research.google/blog](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/).

That post is a design source. It is not a dependency. The journal does not require ScholarPeer, Google, or any other named product, and it does not send the manuscript to those providers. The components below are implemented with the local models and scripts the office has logged. ScholarPeer, as described there, was evaluated on machine-learning papers and on automated-review benchmarks. It was not evaluated as a reviewer of health, sport, or other life-science manuscripts. This journal adapts the architecture to those manuscripts and adds the checks the published description does not provide.

Every tool, model, and version, and the infrastructure it ran on, is written into the report and into the editorial file. A run that does not name them is not a complete Round 1.

The pipeline has the following components. Each one writes into the same report. None of them recommends acceptance or rejection.

**Literature context (sub-domain historian).** A short, sourced note on the sub-field the manuscript claims to sit in, drawn from published literature. It is context for the later checks. It is not a literature review the journal publishes, and it is not a verdict on novelty.

**Missed baselines and datasets.** A look for standard datasets, comparators, or reference methods that the manuscript does not mention. A hit is a question to the authors or the reviewers. It is not a finding that the authors failed.

**Multi-aspect claim verification.** Questions and answers about the claims, across design, measurement, analysis, and interpretation. Each answer points to a passage or a file. Disagreement between the answer and the manuscript is recorded as a question, not as a decision.

**Data–manuscript consistency.** This component is specific to this journal. Every number, statistic, and conclusion in the manuscript is checked against the deposited dataset and the deposited code, under the [Data availability and FAIR policy](data-availability-and-fair-policy.md). The check includes a manuscript drafted with AI. Where the deposited code can be run on that same local infrastructure, the analyses are re-run and the output is compared with the text, the tables, and the data figures. Data under controlled access are read only inside that environment. They are not copied out in order to run the check. A value that cannot be recomputed is marked "Not assessed", with the reason (a missing file, code that does not run, or data the local environment is not allowed to hold). The findings go in the data-consistency section of the report.

**Reporting, ethics, and registration.** This component is specific to this journal. The manuscript is checked against the reporting guideline that fits the design. The working list is the table in the [Author guidelines](author-guidelines.md): CONSORT, STROBE, PRISMA, ARRIVE, SPIRIT, and the others named there. The [EQUATOR Network](https://www.equator-network.org/) is the index the office uses to confirm which guideline and which current version apply. The check also asks whether ethics approval and trial or study registration are present and specific, or whether a reasoned "not applicable" is present.

**Citation existence and accuracy.** This component is specific to this journal. Cited items are checked for existence, and the cited passage is checked against the claim it is attached to. The purpose is to catch hallucinated references and citations that do not support the sentence. An item the checker cannot open is "Not assessed". It is not labelled fake. A human confirms any item that is put to the authors as missing or mismatched, as section 5.3 requires.

The same run still covers completeness and structure, the presence and adequacy of the AI disclosure (including the prompts supplement and the verification statement), and plagiarism or other integrity red flags, together with the journal's similarity software when that service is in place. Those questions are in the checklist at the end of this policy.

The manuscript, the dataset, and the code stay on the journal's infrastructure for every component. Literature context and citation verification are the exception that needs an outside lookup, and only in the narrow sense in section 2: a literature database, a DOI resolver, Crossref, PubMed, or a web search, and only a generic query or a bibliographic identifier. If that lookup cannot be done within the limit, the office supplies a literature pack and the report says so.

The output is one structured report:

- a summary;
- strengths;
- weaknesses;
- questions to the authors;
- data-consistency findings;
- the checklist in the appendix.

The checked report is shared with the human reviewers and with the editor, and with the authors as section 5.4 describes. The report never makes the decision. A human editor decides.

### 5.2 What it is not

The preliminary review does not judge whether the study was worth doing, whether the design was the right one, or whether the interpretation is the best available. It does not confirm that the experiment happened. It does not authenticate images. It does not decide the manuscript.

Strengths, weaknesses, and questions are material for the human reviewers and the editor. They are not a score. A fluent weakness is still only a lead until a person checks it.

Model output can be wrong. A citation flagged as fake, a plagiarism hint, or a numerical mismatch is a lead for a human, not a finding, until a person checks it.

### 5.3 Human check before the report is sent

A named member of the editorial office reads the model output before authors or reviewers see it.

- Allegations the staff member cannot reproduce are deleted or marked "not confirmed — not a query for the authors".
- The staff member does not add scientific praise or blame in the model's voice.
- The released report still states which model and version produced the draft, and who checked it.

Authors are not asked to answer an unsupported AI accusation.

### 5.4 Who receives the report

The checked report goes to the authors and to the handling editor. It goes to the Round 2 reviewers with the manuscript. It is kept in the editorial record, together with every tool, model, and version used in the run, the infrastructure they ran on, the date, and the office prompt. A single model name, when one model drafted the narrative and others were not used, is recorded as such.

Under this draft the report is not published with the article. The article states that an AI preliminary review took place. The board may later decide to publish reports. That choice is listed in the [launch roadmap](launch-roadmap.md).

### 5.5 Outcomes of Round 1

The model does not recommend accept or reject. The human editor chooses one administrative outcome:

- **Proceed to human peer review.**
- **Return for completeness.** The editor tells the authors what is missing (for example an unsigned verification, a dead data link, a missing ethics number). This is not a scientific revision.
- **Escalate.** The editor takes an integrity concern — such as a staff-confirmed fabricated citation, numbers or conclusions that do not match the deposited data or a recomputed analysis, a data figure supplied as a generated image, or a missing ethics statement for research that needs one — and handles it under the [Publication ethics](publication-ethics.md) policy. The AI report is a source of checks, not a verdict.

## 6. Between the rounds

Authors asked to repair completeness submit a tracked change and a short reply. The office confirms that the gaps named by the editor are closed. A locally hosted model may assist that confirmation. The manuscript is not sent to an external AI API for it. The editor releases the file to reviewers.

The manuscript is not sent to Round 2 while the AI disclosure is missing, the data identifier does not resolve, the reviewers cannot open the deposit (including a controlled-access route), or a required ethics or registration statement is absent without an accepted explanation. See the [Data availability and FAIR policy](data-availability-and-fair-policy.md).

## 7. Round 2 — human expert peer review

The handling editor invites at least two reviewers with relevant expertise who have no competing interest that would block them. Reviewers are human researchers or practitioners. A model is not invited as a reviewer.

The editor may invite an additional reviewer for statistics, methods, or a second discipline. If the two reports conflict, the editor may invite a third reviewer or decide on the basis of the reports, the manuscript, and the editor's own reading. The decision letter explains the basis.

Reviewers receive:

- the manuscript and the figures;
- the AI Disclosure Statement and the prompts supplement;
- access to the deposited data and code, or to the review-only access route, already open at submission;
- the checked AI preliminary report, including the data-consistency findings;
- this policy's questions.

A submission whose data the reviewers cannot open does not go to Round 2.

Suggested reports are returned within 21 days. The office sends one reminder. A reviewer who cannot finish is replaced. The identity of a replacement is not shared with the authors if the review is anonymised.

A reviewer who completes a review receives a discount voucher toward the APC of their own future article. The discount is set by the editorial office and published on the site.

## 8. What human reviewers are asked

Reviewers comment on:

1. whether the design can answer the question, and whether the methods are reported in enough detail to repeat the study;
2. whether the analysis matches the design, and whether the numbers in the text match the tables, the figures, and the data-consistency section of the AI report;
3. whether the interpretation stays within the data;
4. what the study adds, without mistaking novelty for a reason to ignore a sound null result;
5. whether ethics, consent, registration, and data availability are adequate for the design;
6. **whether the disclosed AI use is appropriate and whether human oversight looks adequate** for the text, the code, the figures, the numbers, and the citations;
7. any citation that does not exist or does not support the claim;
8. any sign that primary data, primary-data images, or a data figure were generated or altered by a model. A statistical plot supplied as a generated image, rather than as the output of the deposited code, is such a sign.

Reviewers are not asked to re-run every analysis. They are asked to say if the deposited material is insufficient to support the claims.

A reviewer who believes the disclosure is incomplete, or that oversight was inadequate, says so plainly. That comment is grounds for the editor to query the authors. It is not, by itself, a recommendation the editor must follow without reading the manuscript.

## 9. Reviewer conduct

Reviewers:

- declare competing interests before accepting, including recent collaboration, a shared institution where the conflict is real, or a financial interest in the intervention or tool under study;
- treat the files as confidential, including after a recommendation is filed;
- do not upload the manuscript, the data, the code, the AI report, or the review to any external or third-party AI service, including an API. The prohibition is the same as the journal's own rule in section 2;
- if they use a model at all, it runs locally under their own control, and they tell the editor the model name and version. The review they submit is still their own judgement;
- do not ask authors to cite the reviewer's work unless it is necessary for the science;
- do not contact the authors directly about the submission;
- notify the office if they recognise a manuscript they cannot assess fairly.

The editorial office does not obtain reviewer suggestions from an external AI service. Suggestions from a locally hosted tool, if any are used later, are checked by the editor against real publications and conflicts before an invitation is sent.

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

The office may run a locally hosted model to list what changed against the decision letter and whether previously flagged numbers, links, and citations now match. The revision is not sent to an external AI API. A human editor reads that list. Where the revision changes the analysis, the sample, the interpretation, or the images, the editor sends it back to at least one human reviewer unless both reviewers had already confined their requests to items the editor can check directly.

## 12. Appeals

Authors may appeal a rejection once, in writing, to [EMAIL], within 30 days of the decision. The appeal states the factual or procedural error. It is not a resubmission.

A human editor who was not the deciding editor handles the appeal when the board has more than one editor. That editor may consult a new reviewer. The AI preliminary report is not an appealable decision, because it is not a decision. The outcome of the appeal is accept the appeal and obtain further review, invite a revision, or uphold the rejection. The appeal decision is final for that manuscript.

Complaints about conduct, bias, or undisclosed AI use follow the [Publication ethics](publication-ethics.md) policy.

## 13. What readers are told

The published article states that review comprised an AI preliminary review and human expert review, and that a human editor made the decision. It does not name the reviewers unless they have chosen to sign and the board has agreed to publish that signature.

Every tool, model, and version used for Round 1, and the infrastructure they ran on, is recorded in the editorial file and in the report. The board decides, before launch, whether those names are also printed on the article. Until that decision, the public line does not invent a model name. See the [launch roadmap](launch-roadmap.md).

## 14. Related documents

- [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md)
- [Data availability and FAIR policy](data-availability-and-fair-policy.md)
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
| Infrastructure | Journal-controlled host: [description]. Open-weight models, self-hosted. External AI API: no. |
| External lookups | [none / literature database, Crossref, PubMed, DOI resolver, web search]. What left the host: [generic queries and bibliographic identifiers only / none] |
| Office prompt version | [identifier of the internal prompt, kept on file] |
| Human checker | [ROLE, not a public reviewer name — e.g. Editorial office]. Date checked: [YYYY-MM-DD] |
| Similarity software | [TOOL NAME AND VERSION, or "not yet used"] |
| Data seen by the check | [open deposit / controlled-access route / human-only for named files]. Identifier: [DOI OR ACCESSION] |

**Tools, models, and versions used in this run.** One row per component. If one model performed every component, say so on each row. A component that was not run is marked "not run" with the reason.

| Component | Tool or model | Version | What it was allowed to see |
| --- | --- | --- | --- |
| Literature context (sub-domain historian) | | | Published literature only / literature pack supplied by the office |
| Missed baselines and datasets | | | |
| Multi-aspect claim verification | | | |
| Data–manuscript consistency | | | Deposited dataset and code, within the access terms |
| Reporting, ethics, and registration | | | Manuscript, checklist, EQUATOR guideline named: [NAME, VERSION] |
| Citation existence and accuracy | | | |
| Narrative assembly of this report | | | |

**Notice to authors and reviewers.** The model does not decide acceptance. It does not establish that the study took place. Strengths, weaknesses, and questions are not a score. Flags below are queries only where the human checker has confirmed them. Items marked "not confirmed" require no response.

### Summary

[Five to ten sentences. What the manuscript claims, what was checked against the deposit, and what was not checked.]

### Strengths

[Bullets a human checker is willing to leave in the report. No praise the checker has not read.]

### Weaknesses

[Bullets. Each one points to a passage, a file, or a checklist row. Unconfirmed items do not appear here.]

### Questions to the authors

[Numbered questions that follow from confirmed gaps. No question that restates an unconfirmed allegation.]

### Data-consistency findings

| Item in the manuscript | Value as printed | Value from the deposit or the re-run | Re-run? | Result |
| --- | --- | --- | --- | --- |
| [e.g. Abstract, primary outcome] | | | [yes / not run — reason] | [match / mismatch / not assessed] |

Analyses re-run: [list scripts, or "none — reason"]. Conclusions that do not follow from the recomputed or deposited numbers: [none / list].

### Checklist

Use **Met**, **Gap**, or **Not assessed**. Every Gap has a one-sentence note. Every Not assessed states why (for example "full texts of citations were not available to the model").

| # | Question | Result | Note |
| --- | --- | --- | --- |
| 1 | Required sections are present for this article type (title, human authors and affiliations, structured abstract, keywords, introduction, methods, results, discussion, data availability, ethics, AI disclosure pointer, funding, competing interests, references). | | |
| 2 | The byline lists humans only. No model, company, or software product is an author. | | |
| 3 | The AI Disclosure Statement is present and names tools, versions, access mode, uses, the prompts file, and the human verifiers. | | |
| 4 | The statement matches the manuscript (tools mentioned in the text are disclosed; disclosed uses appear where claimed). | | |
| 5 | If no AI was declared, nothing in the file contradicts that declaration. | | |
| 6 | The data availability statement names the repository, a persistent identifier, the licence, and the files (dataset, code, codebook, README). The identifier resolves. The AI review and the human reviewers can open the deposit, or the controlled-access route is described and open to them. | | |
| 7 | Every number, statistic, and conclusion in the abstract, results, tables, figures, and discussion was checked against the deposited dataset and code. State which analyses were re-run and which could not be. List each mismatch. | | |
| 8 | Open or standard formats, a codebook, and a README are present, and a competent reader could repeat the reported analyses from the deposit. | | |
| 9 | Citations: state how many were checked for existence and for whether the cited passage supports the claim, and by which method. List items that do not appear to exist or do not support the claim, only if the human checker confirmed the list. Do not label an unopened item as fake. | | |
| 10 | Similarity / plagiarism screen: tool, score if any, and what the human checker concluded. Overlap limited to methods boilerplate is described as such. | | |
| 11 | Ethics, consent, animal welfare, permits, and trial or protocol registration are present and specific, or a reasoned "not applicable" is present. | | |
| 12 | Competing interests and funding are stated, including "none" where that is the claim. | | |
| 13 | Figure rules: primary-data images are original captures; an AI-assisted methodology or schematic diagram is disclosed and does not display data; data figures and statistical plots come from the deposited code and are not generated images. The model cannot authenticate an image. | | |
| 14 | The relevant reporting guideline is named from the EQUATOR Network (CONSORT, STROBE, ARRIVE, PRISMA, SPIRIT, or another from the author guidelines), the version is the current one, and the checklist is present when the guideline expects one. | | |
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
- the correctness of analyses that the report marks as not recomputed;
- whether the manuscript should be accepted, revised, or rejected.

### Administrative recommendation to the editor

Tick one. Do not tick an accept or reject decision.

- [ ] Proceed to human peer review
- [ ] Return to authors for completeness (list the gaps)
- [ ] Escalate to the handling editor as an integrity concern (list the confirmed flags)

**Human checker sign-off:** I read this report and removed or marked unconfirmed allegations. Signature / name and date: [NAME, ROLE, DATE]

---

### Internal prompt — minimum instructions

The office uses a written prompt that includes at least the following instructions, stored with a version identifier:

1. You are performing an AI preliminary review for the *Journal of AI-Assisted Research for Life Sciences*. You do not recommend acceptance or rejection. You do not score the manuscript.
2. You are running on journal-controlled infrastructure. Do not call an external AI API. Do not send the manuscript, the data, the code, or anything that identifies the authors to any other service. A literature or citation lookup may send only a generic query or a bibliographic identifier (a DOI, a PMID, a title, or an author-year string). If you cannot look something up within that limit, say that the office must supply a literature pack.
3. Complete the structured report: summary, strengths, weaknesses, questions to the authors, data-consistency findings, and the checklist. Use Met, Gap, or Not assessed on the checklist.
4. When checking numbers, compare them with the deposited data and code. Re-run an analysis only inside this deployment, and only when the deposited code runs. If you cannot re-run it, mark it Not assessed and say why. Do not invent a mismatch.
5. Do not invent citations, quotations, ethics numbers, or repository identifiers. If you cannot open a citation, mark it Not assessed. Do not call it fake.
6. Do not rewrite the manuscript.
7. Treat the files as confidential.
8. Name the tool and version you are. The office adds the rest of the tool log.
