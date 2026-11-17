# Author guidelines

**Journal of AI-Assisted Research for Life Sciences**

**Status:** draft for adoption (version 0.1, 14 November 2026). Word limits and the reference style are working defaults from the [launch roadmap](launch-roadmap.md).

**Language:** English · [Wersja polska](../pl/author-guidelines.md)

These are the minimum requirements for a submission. Manuscripts that do not meet them are returned or rejected at triage. See also the [Aims and scope](aims-and-scope.md), the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md), the [Data availability and FAIR policy](data-availability-and-fair-policy.md), and [Publication ethics](publication-ethics.md).

## 1. Who may submit

Anyone may submit a manuscript that fits the scope. Authors are humans who meet the ICMJE authorship criteria. There is no submission fee.

The corresponding author writes to the journal from an email the editorial office can verify, holds an ORCID, and is the contact for data, ethics, and the AI disclosure. The office writes to [EMAIL].

## 2. Minimum requirements

A submission is complete only when all of the following are true:

1. The empirical work was conducted by humans, or the manuscript is a systematic review or a letter as defined below.
2. The [AI Disclosure Statement](ai-disclosure-statement.md) is complete, and the prompts file is attached if a tool was used.
3. The human-collected dataset and the analysis code are deposited under the [Data availability and FAIR policy](data-availability-and-fair-policy.md). The identifier resolves. The AI preliminary review and the human reviewers can open the deposit at submission, including a controlled-access route the editor has already accepted.
4. Ethics, consent, animal welfare, permits, and registration are reported where they apply.
5. Primary-data images are original captures. Data figures and statistical plots are produced by code from the deposited data, not as generated images.
6. Competing interests, funding, and author contributions are stated.
7. The reporting guideline that fits the design is followed, and its checklist is uploaded where one exists.

## 3. Article types and working limits

Limits exclude the reference list. They include the abstract.

| Type | Main text | Abstract | Display items |
| --- | --- | --- | --- |
| Original research | up to 6,000 words | structured, up to 300 words | up to 8 figures and tables combined |
| Brief report | up to 2,500 words | structured, up to 200 words | up to 3 |
| Systematic review or meta-analysis | up to 8,000 words | structured, up to 300 words | up to 8, plus a flow diagram |
| Methods article | up to 5,000 words | structured, up to 300 words | up to 6 |
| Data note | up to 2,000 words | unstructured, up to 200 words | up to 4 |
| Letter | up to 800 words | none | up to 1 |

The editor may agree to a longer methods section when reproducibility requires it. Extra material goes in a supplement, not in an inflated main text.

**Original research and brief reports** report a study the authors carried out: an experiment, a trial, an observational study, a qualitative study, or a pre-specified reanalysis.

**Systematic reviews** follow PRISMA 2020. Humans design the search, screen records, extract data, and assess risk of bias. A model may help only within the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md). The protocol is registered (for example on PROSPERO or OSF) before screening, or the authors explain why it was not.

**Methods articles** report a method the authors built and tested. A simulation is identified as a simulation and is accompanied by runnable code and seeds. A methods article does not present simulated observations as real ones.

**Data notes** describe a dataset collected by humans and deposited under a reuse licence. The note states how the data were collected, the ethics basis, the files, the codebook, and what the dataset is for. It is not a second results paper on the same questions already published elsewhere.

**Letters** comment on an article this journal has published. They are sent to the authors of that article for a reply when the editor judges a reply useful.

## 4. Language and style

Articles are in English. A Polish title and a Polish abstract are welcome and are published if supplied.

Write so that a specialist in a neighbouring field can follow the design. Define abbreviations at first use. Use SI units. Report exact sample sizes. Give estimates with confidence intervals, not p-values alone. State how missing data were handled. Do not describe a result as "trending" toward significance.

The journal's reference style is Vancouver (NLM / ICMJE). Number citations in the order of first appearance.

## 5. Manuscript structure

Use the parts that apply to the article type, in this order.

