---
title: Presentations
description: Three ways to make presentations with AI and how to choose between them, always keeping content separate from design.
derived_from:
  es/webs-educativas/presentaciones.md: "8ba1f937e70def616ac39f15221015ce5d2889c5"
---

## Content first

The most common mistake when making presentations with AI is to ask for “a presentation on X” in one go and keep whatever comes out: eye-catching slides with generic or wrong content. It works much better in two steps:

1. **The content.** Ask for an outline: the title of each slide, its main idea and what you will say aloud. Review and correct it like any other material.
2. **The design.** With the outline checked, generate the slides with the tool you prefer.

It is the same separation between content and design that is explained in [Advanced techniques](../prompts/avanzado.md#separar-contenido-y-diseño), and the one this website uses: the slide decks of each module are written as text and the style is applied afterwards.

## Three routes

### Generating the presentation in a chatbot

- **Gemini** creates presentations in Canvas (“create a presentation on…”, from a topic or from a document you upload) and exports them to Google Slides or to PDF.
- **Gemini notebooks** generate presentations from the notebook’s sources, with their citations; they are covered in [Gemini notebooks](../notebooks/index.md). With accounts of students under 18, this feature is not available.
- **ChatGPT and Claude** create PowerPoint files by running code, ready to download and touch up.

The best thing about this route is that the content comes from your sources or from the conversation; the worst, that the design is basic and usually needs touching up.

### Specialised tools

Services such as [Gamma](https://gamma.app) or [Canva](https://www.canva.com) generate complete presentations, with design and images, from a text or an outline. Canva has a free version for teachers and students ([Canva for Education](https://www.canva.com/education/)).

They give the most eye-catching result for the least effort, in exchange for depending on their platform, their pricing plans and their privacy terms, and for content that has to be checked more carefully because the design invites you to take it as correct.

### Text first, style afterwards

Write (or ask for) the presentation in **Markdown** and turn it into slides with a fixed style using a tool such as [Marp](https://marp.app), [Slidev](https://sli.dev) or [reveal.js](https://revealjs.com). Ask the chatbot for the Markdown in the format of the chosen tool (“one slide per section, separated by `---`”).

It takes a little more practice, but the content stays in a text file that is easy to correct, version, translate and reuse, and the design is always the same.

## How to choose

| Criterion | Chatbot | Specialised tool | Text and style |
| --- | --- | --- | --- |
| Speed to a first result | High | Very high | Medium |
| Control over the design | Low | High, within its templates | Full, once the style is defined |
| Editing afterwards | In PowerPoint or Google Slides | On its platform | In the text |
| Where your data stays | In the chatbot | On one more platform | In your files |
| Cost | Included in the chatbot | Free plans with limits | Free |

## Reviewing before presenting

- [ ] Every figure, date or quotation has been checked against its source.
- [ ] The images are correct and you are allowed to use them (and generated ones are labelled as such where appropriate).
- [ ] One idea per slide and little text: the rest goes in what you say or in the notes.
- [ ] It reads well from the back of the classroom and on the real projector.

## With your students

An activity that works: students generate a draft presentation with AI, identify which content is correct and which is not, correct it and improve the design, and when they present, explain what changed and why. What is assessed is that critical process, not the visual result.
