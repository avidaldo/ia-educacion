---
title: Chatbots
description: The main assistants, what sets them apart, which one suits each task and which settings you need to know before using them in your work as a teacher.
derived_from:
  es/chatbots/index.md: "4af732392e2468a15bc148ee58b090390736787e"
---

> [!IMPORTANT]
> **This page goes out of date quickly**
> Models, plans and their limits change every few weeks: in October 2026, for example, Google cut Gemini’s free plan down to a single, smaller model. The specific facts on this page have been checked on each company’s official pages on the review date shown above. The criteria for choosing and the settings last much longer than the names of the models.

## What they offer today

The big chatbots are increasingly alike. Almost all of them let you:

- **converse** with a language model that can reason before answering;
- **search the web** and cite the sources;
- **attach files** (PDFs, documents, spreadsheets, images) and work on them;
- **talk by voice** and, on a phone, share the camera or the screen;
- **personalise them**: standing instructions, memory between conversations, projects;
- **research in depth** (Deep Research): a long report with dozens of sources;
- **create** documents, code, small applications and, in some, images and video.

The differences lie in the quality of each feature, in what the free plan includes, in the integration with other tools and in how they treat your data.

## The main ones

Reviewed in October 2026.

| Chatbot | Company | Model in the free plan | What sets it apart |
| --- | --- | --- | --- |
| [ChatGPT](https://chatgpt.com) | OpenAI (US) | GPT-6 Luna (paid plans use GPT-6 Sol) | The most widely used. Since October 2026 it answers with charts and interactive elements inside the chat (“Intelligent UI”). Custom GPTs, image generation |
| [Gemini](https://gemini.google.com) | Google (US) | Gemini Flash-Lite (in AI Pro: Gemini 4 Argon, Pro and Flash) | Integration with Docs, Drive and Gmail. Gems, Canvas, notebooks (Gemini Notebook), images and video |
| [Claude](https://claude.ai) | Anthropic (US) | Sonnet and Haiku (Opus in the paid plans) | Artifacts (pages and applications inside the chat), skills and connectors even in the free plan. Chrome extension in the paid plans |
| [Perplexity](https://www.perplexity.ai) | Perplexity (US) | Combines its own models and other companies’ models | Conversational search engine: cites sources in every answer. Spaces and the Comet browser |
| [DeepSeek](https://chat.deepseek.com) | DeepSeek (China) | DeepSeek-V4.1-Flash | Open-weight models under the MIT licence. Free. Data processed in China |
| [Kimi](https://www.kimi.com) | Moonshot AI (China) | Kimi K3 family (July 2026) | Open-weight models with a very large context |
| [Le Chat](https://chat.mistral.ai) | Mistral AI (France) | Mistral models (the most recent, Large 4, is from October 2026) | European company. Open and commercial models; a mode for working with agents |

If your school uses Google Workspace or Microsoft 365 accounts, check which assistant they include (Gemini or Copilot): with an organisation account, the terms for your data are usually different from those of a personal account.

> [!NOTE]
> **Open weights**
> An *open-weight* model has its parameters published: anyone can download it and run it on their own servers. That does not make it safer for your data if you use it on the website of the company that created it, but it does allow a school or a public authority to install it on its own infrastructure.

## Which one to use for what

There is no chatbot that is best for everything, and the rankings change every month. These criteria hold up better:

| If you need… | Use… | Why |
| --- | --- | --- |
| Current information with sources you can check | Perplexity, or any of them with search turned on | They cite the pages they use; you still have to open the sources |
| A report on a new topic (teaching methods, regulations) | Deep Research in ChatGPT, Gemini, Claude or Perplexity | It plans, searches dozens of sources and writes a referenced report |
| To work only with your own documents | Gemini notebooks (NotebookLM) or a ChatGPT or Claude project | They answer from the sources you upload. Covered in [Gemini notebooks](../notebooks/index.md) |
| To repeat a task with the same instructions | A custom assistant (GPT, Gem, project, skill) | You do not rewrite the instructions each time. Covered in [Skills](../skills/index.md) |
| To create a web page or a small application | Claude (Artifacts), ChatGPT or Gemini (Canvas) | They show the result working inside the chat |
| To generate or edit images | ChatGPT or Gemini | They have their own built-in image generators |
| To work inside Docs, Drive or Gmail | Gemini, with the account that holds those documents | It accesses them without downloading or uploading them |

A useful habit: when the result matters, **make the same request in two chatbots** and compare. The differences show where you need to check.

## Settings worth knowing

### Custom instructions

They all let you write instructions that apply to every conversation: who you are, which levels you teach, the tone and format you prefer. It is the setting that improves answers the most for the least effort. Remember that those instructions are sent with every conversation: do not include data you do not want to share.

### Memory

ChatGPT, Gemini, Claude and Le Chat can **remember information between conversations**: what you ask them to remember and, if you allow it, what they infer from your previous chats. In ChatGPT, for example, memory has two parts that are controlled separately: saved memories and reference to chat history.

Memory personalises, but it also **carries context over**: an answer may be shaped by something you said weeks earlier on another topic. To prepare materials for other groups or to see how the model answers “from scratch”, use a temporary chat or turn memory off. They all let you review and delete what they remember.

### Temporary chats

A temporary conversation does not appear in your history, does not create memories and is not used to train models:

- **ChatGPT** (Temporary Chat): kept for up to 30 days for safety purposes and then deleted.
- **Gemini** (temporary chat): kept for 72 hours.
- **Claude** (incognito chat): not saved in your history and not used for training, even if you have model improvement turned on.

Use them for one-off queries and whenever you work with information you do not want linked to your account. Even so, **not even a temporary chat makes it acceptable to enter students’ personal data**: it is kept on the company’s servers for that period.

### Projects

A project groups conversations with shared instructions and files: for example, one project per subject with the course plan and your notes. In ChatGPT, memory can be limited to a project, so that it does not mix contexts.

### Whether your conversations train models

In **personal accounts**, by default, companies may use your conversations to train their models unless you turn this off:

| Chatbot | Where to turn it off |
| --- | --- |
| ChatGPT | Settings → Data controls → “Improve the model for everyone” |
| Gemini | The “Keep Activity” setting (named differently on some screens). In addition, human reviewers may read a portion of conversations, which are then kept for up to three years |
| Claude | Privacy settings → model improvement: taking part is the default and can be turned off |
| DeepSeek | Its privacy policy states that it uses data for training and stores it in China |

Content in organisation accounts (for example, Claude’s Team plan) is not used for training by default. What all this means for working with student data is covered in [Legal framework](../etica-legal/normativa.md#data-protection).

## The context window

The [context window](../intro-ia/funcionamiento.md#tokens-y-ventana-de-contexto) is how much text the model can take into account at once. The large models in the paid plans now reach a million tokens (Gemini states this for its AI Pro plan): more than a thousand pages of text. Free plans and small models work with considerably less, and the actual limit for an attached document can be lower than the window.

In practice:

- With very long documents, ask it to cite the page or section each statement is based on, and check it.
- In very long conversations, the model may lose instructions from the beginning. Open a new chat with a summary of what matters instead of stretching the conversation out indefinitely.
- To work in depth with many of your own documents, a notebook or a project works better than pasting everything into a chat.

## Web search and deep research

**Web search** runs one or more queries, reads some of the results and answers citing them. It is fast and enough for specific questions.

**Deep research** (Deep Research; Research in Claude) is an agent that works for several minutes: it plans the research, runs dozens of searches, reads the pages, searches again where it finds gaps and writes a long report with references. It is useful for preparing a new topic, reviewing teaching methods or getting an overview of a regulatory framework. It is available in ChatGPT, Gemini (including its free plan), Claude (in the paid plans) and Perplexity.

To get the most out of it, the request has to be as specific as a brief:

```text
Write an up-to-date, evidence-based report on strategies for integrating AI
into vocational education and training, for teachers of commerce and marketing.

Include:
1. Uses of AI in teaching, with practical examples and starter prompts.
2. How to create materials that can be imported into Moodle.
3. Documented cases in similar schools, with their sources.
4. Ethical and data protection risks, and recommendations for teacher training.

Distinguish between what is backed by studies and what is a proposal.
Cite the sources for each claim and point out the ones you could not verify.
```

Read the report with the same critical eye as any other: open the sources of the claims you are going to use, because the summary may not say what the source says.

## Images

ChatGPT and Gemini **generate and edit images** with their own models: from a description, a photo or a sketch. They have improved a great deal at text inside the image, consistency across several images and precise editing. Claude does not include an image generator in its list of features: it creates diagrams and charts by writing code.

Limitations that still appear, and that it is worth teaching students to look for:

- details that demand precision: times on clocks, numbers, maps, hands, long text;
- spatial relations and quantities (“three books to the left of two mugs”);
- stereotypes: if it is not specified, the image tends towards what is most frequent in the training data.

Images from OpenAI and Google carry provenance marks (C2PA metadata or invisible watermarks) that make it possible to check that they were generated with AI, although these are lost with screenshots or certain edits.

## Creating documents: the format problem

Asking a chatbot for a document and taking it into Word or Google Docs is a constant source of frustration: tables that fall apart, headings that lose their formatting, formulas that appear as code. What works:

- **Ask for Markdown and paste it where it is understood.** Chatbots naturally write in Markdown. Google Docs can paste it with formatting if you turn on Markdown in its preferences, and many applications import it.
- **Ask for the file directly.** ChatGPT and Claude can create Word documents, spreadsheets, presentations and PDFs by running code, and offer them for download. Check the result: fine formatting usually needs touching up.
- **Use the canvas** (Canvas in ChatGPT and Gemini, Artifacts in Claude) to work on the text before exporting it. Gemini can send the result straight to Google Docs.
- **Separate content and format**: first ask for and review the content; then, in another step, the format or the layout. It is the same idea explained in [Advanced techniques](../prompts/avanzado.md#separar-contenido-y-diseño).
- **Formulas**: ask explicitly for the notation your destination accepts (Word’s equation editor, LaTeX for Moodle).

## Always worth remembering

- What a chatbot generates is **plausible, not necessarily true**: figures, quotations, references and regulations are checked at the source. Why this happens is explained in [How a language model works](../intro-ia/funcionamiento.md#alucinaciones-plausible-no-es-verdadero).
- The same question can give different answers; if it matters, regenerate or compare.
- Chatbots tend to **agree with you**. Ask for explicit criticism, as in [Annotated examples](../prompts/ejemplos.md#pedir-una-crítica-del-propio-prompt).
- **No personal data of students** in personal accounts, with or without a temporary chat.
