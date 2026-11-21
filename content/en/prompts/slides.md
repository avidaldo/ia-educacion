---
derived_from:
  es/prompts/slides.md: "1facdc2a0332ca2b8bb78e8b23eb93be85e3d44e"
---

<!-- .slide: id="especificacion" class="statement" -->
## A good prompt is a specification

It says what product you want, for whom, with what constraints and how you will know it is right.

Notas:
**Key message:** asking an AI for something is more like commissioning work from a competent person than searching on Google. Whatever is not specified, the model fills in on its own.

---

<!-- .slide: id="ingredientes" class="cards fragments" -->
## What most affects the result

### Task
What product you want: activity, rubric, question bank…

### Context
Level, time, resources and group profile, without personal data.

### Output
Format, fixed headings and length limits.

### Constraints
Do not invent regulations or figures; mark the assumptions.

Notas:
These four pieces are the template on the page. You don’t need to use all of them in every request: they are a checklist.

---

<!-- .slide: id="plantilla" class="prompt dense" -->
## A starting template

```text
You are an expert consultant in curriculum design.
Task: I want to create [activity / question bank / rubric].
Context: subject, level, duration, resources, group profile (no personal data).
Before answering: ask me 3–5 clarifying questions; if information is missing, propose up to 3 explicit assumptions.
Output: Markdown, with these headings: […]; max. 1 page.
Constraints: do not invent regulations, data or figures; if you don't know, say so.
```

Notas:
The full version, with every section, is on the page. Copy it from the website, not from the slide.

---

<!-- .slide: id="rol" class="comparison" -->
## The role sets the voice, not the task

### Poor
“You are a Python expert.”

You leave it to the model to decide what “expert” means.

### Better
“Act as a security auditor: review this code for critical vulnerabilities (OWASP Top 10) and suggest fixes.”

The role gives the perspective; the instructions give the task.

Notas:
A role shifts the answer towards the vocabulary and criteria associated with that figure. It does not make the model “smarter”. If the task is factual and we only give a role, we increase the risk of plausible but false answers.

---

<!-- .slide: id="objetivo" class="comparison" -->
## A clear objective, with its evidence

### Poor
“Make an activity about AI.”

### Better
“Create a 50-minute activity for second-year VET students on how to **evaluate an AI’s answers**. Evidence: students identify 3 typical errors and suggest 1 improvement.”

Notas:
Ask the group what the first version is missing before showing the second. The answers come up on their own: level, duration, final product.

---

<!-- .slide: id="contexto" class="fragments" -->
## The minimum teaching context

- **Level**: year or VET programme.
- **Time**: length of the session or the task.
- **Resources**: classroom, projector, mobile phones, internet…
- **Final product**: what students hand in.

With these four pieces of information, most generic answers disappear.

---

<!-- .slide: id="preguntar-primero" class="two-col" -->
## Asking it to question you first

### Use it
For complex design tasks (projects, full rubrics), where the context decides everything.

### Avoid it
For quick requests: it only adds a step.

Notas:
Wording: “Ask me 3–5 clarifying questions, only the necessary ones”. It forces the gaps to be detected before they are filled in, for example by assuming that everyone in the group has a laptop.

---

<!-- .slide: id="supuestos" -->
## Explicit assumptions

- If information is missing, the model fills the gaps or becomes vague.
- Ask it: “if critical information is missing, propose up to 3 explicit assumptions”.
- That way you see what it is assuming, and you correct it before it builds everything on top.

---

<!-- .slide: id="formato" class="two-col" -->
## Format and delimiters

### Delivery format
- Table with fixed columns.
- Checklist.
- Markdown with exact headings.

### Delimiters
Separate your instructions from the text it has to analyse:

```text
School context:
"""
[text]
"""
```

Notas:
Triple quotes or named tags (`<syllabus>…</syllabus>`) both work. What matters is to always use the same ones and to name them in the instruction.

**Demo (5 min): a prompt that writes prompts**. Any chatbot (ChatGPT, Gemini or Claude), in a temporary chat.

1. Paste the first example from the “Annotated examples” page (“Act as an educational adviser… Give me ONLY the final prompt”).
2. Read aloud the template it returns: clarifying questions, assumptions, fixed headings.
3. Open a new chat, paste the template and fill in the topic with a suggestion from the group.
4. Show that the model asks the clarifying questions first.

**Expected result:** a template similar to the one on the page, and an activity that starts by asking questions.
**If it fails:** show the conversation on the page.
**Key message:** for tasks that repeat, the template is worth more than the result, and it can be turned into a custom assistant.

---

<!-- .slide: id="revisar" class="checklist" -->
## Before accepting an answer

- [ ] Ask for a **second pass**: an audit against criteria and an improved version.
- [ ] If you are torn between two versions, ask for a **comparison table** by criteria.
- [ ] Require it to mark the **assumptions** and not to make up data.
- [ ] Check **figures, quotations and regulations** at the source.

---

<!-- .slide: id="no-sabe" class="statement" -->
## A language model does not know when it does not know

It can present an invented fact with the same confidence as a correct one.

Notas:
Instructions against making things up reduce the problem; they do not remove it. That is why the last box on the previous slide is not optional.

---

<!-- .slide: id="razonadores" -->
## With reasoning models

- Ask for a **direct** answer.
- Ask for **assumptions** if information is missing.
- Ask for a **brief justification** based on criteria.
- There is no need to ask them to think “step by step”: they already do.

---

<!-- .slide: id="ejemplos-salida" class="table" -->
## Giving output examples

| Technique | What you give | When |
| --- | --- | --- |
| Zero-shot | Just the instruction | Simple tasks |
| One-shot | One example of the output | Specific formats (an activity plan, a Moodle question) |
| Few-shot | Two or three examples | Complex or delicate formats (rubrics) |

Notas:
Examples are for style and format, not for teaching content. This connects with the Moodle quiz method: export a real question and give it as an example.

---

<!-- .slide: id="practica-reescribir" class="practice" -->
## Rewrite a vague prompt

1. Start from: “Make an activity about AI for my students.”
2. Add level, time, resources and final product.
3. Ask for clarifying questions and a delivery format.
4. Try it, and then ask for a critique of the prompt itself.

**10 minutes.** Product: your prompt and the answer you got.

Notas:
If there is time, share two or three prompts and compare them using the table on the “Annotated examples” page.
