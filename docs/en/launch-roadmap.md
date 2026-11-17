# Launch roadmap

**Journal of AI-Assisted Research for Life Sciences**

**Status:** working checklist (version 0.1, 14 November 2026), not a statement that any step is done.

**Language:** English · [Wersja polska](../pl/launch-roadmap.md)

This list turns the draft policies into a journal that can accept manuscripts. It is operational guidance. It is not legal advice. Court filing, data-protection duties, and the publisher's legal form should be confirmed with the court, the National Library, and a lawyer before money is spent or a public call is issued.

Nothing in this repository asserts that an editorial board already exists, that an ISSN or a DOI prefix has been issued, or that the journal is indexed anywhere.

## 1. Open decisions to confirm before adoption

The policies use the following **working defaults**. The publisher confirms or replaces each one, then updates both language versions so they still say the same thing.

| Decision | Working default in these drafts |
| --- | --- |
| Official title | Journal of AI-Assisted Research for Life Sciences |
| Short / running title | Not chosen. Do not invent an abbreviation in public until it is chosen. |
| Polish parallel title | None. A Polish description on the website is not a second registered title. A separate language edition would usually need its own ISSN. |
| Article language | English, with optional Polish title and abstract |
| Access model | Gold open access: no submission fee; fixed APC of 1000 PLN after acceptance; no fee waivers; reviewer discount vouchers (amount set by the editorial office and published on the site) |
| Article licence | CC BY 4.0; authors retain copyright |
| Peer-review model | Single-anonymised; two human reviewers after the AI preliminary review |
| AI preliminary report | Structured report (summary, strengths, weaknesses, questions, data-consistency findings, checklist), shared with authors, reviewers, and editors; not published with the article. The report never makes the decision |
| Round 1 architecture | Multi-agent pipeline inspired by ScholarPeer (Google Research blog, 8 April 2026). Design inspiration only, not a vendor dependency. Adapted because that evaluation was on machine-learning papers |
| Data deposit | FAIR deposit of the human-collected dataset and the analysis code, with a persistent identifier, before submission. Reviewers and Round 1 have access at submission. Sensitive health data: as open as possible, as closed as necessary |
| Model name on the article | Every tool, model, and version is logged in the editorial file; printing the names on the article is undecided |
| Reference style | Vancouver (NLM / ICMJE) |
| Publication rhythm | Continuous publication, one volume per calendar year. The court application asks for frequency: this description has to match the form. |
| Legal publisher | [PUBLISHER LEGAL NAME] — not yet decided in this repository |
| Editor-in-chief | [EDITOR-IN-CHIEF NAME] — appoint a real person before any filing |
| Contact | [EMAIL], [PUBLISHER ADDRESS], [JOURNAL URL] |

If a default changes, update `docs/en` and `docs/pl` in the same commit. Until the publisher adopts the policies, the status line stays "draft for adoption".

## 2. Phase A — governance and people

Do this before a public call for papers and before naming people on a website.

- [ ] Decide the legal publisher: a university, a scholarly society, a foundation, or another body that can sign contracts and appear in the court register. A GitHub account is not a publisher.
- [ ] Write a short agreement that the publisher does not overrule editorial decisions (see [Publication ethics](publication-ethics.md)).
- [ ] Appoint a human editor-in-chief who accepts the duties of *redaktor naczelny* under the Polish Press Law, if the title will be registered in Poland. Record the legal name, affiliation, and ORCID. Do not file a placeholder.
- [ ] Appoint at least one deputy who can handle appeals and conflicts, [DEPUTY EDITOR NAME].
- [ ] Build a board of active researchers across the scope (health and sport science, and the adjacent fields the journal will actually review). A practical minimum before launch is the editor-in-chief plus enough specialists to cover the first submissions without asking conflicted reviewers — often on the order of eight to twelve members, in more than one country if the journal is international. This is a planning figure, not a filled list.
- [ ] Include, or have on call, a statistical adviser and someone willing to handle integrity cases.
- [ ] Each board member agrees in writing to be listed, to the AI and confidentiality rules, and to the time they can give. Publish name, affiliation, and ORCID. Do not list people who have not agreed.
- [ ] Open a monitored mailbox at [EMAIL]. Do not use a personal address that only one postgraduate can see, unless the publisher accepts that risk in writing.
- [ ] Adopt the policies in `docs/en` and `docs/pl` as the public rules, after the decisions in section 1.
- [ ] Keep this repository as the working copy. The website shows the adopted version and its date.

