# Deck style for the ia-educacion course

## Audience and purpose

Secondary and VET teachers, in a live session that is mostly demonstrations. A slide supports what the teacher says and shows; it is not a handout (the page is the handout). One idea per slide.

## Shape of a module deck

The build generates the module's title slide (from the page title and description); in a full session it also adds the course cover, the agenda and the closing slide with the QR code. Do not write those.

A typical module deck, 15–25 slides (about 45 minutes with demos):

1. A `statement` that states the module's central idea.
2. Blocks of 3–6 slides, one per main section of the page; a `section` divider only when the module has three or more blocks.
3. A `demo` slide wherever the page shows something worth doing live (usually 1–3 per module).
4. A `practice` slide near the end when the page offers a task the group can do in 10–15 minutes.
5. Optionally a closing `statement` or `checklist` that sums up.

## Titles and text

- Titles are **assertions**, not topics: «El rol fija la voz, no la tarea», not «Rol». A statement title alone should carry the message.
- At most 6 bullets, each a single line where possible. No full paragraphs except in `statement`, `quote` and the regions of `comparison`.
- Bold sparingly: one key term per bullet at most.
- Copyable prompts go in a `text` fence on a `prompt` slide; long prompts are shortened on the slide, and the notes say «la versión completa está en la página».
- Links point to the page source (`[Ejemplos comentados](ejemplos.md)`); the build turns them into URLs that open in a new tab.
- Images come from `content/assets/<module>/` with alt text; use `image-full` or `image-text`.

## Using the layouts

- `comparison`: the first `###` region is the weak version, the second the strong one. Region titles short («Mal» / «Mejor», «Antes» / «Después»).
- `two-col`: two parallel things of the same kind; `cards`: three or four, one `###` each, with 1–2 lines per card.
- `big-number`: the first bold text is the figure, the next sentence its meaning, the last line its source.
- `quote`: a blockquote and, on the line after it, the source.
- `timeline`: a list whose items start with **year**.
- `table`: at most 5 rows × 4 columns.
- `checklist`: a task list (`- [ ]`), for verification steps.
- `fragments` when the order of revelation helps the explanation (lists, cards); not by default.

## Ids

ASCII kebab-case from the slide's meaning (`preguntar-primero`, `demo-metaprompting`), unique in the deck, never renamed once published.

## Speaker notes

Every `demo` and `practice` slide has notes; other slides have notes only when there is something to say that the slide does not show. Start the notes with `Notas:` at column 0.

Demo notes follow this template:

```
Notas:
**Demo (5 min)**. Herramienta y cuenta (p. ej. cualquier chatbot, en un chat temporal).

1. Paso concreto.
2. Paso concreto.

**Resultado esperado:** qué debería verse.
**Si falla:** qué enseñar en su lugar (normalmente, el ejemplo de la página).
**Mensaje clave:** la idea que el grupo debe llevarse.
```

Practice notes say how to run it (pairs, time, what to share) and what to look for in the results.
