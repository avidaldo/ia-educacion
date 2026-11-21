---
title: Student data
description: How to use AI to mark work, analyse marks or draft reports without exposing student data, what you can do with a piece of work whose name you have replaced with a code, and what EU law says in each typical case.
adapted: true
derived_from:
  es/datos-alumnado/index.md: "545cc3bc432229ae80c063504f8a2ed617847940"
---

> [!NOTE]
> **A teacher’s reading, not legal advice**
> This page applies what is explained in [Legal framework](../etica-legal/normativa.md#data-protection) to typical cases, with the same approach as the rest of the block: each recommendation says whether it is a **legal obligation**, an **institutional recommendation** or **good practice**. It covers EU law only; your country adds its own rules. For a specific case, the reference is the controller of your students’ data, the body that decides how they are processed (the school or the education authority, depending on where you teach), and its data protection officer, which every public authority or body must have (Article 37(1)(a) GDPR).

## The prior question: does the AI need the data?

You have twenty-five essays to mark and want AI to help you with the feedback. Can you paste them into a chatbot if you replace each name with a code? The answer depends less on the code than on two things: what whoever receives the text can find out, which depends on how you clean it, and the tool you use, which is not for you to choose but for the controller: the body that “determines the purposes and means of the processing” of your students’ data (Article 4(7) GDPR).[^rgpd]

Before cleaning anything, ask yourself whether the AI needs to see your students. It almost never does: in most tasks what it contributes is drafting, structuring or calculating, and you can ask for that without real data. There are three routes, from the safest to the least safe:

| What you send to the AI | Allowed? |
| --- | --- |
| **1. Nothing about your students.** The AI writes the template, the formula or the procedure, and you apply it to the data. It works for reports, messages to families, analysing marks and rubrics | **Yes** |
| **2. The work, with nothing that says whose it is.** The name replaced with a code and the text cleaned of details that give the student away | **Not settled.** If it is properly cleaned, the risk to the student is minimal, but whether you may do it depends on the controller’s instructions ([why](#so-can-i-paste-it-into-a-chatbot-with-my-own-account)) |
| **3. Personal data.** The name, or details that reveal whose it is | **No**, except in tools the controller has contracted or approved |

Route 3 is a **legal obligation**: the authority to process student data belongs to the controller, not to each tool a teacher uses ([who may process student data](../etica-legal/normativa.md#who-may-process-student-data)). Anyone acting under the controller’s authority may process the data only “on instructions from the controller” (Article 29 GDPR), and a company that processes them on its behalf must be a processor bound to it by “a contract or other legal act” (Article 28(3)).[^rgpd] A chatbot used with your personal account is not such a processor: its provider has no contract with the controller.

A model run on your own computer, offline, sends nothing out ([the demonstration](../etica-legal/index.md#privacy-the-practical-rule)): no third party receives the data. But they are still student data, and it is better not to keep them on your personal devices (**good practice**): the controller is responsible for their “appropriate security” (Article 5(1)(f) and 5(2) GDPR), and those devices are outside its control.

## The code table, in four questions

The usual procedure for route 2 is reasonable: you replace the name with a code (`R-07`), keep the table that says who each code is somewhere else, ask the AI for help with the work and, when you finish, give each student back their assessment. It raises four questions, and only one of them is unresolved.

### Can I keep a table saying who each code is?

Yes. There is nothing wrong with your knowing who wrote each piece of work: you are their teacher, and assessing students is part of the school’s work; in public education it is a task carried out in the public interest, whose basis is laid down by Union or national law (Article 6(1)(e) and 6(3) GDPR). Keep the table with the same care as your mark book: never in the AI tool, and preferably in the school’s storage or on a school computer with your own password rather than on a personal device (**good practice**).

### With the code, is the work now anonymous?

It depends for whom. For someone who receives the text without the table, it may be: if they have no other reasonable means of finding out whose it is, for them it is not personal data.[^srb] For you it is not: it is still the student’s data, and the GDPR calls this **pseudonymisation**, not anonymisation.[^rgpd] And not only because of the table: you know whose work it is, because you are going to give it back with your comments. The legal detail is in [Anonymising and pseudonymising](../etica-legal/normativa.md#anonymising-and-pseudonymising).

### So can I paste it into a chatbot with my own account?

**If the text still gives the student away, no** (**legal obligation**): it would mean sending personal data to a company that has no contract with the controller. What can give a student away, besides the name, is in [the next section](#removing-the-name-is-not-enough).

**If it is properly cleaned, it is not settled.** The risk to the student is minimal, because whoever receives the text cannot know whose it is. What is missing is cover: for you they are still the student’s data, and sending them is already processing them, since the GDPR counts “disclosure by transmission” among processing operations (Article 4(2)). Anyone acting under the controller’s authority may process the data only “on instructions from the controller” (Article 29, **legal obligation**),[^rgpd] and it is for those instructions to say whether they cover a text that no longer identifies anyone.

In short: no EU rule expressly forbids it, and whether it is allowed depends on your controller’s instructions.

### What do I do in the meantime?

What follows is **good practice**:

- **If route 1 is enough, use it.** It is the only one with no doubts.
- **If you use route 2, make sure the text is properly cleaned** ([how](#how-to-anonymise-a-piece-of-work)), use a temporary chat with training turned off, and never use it for what cannot be cleaned: recordings, behaviour incidents, health.
- **If you are going to do it often, ask for approval** through your school. If the controller has a data protection officer, they can advise you: one of their tasks is to advise “the employees who carry out processing” of their obligations (Article 39(1)(a) GDPR).[^rgpd]

## Removing the name is not enough

The code is only the first step, because the name is not the only thing that says whose a piece of work is: the file carries the author and the comments, and sometimes the text itself is enough. The answers to an exam and the comments of whoever marks it are also the student’s personal data, and handwritten answers also contain information about their handwriting.[^nowak] This is what can identify a student in a piece of work:

| What | Examples |
| --- | --- |
| Direct identifiers | Name, signature, photo, email address, username in the virtual learning environment, number on the class list |
| File metadata | Author and “last modified by” in the properties, comments, tracked changes, the location of a photo |
| Quasi-identifiers | Class, age, town, club, a relative’s job: separately they say nothing, but together they point to one person |
| Special categories | Health, religion, ethnic origin, sexual orientation: even when they do not identify anyone, they are the most protected data |
| Voice and face | Audio and video recordings of oral presentations |

Quasi-identifiers are the ones that slip through most often: two or three details are enough to isolate a person within a group without knowing their name, and the GDPR counts this among the means of identifying someone (it calls it **singling out**).[^rgpd] In a class of twenty, “the only girl in 4B who plays for the Galician team” needs no name.

And some texts cannot be cleaned without destroying them: an autobiographical essay full of personal details is still recognisable however much you remove. Then it is not route 2, and what is left is route 1 or 3.

## How to anonymise a piece of work

1. **Work on a copy**, never on the file the student handed in.
2. **If the text is enough, copy it and paste it into the chat**: that way no metadata travel with it. If you have to upload the file, clean it first (step 4).
3. **Remove the header, the signature and the identifiers**: name, username, email address, number on the class list.
4. **Clean the metadata and the comments.**
   - In Word: File → Info → Check for Issues → Inspect Document, and remove “Comments, Revisions, Versions, and Annotations” and “Document Properties and Personal Information”.[^word]
   - In LibreOffice, the option “Remove personal information on saving” (Tools → Options → LibreOffice → Security → Options) removes the authorship data and replaces the author of comments with a generic value, but **does not delete the comments**: you have to remove them separately.[^libreoffice]
5. **Rewrite the quasi-identifiers** that the task does not need: “the sports hall in Moaña” becomes “the sports hall”, and “the only girl in 4B who…” goes. Change as little as possible: if you are going to correct the writing, what you correct has to still be there.
6. **Remove special categories and other sensitive details**: a diagnosis, a belief, a family situation.
7. **In photos**, crop out the header and the signature, and check the location: the phone’s camera can record where the photo was taken. On an iPhone you can share a photo without it (in the share sheet, Options → turn off Location) or stop the camera from recording it (Settings → Privacy & Security → Location Services → Camera → Never).[^apple] On Android it depends on each manufacturer’s camera app. The safest option is to photograph students’ work with the camera’s location turned off.
8. **Keep the code → student table outside the tool**, preferably in the school’s storage or on a school computer with your own password.
9. **Do not use an online service to anonymise**: to remove the data, that service has to receive them.
10. **Turn off the use of your conversations to train models** (**good practice**). Where to do it in each chatbot is in [Chatbots](../chatbots/index.md#que-tus-conversaciones-entrenen-modelos).

> [!IMPORTANT]
> **Anonymisation is not always possible**
> The European Data Protection Supervisor and the Spanish data protection authority (AEPD), in a joint paper, sum it up in three ideas that affect any teacher (**institutional recommendation**).[^malentendidos] Changing the name is not anonymising. In a small group, such as a class, a few details are enough for someone who knows the group to tell who is being talked about. And it cannot be left to a program: names can be found automatically, but indirect details are not always obvious.

## Typical cases

| Case | Route | What to do |
| --- | --- | --- |
| Feedback on an essay or a piece of work | 2 | Paste the anonymised text with the rubric; you decide the mark |
| Marking a handwritten exam | 2 | A cropped photo, with no header or location |
| Analysing the marks of a group | 1 | The AI writes the formula from an invented sample |
| Reports and messages to families | 1 | A template with gaps that you fill in on your computer |
| Adapting materials for students with specific needs | 1 | Describe the learning need, not the diagnosis or the person |
| Recorded oral presentations | 3 | Voice and face identify: only contracted tools, or a local model |
| Behaviour and disciplinary matters | 1 | Invented cases only |

### Feedback on an essay or a piece of work

Anonymise the text with the steps above and paste it with the rubric. Ask for an assessment against each criterion, with a quotation from the text that justifies it, and a suggestion for improvement addressed to the student:

```text
You are a [subject] teacher in [year]. Here is an essay and the rubric used to assess it.
For each criterion, tell me which level you would give it, with a short quotation from the text that justifies it,
and a concrete suggestion for improvement addressed to the student. Do not give the final mark: I decide it.

[rubric]

[anonymised text]
```

**Legal obligation.** The AI suggests and you decide the mark, after reviewing the work. A mark that came only from the tool would be a decision “based solely on automated processing”, and the student has the right not to be subject to one that “produces legal effects concerning him or her or similarly significantly affects him or her” (Article 22(1) GDPR).[^rgpd] In addition, the AI Act lists AI systems “intended to be used to evaluate learning outcomes” among the high-risk ones:[^ai-act] this is explained in [High risk in education](../etica-legal/normativa.md#high-risk-in-education).

### Marking a handwritten exam

Models that accept images can read handwriting, but check their transcription before relying on the marking. Before uploading the photo, crop out the header (name, class, signature) and check the location (step 7). If the exam has personal questions or health data, it is not route 2.

Let the AI transcribe the answers and point out errors, and decide the mark for each question yourself, as in the previous case.

### Analysing the marks of a group

The AI does not need the marks to write the formula: the column names and a few invented rows are enough. Then you copy the formula into your spreadsheet, which never leaves your computer.

```text
I have a spreadsheet with these columns: student, test_1, test_2, project, notebook.
These three rows are invented, just so you can see the format:
Student A, 6.5, 7.0, 8.0, 9
Student B, 4.0, 5.5, 6.0, 5
Student C, 3.0, 4.5, 5.0, 5
Write the LibreOffice Calc formula for the weighted average mark (30%, 30%, 30% and 10%)
and another one that counts how many students have less than 5 in each test.
```

It is the safest route and the one most often forgotten: asking for the **procedure** instead of the result. It works just as well with a macro, a script or a pivot table.

### Reports and messages to families

Ask for the template with placeholders (`[NAME]`, `[STRENGTHS]`, `[TO_IMPROVE]`) and fill it in on your computer, by hand or with your word processor’s mail merge. The AI provides the wording; each student’s data never leave your computer.

### Adapting materials for students with specific needs

Describe the learning need, not the diagnosis or the person: “adapt this text for someone who needs short sentences, basic vocabulary and one idea per paragraph” works just as well as naming a disorder, and does not reveal health data. **Legal obligation**: data concerning health are a [special category of personal data](../etica-legal/normativa.md#special-categories-of-personal-data), whose processing the GDPR prohibits except in the cases it lists (Article 9).[^rgpd]

### Recorded oral presentations

A person’s voice and face identify them, and there is no reasonable way to anonymise them. A recording can only go to a tool contracted by the controller. If what you need is a transcript, there are transcription models that run on your own computer, offline.

### Behaviour and disciplinary matters

These are among the most sensitive data a school holds, and they can almost never be anonymised: the facts identify the people involved. If you want help with the wording, ask for a model document based on an invented case and adapt it yourself.

## Practice

This fragment of an essay is invented. Before reading the solution, write down everything you would remove or change before asking for feedback on the writing:

> The most important place for me is the municipal sports hall in Moaña, where I train with the under-16 girls’ handball team. Since I was diagnosed with type 1 diabetes last year, my mother comes to every training session with the glucose meter. This year I am the only girl in 4B who plays for the Galician team, and when I come back from training camps the sports hall is where I feel at home, even though my father, who works nights at the cannery, cannot come.

What had to be changed:

- **Health**: “I was diagnosed with type 1 diabetes” and the glucose meter. It is a special category, and it is not needed to assess the writing.
- **Singling out**: “the only girl in 4B who plays for the Galician team”.
- **Quasi-identifiers**: Moaña, the under-16 girls’ team and the father’s job. Together, they point to a single person.
- **What the fragment does not show**: if it arrived as a file, the header, the properties and the comments.

With all that removed, the sentence still works for correcting the writing: “When I come back from away matches, the sports hall is where I feel at home, even though someone in my family cannot come.”

[^rgpd]: Regulation (EU) 2016/679, General Data Protection Regulation ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)), recital 26 (singling out; pseudonymised data) and Articles 4(2) (processing), 4(5) (pseudonymisation), 4(7) (controller), 5(1)(f) and 5(2) (security and accountability), 6(1)(e) and 6(3) (task in the public interest), 9 (special categories), 22 (automated decisions), 28 (processor), 29 (processing under the authority of the controller) and 39(1)(a) (tasks of the data protection officer).
[^srb]: Judgment of the Court of Justice of 4 September 2025, *EDPS v SRB*, C-413/23 P, paragraphs 77 and 86 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0413)). It interprets Regulation (EU) 2018/1725, on processing by EU institutions, whose definition of personal data the Court reads in the same way as the GDPR’s (paragraph 52).
[^nowak]: Judgment of the Court of Justice of 20 December 2017, *Nowak*, C-434/16, paragraphs 37 and 62 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62016CJ0434)), on the answers of a candidate at a professional examination and the examiner’s comments. It interprets Directive 95/46, which the GDPR replaced with a definition of personal data of essentially the same scope.
[^ai-act]: Regulation (EU) 2024/1689, Artificial Intelligence Act ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)), Annex III, point 3(b).
[^malentendidos]: Spanish Data Protection Agency (AEPD) and European Data Protection Supervisor, [*10 misunderstandings related to anonymisation*](https://www.aepd.es/guides/10-anonymisation-misunderstandings.pdf), 2021, misunderstandings 1, 3 and 7 (pp. 3, 4 and 6).
[^word]: Microsoft, [*Remove hidden data and personal information by inspecting documents, presentations, or workbooks*](https://support.microsoft.com/en-gb/office/remove-hidden-data-and-personal-information-by-inspecting-documents-presentations-or-workbooks-356b7b5d-77af-44fe-a07f-9aa4d085966f), accessed 21 November 2026.
[^libreoffice]: LibreOffice Help, [*Security Options and Warnings*](https://help.libreoffice.org/latest/en-US/text/shared/optionen/securityoptionsdialog.html), accessed 21 November 2026.
[^apple]: Apple, [*Manage location metadata in Photos*](https://support.apple.com/en-gb/guide/personal-safety/ips0d7a5df82/web), accessed 21 November 2026.
