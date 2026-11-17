# AI use and disclosure policy

**Journal of AI-Assisted Research for Life Sciences**

**Status:** draft for adoption (version 0.1, 14 November 2026). This text is written so it can be published on the journal website after the publisher adopts it. Until then it is not in force.

**Language:** English · [Wersja polska](../pl/ai-use-and-disclosure-policy.md)

## 1. Purpose

Authors may use artificial intelligence when they prepare a manuscript. The journal requires them to say exactly how, and to remain responsible for every sentence they sign.

This policy follows the position of the Committee on Publication Ethics (COPE) and the International Committee of Medical Journal Editors (ICMJE): a language model cannot meet authorship criteria, and use of AI-assisted technology is disclosed. It also follows the confidentiality duty in the [COPE guidelines on editors and reviewers](https://publicationethics.org/guidance): unpublished submissions are not pasted into public tools that may train on them.

The operational form authors fill in is the [AI Disclosure Statement](ai-disclosure-statement.md).

## 2. Definitions

| Term | Meaning in this journal |
| --- | --- |
| AI tool | A generative or machine-learning system used to produce or transform text, code, images, audio, or suggestions. Spell-checkers that only flag typos, and grammar tools that do not generate sentences, need not be listed. When in doubt, disclose the tool. |
| Primary data | The observations, measurements, images, recordings, and transcripts produced by the study, as collected. |
| Raw data | Primary data in the form first recorded, before statistical summary, complete enough for a competent researcher to repeat the reported analyses. |
| Modify primary data | To create, impute, delete, replace, or selectively alter observations by a model. A human-specified cleaning rule, written in deposited code and applied by the authors, is processing and must be described in the Methods. It is not permission for a model to invent or rewrite observations. |
| Public consumer model | A chatbot or similar service where the provider may train on inputs, or where no contract forbids training and long-term retention. |
| Permitted deployment | For authors preparing a manuscript: a local model, or an enterprise or API service under a written agreement that the submission and any prompts are not used to train models and are not retained beyond the task. This is not the rule for the journal's own review. |
| Journal-hosted model | An open-weight language model that the journal runs on infrastructure it controls. Round 1, and any later editorial check of a submission, uses only these models. An external or third-party AI API is not a journal-hosted model, even under a no-training contract. |

## 3. Authorship

Authors are humans. Each author must meet all four ICMJE criteria:

1. substantial contribution to the conception or design, or to the acquisition, analysis, or interpretation of the data;
2. drafting the work or revising it critically for important intellectual content;
3. final approval of the version to be published;
4. agreement to be accountable for all aspects of the work, and to ensure that questions about accuracy or integrity are investigated and resolved.

An AI tool meets none of these. It is not listed as an author, co-author, or corresponding author, and it is not thanked as if it were a colleague who did the study. The place for the tool is the AI Disclosure Statement.

Humans who qualify are listed even when a tool drafted the prose. Humans who do not qualify are named in the Acknowledgements, not in the byline. Gift, guest, and ghost authorship are misconduct. See [Publication ethics](publication-ethics.md).

The corresponding author confirms that every listed person has approved the manuscript and the disclosure, and that no qualified person has been omitted.

## 4. The empirical-work rule

Empirical results in this journal come from work humans conducted.

Eligible work includes experiments, observational studies, trials, fieldwork, laboratory measurement, imaging, interviews and other qualitative collection, and reanalysis of a real dataset the authors are allowed to use. A simulation is eligible only as a simulation: the authors ran it, the manuscript says so, and the code and seeds are deposited. A simulation is not a substitute for observations the paper presents as real.

The model may help write the paper about that work. The model does not perform the study.

## 5. Permitted uses

Provided the use is disclosed and the product is checked by a human author, AI tools may be used to:

- draft or revise manuscript text from the authors' notes, analysis outputs, and data;
- edit language or translate text;
- suggest a structure for a section the authors then check;
- format references, after the authors have verified each source;
- suggest search queries, while humans design the search, screen records, and extract data;
- write or debug analysis code that a human author reviews, understands, and runs, including the code that generates data figures and statistical plots from the deposited raw data;
- transcribe real recordings, after a human corrects the transcript against the audio and verifies every quotation;
- draft methodology or schematic diagrams that do not display observations, estimates, or test statistics. A tool of the kind described as PaperVizAgent is an example, not a requirement. The use is disclosed, and a human author checks the diagram against the methods.

Permitted use does not weaken accountability. A drafted paragraph is the authors' text once they submit it.

## 6. Prohibited uses

The following are grounds for rejection, and after publication they are handled under the [Publication ethics](publication-ethics.md) policy:

- generating primary data, or presenting model output as measurements, questionnaire responses, images of samples, or participant quotations;
- modifying primary data as defined above, including generative imputation of outcomes;
- creating or "enhancing" a primary-data image so that it shows detail the capture did not contain;
- producing a data figure or a statistical plot as a generated image, rather than from code run on the deposited raw data;
- presenting an AI-drawn schematic as if it displayed measured results;
- listing an AI tool as an author;
- inserting a citation that no human author has opened and checked;
- inventing a funder, an ethics-approval number, a registration number, a repository identifier, a reviewer, or an affiliation;
- pasting another person's confidential unpublished manuscript, review, or data into any AI tool;
- submitting a manuscript whose disclosure is missing, vague ("AI was used to improve the text"), or contradicted by the manuscript itself.

Disclosure of a prohibited use is not permission. Reporting that a model invented the results leads to rejection. It does not make the results eligible.

## 7. Figures and images

**Primary-data images** — microscopy, blots, gels, photographs of specimens or apparatus, instrument scans, clinical and athlete images — are original captures from the study. They are not generated, inpainted, super-resolved, or replaced by a model.

Linear adjustment of brightness, contrast, or crop is allowed when it is applied to the whole image, does not hide or invent features, and is described when it affects interpretation. Splices, if unavoidable, are marked. Identifiers are removed by cropping or by a solid mask. They are not removed by generative fill.

**Data figures and statistical plots** — any display of observations, estimates, or test statistics, including scatter plots, bar charts, forest plots, survival curves, and Bland–Altman plots — are generated by reproducible code from the deposited raw data. They are not generated images. An image model does not draw them, even when a tool could emit both an illustration and a plot. The authors deposit the script, the input it reads, and the software versions, and a human author who has run the script checks every point, bar, error bar, and label against that output.

**Methodology and schematic diagrams** that do not display observations or estimates (a flow chart of a study design, a measurement sequence, a conceptual diagram) may be AI-assisted. Tools of the kind described as PaperVizAgent, in the same April 2026 Google Research note that describes ScholarPeer, are an example of that kind of assistance. They are not required, and the journal does not depend on that product. The authors disclose the tool, the version, and the figure numbers, and a human author checks that the diagram matches the methods. The journal does not accept the image-generation path for a statistical plot, including from a tool that also offers one.

Composite figures state what each panel is. The journal may ask for the original, unprocessed image files.

## 8. Data and code

AI tools do not generate or modify primary data.

The human-collected dataset and the analysis code are deposited before submission under the [Data availability and FAIR policy](data-availability-and-fair-policy.md): a trusted repository, a persistent identifier (a DOI from Zenodo, OSF, Figshare, Dryad, or a domain accession), rich metadata, open or standard formats, a codebook, a README, and a clear licence (CC BY 4.0 or CC0 for data, unless a privacy rule requires another open or controlled-access regime). The Data Availability Statement is required. It gives the repository, the identifier, the licence, and what was deposited.

Sensitive health data are as open as possible and as closed as necessary. Pseudonymisation under the GDPR is not anonymisation. A controlled-access route is allowed when a statute, a consent form, or biosecurity makes public release unlawful or unsafe. The editor and the reviewers, including the AI preliminary review, still have access at submission. "Available on reasonable request" alone does not meet this policy.

Analysis code is deposited and is readable by a researcher in the field. Code written with AI assistance is disclosed. A human author who understands the code and has run it takes responsibility for it. Code the authors cannot explain is not acceptable. The scripts that build data figures are part of this deposit.

Statistical choices — including any imputation — are human-specified, reported, and distinguished from the raw data. Generative model output is not an imputed dataset.

Further requirements: [Author guidelines](author-guidelines.md).

## 9. Privacy when authors use AI tools

Identifiable participant data, unpublished third-party data, and other confidential material are not pasted into a public consumer model.

Authors use a permitted deployment, or they restrict the prompt to aggregated, de-identified material that they have the right to process that way. Compliance with the EU General Data Protection Regulation and with the study's ethics approval is the authors' duty. A disclosure statement does not cure an unlawful transfer of personal data.

## 10. Mandatory disclosure

Every submission includes a completed [AI Disclosure Statement](ai-disclosure-statement.md), including submissions that used no AI tool.

The statement names:

- each tool, the provider, the model and version, the access mode (local, enterprise with a no-training agreement, or other), and the dates of use;
- exactly what the tool was used for, tied to sections of the manuscript, to code, or to figures;
- the supplementary file that contains the key prompts or a faithful workflow record;
- the named human authors who verified the facts, the numbers, the citations, and the interpretations.

The statement is specific. "ChatGPT was used for language editing" is not enough. The version, the access mode, the sections, and the verification step are required.

The corresponding author uploads the statement as a supplementary file and completes the matching fields in the submission system. The manuscript itself contains a short pointer:

- if tools were used: "Use of AI tools is reported in the AI Disclosure Statement published with this article."
- if no tool was used: "The authors did not use generative AI tools in this work."

A one-line acknowledgement does not replace the statement.

## 11. Prompts and workflow supplement

Authors attach a supplementary file with the key prompts and the workflow.

The file includes, as applicable:

- the tool and version, and the date of each material session;
- the prompts that shaped the Methods, Results, interpretation, code, or figures, or a faithful record of an iterative workflow when there was no single prompt;
- what was given to the model (notes, summary statistics, code, or a described dataset — not a dump of identifiable personal data);
- what the authors kept, edited, or discarded.

Language editing may be documented with the tool and version, a representative prompt, and a statement of which sections were edited. A draft of Results or of the interpretation needs the material prompts, not a sample sentence.

The supplement is published with the article. If a prompt would expose a participant or another person's confidential material, the authors file a redacted public version and give the editor the unredacted file, which is kept in the editorial record.

## 12. Human verification

Before submission, human authors verify the manuscript against the sources of the work. At minimum:

- every number in the abstract, results, tables, and figures matches the analysis output and the deposited data;
- every citation was opened by a human author, exists, and supports the claim attached to it;
- interpretations do not go beyond the data, the design, and the cited literature;
- quotations match the verified transcript or source;
- figures match the data, including labels and units.

The statement names the authors who did the numerical check and the citation check. All authors remain accountable under ICMJE criterion 4. Verification cannot be delegated to the same model that drafted the text.

A false citation is misconduct even when a tool suggested it. Disclosure is the record of tool use. It is not a waiver of the duty to check.

## 13. Publication of the statement

If the article is accepted, the journal publishes:

- the AI Disclosure Statement;
- the prompts and workflow supplement, redacted only as allowed above;
- a line on the article stating that peer review included an AI preliminary review and a human expert review, and that a human editor made the decision.

Readers should not have to guess which parts of the process involved a model.

## 14. Use of AI by the journal

The journal's own use of AI on a submission is limited, labelled, and runs exclusively on journal-hosted models. Manuscripts, datasets, analysis code, and reviewer materials are never sent to an external or third-party AI API. Authors' own tools, disclosed under sections 5 and 9, are a separate matter. The journal does not send the submission to those tools.

**Round 1 — AI preliminary review.** For in-scope submissions, the editorial office runs a multi-agent preliminary review on infrastructure it controls, with open-weight models it hosts itself. No component calls an external AI API. The design is inspired by ScholarPeer (Yoon and Pfister, Google Research blog, 8 April 2026). It is a design source, not a dependency on that product or on any vendor. ScholarPeer was evaluated on machine-learning papers, so this journal adapts it and adds checks for life-science manuscripts. The components are: literature context (a sub-domain historian), a scout for missed baselines and datasets, multi-aspect claim-verification questions and answers, and three checks specific to this journal — data–manuscript consistency (every number, statistic, and conclusion re-checked against the deposited FAIR dataset and code, with analyses re-run where the code can be run), reporting-guideline compliance through the EQUATOR Network (CONSORT, STROBE, PRISMA, ARRIVE, SPIRIT, and the others named in the author guidelines) together with ethics approval and trial or study registration, and citation existence and accuracy, aimed at hallucinated references. Literature context and citation verification may query a literature database, Crossref, PubMed, a DOI resolver, or the public web. Only a generic search query or a bibliographic identifier leaves the infrastructure. Manuscript text, data, code, and author-identifying content do not. Data under controlled access are read only inside the local environment. The output is one structured report: a summary, strengths, weaknesses, questions to the authors, data-consistency findings, and a checklist. Every tool, model, and version, and the infrastructure, is logged in the report and disclosed in the editorial record. A human member of the editorial office reads the report before it is sent, removes any allegation they cannot support, and records that check. The report is shared with the human reviewers and the editor, and with the authors. It never makes the decision. The specification is the [Peer review policy](peer-review-policy.md).

**Editors.** A human editor decides whether the submission proceeds, what the authors must repair, and the final outcome. Editors do not paste submissions into an external AI service.

**Reviewers.** Human reviewers do not upload the manuscript, the data, the code, or their review to any external or third-party AI service. The prohibition is the same as the journal's own rule. A reviewer who uses a model at all runs it locally, tells the editor the model name and version, and remains responsible for the review. Details: [Peer review policy](peer-review-policy.md).

**Revised manuscripts.** The office may use the same locally hosted models to compare a revision with the decision letter and the previous text. The revision is not sent to an external AI API. The editor reads that comparison and decides whether human reviewers should see the revision again.

**Record.** The office keeps every tool, model, and version, the infrastructure they ran on, the date, the prompt used for the editorial check, and the human-edited report. That log is part of the review record.

The journal does not allow submitted manuscripts, reviews, or decision letters to be used as training data.

## 15. Breach

Undisclosed AI use is publication misconduct. The journal applies a zero-tolerance rule: the failure is never waived because the editing "looks minor", and it is never left unrecorded.

- **Before publication.** The submission is rejected. The editor may refuse further submissions from the responsible authors for a period the editor states in writing. Where the breach involves fabricated data, fabricated citations that were material, or a false ethics or registration claim, the editor may notify the authors' institution.
- **After publication.** The journal issues a correction or a retraction and says so publicly. A correction is used when the data, citations, and conclusions remain reliable and the undisclosed use was limited to language or formatting. A retraction is used when numbers, citations, images, or interpretations were produced or altered by a model and were not human-verified, or when the editor can no longer trust the record. See [Publication ethics](publication-ethics.md).

Authors who discover their own omission should tell the editor immediately. Self-reporting is recorded and is taken into account. It does not erase the duty to correct the public record.

## 16. Related documents

- [AI Disclosure Statement (template)](ai-disclosure-statement.md)
- [Data availability and FAIR policy](data-availability-and-fair-policy.md)
- [Peer review policy](peer-review-policy.md)
- [Author guidelines](author-guidelines.md)
- [Publication ethics](publication-ethics.md)
- [Aims and scope](aims-and-scope.md)