## 3. Phase B — registration in Poland and ISSN

Complete this before the journal claims to be a registered title and before an ISSN is printed.

**Press-title registration.** Under the Press Law of 26 January 1984 (*Prawo prasowe*), publishing a newspaper or periodical requires registration with the district court (*sąd okręgowy*) competent for the publisher's seat (Article 20(1)). The application must include (Article 20(2)): the title and the seat and full address of the editorial office; the personal data of the editor-in-chief; the publisher and the publisher's seat and full address; and how often the title appears. The court refuses the application if those data are missing or if registration would infringe protection of an existing title (Article 21). If the court has not decided within 30 days of filing, publication may begin (Article 20(4)). Later changes to the registered data are notified to the court (Article 20(5)). Article 45 provides for a fine for publishing a title that is unregistered or suspended. The Constitutional Tribunal has held the criminal penalty for failing to register a printed magazine unconstitutional in part, while upholding the registration duty for printed magazines. Courts do not all treat a text-only website the same way. Confirm the current text of the Act and the practice of the competent court with a lawyer before filing. This checklist is not that advice.

- [ ] Fix the title string, the publisher's legal name and seat, the editorial address, the frequency, and the editor-in-chief. The title on the website, in OJS, on the ISSN application, and in Crossref must be the same string.
- [ ] File the application with the competent district court, with the annexes that court's current instruction requires. Identity and capacity statements for the editor-in-chief are commonly requested and are not all spelled out in Article 20(2). Pay the fee the court currently charges. Keep the stamp or the decision.
- [ ] Do not describe the title as registered until the court has entered it. Do not publish a first article before that entry, or before the 30-day period in Article 20(4) has passed without a decision. If legal advice is to wait for the entry even after 30 days, follow that advice.
- [ ] If a year passes without an issue, ask the court about keeping the registration valid (Article 23) before it lapses.

**ISSN.** Apply to the National ISSN Centre at the National Library of Poland (*Narodowy Ośrodek ISSN, Biblioteka Narodowa*). Use the contact details and the form published on the National Library's own website. Polish publishers are commonly asked for evidence that the press title is registered. An electronic-only journal receives one ISSN for that edition. A later print edition would need a second ISSN.

- [ ] Apply after the title and the publisher are final and the court registration is in hand, unless the Centre's current instructions say otherwise.
- [ ] Enter the ISSN in OJS and on the website only after it is assigned. Never print a reserved or guessed number.
- [ ] If a Polish-language edition is launched later as a separate edition, ask the Centre whether a second ISSN is required before using one.

## 4. Phase C — platform (OJS)

Use a current, supported release of Open Journal Systems (PKP). Host it on HTTPS, with backups and an update routine. The submission database is not a training set for any model.

