# Docencia con IA

Course materials on artificial intelligence for secondary and vocational teachers (Galicia, Spain), in Spanish and Galician: a website with one page per module and a slide deck per module that can be combined for each session.

**Site:** <https://i.gal/ia-edu>

## How it works

The website is the single source of truth. Each module is written once, in Spanish, as Markdown; its slide deck is derived from it, and the Galician version follows both. A small Python generator turns that into a static site with search, and reveal.js shows the decks.

```text
content/          what is written and translated
  nav.yaml        order of sections, modules and sub-pages
  assets/         images (a name.gl.svg sibling is the Galician variant)
  es/  gl/        one folder per module: index.md, sub-pages, slides.md
engine/           what builds it (scripts run by path, not a package)
  build.py        the site, into engine/_build/ (pages, decks, bridge pages for old addresses, sitemap.xml, search index)
  check.py        links, anchors, slides, translation parity, review dates
  provenance.py   which translations and decks are out of date, and what changed
  shoot.py        screenshots of every slide (fails if one overflows) and, with --audit, the accessibility audit
  redirects.yaml  where each address of the old site went
  templates/ theme/ vendor/   HTML, CSS and the vendored reveal.js
.claude/skills/   update-slides and sync-translation, the two maintenance workflows
```

Every derived file (a deck, a Galician page) records the git hash of the Spanish text it came from, so `provenance.py` can say exactly which ones a change affects and show the diff to apply.

## Working on it

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run engine/build.py --serve            # http://127.0.0.1:8000/ia-educacion/, rebuilds on change
uv run engine/check.py                    # errors fail, warnings are reported
uv run engine/provenance.py status        # what needs updating after an edit
uv run engine/shoot.py --audit --theme both   # accessibility (axe-core) on every page; needs Google Chrome
uv run pytest
```

Every push to `master` runs the same checks (tests, content checks, build and accessibility audit) in GitHub Actions and, if they pass, publishes the site to GitHub Pages ([site.yml](.github/workflows/site.yml)).

Contribution rules (tone, sources, slide layouts, Galician conventions) are in [AGENTS.md](AGENTS.md).

## History

Until October 2026 the site was built with Docusaurus. That version is kept in the `legacy-docusaurus` branch, and its addresses still work: each one is a small page that forwards to its new place.
