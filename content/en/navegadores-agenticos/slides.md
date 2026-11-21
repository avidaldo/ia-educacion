---
derived_from:
  es/navegadores-agenticos/slides.md: "f62993dbbf8ce5006260b16dbc9952e73fcedc87"
---

<!-- .slide: id="actuar" class="statement" -->
## An agent does not just read the page: it acts on it with your sessions open

It clicks, types and fills in forms on your behalf.

---

<!-- .slide: id="leer-o-actuar" class="comparison" -->
## Two very different levels of help

### Reading assistant
Summarises, compares and extracts data from your tabs. It does not touch anything.

### Browsing agent
Clicks, types and moves from one website to another, signed in as you on each one.

---

<!-- .slide: id="herramientas" class="table dense" -->
## What is available today

| Tool | Availability |
| --- | --- |
| Comet (Perplexity) | Free; Windows, Mac, iOS and Android |
| Claude in Chrome | Paid plans; desktop Chrome only |
| ChatGPT | Extension for several browsers, and desktop app |
| Gemini in Chrome | Not available in the EU |

Notas:
Situation in October 2026. Atlas, OpenAI’s browser, was withdrawn in August 2026, less than a year after its launch: better not to build a way of working around one particular tool.

---

<!-- .slide: id="usos" class="two-col" -->
## Worth it with public websites and tasks you can check

### Yes
Comparing pages, extracting deadlines into a table, guiding you through a complicated website, checking your own website.

### No
Websites with other people’s data: the student information system, marks, email with students and families.

Notas:
Anthropic itself advises against it: what is on screen is sent to the provider, and a mistake or an attack would be carried out with your permissions.

---

<!-- .slide: id="inyeccion" class="statement" -->
## The agent cannot tell your instructions from those someone hid in the page

This is prompt injection.

Notas:
**Demo (5 min): an instruction hidden in a page**. Comet or Claude in Chrome, in a browser profile with no open sessions, with the demonstration page saved as `demo.html`.

1. Open `demo.html`: it looks like an ordinary page about the water cycle.
2. Ask the assistant to “summarise this page”.
3. Read the summary aloud.
4. Select all the text (Ctrl+A) to reveal the hidden instruction.

**Expected result:** the summary ends with “Frogs have opinions too”, or the assistant warns about the instruction.
**If it fails:** both results work; if no agent is available, show the page’s code and explain what it would do.
**Key message:** the text the agent reads can also give it orders.

---

<!-- .slide: id="ncsc" class="quote" -->
## It is not a flaw that an update will fix

> It’s very possible that prompt injection attacks may never be totally mitigated in the way that SQL injection attacks can be.

UK National Cyber Security Centre, December 2025

Notas:
The reason is how the model works: it receives a single text and predicts how to continue it, without separating data from instructions. OpenAI says the same: like scams on the web, it is “unlikely to ever be fully ‘solved’”.

---

<!-- .slide: id="caso-comet" class="fragments" -->
## All it took was asking for a summary

- A Reddit comment hid instructions.
- The assistant went to the user’s Perplexity account and copied their email address.
- It requested a login code and read it in Gmail.
- It posted both in a reply to the comment.

Notas:
Brave’s research on Comet, August 2025. Providers now train their models against these attacks and ask for confirmation before sensitive actions; Anthropic reports that fewer than 0.08% of attacks succeed in its internal tests, and even so warns that the risk is not zero.

---

<!-- .slide: id="triada" class="cards" -->
## The lethal trifecta: the danger lies in combining all three

### Private data
Your sessions, your email, your documents.

### Untrusted content
Pages, emails and comments you do not control.

### External communication
Sending, posting, opening an address.

Notas:
Simon Willison, June 2025. A browsing agent with your sessions open has all three; each protective measure removes one or limits it.

---

<!-- .slide: id="con-cabeza" class="checklist" -->
## Using them wisely

- [ ] A browser profile with no sensitive sessions.
- [ ] Specific, well-defined tasks.
- [ ] Trusted websites first.
- [ ] Read every confirmation before accepting.
- [ ] Block sensitive sites in the settings.
- [ ] Stop the task if it does anything unexpected.

Notas:
If you handle sensitive data and do not need the agent, ChatGPT has a Lockdown Mode that limits outbound connections; in exchange, it turns off live web browsing, deep research and agent mode.

---

<!-- .slide: id="responsable" class="statement" -->
## What the agent does on your behalf, you have done

Mistakes and purchases included: Anthropic and Google say so explicitly.

---

<!-- .slide: id="que-ve" class="table" -->
## Besides what it does, what it sends matters too

| Tool | What reaches the provider |
| --- | --- |
| Claude in Chrome | Screenshots of the tabs it works in |
| Comet | The context of each request, for up to 30 days |
| Gemini in Chrome | The current tab, in your Gemini activity |

Notas:
The rules on personal data are those of any chatbot, with one addition: here, everything visible on screen counts too.

---

<!-- .slide: id="alumnado" class="statement" -->
## With students, better as a subject of study than as a tool

In computing courses, prompt injection is cybersecurity content.

Notas:
Claude requires users to be 18 and Gemini in Chrome is not available in the EU. Comet inherits Perplexity’s minimum age of 13 and ChatGPT asks for parental consent for users under 18, but an agent with the student’s sessions open raises the same problems as one with yours.