1. **Title page** (a separate file if the office later adopts double-anonymised review; under this draft it may be the first page). Title; full names of human authors; affiliations; corresponding author's name, email, and ORCID; short running title.
2. **Abstract**, structured as Background, Methods, Results, Conclusions for research articles and reviews. The Results sentence contains the main quantitative findings, which match the paper. Trials include the registration identifier.
3. **Keywords** — four to six. Medical Subject Headings are used where a heading exists.
4. **Introduction** — the question, what is already known, and what this study adds. No broad claims the data cannot support.
5. **Methods** — design, setting, participants or materials, inclusion and exclusion criteria, variables, measurement, sample-size justification, analysis plan, software and versions, deviations from any protocol, and ethics. AI-assisted code is identified here and in the disclosure statement.
6. **Results** — who was included, the findings, and the uncertainty. No interpretation that belongs in the Discussion. No data that are absent from the deposited set.
7. **Discussion** — what the findings mean, comparison with prior work, limitations, and a conclusion that stays within the design.
8. **Data Availability Statement** — required; see section 7.
9. **Ethics statement** — see section 8.
10. **AI-use pointer** — the one-line statement required by the AI policy.
11. **Author contributions** — CRediT roles.
12. **Funding** — grant numbers, or "This research received no specific grant."
13. **Competing interests.**
14. **Acknowledgements** — people who are not authors, including those who collected data under supervision. Do not thank an AI tool here; put it in the disclosure statement.
15. **References.**
16. **Figure legends and tables**, if not placed next to the items.

## 6. Reporting standards

Use the current version of the guideline that matches the design, and upload the completed checklist as a supplementary file.

| Design | Guideline |
| --- | --- |
| Randomised trial | CONSORT, current version, with the registration number in the abstract |
| Observational study | STROBE |
| Animal research | ARRIVE 2.0 |
| Systematic review or meta-analysis | PRISMA 2020 |
| Study protocol | SPIRIT, if protocols are added to the journal later |
| Case report | CARE, plus consent to publish |
| Diagnostic accuracy | STARD |
| Prediction model | TRIPOD, current version |
| Qualitative research | SRQR or COREQ |
| Economic evaluation | CHEERS |
| Sex and gender in human, animal, or cell research | SAGER guidelines |

Name the guideline in the Methods. If no guideline fits, say what was reported so that the study can be repeated, and note the gap.

Clinical trials of interventions are registered in a public registry before the first participant is enrolled (ICMJE policy). Trials of medicinal products also meet the applicable EU and national law, including the Clinical Trials Information System where it applies. Exercise and other non-drug trials are registered in a public registry or, where no clinical registry fits, the protocol is time-stamped on OSF or an equivalent public registry before data collection. A retrospective registration is disclosed as retrospective.

## 7. Data availability

The full rule is the [Data availability and FAIR policy](data-availability-and-fair-policy.md). This section is the minimum a submission must already meet. The dataset is the human-collected data behind the article. The manuscript may be AI-written. The numbers in it are checked against this deposit.

### 7.1 What is deposited, before submission

Deposit the dataset needed to repeat the reported analyses, the analysis code (including every script that builds a data figure or a statistical plot), a data dictionary (codebook), and a README. The repository is a trusted one and assigns a persistent identifier. A DOI is the working default. Suitable repositories include Zenodo, OSF, Figshare, Dryad, and domain repositories (for example the Sequence Read Archive, Gene Expression Omnibus, or a controlled-access repository such as the European Genome-phenome Archive when the data cannot legally be public). Cite the dataset in the reference list.

The identifier is live at submission. The AI preliminary review and the human reviewers can open the files, or the controlled-access route is already open to them. "To be deposited on acceptance" does not meet these guidelines.

### 7.2 FAIR

The deposit follows the FAIR principles (Findable, Accessible, Interoperable, Reusable):

- **Findable.** A trusted repository, a persistent identifier, and rich metadata (title, human creators, description, year, keywords or subject, licence).
- **Accessible.** Open where that is lawful and safe. Where it is not, a controlled route a qualified researcher can follow. Reviewers have access at submission either way.
- **Interoperable.** Open or standard formats (CSV or TSV for tables, plain-text code, an open image format where the instrument allows it). A proprietary file may accompany the open copy. It does not replace it. A screenshot is not the dataset.
- **Reusable.** A clear licence (CC BY 4.0 or CC0 for data, unless a repository or a privacy rule requires another open or controlled-access regime; an OSI-approved licence for code, such as MIT, Apache-2.0, or GPL), a codebook, and a README that says how to run the analysis.

### 7.3 Data availability statement

