---
adapted: true
derived_from:
  es/datos-alumnado/slides.md: "0eadf84db108779f8a39c00afe3fb923606578c5"
---

<!-- .slide: id="idea-central" class="statement" -->
## AI almost never needs to see your students

Ask for the template or the procedure; anonymise only when the content is needed.

Notas:
**Key message:** before asking how to anonymise, ask whether any data need to be sent at all. In most tasks, what the AI contributes is drafting, structuring or calculating, and you can ask for that without real data.

---

<!-- .slide: id="tres-vias" class="cards fragments" -->
## Three routes, in this order

### 1. No data: yes
The AI writes the template, the formula or the procedure; you apply it to the data.

### 2. Cleaned work: not settled
Only the content, with a code. The risk is minimal, but it depends on the controller’s instructions.

### 3. Personal data: no
Except in tools the controller has contracted or approved.

Notas:
The third is a legal obligation: the authority to process student data belongs to the controller (the school or the education authority, depending on where you teach), not to each tool a teacher uses. Anyone acting under its authority processes the data only on its instructions (Article 29 GDPR), and a chatbot with a personal account is not a processor bound to it by a contract (Article 28). The second is the one people ask about most, and the next slide covers it. A local model, offline, sends nothing out, but the work is still student data, and it is better not to keep it on teachers’ personal devices.

---

<!-- .slide: id="tabla-codigos" class="bullets" -->
## With a code, the risk goes down, but the controller decides

- **Keeping the table**: yes, like the mark book, outside the tool
- **For whoever receives** the cleaned text, it is not personal data
- **For you** it is still the student’s data, and sending it is already processing it
- **The controller’s instructions** decide; its **data protection officer** can advise

Notas:
This is the question asked most often: if I replace the name with a code and keep the table, can I paste the work into a chatbot with my own account? If the text still gives the student away, no: that is a legal obligation. If it is properly cleaned, no EU rule expressly forbids it, and whether it is allowed depends on the controller’s instructions, because anyone acting under its authority processes the data only on its instructions (Article 29 GDPR). In the meantime: route 1 if it is enough; if route 2 is used, a properly cleaned text, a temporary chat and training turned off; and if it is going to be done often, ask for approval through the school, with the advice of the controller’s data protection officer.

---

<!-- .slide: id="seudonimizar" class="statement" -->
## Changing the name is only the first step

You may know whose work it is; whoever receives the text must not be able to find out.

Notas:
What is at stake in route 2 is what whoever receives the text can work out. The name is the easy part: the file carries the author and the comments, and the text itself may be enough.

---

<!-- .slide: id="que-identifica" class="table" -->
## What identifies a student besides the name

| What | Examples |
| --- | --- |
| Identifiers | Name, signature, email address, username in the virtual learning environment |
| Metadata | Author in the properties, comments, location of a photo |
| Quasi-identifiers | Class, age, town, club, a relative’s job |
| Special categories | Health, religion, ethnic origin |
| Voice and face | Audio and video recordings of presentations |

---

<!-- .slide: id="singularizacion" class="statement" -->
## Without a name, a student can still be identified

“The only girl in 4B who plays for the Galician team” needs no name.

Notas:
The GDPR calls this singling out: isolating a person within a group. In a class of twenty, two or three details are enough. And some texts cannot be cleaned without destroying them, such as an autobiographical essay: then it is not route 2.

**Demo (10 min): removing the name is not enough**. Word or LibreOffice, and any chatbot in a temporary chat. Material: an invented essay in `.docx`, like the one in the page’s “Practice” section, with the name in the header, the author in the properties and a comment by the student with a health detail.

1. Open the essay and ask the group what data they can see: the name in the header.
2. Show the file’s properties (author, “last modified by”) and the comment. In Word, File → Info → Check for Issues → Inspect Document.
3. In LibreOffice, turn on “Remove personal information on saving”, save and reopen: the comment is still there, with a generic author. It has to be deleted separately.
4. Read the text aloud and ask the group to point out the quasi-identifiers and the health detail.
5. Paste only the cleaned text into the chat, with the rubric, and ask for an assessment against each criterion with no final mark.

**Expected result:** the group discovers at least one piece of data they had not seen (the metadata or the comment), and the feedback on the writing is just as useful with the cleaned text.
**If it fails:** do the “Practice” exercise on the page, aloud.
**Key message:** the safest option is to copy only the text; the file carries more than you can see.

---

<!-- .slide: id="pasos-anonimizar" class="checklist" -->
## Before asking for help with a piece of work

- [ ] A copy, and if the text is enough, only the text.
- [ ] No header, signature or identifiers.
- [ ] No metadata or comments.
- [ ] Quasi-identifiers rewritten, as little as possible.
- [ ] No special categories.
- [ ] Photos cropped and without location.
- [ ] The code table, outside the tool.

