---
derived_from:
  es/vibe-coding/slides.md: "5f3a6f8ed70c31f1f8811b9e5ab2a97148dc93df"
---

<!-- .slide: id="olvidar-codigo" class="statement" -->
## Vibe coding: ask, accept everything and forget that the code exists

Karpathy, February 2025: for “throwaway weekend projects”.

---

<!-- .slide: id="vibe-o-programar" class="comparison" -->
## Not all programming with AI is vibe coding

### Vibe coding
You accept what it proposes without reading it and paste the errors into it until it works.

### Programming with AI
You review the code, test it and could explain how it works.

Notas:
The distinction is Simon Willison’s. It matters because vibe coding is perfect for a prototype and risky for anything that handles data or that other people depend on.

---

<!-- .slide: id="niveles" class="table dense" -->
## Three levels of tools

| Level | Examples | What you get |
| --- | --- | --- |
| Chat with preview | Canvas, Artifacts, Sites | A page or a lightweight application |
| App builders | Google AI Studio, Lovable | A complete application, published |
| Coding agents | Claude Code, Codex, Copilot | Work on the files of a project |

Notas:
Claude Code is included in all of Claude’s paid plans; Codex, in all of ChatGPT’s, the free one too, with limits. GitHub offers Copilot Pro free of charge to teachers verified through GitHub Education.

---

<!-- .slide: id="metodo" class="fragments" -->
## A method: specify, start small, test

- The specification first, and a plan before the code.
- The minimum that works; then, one change at a time.
- Test it as students would.
- Keep versions so you can go back.
- Describe failures: what you did, what you expected, what happened.
- Ask it to explain the delicate parts.

---

<!-- .slide: id="especificacion" class="prompt dense" -->
## A specification before the code

```text
I want a web application for my third-year lower secondary students
to practise naming inorganic compounds. Before writing code, ask me
the questions you need and propose a plan of screens and features.
Requirements: no sign-up; it does not collect or send data; progress is saved
only in the browser; three levels, with a hint and an explained correction;
usable on a phone and with the keyboard; no external services.
```

Notas:
The full version is on the web page.

**Demo (10 min): from the specification to a working application**. Google AI Studio (Build mode) or Lovable, with a test account.

1. Paste the specification from the web page and answer the questions.
2. Review the plan before it writes any code.
3. Test the first version with wrong answers and on a phone.
4. Ask for a specific change and go back to the previous version from the history.

**Expected result:** an application that works with no sign-up and no data outside the browser.
**If it fails:** show the version history and going back, which is what gets used most.
**Key message:** the specification and the versions matter more than the perfect prompt.

---

<!-- .slide: id="limite" class="statement" -->
## What you gain in speed you lose in control if nobody understands the code

---

<!-- .slide: id="riesgos" class="cards" -->
## Four specific risks

### Security
Databases open to anyone, as in applications made with Lovable in 2025.

### Made-up packages
At least 5% of the suggested libraries do not exist.

### Keys and costs
The usage of whoever uses the application is charged to your account.

### Maintenance
If you do not understand the code, every change is a lottery.

Notas:
The made-up packages, according to a USENIX Security 2025 study of 576,000 code samples from 16 models: 5.2% in commercial models and 21.7% in open ones. An attacker can register those names with malicious code.

---

<!-- .slide: id="gemini-menores" class="statement" -->
## An application with Gemini inside cannot be given to under-18s

Its API terms forbid it; an application with no calls to any model is a different matter.

Notas:
The terms also require the paid services to be used to offer the application to users in the European Economic Area.

---

<!-- .slide: id="adelante" class="table" -->
## Where the line is

| Go ahead | Better not, without a code review |
| --- | --- |
| Prototypes and demonstrations | User sign-up |
| Personal tools | Student data |
| Nothing stored outside the browser | Paid APIs |
| Material that can be redone | Tools that others depend on |

Notas:
For anything that handles student data there are already the school’s tools, such as the virtual learning environment.

---

<!-- .slide: id="ciclos" class="section" -->
## In computing VET programmes

---

<!-- .slide: id="estudio" class="big-number" -->
## Programming with AI can slow down learning

**17%** lower on a quiz about the concepts they had just used.

Anthropic, January 2026: a controlled trial with 52 programmers.

Notas:
They were learning a new Python library. The biggest difference was in the debugging questions, and they were not significantly faster. It is a single study, by a company in the sector and on one specific task.

---

<!-- .slide: id="explicaciones" class="statement" -->
## Asking for explanations seemed to help, but that comparison does not prove the cause

Notas:
Those who asked the assistant for explanations and conceptual questions scored better than those who only asked it for code. But each person chose how to use the AI, the groups had 2 to 7 people and the authors warn that it does not establish a causal relationship: perhaps those who ask for explanations are the ones who most want to learn.

---

<!-- .slide: id="aula" -->
## In the classroom

- Use the agent to understand: explanations, alternatives, errors pointed out.
- Predict before running.
- Debug part of the work without help.
- Defend the code: you do not hand in what you cannot explain.

---

<!-- .slide: id="practica-especificacion" class="practice" -->
## Your specification

1. Think of an application for your subject that stores no data.
2. Write its specification following the example.
3. Ask the chatbot for questions and a plan, still without code.
4. Review the plan: what it stores, what it sends outside.

**15 minutes.** Outcome: a specification ready to build.

Notas:
In pairs. At the end, two pairs read out their specification and the group looks for data the application would store without them having asked for it.