The statement is required. It names the repository, the identifier, the licence, what was deposited, whether access is open or controlled, and — if controlled — the barrier and the procedure. It states that the files are the data and the code behind the tables, the data figures, and the conclusions. Authors confirm in the cover letter that they can open the raw files.

"Available from the authors on reasonable request", with no repository record, does not meet these guidelines.

### 7.4 Sensitive health data

Health and athlete data that can identify a person are as open as possible and as closed as necessary. Public release of identifiable or pseudonymised microdata is not required where the GDPR (Regulation (EU) 2016/679), the consent, or participant safety forbids it. Pseudonymisation is not anonymisation: if a person can still be singled out, the file is not anonymous. The public deposit is then the anonymised subset or the aggregate tables that support the published numbers, plus the codebook, the README, and the code. The fuller file keeps a persistent identifier and a controlled-access route. The editor and both review rounds still receive access. Identifiable data are not pasted into a public consumer model.

Do not deposit names, contact details, facial images, or other direct identifiers unless the ethics approval and the consent cover publication of those data. Do not deposit data generated by a model and label them as the study's observations.

If an error is found after publication, the authors version the repository record and the journal links the correction to both identifiers. The original deposit is not overwritten in silence.

## 8. Ethics, consent, and registration

**Humans.** Research involving human participants, human material, or identifiable personal data reports the approving committee's name, the approval number, and the date, and states that the work complied with the Declaration of Helsinki. Informed consent is described. Consent to publish identifiable images or quotations is separate and specific. A waiver is reported as a waiver, with the body that granted it.

Sport and exercise studies that expose participants to physical risk state the medical screening used and how adverse events were recorded. A questionnaire study of adults may still need approval or a documented waiver; authors do not decide "low risk" in place of the committee.

**Animals.** Report the approving committee, the approval number, species, strain, sex, housing, and the steps taken to reduce harm, and follow ARRIVE 2.0.

**Field and environmental work.** Report permits and, where genetic resources are used, compliance with access rules that apply to the material.

**Biosafety.** Laboratory work reports the containment level and the institutional approval the law requires. The journal does not consider work that lacks an approval the applicable law requires.

**Registration.** Report trial and protocol identifiers as in section 6.

The ethics statement is specific. "The study was approved by the local committee" is not enough.

## 9. Figures and tables

- Primary-data images are original captures. They are not AI-generated and are not generatively enhanced. See the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md).
- Submit original image files when the office asks, including unprocessed blots and micrographs.
- Methodology and schematic diagrams, which do not display observations or estimates, may be AI-assisted (tools of the kind described as PaperVizAgent are an example, not a requirement). Disclose the tool, the version, and the figure numbers. A human author checks that the diagram matches the methods.
- Data figures and statistical plots are generated by reproducible code from the deposited raw data. They are never submitted as generated images. The script is in the deposit, a human author has run it, and the figure matches that output.
- Each axis has a quantity and a unit. Error bars are defined (standard deviation, standard error, or confidence interval) and the sample size is on the figure or in the legend.
- Tables are text, not images. They do not repeat the same numbers already shown in a figure without a reason.
- Identify any panel that has been spliced. State any adjustment of brightness or contrast that affects how the image should be read.
- Remove direct identifiers from images by cropping or a solid mask.

## 10. AI disclosure

Complete the [AI Disclosure Statement](ai-disclosure-statement.md) for every submission.

In the manuscript, add one sentence:

- "Use of AI tools is reported in the AI Disclosure Statement published with this article." or
- "The authors did not use generative AI tools in this work."

Update the statement if a revision uses a tool the original statement did not cover.

## 11. Authorship, contributions, funding, and interests

List only humans who meet all four ICMJE criteria. Use CRediT to state each person's contribution (conceptualisation, methodology, investigation, data curation, formal analysis, software, visualisation, writing — original draft, writing — review and editing, supervision, funding acquisition, and the others as applicable).

The corresponding author confirms that all authors approved the submitted version and the disclosure.

**Competing interests.** Declare financial and non-financial interests for every author, including employment or equity in a company whose product or AI tool is assessed in the manuscript, and personal relationships that a reader could reasonably think relevant. If there are none, write "The authors declare no competing interests."

**Funding.** Name the funder and the grant. If a funder had a role in design, analysis, or the decision to submit, say so. If not, say so.

The journal uses the ICMJE disclosure form as a supplementary file when the editor asks for it.

