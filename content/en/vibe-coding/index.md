---
title: Vibe coding
description: Building applications through prompts, which tools there are for each level, a method that works, and where the line lies between a prototype and something students can use.
derived_from:
  es/vibe-coding/index.md: "7fa3cd2ac07e6dc2d21eaa37d0b88cd546283290"
---

## What it is

Andrej Karpathy, who was part of OpenAI’s founding team, coined the term in February 2025 to describe a way of programming in which you “fully give in to the vibes” and “forget that the code even exists”: you ask for changes in natural language, accept everything the AI proposes without reading it and, when something fails, paste the error message into it until it works.[^karpathy] He himself presented it as something for “throwaway weekend projects”. The term spread so widely that Collins Dictionary chose it as its word of the year for 2025.[^collins]

It is worth telling it apart from programming with the help of AI. Simon Willison puts it this way: if you review the code the model writes, test it thoroughly and could explain to someone else how it works, that is no longer vibe coding; it is software development, and the fact that a model helped you hardly matters.[^willison] The distinction matters because vibe coding is perfect for a prototype or a personal tool and risky for anything that handles data or that other people depend on.

Compared with [Educational web pages](../webs-educativas/index.md), the difference is one of size: there it is a page in a single file; here, an **application**, with several screens, saved data, users or a server.

## Three levels of tools

