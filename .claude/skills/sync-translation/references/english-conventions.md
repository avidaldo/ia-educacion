# English edition: conventions

The English edition (`content/en/`) presents the course to teachers and schools across Europe. It is the Spanish site with two differences: it is in English, and it leaves out what only applies in Spain or Galicia, replacing it with the European Union rule where one exists. Everything else is translated faithfully, so that later Spanish changes can be applied to it as diffs, like the Galician ones.

## Two kinds of English file

- **Mirrors** (every page and deck except the ones below): same headings in the same order and number, same blocks, chats, alerts, fences, tables, slide separators and slide ids, same link and image paths. The build gives their headings the Spanish anchor ids by position, so a missing or extra heading breaks every link into the page.
- **Adaptations**, marked `adapted: true` in their front matter: `index.md`, `etica-legal/index.md`, `etica-legal/normativa.md` and `datos-alumnado/index.md`, and the decks `etica-legal/slides.md` and `datos-alumnado/slides.md`. Their structure follows the content: headings and slides can be dropped, merged or added. Their anchor ids come from their own English headings, so a link into an adaptation uses the English anchor (`../etica-legal/normativa.md#data-protection`); every other link keeps the Spanish anchor. In an adapted deck, a slide that comes from a Spanish one keeps its id; a new slide gets a new English id.

A Spanish change to a mirror is applied at the same place. A Spanish change to an adaptation is applied if it concerns the EU or is general, and skipped if it only concerns Spain or Galicia.

## What goes and what replaces it

