---
derived_from:
  es/skills/slides.md: "724ecefcb738029015302f40fe39f4bd12e5642d"
---

<!-- .slide: id="no-repitas" class="statement" -->
## If the task repeats, do not repeat the prompt

Save the instructions, the materials and the procedure.

---

<!-- .slide: id="tres-niveles" class="cards fragments" -->
## Three levels

### Custom instructions
They apply to **all** your conversations.

### Custom assistant
Instructions and documents for **that assistant’s conversations**: GPT, Gem, project, space.

### Skill
A **procedure** that is loaded only when the task requires it, in any conversation.

---

<!-- .slide: id="asistentes" class="table" -->
## Custom assistants

| Tool | Name |
| --- | --- |
| ChatGPT | GPTs and projects |
| Gemini | Gems (they become skills from November 2026) |
| Claude | Projects |
| Perplexity | Spaces |

A fixed prompt plus optional context, reused across many conversations.

---

<!-- .slide: id="como-funciona-skill" class="fragments" -->
## How a skill works

- A folder with a `SKILL.md` file: name, **when** to use it and **how** to do the task.
- It can include examples, templates and code.
- At the start, the assistant only reads the name and the description.
- When your request matches, it loads the whole skill and follows the procedure.

Notas:
That is why it can have many skills available without filling the conversation, and there is no need to choose the right assistant: you just ask for the task. It is an open standard (Agent Skills) published by Anthropic.

---

<!-- .slide: id="donde" class="table" -->
## Where they can be used

| Where | Availability |
| --- | --- |
| Claude | All plans, with code execution turned on |
| ChatGPT | Business, Enterprise and Edu plans |
| Gemini | Since October 2026, personal accounts of adults |
| Coding tools that work as agents | From project folders |

---

<!-- .slide: id="ejemplo-skill" class="prompt dense" -->
## A skill for Moodle questions

```markdown
---
name: gift-questions
description: Generates multiple-choice questions in GIFT format, importable into Moodle.
  Use it when asked for quiz questions, a question bank or an exam for Moodle.
---
1. If not stated, ask for the level and the number of questions.
2. 4 options, one correct; wrong answers deduct 25%.
3. Follow exactly the format of example.gift.
4. Escape ~ = # { } : in the text.
5. Check the key before delivering.
```

Notas:
The description is the most important part: it is what the assistant reads to decide whether to use it. The folder is completed with a question exported from your own Moodle. The full version is on the page.

**Demo (8 min): a skill that creates skills**. Claude (free plan, with code execution turned on in Settings → Capabilities) or ChatGPT Edu.

1. Ask: “I want a skill that generates GIFT questions for Moodle with these rules…” and paste the rules from the page.
2. Review the description and the instructions it proposes; correct whatever does not fit.
3. Install it and, in a new chat, ask for “ten quiz questions about…” without mentioning the skill.
4. Check that it has used it and review the questions.

**Expected result:** the assistant recognises the task and applies the procedure without you reminding it.
**If it fails:** show the example skill from the page.
**Key message:** it is metaprompting applied to a procedure; a skill is tested with real cases before you rely on it.

---

<!-- .slide: id="error-comun" class="comparison" -->
## Instructions, not descriptions

### Bad
“Create a quiz question generator that…”

### Better
“When the user gives you a topic, generate 10 questions in GIFT format…”

---

<!-- .slide: id="ideas" -->
## Ideas for teaching

- Question bank in your Moodle’s format.
- Materials adapter for several levels.
- Activity reviewer with your criteria.
- Writer in the department’s style.
- Rubric-based marker, without identifying data.

---

<!-- .slide: id="terceros" class="statement" -->
## Install only skills you have read

Like a browser extension, a third-party skill can contain harmful instructions or code.

---

<!-- .slide: id="antes-de-compartir" class="checklist" -->
## Before using or sharing it

- [ ] Goal and format defined.
- [ ] Explicit quality criteria.
- [ ] Tested with real cases, including a difficult one.
- [ ] Does not ask for or store student data.
- [ ] The documents it carries can be shared.

---

<!-- .slide: id="practica-asistente" class="practice" -->
## Create your assistant

1. Choose a task you repeat every week.
2. Write its instructions with the template from the page.
3. Create a Gem, a GPT or a project with them.
4. Test it with two real cases and correct the instructions.

**15 minutes.** Outcome: an assistant that already works.

Notas:
The template is on the page, under “How to write the instructions”. Share which tasks people have chosen: question banks, adaptations and messages to families usually come up.
