---
name: update-slides
description: Create or update the reveal.js slide decks of the ia-educacion course site (content/es/<module>/slides.md) from the module's pages, redoing only the slides affected by what changed in those pages. Use when a page under content/es changed and its deck is stale, when a module has no deck yet, when engine/check.py or engine/provenance.py status reports a deck as stale, unstamped or missing, or when the user asks to prepare, refresh, shorten or restyle a presentation, deck or "diapositivas" of the course.
allowed-tools: Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py *), Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/build.py *), Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/shoot.py *), Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/check.py *)
---

# Update slides — the page is the source, the deck is derived

## Stance

The web pages are the single source of truth. A deck is a condensed, spoken companion to its module's pages: it never says anything the pages don't, and the teacher does live demos with it, so its speaker notes are the demo script. Content and style are separate: a deck is Markdown plus layout names from a closed vocabulary; the look lives in `engine/theme/` and is never touched from a deck.

The chain is **Spanish page → Spanish deck (this skill) → Galician page and deck (sync-translation)**. Only Spanish decks are written here.

## Read first

- `engine/theme/layouts.yaml` — the only allowed slide layouts and modifiers, with each one's purpose and soft limits. The build fails on anything else.
- [references/deck-style.md](references/deck-style.md) — how to write slides and notes for this course. Read it before writing a single slide.
- `content/es/prompts/slides.md` — the reference deck; match its tone, density and notes.

All commands run from the repository root (`projects/ia-edu/ia-educacion`); the `--directory` form below works from anywhere.

## Workflow

### 1. Find what needs work

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py status
```

Work on the lines of kind `deck`: `stale` (a source page changed), `trivial` (only non-translatable keys such as `reviewed:` changed: run `provenance.py stamp --if-trivial` on it and move on), `unstamped` (made before provenance existed: compare it with the whole module) or `missing` (the module has pages but no deck). If the user named a module, do only that one.

### 2. Read the change, not the whole module

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py diff content/es/<module>/slides.md
```

It prints, per source page, a unified diff between the text the deck was made from and the text now. For a missing deck, or when the diff says the recorded version is not in git, read the module's pages in full (`index.md` and the sub-pages listed in `content/nav.yaml`).

### 3. Edit only the affected slides

- Map each changed hunk to the slides built from that section; edit those, add slides for new sections, and remove slides whose section was removed.
- Leave every other slide **byte-identical**, and keep existing `id`s: they are deep links (`presentacion/?m=<module>#/<module>--<id>`) that the teacher may have saved.
- If the change only touched wording that no slide uses, the deck may need no edit at all; still stamp it (step 4).
- When a demo needs a step the page does not contain, **do not put it only in the notes**: propose the addition to the page to the user first (people studying alone need it too), then use it in the notes.

### 4. Record the provenance

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py stamp content/es/<module>/slides.md
```

Never write or edit `derived_from` by hand.

### 5. Build and look at it

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/build.py --no-search
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/shoot.py --module <module>
```

The build must report 0 errors; fix `slide-*` warnings about regions or soft limits unless there is a clear reason. `shoot.py` exits 1 and names any slide whose content overflows 1280×720: split it, cut text, or as a last resort add `dense`. Open the PNGs in `engine/_screens/es/<module>/` for every slide you added or changed and check them visually.

### 6. Report

Give the user a table `slide id | page section | new / changed / removed`, list any page additions you are proposing, and remind them that the Galician deck is now stale (`sync-translation`).

## Guardrails

- No claim on a slide that is not in the pages: condense, never add. Volatile facts (model versions, prices, plan limits) stay on the dated page; the slide says where to look.
- No HTML, no `style=`, no class outside `layouts.yaml`, no new layout. If the vocabulary cannot express something, say so and propose a vocabulary change instead of working around it.
- No edits to the pages, `content/gl/`, `engine/` or the theme from this skill unless the user agrees.
- Spanish conventions: unadapted English words in italics (*prompt*, *chatbot*), «comillas latinas», sentence-case titles.