| Remove | Replace with |
| --- | --- |
| Spanish and Galician norms: LOPDGDD, LOE/LOMLOE, royal decrees, Galician laws and decrees, bills | The EU rule that governs the same point (GDPR, AI Act), or a plain statement that national law decides it |
| Spanish and Galician bodies as a source of rules or advice: Xunta, Consellería, Ministerio, INTEF, AEPD, AESIA | EU sources (EDPB, EDPS, European Commission guidelines), or "your education authority", "your national data protection authority", "your school's data protection officer" |
| Galician plans, press releases, protocols and training decks; Spanish ministry guides | Nothing, unless the idea stands on its own: then it is said in the site's own voice. If the idea is that source's own (a framing, a checklist), the footnote keeps a short credit ("Adapted from a training deck of the Galician education authority, December 2025, p. 12"); if it is common knowledge, or an EU source says the same, the footnote goes or points to the EU source |
| Spain-only platforms and labels (Abalar, the Xunta's virtual classrooms, Edixgal, ESO, Bachillerato, EBAU) | Generic terms: "your school's virtual learning environment", "lower secondary", "upper secondary", "university entrance exams" |

- **Where EU law leaves the choice to each country, say so and stop there.** Examples: the age from which a child's own consent is enough for an online service to process their data (GDPR art. 8: 16, or lower by national law but not below 13); the legal basis that lets a school process student data for teaching (a task in the public interest set by national law, GDPR art. 6(1)(e) and 6(3)); the authority that supervises the AI Act in each country. Never state what a particular national law says.
- **Practical advice that came from a Spanish or Galician guide** (ask the data protection officer, use only the tools the education authority provides) stays only if it follows from the GDPR or is sound practice anywhere, and it is labelled accordingly: legal obligation (with the GDPR or AI Act article), institutional recommendation (with the EU source), or good practice. Never attribute it to a source the reader cannot consult, and never present it as the law of the reader's country.
- If a passage has no EU equivalent and nothing general to keep, cut it. A correction never grows the text.
- Spain in a non-legal context: "not available in Spain or in the rest of the EU" becomes "not available in the EU". A worked example built on a Spanish source (a workflow that reads Spain's official gazette) is kept as it was tested, presented as an example ("Spain's official gazette, the BOE"), with a line saying the same pattern works with any similar source.

## Sources and quotations

- **Official EU texts are quoted from their English version, copied verbatim** from the copies saved in `domain/normativa/eu/` (find the passage with `grep` in the `.txt` or `.md` twin). Never translate a quotation from the Spanish version.
  - GDPR: `regulation-2016-679-gdpr-en.txt`
  - AI Act as published: `regulation-2024-1689-ai-act-en.txt`; its amendment by the Digital Omnibus on AI: `regulation-2026-1744-digital-omnibus-ai-en.txt` (read both: the amendment replaced art. 4, added letters to art. 5(1) and moved application dates)
  - CJEU *Nowak* (C-434/16): `cjeu-c-434-16-nowak-2017-en.txt`; CJEU *EDPS v SRB* (C-413/23 P): `cjeu-c-413-23-p-edps-srb-2025-en.txt`
  - AEPD and EDPS, *10 misunderstandings related to anonymisation*: `aepd-edps-10-misunderstandings-anonymisation-2021-en.md`
  - European Commission, *Guidelines on the ethical use of AI and data in teaching and learning for educators*, 2026: `guidelines-ethical-use-ai-data-teaching-learning-2026.txt`
- Footnotes link the official English page: EUR-Lex for EU law and case law (`https://eur-lex.europa.eu/eli/reg/2016/679/oj`, `https://eur-lex.europa.eu/eli/reg/2024/1689/oj`, `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62016CJ0434`), never the BOE.
- Cite EU articles in the EU's own form: "Article 6(1)(e) GDPR", "Article 5(1)(f) of the AI Act", "recital 26".
- Research papers and English sources keep their links. A source that exists only in Spanish keeps its link with "(in Spanish)"; a quotation from it is translated and marked "(our translation)" in the footnote. Help pages of products (Microsoft, Apple, LibreOffice) link their English version (`en-us`, `en-gb`, `/en/`) when the Spanish link has a language code in it.
- Dates of access: "accessed 5 November 2026".

## Language

- **British English, as in EU institutions**: -ise spellings (organise, anonymise, pseudonymise), programme (but "computer program"), behaviour, "mark" for a grade. Dates: 21 November 2026. Sentence-case headings, as in Spanish.
- **Plain, direct, teacher to teacher**, second person. Same rules as the Spanish site: *language model* for the model, *chatbot* for the product, *agent* only for systems that act with tools in a loop; no anthropomorphism; each bias attributed to the stage where it enters and the human decision behind it.
- **Quotation marks**: curly double quotes in prose (“ ”, for the Spanish « »), single ones inside them, and the curly apostrophe (’). Quotations from EU texts keep their own marks (‘personal data’). Inside code fences and inline code, keep what the Spanish has.
- **No italics for English words**: the Spanish rule for anglicisms does not apply (prompt, chatbot, notebook, skill, vibe coding are plain English). Italics stay for titles of works and for non-English words.
- **Chats** (`:::: chat`): translate the messages; keep `model=` and `date=`, except descriptive words inside `model=`, which the page shows (`ChatGPT (custom GPT)`).
- **Fences**: translate `text` fences and `markdown` fences that hold a prompt or a skill, and the labels of `mermaid` diagrams (keep node ids and syntax). Unlike in Galician, also translate the data examples in `gift`, `aiken` and `xml` fences (questions, answers, feedback), keeping their syntax exactly. Every other fence (`html`, `json`, `bash`…) stays, except comments meant for the reader and, in an `html` fence that is a demo page or a snippet to copy, the text a reader sees and the placeholders (`lang`, `title`, headings, paragraphs, `https://your-page-address`).
- **Images**: a diagram with text in it gets an English sibling `name.en.svg` (copy the Spanish SVG and translate only the text nodes, keeping layout and sizes; check that no English label overflows its box). Moodle captures have no English variant: they show a Spanish interface, so their alt text says so ("Moodle's question import form, in Spanish").
- **Interface names** are written as the English interface of the product shows them (Moodle 4.x: Question bank, Import, Export, Preview…). If unsure of the exact label, describe the control instead of quoting it.
- **Front matter**: translate `title` and `description`; do not copy `reviewed`, `review_every` or `draft` (they are inherited); add `adapted: true` only to the adaptations; leave `derived_from` to `engine/provenance.py stamp`.

## Glossary

| Spanish | English |
| --- | --- |
| docente, profesorado | teacher, teachers |
| alumnado, alumno | students, student (learners where it reads better) |
| centro (educativo) | school |
| FP, formación profesional | VET, vocational education and training |
| ciclo (de FP) | VET programme |
| ESO / Bachillerato | lower secondary / upper secondary |
| secundaria | secondary |
| administración educativa, Consellería | education authority |
| equipo directivo / jefatura de estudios | school management / head of studies |
| tutor/a (de grupo) | form tutor |
| claustro | teaching staff |
| programación didáctica / unidad didáctica | course plan / teaching unit |
| criterios de evaluación / resultados de aprendizaje | assessment criteria / learning outcomes |
| evaluación / calificar, nota | assessment / to mark, mark |
| corregir (un examen) | mark, correct |
| retroalimentación | feedback |
| rúbrica | rubric |
| familias | families, parents |
| aula virtual | virtual learning environment (Moodle site, when it is Moodle) |
| banco de preguntas | question bank |
| cuestionario (Moodle) | quiz |
| modelo de lenguaje / *chatbot* / agente | language model / chatbot / agent |
| ventana de contexto | context window |
| alucinación | hallucination (explained as the site explains it) |
| dato personal / tratamiento | personal data / processing |
| responsable / encargado del tratamiento | controller / processor |
| persona delegada de protección de datos | data protection officer (DPO) |
| seudonimizar / anonimizar | pseudonymise / anonymise |
| categorías especiales de datos | special categories of personal data |
| evaluación de impacto | data protection impact assessment (DPIA) |
| RGPD / RIA | GDPR / AI Act |
| proveedor / responsable del despliegue | provider / deployer |
| sistema de IA de alto riesgo | high-risk AI system |
| alfabetización en IA | AI literacy |
| Para saber más | Going further |
| Para practicar | Practice |
| Con el alumnado | With your students |
| obligación legal / recomendación institucional / buena práctica | legal obligation / institutional recommendation / good practice |
