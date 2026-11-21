---
title: Annotated examples
description: Real conversations, translated, that show each technique, with the reasons why they work.
derived_from:
  es/prompts/ejemplos.md: "38f2792c4a6aa0a990983532a641e5860ed99aae"
---

The point is not to copy the content the AI generates, but to **learn how to ask for it**: with context, constraints and verification.

## A prompt that writes prompts

This is a case of [metaprompting](index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt): instead of asking for an activity, you ask for the template you will use to ask for any activity.

:::: chat
::: user
Act as an educational adviser specialising in secondary and VET.

Goal: I need a reusable prompt to ask an AI to generate a classroom activity (45-60 min) on any topic.

Requirements for the prompt:

- It must start by asking 3-5 clarifying questions (level, subject, school requirements, time, resources).
- It must produce a ready-to-use activity plan with: objectives, success criteria, materials, minute-by-minute steps, differentiation (2 adaptations), and a quick assessment (exit ticket).
- It must avoid inventing regulations or “school data”; if information is missing, it must mark it as an assumption.
- It must ask for the output in Markdown with fixed headings.

Give me ONLY the final prompt (in English).
:::
::: assistant collapsed
Copy and paste this prompt (it is a “template prompt”):

```text
You are a lesson design assistant for secondary and VET. Your goal is to help me create a ready-to-use classroom activity.

1) Before proposing the activity, ask me 3–5 clarifying questions (only the necessary ones) about:
- Subject/topic and year or level
- Time available (45–60 min)
- Resources (classroom, projector, mobile phones, internet, etc.)
- Group profile (mixed abilities, special educational needs, language level)
- Learning criteria or evidence I want to observe

2) If critical information is missing, propose explicit assumptions (maximum 3) and carry on.

3) Generate an activity plan in Markdown with these EXACT headings:
- Aim
- Learning objectives (3–5)
- Success criteria (observable)
- Materials
- Procedure (minute by minute)
- Differentiation (2 adaptations: support and extension)
- Quick assessment (3-item exit ticket)
- Risks and how to mitigate them

4) Constraints:
- Do not invent regulations, school data or figures. If something is not in the context, mark it as an assumption.
- Avoid unnecessary jargon; write for a beginner/intermediate teacher.

Topic: [write the topic here]
```
:::
::::

> [!TIP]
> **Why it works**
> - It sets the role (educational adviser) and the **goal** (a ready-to-use activity).
> - It requires **clarifying questions** before the proposal is written.
> - It controls the output with **fixed headings** and constraints (no invented data, assumptions marked).
> - It builds in a good **privacy** practice: no school or student data.

## Giving an example output (one-shot)

:::: chat
::: user
I want an example output for an “activity plan” that I can use as a pattern.

Example (format pattern) for any activity:

- Title: ...
- Objective: ...
- Procedure: 3 numbered steps
- Assessment: 2 criteria

Now create ONE new plan on “how to teach my students to write good prompts”, for the final year of lower secondary or the first year of basic VET. Rules:

- Maximum 180 words.
- Keep the same format pattern.
:::
::: assistant
- Title: Quick workshop: “Asking an AI the right way”
- Objective: Students turn a vague request into a clear prompt with context, constraints and format.
- Procedure:
  1. (10 min) In pairs, they rewrite “Explain X to me”, adding audience, length and format.
  2. (20 min) They compare two prompts on the same topic and choose the more verifiable one.
  3. (15 min) They write their own prompt to generate a study sheet and test it.
- Assessment:
  - The prompt includes context (level, topic, objective) and constraints (length/format).
  - The output can be assessed (it has success criteria or a checklist).
:::
::::

## Giving several examples (few-shot)

:::: chat
::: user
I’m building an assistant for teachers. I need the AI to generate “task instructions” in a consistent style.

Here are TWO examples of the exact style I want (format and tone):

Example 1
Task: Summarise a text.
Deliverable: 8-10 lines.
Criteria: include the central idea + 3 key ideas + 1 open question.

Example 2
Task: Guided debate.
Deliverable: 1 position + 2 arguments + 1 counterargument.
Criteria: arguments based on evidence from the material.

Now generate 3 new task instructions for “learning to use AI responsibly in class”. Rules:

- Keep EXACTLY the same 3-line pattern (Task / Deliverable / Criteria).
- Level: second year of intermediate VET.
:::
::: assistant
Task: Audit an AI answer.
Deliverable: 6-8 lines with 3 risks and 3 mitigations.
Criteria: covers privacy, bias and verification.

