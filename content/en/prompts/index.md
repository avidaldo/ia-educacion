---
title: Prompt design
description: How to specify a task so that the result is useful, verifiable material, not a generic answer.
derived_from:
  es/prompts/index.md: "8213a6230501b5e49f5473d1e4fb01d041eb5454"
---

## What makes a good prompt

An effective prompt works like a **specification**: it says what product you want, for whom, with what constraints and how you will know it is right. The more it resembles a well-written brief for a competent person, the better it works.

In teaching, it pays to aim it at **functional, verifiable materials**, for example:

- activity plans with the sequence and timings;
- question banks in formats that Moodle imports directly (GIFT, XML);
- rubrics with observable indicators;
- adaptations that stay aligned with the learning objectives.

## A reference structure

This template is a starting point. You don’t need to fill in every section for every request: it is a list of what most affects the result.

```text
You are an expert consultant in curriculum design and education regulations.

Task:
- I want to create: [activity / question bank / rubric / study guide]

Context:
- Subject/topic:
- Level (year or VET programme):
- Duration:
- Available resources:
- Group profile (general, no personal data):

Before answering:
- Ask me 3–5 clarifying questions (only the necessary ones).
- If critical information is missing, propose up to 3 explicit assumptions and carry on.

Output:
- Format: Markdown
- Fixed headings: [list of headings]
- Limits: [e.g. max. 1 page / max. 12 items / table]

Constraints:
- Do not use students' personal data.
- Do not invent regulations, school data or figures. If you don't know, say so.

Quality criteria:
- It must include observable success criteria and a quick assessment.
```

## The techniques that make the most difference

### Defining a role

Assigning a role does not make the model “smarter”: it **compresses instructions**. A role shifts the answer towards the vocabulary, tone and criteria associated with that figure in the texts the model was trained on. It is mainly useful for setting the **style** of the answer, and it stops being necessary once the description of the result is detailed enough.

Poor use
: “You are a Python expert.” You leave it to the model to decide what “expert” means, and it may draw on practices you don’t want (for example, outdated libraries).

Good use
: “Act as a security auditor: review this code for critical vulnerabilities (OWASP Top 10) and suggest fixes.” The role sets the perspective; the instructions define the task.

The role sets the *who* (the voice), but it does not replace the *what* (the instructions). If you rely on the role alone for a factual task, you increase the risk of plausible but false answers.

### A clear objective, with its evidence

Poor: “Make an activity about AI.”

Better: “Create a 50-minute activity for second-year VET students on how to **evaluate an AI’s answers**. Evidence: students identify 3 typical errors and suggest 1 improvement.”

### The minimum teaching context

Always include **level**, **time**, **resources** and **final product**. With those four pieces of information, most generic answers disappear.

### Asking it to question you first

This means asking the model to interview you before it generates the answer (“Ask me 3–5 clarifying questions, only the necessary ones”). It forces the model to detect the gaps in your request before filling them on its own, for example by assuming that everyone in the group has a laptop.

- **Use it** for complex design tasks (projects, full rubrics), where the context decides everything.
- **Avoid it** for quick requests: it only adds a step.

### Explicit assumptions

If the model lacks information, it will tend to fill the gaps or to be vague. Asking it to “propose up to 3 explicit assumptions if critical information is missing” makes visible what it is assuming, and lets you correct it (“they don’t have laptops, they have tablets”) before it builds everything on top.

### The delivery format

Specify the format as if it were a submission template:

- a comparison table with fixed columns;
- a checklist;
- Markdown with exact headings;
- titles in sentence case (a capital only on the first word), except for proper nouns.

### Delimiters

If you include long texts (a syllabus, school rules, a student’s text already anonymised), separate them with delimiters so that the model does not confuse your instructions with the text it has to analyse. Triple quotes or named tags such as `<syllabus>…</syllabus>` both work; what matters is to always use the same ones and to name them in the instruction:

```text
School context:
"""
[paste the text here]
"""
```

## Checking before accepting an answer

### Two passes: draft, audit and final version

Ask first for a version and then for an audit against criteria:

```text
Review your proposal against this list:
1) Is the objective observable?
2) Are there privacy risks?
3) Does the assessment measure what it is meant to?
4) Are there unstated assumptions?

Return: (a) findings, (b) improved version.
```

### Comparing two versions

Instead of “improve it”, give two versions and ask for a table by criteria:

```text
Compare prompt A with prompt B on: clarity, format, verifiability and risks.
Return a table and a recommendation.
```

### Not making things up

In teaching, the problem is not only getting it right: it is **not making things up**. Include constraints such as:

- “If you need data (dates, regulations, statistics), say so and suggest how to verify it. Do not make anything up.”
- “Clearly mark anything that is an assumption.”

> [!WARNING]
> **These instructions reduce the problem; they do not remove it**
> A language model does not know when it does not know: it can present an invented fact with the same confidence as a correct one. Figures, quotations and regulations are always checked at the source.

## Metaprompting: asking the AI to write the prompt

When a task repeats (generating quizzes, adapting activities, writing rubrics), it pays to ask first for **the reusable prompt** instead of the result. You describe what that prompt must do, what it must ask and what format it must require, and the model gives you back a template that you can review, save and reuse, or turn into a custom assistant.

It works for two reasons: it makes you think through the requirements before asking for the product, and the model tends to write more complete instructions than we would by hand. The risk is the usual one: the template has to be read and tested before you rely on it.

There is a complete example in [Annotated examples](ejemplos.md#un-prompt-que-escribe-prompts).

## Reasoning models

Current models can spend time “thinking” before they answer. With them, it usually works better to:

- ask for a **direct** answer;
- ask for **assumptions** if information is missing;
- and ask for a **brief justification** based on criteria, not a long chain of reasoning.

There is no need to ask them to think “step by step”: they already do. If the output is well specified, the model organises itself.

## Giving output examples

Examples are mainly useful for **style and format**, not for teaching content.

Zero-shot
: Just the instruction, with no examples.

One-shot
: One example of the desired output.

Few-shot
: Two or three examples, when the format is complex or delicate (for example, rubrics or Moodle questions).

## When chat is not enough

An **agent** makes sense when you want the system to follow a plan, use tools (convert to GIFT, apply a rubric, check a format) and stop when certain criteria are met. If you design a flow like that, specify:

- the objective and the stopping criteria;
- the tools allowed;
- the constraints (privacy, sources);
- the output format.

Techniques for long tasks, or for tasks with several alternatives, are in [Advanced techniques](avanzado.md).

## Official guides

- [OpenAI: prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google: prompting strategies for Gemini](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Anthropic: prompt engineering for Claude](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- For anyone who wants the academic overview: Schulhoff et al. (2024), [*The Prompt Report*](https://arxiv.org/abs/2406.06608), a systematic review of 58 text-based prompting techniques.
