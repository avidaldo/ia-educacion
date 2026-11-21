---
derived_from:
  es/webs-educativas/slides.md: "9fc62f8e828e540a2aae8bf38aa8b1e6d6b4e405"
---

<!-- .slide: id="sin-programar" class="statement" -->
## An interactive page for class, without knowing how to program

Simulators, revision exercises, timelines, games: a single HTML file.

---

<!-- .slide: id="ejemplos" class="fragments" -->
## What works well

- A simple simulator.
- A revision exercise with hints and instant correction.
- A timeline or a map explored by clicking.
- A calculator for the subject.
- A vocabulary or concept-matching game.

---

<!-- .slide: id="donde-crear" class="table dense" -->
## Where to create them

| Tool | Sharing the result |
| --- | --- |
| Claude (Artifacts) | Whoever opens it needs a Claude account (18+) |
| Gemini (Canvas) | Public link; anyone who has it can edit the app’s data |
| ChatGPT (Canvas, Sites) | Sites, on Plus and Pro, publishes it at an address of its own; otherwise, download the code |

Notas:
In every case, the most robust route is to ask for a single HTML file, download it and publish it yourself where students already go.

---

<!-- .slide: id="prompt-pagina" class="prompt dense" -->
## How to ask for it

```text
Create an interactive web page in a single HTML file, with no external dependencies,
for [level] on [topic].
It must let students: [what students will do, step by step].
Design readable on a phone and a projector, good contrast, usable with the keyboard.
Do not collect or send any user data.
```

Notas:
**Demo (10 min): from the request to Moodle**. Gemini (Canvas) or Claude, and a Moodle test course.

1. Ask for a page with the prompt from the web page and a topic suggested by the group.
2. Try it and ask for two specific changes (“add a hint to each question”).
3. Download the HTML file.
4. Create a Page resource in Moodle and paste the code into the source code view.

**Expected result:** the page works inside Moodle.
**If it fails:** if Moodle deletes the code, upload the file as a File resource.
**Key message:** the content is checked like any other material; the design is the easy part.

---

<!-- .slide: id="moodle" class="table" -->
## Publishing it on Moodle

| Option | When |
| --- | --- |
| Page resource, pasting the HTML | The simplest option |
| Text and media area with an `<iframe>` | To see it on the course page |
| File resource with the `.html` | If Moodle deletes the code |
| URL resource | If it is already published elsewhere |

Notas:
Moodle cleans the HTML in most places (forums, for example), but not in the Page resource or in descriptions such as the text and media area, unless the administrators have turned on cleaning for the whole site.

---

<!-- .slide: id="fuera" class="two-col" -->
## Publishing it outside Moodle

### Netlify Drop
Drag in the folder and get a public address.

### GitHub Pages
Free and stable; this website is published with it.

---

<!-- .slide: id="revisar" class="checklist" -->
## Before publishing

- [ ] Correct content.
- [ ] Works on a phone, a computer and a projector.
- [ ] Accessible: contrast, keyboard, alternative text.
- [ ] Collects no data and loads no resources from other websites.
- [ ] Images your own or licensed.

---

<!-- .slide: id="presentaciones" class="section" -->
## Presentations

---

<!-- .slide: id="contenido-primero" class="statement" -->
## The outline first; the design afterwards

Asking for “a presentation on X” in one go gives eye-catching slides with generic content.

---

<!-- .slide: id="tres-caminos" class="cards" -->
## Three routes

### Chatbot
Gemini (Canvas, to Google Slides), notebooks, ChatGPT and Claude (PowerPoint).

### Specialised tool
Gamma or Canva: the most eye-catching result, on their platform.

### Text and style
Markdown converted with Marp, Slidev or reveal.js: reusable content, fixed design.

---

<!-- .slide: id="practica-presentacion" class="practice" -->
## From the outline to the slides

1. Ask for a ten-slide outline on a topic from your subject.
2. Correct it: data, order, what is not needed.
3. Generate the slides by one of the three routes.
4. Review what changed between the outline and the result.

**15 minutes.** Outcome: a presentation with checked content.
