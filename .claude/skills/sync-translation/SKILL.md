---
name: sync-translation
description: Keep the Galician version of the ia-educacion course site (content/gl/) in step with its Spanish source (content/es/) by applying only what changed — pages, slide decks and interface strings (_ui.yaml) — and write the first Galician version of new ones. Use when Spanish content changed, when engine/check.py or engine/provenance.py status reports Galician files as stale, unstamped or missing, or when the user asks to translate, "traducir", "pasar ao galego" or sync the translations of the course site.
allowed-tools: Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py *), Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/build.py *), Bash(uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/check.py *), Bash(git mv *)
---

# Sync translation — Spanish is the source, Galician follows the diff

## Stance

Spanish (`content/es/`) is the single source of truth; `content/gl/` mirrors it file by file. A Galician file is never rewritten from scratch when its source changes: the change in the Spanish text is located and the same change is made at the same place in the Galician text, so the rest of the translation — including wording the teacher may have polished — stays as it is.

Translate only reviewed Spanish: if the user is still editing a Spanish page or its deck is about to be updated (`update-slides`), wait, or translating twice costs double.

## Read first

- [references/galician-conventions.md](references/galician-conventions.md) — normative Galician, the anglicism rule, typography, frequent Spanish calques.
- [references/glossary-es-gl.md](references/glossary-es-gl.md) — fixed terms, including Moodle's Galician interface. Add to it when you settle a new term, and tell the user.

All commands run from the repository root (`projects/ia-edu/ia-educacion`); the `--directory` form below works from anywhere.

## Workflow

### 1. Find what needs work

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py status
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py moves
```

Work on kinds `translation`, `deck-translation` and `ui-translation`:

- `stale`: the Spanish source changed → step 2.
- `trivial`: only non-translatable keys changed (`reviewed:`, or the `derived_from` of a Spanish deck after it was restamped) → `provenance.py stamp --if-trivial <file>`, no edit.
- `missing`: no Galician file yet → translate the whole Spanish file (step 3).
- `unstamped`: a Galician file made before provenance existed → compare it in full with the Spanish file, fix every divergence, then stamp.
- `moves` prints `git mv` commands for translations whose source was renamed: run them first. If a Spanish file was deleted, propose deleting its Galician twin; never delete unasked.

### 2. Apply the diff

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py diff content/gl/<path>
```

For each hunk, find the corresponding passage in the Galician file (same heading, same position) and make the equivalent edit with a targeted Edit — never rewrite the file. If the diff says the recorded version is not in git, compare the whole Spanish and Galician files instead.

### 3. Translate a new file

Mirror the Spanish file exactly: same headings in the same order and number (the build gives Galician headings the Spanish anchor ids **by position**), same blocks, chats, alerts, fences, tables and slide separators, same link and image paths. Front matter: translate `title` and `description`; do not copy `reviewed`, `review_every` or `draft` (they are inherited); leave `derived_from` to the script.

### What is translated and what is not

| Translate | Keep exactly as in Spanish |
| --- | --- |
| Prose, headings, list items, table cells, alert titles | URLs and link paths (`../tests-moodle/index.md#gift`), anchors after `#` |
| Chat messages (user and assistant) | Chat `model=` and `date=` parameters |
| `text` fences (they are prompts to copy) | Every other fence: `gift`, `aiken`, `xml`, `html`, `json`, `mermaid` labels… — except comments meant for the reader |
| Slide content and `Notas:` (the marker stays `Notas:`) | Slide comments `<!-- .slide: id="…" class="…" -->` |
| `title`, `description` | Image paths (a Galician capture is a `name.gl.webp` sibling, chosen by the build) |

Product and interface names are kept as the product shows them in Galician when it has a Galician interface (Moodle: see the glossary), otherwise as in Spanish.

### 4. Stamp and check

```
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/provenance.py stamp content/gl/<path> [...]
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/check.py --only parity links stale --lang gl
uv run --directory ${CLAUDE_SKILL_DIR}/../../.. engine/build.py --no-search
```

`heading-parity` means the Galician headings no longer line up with the Spanish ones: fix the structure, not the ids. The build must report 0 errors.

### 5. Report

List the files touched and, for each, one line on what changed. List any term you had to decide (and added to the glossary) so the user can confirm it.

## Guardrails

- Never edit `content/es/` from this skill; if the Spanish text has an error, report it.
- Never write `derived_from` by hand.
- No machine-translation tools or external services: you translate, applying the conventions.
