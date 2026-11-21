---
title: Assistants and skills
description: How to save instructions and materials for the tasks you repeat, from a custom assistant to a skill.
derived_from:
  es/skills/index.md: "f28eecf86c888bb077a33a0a55fb4e7a88c89961"
---

## Why save the instructions

If you write quiz questions every week, adapt activities to several levels or review course plans against the same criteria, rewriting the prompt each time is slow and gives uneven results. Every chatbot lets you **save the instructions** (and sometimes materials and procedures) to reuse them. There are three levels:

Custom instructions
: They apply to **all** your conversations: who you are, what you teach, the tone you prefer. They are in each chatbot’s settings; they are covered in [Chatbots](../chatbots/index.md#instrucciones-personalizadas).

Custom assistant
: Fixed instructions, and optionally documents, that apply to **that assistant’s conversations**: a GPT in ChatGPT, a Gem in Gemini, a project in ChatGPT or Claude, a space in Perplexity.

Skill
: A packaged **procedure** (instructions, examples, templates and, if needed, code) that the assistant **loads only when the task requires it**, within any conversation.

## Custom assistants

| Tool | Name | What it includes |
| --- | --- | --- |
| ChatGPT | GPTs | Instructions, knowledge files and capabilities (search, images, code). They can be shared with a link |
| ChatGPT and Claude | Projects | Instructions and files shared by a group of conversations |
| Gemini | Gems | Instructions and files. Also available on the free plan. Google turns them into skills from November 2026 (in school accounts, in 2027) |
| Perplexity | Spaces | Instructions, files and web search. They are covered in [Educational bots](../bots-educativos/index.md) |

The names, and what each plan includes, change often. What does not change is the idea: **a fixed prompt plus optional context**, reused across many conversations.

## Skills

A skill is a folder with a `SKILL.md` file: a name, a description of **when** to use it and the instructions on **how** to do the task, plus the files it needs (examples, templates, scripts). The difference from an assistant is how it is used:

- When a conversation starts, the assistant only has the name and the description of each installed skill.
- When your request matches a description, it loads that whole skill and follows its procedure.
- That way it can have many skills available without filling the conversation with instructions, and you do not have to choose the right assistant: you just ask for the task.

Anthropic published the format as an open standard ([Agent Skills](https://agentskills.io)), and other tools have adopted it. As of October 2026:

| Where | Availability |
| --- | --- |
| Claude (web and apps) | All plans, including the free one. Code execution must be turned on in Settings → Capabilities |
| ChatGPT | Business, Enterprise and Edu plans |
| Gemini | Rolling out since October 2026: for now, personal accounts of users aged 18 or over; school accounts will follow. They are invoked with `/`, or Gemini applies them when they fit |
| Coding tools that work as agents (Claude Code, Codex, Gemini CLI…) | They load skills from project folders |

Skills can include code that the assistant runs. That is why you should **install only skills you have read** or that come from a trusted source: like a browser extension, a third-party skill can contain harmful instructions or code.

### An example skill

A skill to generate Moodle questions. The description is the most important part: it is what the assistant reads to decide whether to use it.

```markdown
---
name: gift-questions
description: Generates multiple-choice questions in GIFT format, importable into Moodle, from a topic or from some material, with penalties and feedback. Use it when asked for quiz questions, a question bank or an exam for Moodle.
---

# GIFT questions for Moodle

1. If not stated, ask for the students' level and the number of questions.
2. Generate each question with 4 options and only one correct; wrong answers deduct 25%.
3. Follow exactly the format of `example.gift` (in this same folder).
4. Escape with \ the characters ~ = # { } : that appear in the text.
5. Check before delivering: correct key, no clues from option length, no negatives.
6. Deliver only the content of the .gift file.
```

The folder is completed with `example.gift`, a question exported from your own Moodle, as explained in [Moodle quizzes](../tests-moodle/index.md#el-método-más-fiable-partir-de-una-exportación-de-moodle).

You do not have to write it by hand: Claude, ChatGPT and Gemini let you create a skill by describing it in the chat. Describe the task (“I want a skill that generates GIFT questions with these rules…”), review what it proposes and test it with real cases before using it. It is [metaprompting](../prompts/index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt) applied to a procedure.

## How to write the instructions

This works for an assistant and for a skill:

```text
Role and goal:
You are a lesson design assistant for secondary and VET teaching.
Your goal is [specific task].

Fixed context:
- Level: [if applicable]
- Constraints: do not use personal data; do not invent regulations.

Output format:
- [Fixed headings / table / GIFT]

Procedure:
1. Ask clarifying questions (only the necessary ones).
2. Generate the proposal.
3. Include observable success criteria.
```

> [!WARNING]
> **The most common mistake**
> Do not describe the assistant (“Create a quiz question generator that…”): write the instructions it must follow in each conversation (“When the user gives you a topic, generate 10 questions in GIFT format…”).

## Ideas for teaching

- **Question bank**: GIFT or XML format, quality criteria and an example exported from your Moodle.
- **Materials adapter**: converts a text to several levels (support and extension) without losing the objectives.
- **Activity reviewer**: checks that a proposal has observable objectives, assessment and support for diverse learners.
- **Writer in the department’s style**: templates for reports, messages or course plans in the school’s format.
- **Rubric-based marker**: applies your rubric and suggests feedback, which you review. Never with identifying student data in a personal account.

It is not worth it for one-off or exploratory tasks (use a normal chat), or when the instructions change every time.

## Before using or sharing it

- [ ] **Clear goal**: what exactly does it produce?
- [ ] **Defined format**: table, list, GIFT, fixed headings?
- [ ] **Quality criteria**: how will you know the result is good?
- [ ] **Tested**: have you used it with three or four real cases, including a difficult one?
- [ ] **Privacy**: does it avoid asking for or storing students’ personal data?
- [ ] **Documents checked**: can the files it carries be shared with whoever is going to use it?
