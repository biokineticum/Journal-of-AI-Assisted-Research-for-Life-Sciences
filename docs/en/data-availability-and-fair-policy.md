# Data availability and FAIR policy

**Journal of AI-Assisted Research for Life Sciences**

**Status:** draft for adoption (version 0.1, 14 November 2026).

**Language:** English · [Wersja polska](../pl/data-availability-and-fair-policy.md)

## 1. Purpose

Empirical results in this journal come from work humans conducted. The manuscript may be drafted with a generative tool from those results. The dataset and the analysis code are how a reader, a reviewer, and the AI preliminary review check that the text is about the work that was done.

This policy requires the underlying human-collected dataset, and the code that analyses it, to be deposited before submission in line with the FAIR principles: Findable, Accessible, Interoperable, and Reusable (Wilkinson and colleagues, Scientific Data, 2016; [doi:10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)).

Sensitive health data follow the working rule used in European research-data practice: as open as possible, as closed as necessary. A public deposit that would identify a participant, or that the law forbids, is not required. A deposit that reviewers cannot open is not acceptable.

The [Author guidelines](author-guidelines.md) repeat the operational minimum. This page is the full rule. Figure rules that depend on the deposit are in the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md).

## 2. What is deposited, and when

Before submission, the authors deposit:

- the dataset needed to repeat the reported analyses: the recordings, spreadsheets, images, or transcripts behind the tables, the data figures, and the conclusions, at the level of detail the paper uses;
- the analysis code, including the scripts that build every data figure and statistical plot, with the software versions and any seed the script needs;
- a data dictionary (codebook) that defines every variable, unit, allowed value, and missing-data code;
- a README that says what the study is, how the files are organised, how to run the analysis, which licence applies, and a contact route the repository itself supports;
- a licence, stated in the repository record and in the manuscript.

The repository assigns a persistent identifier. A DOI is the working default (Zenodo, Figshare, Dryad, and OSF can provide one). A domain accession that the relevant community treats as persistent (for example a Sequence Read Archive or Gene Expression Omnibus accession, or a controlled-access accession such as the European Genome-phenome Archive) meets the same requirement. The identifier is cited in the reference list and is live at submission. "To be deposited on acceptance" does not meet this policy.

The authors confirm in the cover letter that they can open the raw files and that those files are the data behind the tables, the figures, and the conclusions. A model does not make that confirmation for them.

A reanalysis of an existing dataset cites the original identifier and the licence under which the authors used it, and deposits the derived files and the code that produce the numbers in this manuscript. A simulation is deposited as a simulation: code, seeds, and inputs, labelled as simulated.

## 3. The FAIR principles

The four words are requirements, not a slogan. A deposit that fails one of them is incomplete.

### 3.1 Findable

The record lives in a trusted repository that assigns a persistent identifier and exposes metadata a machine can read. Suitable repositories include Zenodo, OSF, Figshare, Dryad, and a domain repository when one is the standard place for that kind of data.

The metadata include, at minimum: a title; the human creators, with ORCID where a creator has one; a description of the study and of what the files contain; the year; keywords or a subject; the licence; and, once the article exists, the link to it. The files are named so that a reader can tell the raw data from the code, the codebook, and the README without opening every file.

A personal website, a link in a cloud drive with no persistent identifier, or a record that exists only inside the submission system is not a deposit.

### 3.2 Accessible

The identifier resolves to a page that says how to obtain the files, including when the files themselves are not on the open web.

Open access is the default for data that can lawfully and safely be public. The retrieval method is stated (direct download, or the steps a qualified researcher follows for a controlled-access record).

Access for review is part of accessibility, not a favour. At submission, the editorial office, the AI preliminary review, and the human reviewers can open the files the manuscript relies on. Section 6 states how that works for sensitive data.

### 3.3 Interoperable