| Level | Examples | What you get | Who it is for |
| --- | --- | --- | --- |
| Chat with preview | Canvas in Gemini and ChatGPT, Artifacts in Claude, Sites in ChatGPT | A page or a lightweight application inside the chatbot | Anyone; it is the starting point of [Educational web pages](../webs-educativas/index.md) |
| App builders | [Google AI Studio](https://aistudio.google.com) (Build mode), [Lovable](https://lovable.dev) | A complete application (interface, server, database, sign-in) published at an address of its own | No installation needed; free plans with limits |
| Coding agents | Claude Code, Codex, GitHub Copilot, Gemini CLI | An agent that works on the files of a project: it reads them, modifies them, runs the program and the tests, and fixes what fails | Those who already program or are learning to, as in computing VET programmes |

Some useful facts for the last level: Claude Code is included in all of Claude’s paid plans, Codex in all of ChatGPT’s (the free one too, with limits), and GitHub offers Copilot Pro free of charge to teachers verified through GitHub Education.[^planes]

## A method that works

1. **The specification first.** Before asking for code, describe what the application does, who uses it, on which devices and what data it stores (ideally, none). Ask the chatbot to ask you questions until everything is clear, as in [metaprompting](../prompts/index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt), and to propose a plan before writing anything.
2. **The minimum that works.** A first version with a single feature. Then, one change at a time.
3. **Test it yourself**, as students would: on a phone, with wrong answers, tapping where they should not.
4. **Keep versions.** All these tools have a history or connect to GitHub: when a change breaks everything, you go back instead of asking for fixes on top of fixes.
5. **Describe failures precisely**: what you did, what you expected and what happened, rather than just pasting the error.
6. **Ask for explanations of the delicate parts**: where the data is stored, what is sent outside, what happens if someone types something unexpected.

An example of a specification:

```text
I want a web application for my third-year lower secondary students
to practise naming inorganic compounds. Before writing code, ask me
the questions you need and propose a plan of screens and features.

Requirements:
- No sign-up or log-in. It does not collect or send any data.
- Progress is saved only in the student's browser.
- Three difficulty levels; for each question, a hint and an explained correction.
- It works on a phone and can be used with the keyboard.
- No external services: no analytics, fonts or libraries from other websites.
```

## Where the line is

What you gain in speed you lose in control when nobody understands the code. These are the specific risks:

Data security
: In 2025 a vulnerability was recorded in applications generated with Lovable: insufficient access rules in the database let anyone read or modify their tables without identifying themselves. Lovable disputed it, arguing that the security of each application is the responsibility of whoever creates it.[^lovable] That is precisely the point: if an application stores data and has users, someone has to understand how it is protected.

Made-up packages
: Models sometimes recommend libraries that do not exist. A study presented at USENIX Security 2025 analysed 576,000 code samples from 16 models: at least 5.2% of the packages suggested by commercial models, and 21.7% of those suggested by open models, were made up.[^paquetes] An attacker can register those names with malicious code, and anyone who does not check what they install downloads it.

Keys and costs
: An application that uses a language model needs an access key to its API, which must not be left visible in the code that runs in the browser, and each use has a cost. Current platforms usually keep the key on the server, but the usage of whoever uses the application is charged to your account.

Terms of use
: The terms of the Gemini API, which AI Studio applications use, require users to be 18, forbid using it in applications aimed at under-18s or likely to be used by them, and require the paid services to be used to offer an application to users in the European Economic Area.[^gemini-api] An application with AI inside made in AI Studio cannot, therefore, be given to students under 18. An application that makes no calls to any model, like the one in the example, is a different matter: it is code like any other.

Maintenance
: If you do not understand the code, every change is a lottery. And tools change: what is done on a platform today may not exist next school year.

| Go ahead | Better not, unless someone reviews the code |
| --- | --- |
| Prototypes and demonstrations for class | Applications with user sign-up |
| Personal tools (a rubric generator, a format converter) | Applications that store student data |
| Applications that store nothing outside the browser | Applications that use paid APIs with someone’s money |
| Material that can be thrown away and redone | Tools that other teachers are going to depend on |

For anything that handles student data there are already school tools, such as the virtual learning environment, with their data protection already sorted out.

## In computing VET programmes

For those learning to program, the risk is not only the quality of the code but **no longer learning**. In a controlled trial published by Anthropic in January 2026, 52 programmers learned a new Python library: those who used an AI assistant scored 17% lower on a quiz about the concepts they had just used, and the biggest difference was in the debugging questions. They were not significantly faster. The study also observed that those who asked the assistant for explanations and asked it conceptual questions got better results than those who only asked it for code, but that comparison is weaker: each person chose how to use the AI, the groups had between 2 and 7 people, and the authors themselves warn that it does not establish a causal relationship.[^anthropic-aprendizaje] It is a single study, carried out by a company in the sector and on one specific task: a signal worth bearing in mind, not a conclusion (more in [Learning with AI](../etica-legal/index.md#learning-with-ai-an-open-question)).

Some ideas for the classroom:

- **Using the agent to understand, not only to produce**: asking it to explain, to propose alternatives and to point out errors instead of fixing them.
- **Predicting before running**: what this code will do and why.
- **Debugging part of the work without help**, which is exactly what suffers most.
- **Defending the code** orally or by modifying it live. Willison’s rule works as an assessment criterion: you do not hand in code you cannot explain.[^willison]

[^karpathy]: Karpathy’s original post, from February 2025, is quoted in full in Simon Willison’s article in the next note.
[^collins]: Collins, [*Word of the Year 2025*](https://www.collinsdictionary.com/woty).
[^willison]: Simon Willison, [*Not all AI-assisted programming is vibe coding (but vibe coding rocks)*](https://simonwillison.net/2025/Mar/19/vibe-coding/), 19 March 2025.
[^planes]: According to the pages on [Claude pricing](https://claude.com/pricing), [Codex pricing](https://developers.openai.com/codex/pricing) and [GitHub Copilot for teachers](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers), accessed 22 October 2026.
[^lovable]: [CVE-2025-48757](https://www.cve.org/CVERecord?id=CVE-2025-48757), published on 30 May 2025, with a note that the vendor disputes it.
[^paquetes]: Spracklen et al., [*We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*](https://arxiv.org/abs/2406.10279), USENIX Security 2025.
[^gemini-api]: Google, [*Gemini API Additional Terms of Service*](https://ai.google.dev/gemini-api/terms), sections “Age Requirements” and “Use Restrictions”, accessed 22 October 2026.
[^anthropic-aprendizaje]: Anthropic, [*How AI assistance impacts the formation of coding skills*](https://www.anthropic.com/research/AI-assistance-coding-skills), 29 January 2026.