- [ ] Install the English locale as the publication language and the Polish locale for the public policies and the interface.
- [ ] Masthead: title, publisher, address, editor-in-chief, board, [EMAIL], ISSN once assigned.
- [ ] Publish the adopted aims and scope, AI policy, disclosure template, peer-review policy, author guidelines, data availability and FAIR policy, and ethics policy in both languages.
- [ ] State on the site: gold open access, a fixed APC of 1000 PLN charged only after acceptance, no submission fee, licence CC BY 4.0, copyright retained by authors, and the current reviewer-voucher discount.
- [ ] Configure the submission checklist from the [Author guidelines](author-guidelines.md).
- [ ] Require two supplementary genres: `AI Disclosure Statement` and `AI prompts and workflow`, using the fields in the [template appendix](ai-disclosure-statement.md).
- [ ] Require the data availability statement, the repository identifier, the licence, the codebook, and the README, plus ethics and registration fields (or a reasoned "not applicable"), competing interests, and funding. A submission is not complete while reviewers cannot open the deposit.
- [ ] Add a review form that includes the AI-oversight questions from the [Peer review policy](peer-review-policy.md), and a required reviewer declaration that the manuscript was not uploaded to a public consumer model.
- [ ] Configure a two-stage workflow the staff can actually follow: triage, AI preliminary review, human review, human decision. OJS will not do this by itself; write a one-page internal operating note that names who runs the check and where the report is stored.
- [ ] In that note, specify Round 1 as the multi-agent pipeline in the [Peer review policy](peer-review-policy.md): literature context, missed baselines and datasets, claim-verification questions, data–manuscript consistency (re-run the deposited code where it runs), reporting and ethics against the EQUATOR guideline, and citation checks. The design is inspired by ScholarPeer. The note states that the journal does not buy or depend on that product, and that the published evaluation was on machine-learning papers.
- [ ] Log every tool, model, and version used in a Round 1 run, and store that log with the human-checked report.
- [ ] Before Round 1 runs, confirm that the check and the human reviewers can open the deposit, including any controlled-access route. Do not paste identifiable health data into a public consumer model.
- [ ] Select the permitted deployment (local or enterprise, with a written no-training and limited-retention agreement) before the first submission is processed. Record the provider and the contract reference in the editorial file.
- [ ] Enable ORCID. Enable the Crossref export plugin only once a membership and a DOI prefix exist.
- [ ] Publish a privacy notice that meets the GDPR: what author and reviewer data are processed, for how long, on what basis, and that manuscripts are not used to train models.
- [ ] Plan similarity-checking software ([SIMILARITY-CHECK TOOL]) and say on the site when it is actually in use. Until then the AI report field stays "not yet used".
- [ ] Test the path with a dummy submission: incomplete disclosure blocked, report template filled, human checker sign-off stored, reviewer can see the report.

## 5. Phase D — first publication

- [ ] Adopt the policies and replace the draft status line with the adoption date.
- [ ] Publish the masthead with real names only.
- [ ] Open submissions only after phases A, B, and C are far enough along that an author can read the rules, the board, the licence, and the contact address, and the title is registered before publication.
- [ ] Write a call for papers that describes the human-data rule and the AI disclosure. Do not promise indexing, impact factors, or decision times the journal has not set.
- [ ] For the first articles, the editor reads every AI preliminary report and at least two human reviews, and keeps the correspondence.
- [ ] Publish each article with the AI Disclosure Statement, the prompts supplement, the Data Availability Statement, the data identifier, the licence, and the sentence on how the manuscript was reviewed.
- [ ] Proofread the Polish and English policy pages against each other after any last-minute change.

## 6. Phase E — DOI, preservation, Google Scholar

**Crossref.** Join Crossref as a publisher when the legal publisher exists. Use the fee schedule on Crossref's website; do not budget from a guessed figure. Deposit DOIs for articles and, when issued, for retraction and correction notices. Check that the title, ISSN, licence, and author names in the XML match the article page. ORCID and the data citation should travel in the metadata where the schema allows.

- [ ] Membership in the legal publisher's name.
- [ ] DOI prefix configured in OJS.
- [ ] A test deposit on a dummy or first article, resolved in a browser.
- [ ] Fund the annual membership from the journal's operating funds. Do not bill authors a separate Crossref charge on top of the APC.

**Preservation.** Join the PKP Preservation Network or another archiving service DOAJ will recognise (for example CLOCKSS or an institutional dark archive). A journal that exists only on one virtual machine is not preserved.

- [ ] Archiving arrangement in place before the DOAJ application, and named on the website.

**Google Scholar.** Scholar crawls public scholarly pages; it is not an index the journal can buy. Follow Google's current inclusion guidance: stable URLs, full author names, titles, abstracts, and references as text rather than images, HTML or PDF full text, and bibliographic meta tags (OJS emits these). Request inclusion only after real articles are online. Check the result. Do not put a Scholar badge on the site until the journal's articles are visibly indexed.

## 7. Phase F — DOAJ and later indexes

DOAJ is the realistic indexing goal after the journal has a publishing record, not on the day submissions open.

Before applying, read the current DOAJ guide and confirm that the live site shows at least:

