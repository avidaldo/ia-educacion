---
title: Legal framework
description: What the GDPR and the AI Act say about using AI in a school, with the AI Act’s application timeline and the points that EU law leaves to each country.
adapted: true
derived_from:
  es/etica-legal/normativa.md: "ba7cafda6c3309b0b32791a59b2afe6dbe09801f"
---

> [!NOTE]
> **A teacher’s reading of the law**
> This page explains the rules from a teacher’s point of view and cites their articles so that you can check them. It is not legal advice: for a specific case, the reference is your school or education authority and its data protection officer, whom every public authority or body must designate. Situation reviewed on 5 November 2026.

## How the rules fit together

An EU **regulation** is binding and directly applicable in all Member States, with no need for a national law to transpose it; a **directive**, by contrast, sets objectives that each State incorporates through its own law. But “directly applicable” does not mean “applicable from publication”: each regulation sets its date of entry into force and its application deadlines. The AI Act, for example, was published in July 2024, entered into force on 1 August 2024 and applies in stages ([timeline](#timeline)).

Below them come each country’s laws, national and, where they exist, regional. And outside that hierarchy are **guidelines and recommendations**, such as the European Commission’s, which guide but do not bind.

## Data protection

The core rule is the General Data Protection Regulation (GDPR), the same in every Member State. It leaves some points to national law, such as the age from which a child can consent alone to an online service and the legal basis on which schools process student data; this page points them out where they come up.

### What counts as personal data

The GDPR defines it very broadly: “any information relating to an identified or identifiable natural person”, and a person is identifiable if they “can be identified, directly or indirectly”, for instance by reference to “one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person”.[^rgpd] A mark, a comment on behaviour or a description that reveals who is being talked about are personal data, even if no name appears. So are a candidate’s answers in an exam and the examiner’s comments on them, according to the Court of Justice of the EU: the answers reflect “the extent of the candidate’s knowledge and competence in a given field” and, in a handwritten script, “contain, in addition, information as to his handwriting”.[^nowak]

### Anonymising and pseudonymising

The GDPR distinguishes two operations that are often confused. **Pseudonymising** is processing data “in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately” and protected: it is what you do when you replace names with codes and keep the table that links them somewhere else. Pseudonymised data are still personal data, because they “could be attributed to a natural person by the use of additional information”. **Anonymising** is making sure that no one is identifiable by the means reasonably likely to be used “either by the controller or by another person”, among which the Regulation counts “singling out”: isolating one person within a group without knowing their name. The Regulation stops applying only to anonymous information.[^rgpd]

In 2025 the Court of Justice clarified for whom pseudonymised data remain personal data. For whoever holds the information that allows the pseudonymisation to be reversed, they are “in spite of pseudonymisation, still personal in nature”. For a recipient who does not have it, they may not be, but only if it cannot reasonably attribute them to anyone: “in so far as it cannot be ruled out” that it does, for instance by cross-checking them with other data it holds, “pseudonymised data should be considered to be personal in nature”.[^srb] In a school, whoever keeps the code table is always in the first case, and a text full of personal details may allow a recipient to identify the person even without a name.

What the judgment does not change is the position of the sender. Sending is already processing (the GDPR lists “disclosure by transmission” among the operations that make up processing), and the very existence of the information that allows identification “precludes data that have undergone pseudonymisation from being regarded, in all cases, as anonymous data”. The Court applied this to the duty to inform data subjects of who will receive their data: it applies before the transfer, “irrespective of whether or not those data were personal data” for the recipient.[^srb] That is why pseudonymising reduces the risk but does not, by itself, decide which tool may be used. That depends on the instructions of the controller, which, depending on the country, may be the school or the authority that runs it, because anyone acting under its authority may process the data only “on instructions from the controller”.[^rgpd]

Pseudonymising is not pointless: the GDPR gives it as an example of the measures with which the controller protects data by design and ensures their security.[^rgpd] But it does not make the data free to use. What it means for a teacher who replaces the name on a piece of work with a code before asking AI for help is covered in [the code table, in four questions](../datos-alumnado/index.md#the-code-table-in-four-questions).

### Who may process student data

A school needs a legal basis to process its students’ data. For its educational task, the GDPR provides one when processing “is necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller”, provided that its basis is laid down by Union law or by “Member State law to which the controller is subject”.[^rgpd] So the purpose of that processing, and possibly the data it covers, is set by each country’s law. Whatever that law says, the GDPR adds two conditions that matter here:

- the data must be processed “in a manner that ensures appropriate security of the personal data”;
- anyone acting under the controller’s authority who has access to the data, teachers included, “shall not process those data except on instructions from the controller”.

That basis belongs to the school and the education authority, not to each tool a teacher uses. When a third party processes data on the school’s behalf, the GDPR requires it to be a **processor** chosen among those “providing sufficient guarantees”, bound by a contract or other legal act that governs the processing.[^rgpd] A chatbot with a personal account is not that: that is why student data only go into tools that your school or education authority has contracted or authorised. And even there, only what is essential: data must be “limited to what is necessary in relation to the purposes for which they are processed” (data minimisation).[^rgpd]

### Special categories of personal data

Some categories have reinforced protection: the GDPR prohibits in principle processing data revealing racial or ethnic origin or religious beliefs, or data concerning health or sexual orientation, among others, except in the cases it lists.[^rgpd] A special educational needs report, a diagnosis or an adjustment for health reasons fall here: they are the last data that should end up in an AI tool.

### Students’ age

The GDPR sets the age from which a child’s own consent is enough when an online service (an “information society service”) is offered directly to them and the processing relies on consent: it “shall be lawful where the child is at least 16 years old”; below that age, only “if and to the extent that consent is given or authorised by the holder of parental responsibility over the child”. But Member States “may provide by law for a lower age for those purposes provided that such lower age is not below 13 years”, so the age that applies to your students, between 13 and 16, is set by your country’s law.[^rgpd]

### Automated decisions and impact assessments

Everyone has the right “not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her”.[^rgpd] So a mark, a sanction or a decision on progression to the next year cannot come from a tool alone, except in the cases Article 22(2) lists, such as a law that authorises it and lays down safeguards.

And when a controller plans a type of processing, “in particular using new technologies”, that “is likely to result in a high risk to the rights and freedoms of natural persons”, it must first carry out a **data protection impact assessment**.[^rgpd] That is the responsibility of the controller that introduces the tool, not of the teacher who uses it, but it explains why an AI platform with student data should not be adopted without the controller’s decision.

## The AI Act

Its logic is to grade obligations according to risk: a few practices are prohibited, certain uses are high-risk and carry strict obligations, some systems have transparency obligations, and the rest, which is most uses, has no specific obligations. Separately, general-purpose AI models, such as those behind chatbots, have their own obligations, which fall on whoever develops them.

### Timeline

Regulation (EU) 2024/1689, known as the AI Act, applies in stages. In July 2026 it was amended by Regulation (EU) 2026/1744, the Digital Omnibus on AI, which postponed the obligations for high-risk systems and added new prohibitions.[^ria] [^omnibus]

| From | What applies | Relevance for a school |
| --- | --- | --- |
| 1 August 2024 | Entry into force | No obligations yet |
| 2 February 2025 | General provisions, AI literacy and prohibited practices | Inferring emotions in education institutions is prohibited |
| 2 August 2025 | General-purpose models, governance and penalties | Obligations for the providers of the models |
| 2 August 2026 | General application, including the transparency obligations | Telling people they are talking to an AI; labelling deep fakes |
| 2 December 2026 | New prohibitions from the Omnibus | Systems for generating non-consensual intimate images are prohibited |
| 2 December 2027 | High-risk systems in Annex III, among them those in education | Obligations for whoever deploys systems that assess or admit students |
| 2 August 2028 | High-risk systems built into products (Annex I) | Little |
| 2 August 2030 | High-risk systems intended for public authorities that were already in service | Final deadline to bring into line the high-risk education systems that public authorities were already using before December 2027 |

The high-risk dates used to be 2 August 2026 and 2027. Many guides published before July 2026, including the European guidelines for educators, still give the old dates.

### Who is who

The Regulation divides obligations between the **provider**, who develops a system, or has it developed, and places it on the market or puts it into service under its own name, “whether for payment or free of charge”, and the **deployer**, who uses it “under its authority except where the AI system is used in the course of a personal non-professional activity”.[^ria] When your school or education authority introduces a tool it has bought, it is the deployer, and the teacher uses the tool on its behalf; if it develops the tool, or has it developed, to put it into service under its own name, it is also its provider. What a teacher does on their own initiative for their work falls into a less clear area, and it is one more reason to use the tools your school or education authority provides.

### AI literacy

Article 4 originally required providers and deployers to “take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff”.[^ria] Since 27 July 2026, after the Omnibus, the obligation is softer: they must “take measures to support the development of AI literacy of their staff”, and the text makes clear that it does not require them “to guarantee any specific level of AI literacy of any individual”. The Commission and the Member States must support and facilitate that effort.[^omnibus]

### Prohibited practices

The most relevant in education is in Article 5(1)(f): the use of AI systems “to infer emotions of a natural person in the areas of workplace and education institutions”, except for medical or safety reasons. It has been prohibited since 2 February 2025.[^ria] The Commission’s guidelines illustrate it with examples:[^directrices]

- A language-learning application with emotion recognition is not prohibited if it is used outside an education institution; if the school requires students to use it, it is.
- An online exam proctoring system that tracks students’ gaze to detect unauthorised material is not prohibited; if it also detects nervousness or anxiety, it is.
- Using emotion recognition to infer students’ interest or attention is prohibited.

The rest of the list (subliminal manipulation, exploiting vulnerabilities, social scoring, predicting crimes based solely on a person’s profile, facial recognition databases, biometric categorisation to deduce sensitive data, real-time biometric identification in public spaces for law enforcement) has little bearing on a school’s work.

From 2 December 2026, two prohibitions are added with direct consequences for life at school: systems that generate realistic images, videos or audio “of an identifiable natural person’s intimate parts”, or of an identifiable person engaged in sexually explicit activities, without their consent, and those that generate child sexual abuse material.[^omnibus] This covers fake “nude” apps, whose use among students puts relationships at school at risk.

### High risk in education

Annex III treats as high-risk four uses in education and vocational training:[^ria]

- (a) determining access or admission to institutions, or assigning students to them;
- (b) evaluating learning outcomes, including when they are used to steer the learning process;
- (c) assessing the appropriate level of education a person will receive or will be able to access;
- (d) monitoring and detecting prohibited behaviour of students during tests.

Not every system that touches these areas is high-risk. Under Article 6(3), it is not when it does not materially influence the decision: if it performs a narrow procedural task, improves the result of a previously completed human activity, detects decision-making patterns or deviations from them without replacing human assessment, or performs a preparatory task. But it always is when it performs profiling of people.[^ria]

The corresponding obligations apply from 2 December 2027. For the school or education authority that deploys one of these systems, they include assigning human oversight “to natural persons who have the necessary competence, training and authority”, informing students that the system is used with them and, for a body governed by public law, carrying out a fundamental rights impact assessment before deploying it.[^ria]

One question remains open: Article 25(1)(c) makes the provider of a high-risk system anyone who modifies “the intended purpose of an AI system, including a general-purpose AI system”, so that it becomes high-risk.[^ria] How that applies to a teacher who uses a general-purpose chatbot to mark is not settled in the text. It is one more argument, together with Article 22 GDPR, for not letting AI decide the mark.

### Transparency

From 2 August 2026, providers must inform people that they are interacting with an AI system and mark synthetic content so that it is detectable; generative systems already on the market before that date have until 2 December 2026 to mark it. Whoever uses a system to generate deep fakes must disclose that the content “has been artificially generated or manipulated”, and whoever publishes AI-generated text “with the purpose of informing the public on matters of public interest” must say so, unless it has undergone human review or editorial control and someone holds editorial responsibility for it.[^ria] Ordinary class materials do not fall under these cases: labelling them is good practice, not an obligation.

### Who supervises

Each Member State must “establish or designate as national competent authorities at least one notifying authority and at least one market surveillance authority” for the AI Act, and those authorities “may provide guidance and advice on the implementation of this Regulation”.[^ria] The European Commission supervises the providers of general-purpose AI models, a task it entrusts to its AI Office.[^ria] Everything to do with personal data remains the task of each country’s data protection supervisory authority under the GDPR.[^rgpd]

## What each country decides

EU law leaves several points on this page to each Member State. Check them with your education authority or your data protection officer:

- the age, between 13 and 16, from which a child can consent alone to an online service offered directly to them (Article 8(1) GDPR);
- the legal basis on which schools process student data for teaching, and who the controller is (Articles 6(3) and 4(7) GDPR);
- the authorities that supervise the AI Act (Article 70 of the AI Act) and the data protection supervisory authority (Article 51 GDPR).

[^rgpd]: Regulation (EU) 2016/679, General Data Protection Regulation ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)): recital 26 (anonymous information and pseudonymised data) and Articles 4(1) (personal data), 4(2) (processing), 4(5) (pseudonymisation), 4(7) (controller), 5(1)(c) (data minimisation), 5(1)(f) (integrity and confidentiality), 6(1)(e) and 6(3) (task carried out in the public interest), 8(1) (child’s consent in relation to information society services), 9(1) (special categories), 22(1) and 22(2) (automated decisions), 25(1) (data protection by design), 28(1) and 28(3) (processor), 29 (processing under the authority of the controller), 32(1)(a) (security of processing), 35(1) (data protection impact assessment), 37(1)(a) (data protection officer of public authorities) and 51(1) (supervisory authority).
[^nowak]: Judgment of the Court of Justice of 20 December 2017, *Nowak*, C-434/16, paragraphs 37 and 62 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62016CJ0434)). It interprets Directive 95/46, which the GDPR replaced with a definition of personal data of essentially the same scope.
[^srb]: Judgment of the Court of Justice of 4 September 2025, *EDPS v SRB*, C-413/23 P, paragraphs 73, 76, 77, 85, 86 and 112 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0413)). It interprets the data protection regulation for the EU institutions, whose definition of personal data is “essentially identical” to that of the GDPR (paragraph 52).
[^ria]: Regulation (EU) 2024/1689, Artificial Intelligence Act ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)): Articles 3(3) (provider), 3(4) (deployer), 4 (AI literacy, original text), 5(1)(d), 5(1)(f), 6(3), 25(1)(c), 26(2), 26(11), 27, 50, 70(1), 70(8), 88(1) and 113, and Annex III, point 3.
[^omnibus]: Regulation (EU) 2026/1744 of 8 July 2026, Digital Omnibus on AI ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)), amending the AI Act: new Article 4; Article 5(1), points (ba) and (bb); Article 111(2) and (4); Article 113.
[^directrices]: European Commission, [*Guidelines on the ethical use of artificial intelligence and data in teaching and learning for educators*](https://data.europa.eu/doi/10.2766/7967834), 2026, table 1, with examples from the Commission’s guidelines on prohibited AI practices.
