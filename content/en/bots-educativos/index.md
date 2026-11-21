---
title: Educational bots
description: Assistants set up by the teacher for students to use as a tutor, and what has to be decided before putting them in their hands.
derived_from:
  es/bots-educativos/index.md: "a9d495ae5a90f82a40f955ca1ec364d910b920cb"
---

## What an educational bot is

An educational bot is a [custom assistant](../skills/index.md) that the teacher sets up **for students to use**: a tutor that guides without giving the solution, a revision partner with questions on the syllabus, an assistant that helps with understanding a reading. Students see a normal chat, but the bot always follows the instructions you set.

The most interesting idea is not that it gives answers, but that it **guides reasoning**: asking questions, breaking the problem into steps, pointing out contradictions so that the student spots their own mistake.

## First of all: which account students sign in with

Before designing the bot, there is a question that shapes everything else: **which account each student is going to use**. It determines the minimum age, the terms that apply to their data and whether the school can be accountable for that use.

| Service | Minimum age with a personal account |
| --- | --- |
| ChatGPT | 13, or the minimum age for consent in the country; under 18, with the consent of a parent or guardian |
| Gemini | 13, or the age set in the country; with a school account, its administrator enables it |
| Perplexity | 13; minors, only if a parent or guardian accepts the terms |
| Claude | 18 |

Under the GDPR, when an online service needs consent to process a child’s data, the child’s own consent is enough from the age of 16; below that age, the holder of parental responsibility must give or authorise it. Each country may lower that age by law, but not below 13 (Article 8 GDPR). Asking students to sign up for a service with their personal account hands each family a decision that belongs to the school.

The option with the most safeguards is the one **provided by the school or the education authority**: educational accounts contracted with specific terms. With **Google Workspace for Education**, for example, the Gemini app is available to students of all ages if the administrator turns it on, with enterprise-grade data protection; students under 18 can use Gems, Guided Learning, Canvas and quizzes, but not Deep Research or Gemini Live. The legal implications are covered in [Legal framework](../etica-legal/normativa.md#students-age).

> [!CAUTION]
> **What no longer works: the Perplexity space without an account**
> For a while, a Perplexity space could be shared with an open link, and it was recommended so that students could use it without signing up. Spaces are now called **projects** and, on personal accounts, only invited people can access them: “Projects cannot be made publicly queryable”, according to its help centre (October 2026). Besides, not requiring an account never made its use compliant with the law on its own: what students type is still sent to a third party, together with technical data such as the IP address, and the minimum age in the terms of use still applies.

## How to share a bot in each tool

| Tool | How it is shared | Keep in mind |
| --- | --- | --- |
| Gemini (Gems) | Like a Drive file: with specific people or with anyone who has the link, as the administrator allows | Requires a Google account. From November 2026 Gems become skills (in school accounts, in 2027) |
| ChatGPT (GPTs) | With a link or published in the GPT Store | Requires a ChatGPT account; see the minimum age |
| Perplexity (projects) | By inviting each person; up to 5 collaborators, or 9,999 if the owner is a verified teacher or student | Requires a Perplexity account; see the minimum age |

## Built-in tutor modes

Before building a tutor, check whether the one each tool already has is enough:

- **ChatGPT, study mode**: guides with questions instead of giving the answer, explains by levels and checks understanding. Available on all plans.
- **Gemini, Guided Learning**: also available to students under 18 with Workspace for Education accounts.
- **Perplexity, learning mode**: explains step by step and generates flashcards and quizzes from the materials.

A bot of your own pays off when you need something these modes do not do: sticking to your syllabus and your materials, following your methodology or a specific level, or limiting itself to one type of task.

## A Socratic tutor

These instructions are a good starting point. Adapt them to the subject, the level and the materials you attach:

```text
Role:
You are a Socratic [subject] tutor for [level] students. Your goal is to help them reach the answer by themselves, never to give the solution directly.

Rules:
1. Do not solve the problem or give the final answer, even if asked.
2. If asked for the answer, kindly explain that your job is to help them think.
3. Break the problem into small steps and ask only ONE question at a time.
4. If there is a mistake, do not say “that's wrong”: ask why that approach was chosen or point out the contradiction.
5. Use clear language suited to the level, with a patient tone.
6. Base your explanations on the attached materials; if something is not in them, say so.
7. Do not ask for or store personal data.
8. If the question is not about the subject or is sensitive, recommend talking to a teacher.

Start:
Introduce yourself in one sentence as an AI assistant and ask which exercise or concept they are stuck on.
```

## Test it before sharing it

A bot behaves differently depending on how it is spoken to. Before giving it to your students, test it as a student would:

- [ ] Ask for the solution directly, several times and insistently.
- [ ] Ask it to ignore its instructions or to “make an exception”.
- [ ] Ask a question outside the syllabus and another one that is personal or sensitive.
- [ ] Make a mistake on purpose and check how it deals with it.
- [ ] Check that what it explains matches your materials.

> [!WARNING]
> **Instructions are not a safety barrier**
> With enough insistence, a student can get the bot to step outside its instructions and give the answer. The bot helps those who want to learn; it does not replace supervision, nor can it control those who want to get round it.

## In class

- Explain to your students that it is an AI tool, that it can make mistakes and that its answers have to be checked.
- Define what it can and cannot be used for, especially in assessed tasks.
- Check from time to time how they are using it and adjust the instructions.
- Assessment is still yours: the bot supports study, it does not mark.