Tables are deposited in an open, standard format (CSV or TSV, UTF-8, or another format a researcher in the field can open without a single vendor's current release). Code is plain text. Primary-data images use an open format (for example TIFF or PNG) when the instrument allows it. A proprietary file may sit beside the open copy. It does not replace it.

A screenshot, a PDF of a spreadsheet, or a generated picture of a plot is not the dataset and is not the statistical figure. Units, coding of categories, and relations between tables are in the codebook, not left for the reader to guess.

### 3.4 Reusable

The licence is stated and is one a reader can use. Data should be released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) or [CC0](https://creativecommons.org/publicdomain/zero/1.0/), unless a repository or a privacy rule requires another open licence or a controlled-access regime. Code carries an OSI-approved licence (for example MIT, Apache-2.0, or GPL).

The README and the codebook are what make the files reusable by someone who was not in the study. The Methods and the README agree on the software versions, the inclusion rules, and the handling of missing data. A human-specified cleaning rule is described in the Methods and implemented in the deposited code. It is not a licence for a model to invent or rewrite observations.

## 4. Data availability statement

Every article has a Data Availability Statement. A submission without one is incomplete.

The statement names:

- the repository;
- the persistent identifier, as a resolver link;
- the licence;
- what was deposited (dataset, code, codebook, README, and any restricted portion);
- whether access is open or controlled;
- if access is controlled, the barrier and the procedure a qualified researcher follows;
- that these files are the data and the code behind the tables, the data figures, and the conclusions.

An example of the level of detail, for a fictional open deposit:

> The individual-level force-plate recordings, the codebook, the README, and the analysis code are deposited in Zenodo (doi:10.5281/zenodo.0000000; CC BY 4.0). These files are the data behind Table 1, Figure 2, and the estimates in the Results. Figure 2 is rebuilt by `analysis/cmj_figures.R`.

An example of a controlled-access statement:

> Individual-level health records cannot be published because participants could be identified and the consent does not allow public release. Anonymised aggregate tables, the codebook, the README, and the analysis code are in Zenodo (doi:10.5281/zenodo.0000000; CC BY 4.0). The individual-level file is under controlled access at [repository, accession]. A qualified researcher applies as that repository describes. Editors and reviewers were given access for the whole review.

"Available from the authors on reasonable request", with no repository record, does not meet this policy.

## 5. Sensitive health data

Health, clinical, and athlete data are often personal data. Where the people concerned are in the European Economic Area, the authors comply with Regulation (EU) 2016/679 (General Data Protection Regulation, GDPR) and with the ethics approval. A disclosure statement does not cure an unlawful transfer.

The journal uses the words in their ordinary legal sense:

- **Pseudonymisation** removes or replaces direct identifiers while a key, or a combination of remaining variables, can still identify a person. Pseudonymised data are still personal data.
- **Anonymisation** means re-identification is not reasonably likely, including by someone who knows the setting. Removing a name column from a small sample, while leaving age, club, event, and a rare measurement, is not anonymisation.

The authors say which they did, in the ethics statement and in the README. They do not describe a pseudonymised file as anonymous.

The public deposit is the largest share that is lawful and safe: anonymised microdata where that is real, or the aggregate tables that support the published numbers, plus the codebook, the README, and the code. The fuller file, when it must stay restricted, goes to a controlled-access repository or a documented access procedure, still with a persistent identifier.

Direct identifiers — names, contact details, facial images, device identifiers that point to a person — are not in the public deposit unless the ethics approval and a specific consent cover publication of those data. The same limit applies to data a model generated and that the authors might be tempted to label as observations. Those data are not the study's observations. See the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md).

Biosecurity and comparable legal barriers are handled the same way: the largest shareable set in public, the restricted set under a controlled route, and the reason in the statement. A human editor accepts the split. The editor does not accept the absence of a deposit.

## 6. Access for review

Reviewers must have access to the data at submission. That includes the AI preliminary review and the human reviewers.

- The identifier resolves when the manuscript is submitted.
- For an open deposit, the link in the manuscript and in the cover letter opens the files.
- For a controlled-access deposit, the authors provide a review token, a time-limited account, or an equivalent route that works for the editorial office and for the reviewers throughout the review. The route is described in the cover letter.
- The AI consistency check runs only on the journal's locally hosted models, on infrastructure the journal controls. See the [Peer review policy](peer-review-policy.md). Identifiable or pseudonymised participant-level data are not sent to an external or third-party AI API.
- Data under controlled access are processed only inside that local environment. A review token is used to read the files there. The files are not copied to an outside AI service in order to check the manuscript.
- If the access terms or the ethics approval forbid showing a file to the model, a human member of the office does the numerical check against that file, and the report marks the model step "Not assessed" for that file and says why. The human reviewers still receive access.

**Confidentiality and the GDPR.** This limit is a data-protection safeguard as well as a confidentiality rule. Where the dataset contains personal data, sending it to an external AI provider would be a transfer the journal does not make. The consistency check stays inside the journal's infrastructure. A literature or citation lookup, where the peer-review policy allows one, sends only a generic query or a bibliographic identifier. It does not send the dataset, the manuscript text, or anything that identifies the authors. Human reviewers are under the same prohibition: they do not upload the dataset or the manuscript to an external AI service. The model name, the version, and the infrastructure are written into the review record.

A manuscript is not sent to human peer review while the data link does not resolve, the reviewers cannot open the files, or the controlled-access route is only a promise.

## 7. Code and data figures

Data figures and statistical plots are generated by the deposited code from the deposited raw data. They are not generated images. The script, the input it reads, and the software versions are in the deposit. A human author has run the script.

Methodology and schematic diagrams, which do not display observations or estimates, may be AI-assisted. That use is disclosed. It does not change the duty to deposit the data and the analysis code. The figure rules are in the [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md) and the [Author guidelines](author-guidelines.md).

Code written with AI assistance is disclosed. A human author who understands the code and has run it is responsible for it. Code the authors cannot explain is not acceptable. Generative output is not an imputed dataset. Any imputation is human-specified, reported, and distinguished from the raw data.

## 8. After publication

The version of record links the Data Availability Statement and the persistent identifier. If an error is found, the authors version the repository record and the journal links the correction to both identifiers. The original deposit is not overwritten in silence.

A reader who cannot reconstruct the reported numbers from the deposit has found a problem with the article. The editor treats that as an integrity query under [Publication ethics](publication-ethics.md), whether the cause is an honest error or a manuscript a model wrote past the data.

## 9. Related documents

- [Author guidelines](author-guidelines.md)
- [AI Use and Disclosure Policy](ai-use-and-disclosure-policy.md)
- [Peer review policy](peer-review-policy.md)
- [Publication ethics](publication-ethics.md)
- [Aims and scope](aims-and-scope.md)
