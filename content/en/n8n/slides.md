---
derived_from:
  es/n8n/slides.md: "33fb9b6b5d8ffb970486b3ad37f5eea957522585"
---

<!-- .slide: id="receta" class="statement" -->
## An automation is a recipe the computer follows without you

A trigger and some fixed steps, every time the conditions are met.

---

<!-- .slide: id="tres-formas" class="cards" -->
## Chatbot, automation and agent

### Chatbot
Answers when you ask.

### Automation
Always the same steps, without you: predictable.

### Agent
Decides the steps itself: flexible and less predictable.

Notas:
An automation can include a language model in a step, and even an agent, but you decide the skeleton.

---

<!-- .slide: id="herramientas" class="cards" -->
## Several tools, the same pieces

### Zapier
Data in the United States; its free plan does not allow AI steps.

### Make
Free plan, with the data in the EU if you choose it at sign-up.

### n8n Cloud
Free trial; the workflows in its gallery can be viewed without an account.

### Power Automate
Included in Microsoft 365 education licences.

Notas:
Prices and limits are in the table on the page, with their review date. The examples use n8n, which can also be installed on your own server. For simple tasks you do not even need a workflow: some assistants, such as Claude in Chrome, schedule recurring tasks.

---

<!-- .slide: id="piezas" -->
## The pieces of a workflow

- **Trigger**: a time, a form, an RSS feed, an email.
- **Nodes**: each step receives data, does its work and passes it on to the next.
- **Expressions**: you drag a piece of data from an earlier step and it becomes `{{ $json.title }}`.
- **Credentials**: accounts and keys, stored separately.
- Workflows are JSON: you copy them and paste them onto the canvas.

---

<!-- .slide: id="ejemplo-boe" class="fragments" -->
## What’s new in Spain’s official gazette, summarised every Monday

1. Every Monday at 8:00.
2. Read the BOE’s RSS feed on education and teaching.
3. Keep this week’s items.
4. Summarise each provision with a language model.
5. Send you a single email with the links.

Notas:
A good first workflow: it handles no personal data, each summary comes with its link so you can check it, and if it fails, nothing serious happens. The same pattern works with any similar feed.

**Demo (12 min): a first workflow, node by node**. An n8n Cloud trial account, created a few days before the session.

1. Create the Schedule Trigger and the RSS Read node with the feed address.
2. Run the RSS node and show the items it outputs.
3. Add the language model node with the instructions from the page and the title expression.
4. Send the email to a test account.

**Expected result:** an email with the summaries and their links.
**If it fails:** show the output of each node, which is what explains how the data travels. Without an account, walk through the example workflow from the gallery that the page links to.
**Key message:** each node receives items and passes them on to the next; you decide the skeleton.

---

<!-- .slide: id="agente-en-flujo" class="statement" -->
## An agent inside a workflow brings the risks of agents with it

Reading anyone’s emails and being able to send them is the complete lethal trifecta.

---

<!-- .slide: id="aprobacion" class="statement" -->
## Human approval before sending, publishing or deleting

n8n stops the workflow until someone approves or rejects the action.

---

<!-- .slide: id="que-automatizar" class="table" -->
## What to automate in a school

| What | How |
| --- | --- |
| Digests, reminders, alerts | Go ahead |
| Student or family data | Only in tools your school or education authority authorises |
| Decisions about students | No, not without human review |

---

<!-- .slide: id="ejecuciones" class="statement" -->
## n8n Cloud stores the data of each execution

What passed through each node is kept for as long as your plan sets.

Notas:
Whatever is sent to the language model reaches its provider. An automation service with your account is, like a chatbot with a personal account, an external platform: student data only go to tools that your school or education authority has contracted or authorised. There is no Moodle node either: connecting to its API requires a permission that only the Moodle site’s administrators can grant.