## 12. References

- Vancouver style, numbered in order of citation.
- Every reference was opened by a human author. It exists, and it supports the sentence that cites it.
- Do not cite a source you cannot read. Mark a translation or a secondary citation honestly, and prefer the primary source.
- Datasets, code, and preprints are cited with their identifiers.
- Software used for the analysis is cited with the version.
- AI tools are not references in place of the disclosure statement. A methods paper about a model may be cited in the ordinary way when the authors rely on it as literature.

## 13. Files to upload

| File | Required |
| --- | --- |
| Manuscript, `.docx` or `.odt`, with line numbers | yes |
| Title page, if kept separate | yes when the manuscript file is anonymised; otherwise include it in the manuscript |
| AI Disclosure Statement | yes |
| AI prompts and workflow | yes, if any AI tool was used |
| Figure files | yes, if the article has figures |
| Data availability identifier, already active | yes |
| Reporting-guideline checklist | yes, when a guideline applies |
| Ethics approval (copy or number the office can check) | yes, when the study needs approval |
| ICMJE competing-interest form | when requested |
| Cover letter | yes |

The cover letter states: the question and the design in a few sentences; that the work is original and not under consideration elsewhere; the data identifier; the ethics and registration identifiers or why they do not apply; whether a preprint exists; and any request for a controlled-access exception. It confirms that the authors can access the raw data.

## 14. Submission checklist

Authors tick this list in OJS. A manuscript that fails an item is not complete.

- [ ] The manuscript is within the journal's scope, and the study (or the review screening) was conducted by humans.
- [ ] All authors are humans, meet the ICMJE criteria, and have approved the manuscript and the AI disclosure.
- [ ] The AI Disclosure Statement is uploaded and matches the manuscript.
- [ ] The prompts and workflow file is uploaded, or no AI tool was used.
- [ ] The dataset and the analysis code are deposited, the identifier resolves, the codebook and README are present, and the authors — and the reviewers — can open the files, or a controlled-access route is already open and is explained in the cover letter.
- [ ] The Data Availability Statement, ethics statement, funding, competing interests, and CRediT roles are in the manuscript.
- [ ] The reporting checklist for the design is uploaded where one exists.
- [ ] Primary-data images are original captures. Any AI-assisted schematic is disclosed and checked. Data figures and statistical plots come from the deposited code, not from a generated image.
- [ ] Every citation was opened and supports the claim.
- [ ] A preprint, if one exists, is linked in the cover letter.
- [ ] The authors agree to the copyright and licence terms published on the journal website at the time of submission (working default in this draft: authors retain copyright, licence CC BY 4.0).

## 15. After submission

The corresponding author receives an acknowledgement. The process then follows the [Peer review policy](peer-review-policy.md): human triage, AI preliminary review, human peer review, human decision.

Do not submit the same manuscript to another journal while it is under consideration. If you withdraw, tell the office.

After acceptance the corresponding author checks the proofs. Changes at proof stage are limited to errors of fact or production. New AI use at proof stage is disclosed before publication.

## 16. Fees, copyright, and licence

There is no submission fee. A fixed article processing charge (APC) of 1000 PLN is charged only after the article is accepted. The charge never influences the editorial decision, and editors and reviewers deciding on a paper do not see payment status. There are no fee waivers.

Reviewers who complete a review receive a discount voucher toward the APC of their own future article. The discount is set by the editorial office and published on the site.

The journal does not charge for colour or for speed. There is no paid fast track, and no paid guarantee of acceptance.

Under this draft, authors retain copyright and grant the journal a licence to publish the version of record under CC BY 4.0. Third-party material is included only when the authors have permission, and it is labelled with its own licence.

Preprints on public servers (for example bioRxiv, medRxiv, SportRxiv, or OSF) are allowed and are not treated as prior publication. The preprint is updated with a link to the version of record after publication. The AI disclosure on the preprint and on the version of record should match. If they do not, the version of record and its statement are the ones the authors stand behind, and the difference is explained to the editor.

## 17. Related documents

- [AI Disclosure Statement (template)](ai-disclosure-statement.md)
- [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md)
- [Data availability and FAIR policy](data-availability-and-fair-policy.md)
- [Peer review policy](peer-review-policy.md)
- [Publication ethics](publication-ethics.md)
