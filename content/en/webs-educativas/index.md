---
title: Educational web pages
description: Create small interactive pages for class with AI (simulators, revision exercises, games) and publish them where students can use them.
derived_from:
  es/webs-educativas/index.md: "ffaa09e32dced5a94e8f12000040daf964147b26"
---

## What you can create

From a description in natural language, chatbots generate **interactive web pages** that work in the browser: you do not need to know how to program to get a first useful result. Some examples that work well in class:

- a simple simulator (a circuit, an inclined plane, an economy with two variables);
- an interactive revision exercise with questions, hints and instant correction;
- a timeline or a concept map explored by clicking;
- a calculator specific to the subject (scales, percentages, units);
- a vocabulary game or a concept-matching game.

A page like this is a single HTML file with its design and its code. When the project grows (several screens, saved data, users), it is no longer a page but an application: that is covered in [Vibe coding](../vibe-coding/index.md).

## Where to create them

| Tool | How it is created | Sharing the result |
| --- | --- | --- |
| Claude | Artifacts show the page working next to the chat | With a link, but **whoever opens it needs a Claude account** (and Claude requires users to be 18). For students, download the code and publish it somewhere else |
| Gemini | Canvas, also on the free plan | With a public link that opens on gemini.google.com. According to Google, anyone with the link can view and edit the data associated with the app |
| ChatGPT | Canvas for code and, since GPT-6, answers with interactive elements. On the Plus and Pro plans, Sites (in beta) creates and publishes pages and lightweight applications | With Sites, at an address of its own; otherwise, download the code to publish it outside ChatGPT |

In every case, the most robust route is the same: **ask for the page as a single HTML file, download it and publish it yourself** where students already go.

## How to ask for it

```text
Create an interactive web page in a single HTML file, with no external dependencies
(no CDNs, fonts or images from other websites), for [level] on [topic].

It must let students: [what students will do, step by step].
Design: clear and readable on a phone and on the projector, with good contrast,
usable with the keyboard and with alternative text for the images.
Language: [the language of the class].
Do not collect or send any user data.
At the end, explain in three lines how to use it.
```

Then iterate as with any other text: try the page, describe what fails or what you want to change (“the check button does not reset the answers”, “add a hint to each question”) and ask for the complete corrected version.

> [!TIP]
> **Content first, design afterwards**
> If the page explains something, review the content first (as text, or in a Mermaid diagram) and then ask for the page with that content already checked. Mixing reasoning and design in a single request increases errors, as explained in [Advanced techniques](../prompts/avanzado.md#separar-contenido-y-diseño).

## Publishing it on Moodle

| Option | How | When to use it |
| --- | --- | --- |
| **Page** resource | Paste the HTML into the editor’s source code view | The simplest option for a self-contained page |
| **Text and media area** (formerly “Label”) | Insert an `<iframe>` that points to the page published somewhere else | To show it directly on the course page |
| **File** resource | Upload the `.html` file | If you prefer it to open in a separate tab |
| **URL** resource | Link to the page published outside Moodle | If it is already hosted on another website |

An `<iframe>` looks like this:

```html
<iframe src="https://your-page-address" width="100%" height="600" title="Circuit simulator"></iframe>
```

> [!NOTE]
> **Why Moodle sometimes deletes the code**
> Moodle “cleans” the HTML written in most places (in forums, for example) and removes `<iframe>` elements and code. The content of a **Page** resource and the descriptions of resources and activities, such as the text and media area, are shown without cleaning, so it works there. The exception is when the site administrators have turned on content cleaning for the whole site: in that case, the options left are the **File** resource or a link.

## Publishing it outside Moodle

- **[Netlify Drop](https://app.netlify.com/drop)**: you drag in the folder with the page and get a public address in seconds.
- **[GitHub Pages](https://pages.github.com)**: free and stable for those who already use GitHub; it is how this website is published.
- **Google Sites** lets you embed HTML code in a page of the site.

Once published, the address can be linked from Moodle or embedded with an `<iframe>`.

## Before publishing it

- [ ] **The content is correct**: check data, formulas and text as you would check any material.
- [ ] **It works** on a phone, on the classroom computer and on the projector.
- [ ] **It is accessible**: enough contrast, usable with the keyboard, alternative text.
- [ ] **It collects no data** and loads no resources from other websites (fonts, analytics, CDNs), which would send students’ information to third parties.
- [ ] **The images** are your own or have a licence that allows you to use them.
