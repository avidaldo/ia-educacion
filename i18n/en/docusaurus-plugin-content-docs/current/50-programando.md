# Creating applications without knowing how to program

##VibeCoding

**Vibe coding** is a term coined by [Andrej Karpathy](https://twitter.com/karpathy) in February 2025 to describe a new way of programming where the AI ​​generates the code and the human guides it through prompts in natural language.

> "The hottest new programming language is English" — Andrej Karpathy

### How does it work?

1. **You describe** what you want in natural language
2. AI **generates** the code
3. **You run** and observe the result
4. **Iterates** with corrections until you achieve what you want

### Tools for Vibe Coding

| Tool | Description |
|-------------|-------------|
| **Claude Artifacts** | Create web applications and host them automatically |
| **ChatGPT Canvas** | Workspace with code editing and execution |
| **Gemini** | Generate code with the possibility of exporting |
| **Cursor / GitHub Copilot** | Code editors with integrated AI |

### Advantages
- ✅ You don't need to know how to program to create simple applications
- ✅ Very fast prototyping
- ✅ Ideal for small educational tools

### Limitations
- ⚠️ The code may have errors or vulnerabilities
- ⚠️ Difficult to maintain if you don't understand the code
- ⚠️ Better for prototypes than production

---

## From Vibe Coding to agents (automation with criteria)

Vibe coding is often described as “iterating by feel” until something works. That's useful for prototypes, but as soon as you want **reliability**, it's a good idea to move from “chat” to an **agent-type flow**.

### What is an agent (in practice)

An agent is not “a smarter AI”, but a system that:

- pursues an **objective** (with acceptance criteria),
- maintains **state** (what was tried, what failed, what remains),
- you can use **tools** (tests, linters, search, format converters, etc.),
- runs a controlled loop and **stops** when the goal is met.

If you want to see templates aimed at teaching, here are examples ready to reuse:

- [/docs/examples/agents-and-orquestation](/docs/examples/agents-and-orquestation)
- [/docs/examples/advanced-reasoning](/docs/examples/advanced-reasoning)

### Patterns that work (and how to order them)

**1) Planner/Executor (plan → execute → validate)**

- Ask for a short plan (3–7 steps), then step-by-step execution with validation.
- Define a “Definition of Done”: what tests to pass, what files to change, what format to deliver.

**2) Critique loop (draft → critique → final version)**

- Useful for: rubrics, activities, question banks, explanatory texts.
- Limit rounds (1–2) and define criteria (clarity, privacy, verifiability).

**3) Tool-use / ReAct (Action → Observation → Adjustment)**

- Useful for: research with sources, verification, extraction and re-formatting.
- Ask for “actions and observations” (what you did and what you got). Avoid asking for “step-by-step thinking.”

**4) Multi-agent (roles: design → evaluate → edit)**

- Useful when you want to separate creativity, critical review and final editing.
- Define roles and strict order to reduce self-confirmation bias.

### Most useful prompts when programming with AI

When using Copilot/Cursor/Canvas/Artifacts, these requirements usually greatly improve quality:

- Inputs/outputs as a contract: “just return the code”, “fixed headers”, “table with X columns”.
- Stopping criteria: “for when X passes / when there are no warnings / when it compiles”.
- Restrictions: “do not add dependencies”, “do not invent data”, “do not use personal data”.

For the prompting basis (formatting, delimiters, verification), see: [/docs/prompt](/docs/prompt)

---

## Workspaces in chatbots

### Claude Artifacts

[Claude Artifacts](https://claude.ai/artifacts) allows you to create and publish web applications directly from the chat.

**Quick guide**:
1. Visit [Claude.ai](https://claude.ai/) and log in with your account
2. Describe the application you need
3. Claude creates it automatically and gives you a link to share
4. The code is hosted on Anthropic servers

:::note[Artículo interesante]
[How to create educational mini-applications with Claude](https://educacion.bilateria.org/como-crear-aplicaciones-educativas-con-claude)
:::

**Examples of educational use**:
- Interactive calculators
- Quizzes and educational games
- Concept visualizations
- Simple simulators

### ChatGPT Canvas

[Canvas](https://openai.com/index/introducing-canvas/) is ChatGPT's workspace for more elaborate projects.

**Characteristics**:
- Chat panel + integrated editor
- **Inline editing**: select code and request specific changes
- **Python execution**: execute code directly
- **Version control**: undo changes, restore versions
- **Code tools**: debug, comment, refactor, translate to other languages

**How ​​to activate it**:
- Automatically when detects long code
- Manually typing "use canvas" or "open a canvas"

### Gemini

Gemini can also generate code and applications, although with less direct hosting capability. However, it allows:
- Generate code in multiple languages
- Collaborate in editing
- Export for use on other sites

---

## Integrate applications in Moodle

To insert an application (such as a Claude Artifact) into Moodle:

### Using the app URL

You can use the URL (Claude Artifacts link) to insert it into Moodle directly with a resource of type "URL".

### Using an iframe

1. Get your app link
2. In your Moodle course, activate editing mode
3. Add a resource or activity of type "Page" or "Label"
4. Click the HTML code icon `<>`
5. Paste an iframe code:
   ```html
   <iframe src="https://tu-enlace-de-aplicacion" width="100%" height="600px" frameborder="0"></iframe>
   ```
6. Save changes

### Creating HTML pages

Any chatbot can easily create HTML pages at the touch of a prompt. Then you can:
- Download the page and paste the code into a Moodle "Page" resource
- Use a "Label" resource to be viewed directly on the course page

---

## Related resources

- [Tests for Moodle](./41-cases-use/01-tests-moodle.mdx) - Generation of importable questions
- [Custom Wizards](./31-examples/09-custom-wizard.mdx) - Create GPTs and Gems
