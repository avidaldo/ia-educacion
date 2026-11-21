---
title: Gemini notebooks (NotebookLM)
description: An assistant that works from your documents, with citations, and turns the sources into audio and video overviews, quizzes, flashcards or slide decks.
derived_from:
  es/notebooks/index.md: "9c7ee23c1f766944450f01cf9f1012ade3fc73d9"
---

## What it is

[Gemini Notebook](https://notebook.google.com) is Google’s tool for **working with your own sources**: you upload notes, articles, videos or the course plan for your subject, and the assistant answers, summarises and generates materials from them, citing where each statement comes from.

Until July 2026 it was called **NotebookLM**; the old address redirects to the new one. It is still a standalone application, but notebooks can also be created and used from the Gemini app, kept in sync between the two.

## What makes it different: your sources

A general chatbot answers with what it learned in training and with what it finds on the web. A notebook answers **from the sources you give it**, and each answer includes citations that lead to the exact passage in the document.

That has two clear advantages for teaching: the answers fit your syllabus rather than “what is usually said”, and every statement can be checked with one click.

> [!WARNING]
> **Grounded is not infallible**
> The model can summarise a source badly, mix up two, or fill in with general knowledge what the sources do not say. The citations are there precisely to check this: open them before using a statement. And if you use the **discover sources** option, the notebook adds web pages that need checking like any other search.

## Which sources it accepts

PDFs, web pages, YouTube videos, audio files, Google Docs and Slides, pasted text and, from a phone, photos of handwritten notes or worksheets. In the mobile app you can record audio (a lesson, an idea) and add it as a source.

With standard access, each person can have up to **100 notebooks** with up to **50 sources** each. Paid plans raise those limits and the number of outputs that can be generated per day.

## What it can generate

| Format | What it is for in class |
| --- | --- |
| Audio overview | A conversation between two voices that goes over the sources, like a podcast. Its length and focus can be adjusted |
| Video overview | A narrated explanation with slides and illustrations; short one-minute versions and more elaborate ones |
| Reports | Study guides, briefing documents and other written reports |
| Flashcards and quizzes | Revision and self-assessment; questions can be edited and added |
| Mind map | The concepts in the sources and how they relate, to explore |
| Infographics and slide decks | Visual material from the sources |
| Voice conversation | On a phone, talking to the notebook about its sources and interrupting when needed |

Since September 2026 you can also create **interactive learning summaries** that combine a summary, an infographic, a quiz and flashcards in a single report.

## Uses in teaching

To prepare lessons:

- One notebook per subject with the course plan, the notes and the readings: questions such as “which assessment criteria does this activity cover?” are answered with citations.
- Compare several sources on the same topic and ask where they agree and where they do not.
- Generate a study guide or a glossary for a unit and review them before sharing them.
- Prepare an audio overview of a reading for students who need another format.

With your students:

- Have them build their own notebook with their notes and use it to revise with flashcards and quizzes.
- Compare the notebook’s summary with their own and discuss what has been lost.
- Analyse the citations: does the source say what the notebook claims it says?

> [!TIP]
> **Questions for Moodle**
> The notebook’s quizzes are not exported in a format Moodle can import. For a question bank built from your sources, ask the notebook’s chat for questions in GIFT format following an example exported from your Moodle, as explained in [Moodle quizzes](../tests-moodle/index.md#el-método-más-fiable-partir-de-una-exportación-de-moodle).

## With underage students

With **Google Workspace for Education** accounts, Gemini Notebook is available to users of all ages, but users under 18 do not get some features: Deep Research, infographics, slide decks, cinematic-style videos and the interactive mode of audio overviews (according to Google’s documentation updated in September 2026). Whether a school has it turned on depends on how its Google Admin console is managed.

Before suggesting it to your students, check which accounts they use and what terms apply to them: the data protection implications are covered in [Legal framework](../etica-legal/normativa.md#data-protection).

## Your data

According to Google, the content of a notebook is not used to train the models unless you send feedback (in that case, the whole interaction may be reviewed). With Workspace or Workspace for Education accounts, moreover, **there is no human review** of the files, chats or outputs. Even so, the general rule still holds: do not upload documents with students’ personal data to a personal account.

## Notebook or project

| Aspect | Gemini notebook | ChatGPT or Claude project |
| --- | --- | --- |
| Answers from | Your sources, with citations to the passage | Your files and its general knowledge |
| Study formats | Audio, video, flashcards, quizzes, maps, slide decks | Whatever you ask for in the chat |
| Best for | Studying or teaching a specific syllabus | Producing documents, code or materials from a context |

The two complement each other: the notebook to understand and revise a set of sources; the project to work with them.