Notas:
And two steps that are often forgotten: no online services to anonymise, because to remove the data they have to receive them, and turn off the use of conversations to train models (the Chatbots page shows where).

---

<!-- .slide: id="nota-docente" class="statement" -->
## The AI suggests; you decide the mark

A mark that came only from the tool would be a decision based solely on automated processing (Article 22 GDPR).

Notas:
In addition, the AI Act lists AI systems intended to be used to evaluate learning outcomes as high-risk (Annex III, point 3(b)). The legal framework page of the ethics block has the details.

---

<!-- .slide: id="prompt-procedimiento" class="prompt" -->
## The columns and three invented rows are enough

```text
I have a spreadsheet with these columns: student, test_1, test_2, project, notebook.
These three rows are invented, just so you can see the format: […]
Write the LibreOffice Calc formula for the weighted average (30%, 30%, 30% and 10%)
and another one that counts how many students have less than 5 in each test.
```

Notas:
The full version, with the three rows, is on the page.

**Demo (5 min): the AI writes the formula without seeing the marks**. LibreOffice Calc or Excel, and any chatbot in a temporary chat. Material: a spreadsheet with about twenty invented students and four marks each.

1. Show the full spreadsheet and say that this is the one that will never leave the computer.
2. Paste the prompt from the page into the chat: only the columns and three invented rows.
3. Copy the formulas it returns into the spreadsheet and check one row by hand.

**Expected result:** two formulas that work on the real spreadsheet without the AI having seen it.
**If it fails:** if the formula gives an error, paste the error message into the chat; if there is no network, show the formula already prepared.
**Key message:** asking for the procedure instead of the result is the safest route, and the one most often forgotten.

---

<!-- .slide: id="casos-anonimizables" class="table" -->
## Typical cases and their route

| Case | Route | What to do |
| --- | --- | --- |
| Essay or piece of work | 2 | Anonymised text and rubric |
| Handwritten exam | 2 | Cropped photo, without location |
| Marks of a group | 1 | The formula, with an invented sample |
| Reports and families | 1 | A template with gaps |
| Specific needs | 1 | The learning need, not the diagnosis |

Notas:
To adapt a material, “needs short sentences, basic vocabulary and one idea per paragraph” works just as well as naming a disorder, and does not reveal health data. The page has all seven cases. For the exam, the AI transcribes and points out errors, and the teacher decides the mark for each question.

**Demo (5 min): a template with gaps**. Any chatbot in a temporary chat and a word processor. Material: an invented table with the data of five students (name, class, strengths, areas to improve, next steps).

1. Ask the chat for a form tutor’s report for the first term with the placeholders `[NAME]`, `[CLASS]`, `[STRENGTHS]`, `[TO_IMPROVE]` and `[NEXT_STEPS]`.
2. Paste the template into the word processor.
3. Fill in one report with find and replace, or all of them with mail merge from the table.

**Expected result:** a well-written report with data that never left the computer.
**If it fails:** show a template already generated and fill it in.
**Key message:** the AI provides the wording; you add each student’s data.

**Demo (5 min): a handwritten exam**. A phone, the computer’s photo viewer and a chatbot that accepts images. Material: an invented exam filled in by hand with an invented name, photographed with the camera’s location turned on.

1. Show, in the photo’s properties, the location the camera recorded.
2. Crop out the header and the signature, and share or export the photo without location (on an iPhone, Options → turn off Location when sharing).
3. Upload the cropped photo to the chat and ask it to transcribe the answers before assessing them.
4. Compare the transcription with the original: reading errors show up there, before the marking.

**Expected result:** a transcription that can be checked and an assessment for each question, with no name, signature or location.
**If it fails:** show the cropped photo and explain the steps.
**Key message:** the photo carries more than what you can see, and the transcription is checked before relying on the marking.

---

<!-- .slide: id="sin-anonimizacion" class="bullets" -->
## Where anonymisation is not possible

- **Recordings**: voice and face identify; only contracted tools, or transcription on your own computer.
- **Behaviour and disciplinary matters**: the facts identify the people; invented cases only.
- **Autobiographical texts**: if nothing is left after cleaning them, it is not route 2.

---

<!-- .slide: id="practica-fragmento" class="practice" -->
## What would you remove?

1. Read the essay fragment in the page’s “Practice” section.
2. Write down everything you would remove or rewrite before asking for feedback on the writing.
3. Compare your list with someone else’s, and then with the solution.

10 minutes, in pairs.

Notas:
When pooling answers, look for the three kinds of data: health (the diabetes and the glucose meter), singling out (“the only girl in 4B…”) and the quasi-identifiers (Moaña, the under-16 girls’ team, the father’s job). At the end, ask what the fragment does not show: the header, the properties and the comments, if it arrived as a file.