- ISSN, open-access statement, and the publicly stated APC (1000 PLN, charged after acceptance);
- aims and scope, author instructions, peer-review description (including the labelled AI round and the human decision), and the ethics policy;
- an editorial board with names and affiliations;
- licensing and copyright terms on the articles;
- contact details that work;
- a record of research articles consistent with DOAJ's current minimum activity (confirm the current threshold; it has long been at least five research articles a year);
- a preservation arrangement.

- [ ] Apply only when those items are true on the public site.
- [ ] If DOAJ asks for changes, change the site or the practice. Do not shop for a badge the journal does not meet.
- [ ] MEDLINE / PubMed, Scopus, and Web of Science are later applications with their own criteria and a longer publishing history. They are not launch claims and they are not promised to authors.

## 8. Funding

Gold open access with a fixed article processing charge (APC) of 1000 PLN, charged only after acceptance, is the journal's stated model. The APC is public, fixed, and stated up front. Budget for:

- court fee for press registration (use the current court tariff);
- hosting, backups, and a domain for [JOURNAL URL];
- Crossref membership and deposits (current Crossref schedule);
- the permitted AI deployment under a no-training contract;
- similarity-checking software, when the budget allows;
- editorial time, which is often unpaid at the start and should be acknowledged honestly;
- legal advice for the registration, the publisher's form, and the GDPR notice;
- preservation fees if the chosen archive charges any.

ISSN assignment by the National Library is not a per-article charge. Confirm any handling expectation on the Centre's current page.

Possible sources, to be chosen by the publisher: the APC, a host institution, a research grant that allows publishing costs of a journal, a scholarly society, or in-kind support. Not acceptable as the business model: a later change of the APC that is not first published on the site, a paid guarantee of acceptance, a paid fast track, or a sponsor who selects articles. There are no fee waivers for inability to pay. Reviewers who complete a review receive a discount voucher toward the APC of their own future article; the discount is set by the editorial office and published on the site.

- [ ] Name the funding source on the website before launch: [FUNDING SOURCE].
- [ ] State that the source has no role in acceptance decisions.

## 9. Claims the journal will not make

- That it has an impact factor, a CiteScore, a DOAJ Seal, or an index membership before the notice is real.
- That review is "AI-powered" in place of human review, or that Round 1 is Google's ScholarPeer or any other named product. The accurate sentence is: a multi-agent preliminary review inspired by that published design and adapted for this journal, then human peer review, then a human decision. The AI report is not the decision.
- That a data figure was drawn by a model. Data figures and statistical plots come from code run on the deposited data. A schematic may be AI-assisted only when it does not display data, and only with disclosure.
- That acceptance is likely, fast, or for sale.
- That the editorial board includes a person who has not agreed, or that [EDITOR-IN-CHIEF NAME] has been appointed before they have.
- That a policy in this repository is in force while its status line still says "draft".

## 10. Document map

| Document | English | Polish |
| --- | --- | --- |
| Aims and scope | [aims-and-scope.md](aims-and-scope.md) | [aims-and-scope.md](../pl/aims-and-scope.md) |
| AI use and disclosure | [ai-use-and-disclosure-policy.md](ai-use-and-disclosure-policy.md) | [ai-use-and-disclosure-policy.md](../pl/ai-use-and-disclosure-policy.md) |
| AI disclosure statement | [ai-disclosure-statement.md](ai-disclosure-statement.md) | [ai-disclosure-statement.md](../pl/ai-disclosure-statement.md) |
| Peer review | [peer-review-policy.md](peer-review-policy.md) | [peer-review-policy.md](../pl/peer-review-policy.md) |
| Author guidelines | [author-guidelines.md](author-guidelines.md) | [author-guidelines.md](../pl/author-guidelines.md) |
| Data availability and FAIR | [data-availability-and-fair-policy.md](data-availability-and-fair-policy.md) | [data-availability-and-fair-policy.md](../pl/data-availability-and-fair-policy.md) |
| Publication ethics | [publication-ethics.md](publication-ethics.md) | [publication-ethics.md](../pl/publication-ethics.md) |
| This checklist | [launch-roadmap.md](launch-roadmap.md) | [launch-roadmap.md](../pl/launch-roadmap.md) |