Task: Design a safe prompt.
Deliverable: 1 prompt with context + 3 constraints + output format.
Criteria: avoids personal data and asks for evidence.

Task: Responsible use checklist.
Deliverable: 7-item “before/during/after” list.
Criteria: actionable, verifiable items.
:::
::::

> [!TIP]
> **Why it works**
> - The examples set a stable output pattern.
> - It controls the **format** (three fixed lines) and the **level**.
> - It reduces ambiguity: the result can be assessed.

## Asking for a critique of the prompt itself

Explicitly asking for everything questionable to be pointed out avoids chatbots’ tendency to agree with you, and forces an analysis against criteria.

:::: chat
::: user
Do a thorough analysis pointing out everything that may be questionable, incomplete or open to improvement in the following prompt.

I want you to evaluate it critically with a teacher’s mindset: spot ambiguities, possible biases (e.g. stereotyped examples), privacy risks, and lack of verifiability. Then propose a better version.

Prompt: “Create a fun activity about AI for my class and use real examples from my students.”
:::
::: assistant collapsed
**Critical analysis of the prompt**

1. **Ambiguity.** “Fun activity” does not define objectives, duration, level or final product. “About AI” is too broad: responsible use, concepts, tools, ethics, bias, evaluating answers?
2. **Privacy risks.** “Real examples from my students” may involve personal data or identifiable situations. It is a clear and avoidable risk.
3. **Bias and stereotypes.** Without constraints, the model may use “typical” examples with biases (gender, origin, etc.) or sensitive situations.
4. **Lack of verifiability.** There are no success criteria and no assessment, and without a format the answer may be hard to use.

**Improved version**

```text
You are a lesson design assistant for secondary/VET.

Before proposing anything, ask me 4 clarifying questions about: level, exact topic (responsible use / evaluating answers / bias), time and resources.

Requirements:
- Do NOT use personal data or examples based on real students. Use fictional, neutral examples.
- Include: objectives (3), success criteria, materials, minute-by-minute procedure, 2 adaptations (support and extension) and a 3-item exit ticket.
- Format: Markdown with fixed headings.

Initial context: [describe your group here in general terms, without personal data].
```
:::
::::

## Comparing two prompts in a table

When you are torn between two versions, a comparison by criteria gives more concrete feedback than “which one is better?”.

:::: chat
::: user
I’m a teacher and I have two versions of a prompt to generate an activity plan. I want you to compare them and tell me which is better and why, in a table.

Columns: “Criterion”, “Prompt A”, “Prompt B”, “Recommendation”. Minimum criteria: clarity of the objective, missing information, control of the format, verifiability, and risks (bias/privacy).

Prompt A: “Make me an activity about artificial intelligence for my students.”

Prompt B: “Create a 50-min activity for second-year VET on how to evaluate an AI’s answers. Include objectives, materials, minute-by-minute steps, 2 adaptations and an exit ticket. Do not invent regulations or data. Markdown format with headings.”
:::
::: assistant collapsed
| Criterion | Prompt A | Prompt B | Recommendation |
| --- | --- | --- | --- |
| Clarity of the objective | Vague: it does not say what it is meant to achieve (learning, product, duration). | Clear: it sets a specific topic (evaluating AI answers) and a duration. | Keep an observable objective (“students spot 3 typical errors…”). |
| Missing information | It does not ask for context (level, resources, time, profile). | It includes level and time; resources and group profile are missing. | Add 3–5 clarifying questions before generating the activity. |
| Control of the format | No format: unpredictable output. | It asks for Markdown with headings. | Specify fixed headings and limits (e.g. “max. 1 page”). |
| Verifiability | Hard to judge whether it “works”. | It includes an exit ticket and a structure; easier to assess. | Add success criteria and evidence of learning. |
| Risks | It mentions no risks: it may bring in problematic examples or ask for personal data. | It mentions not inventing regulations; it does not deal with privacy. | Add: “do not use personal data; include warnings about bias and verification”. |

Better prompt: **B**, because it reduces ambiguity and controls the output. Even so, I would improve it by asking for clarifications and adding privacy and verification.
:::
::::

> [!TIP]
> **Why it works**
> - It turns an opinion into a **structured** review.
> - It forces a discussion of format, verifiability and risks.
> - The final recommendation comes from criteria, not from style preferences.
