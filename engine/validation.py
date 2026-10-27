"""Checks that need rendered content (anchors, images) or workflow state (review dates, provenance).

The build runs validate_rendered; check.py runs everything and groups findings by category."""

import datetime

from content_model import ContentModel, Problem, repo_relative

FOOTNOTE_ANCHOR_PREFIXES = ("fn", "fnref")
CATEGORIES = {
    "links": {"broken-link", "link-not-md", "broken-anchor", "slide-anchor-link"},
    "assets": {"missing-asset", "external-image", "image-class", "image-size", "image-alt"},
    "slides": {"slide-id", "slide-id-duplicate", "slide-attribute", "slide-class", "slide-layouts", "slide-regions",
               "slide-words", "slide-bullets"},
    "parity": {"heading-parity", "orphan-translation"},
    "stale": {"stale", "trivial", "unstamped", "missing"},
    "reviewed": {"reviewed-missing", "reviewed-stale"},
    "content": {"inline-style", "body-h1", "front-matter", "nav-entry", "nav-missing-page", "not-in-nav", "reserved-slug",
                "todo"},
}


def category_of(code: str) -> str:
    return next((category for category, codes in CATEGORIES.items() if code in codes), "content")


def months_between(earlier: datetime.date, later: datetime.date) -> int:
    return (later.year - earlier.year) * 12 + later.month - earlier.month


def heading_ids(rendered: dict) -> dict[tuple[str, str], set[str]]:
    return {(language, relative_path): {heading.id for heading in page.context.headings}
            for language, pages in rendered.items() for relative_path, page in pages.items()}


def validate_rendered(model: ContentModel, rendered: dict, decks: dict) -> list[Problem]:
    problems: list[Problem] = []
    ids = heading_ids(rendered)
    for language, pages in rendered.items():
        for relative_path, rendered_page in pages.items():
            if rendered_page.page.is_fallback:
                continue
            context = rendered_page.context
            for link in context.links:
                target = link.target_page or relative_path
                problems += check_anchor(ids, language, target, link.anchor, link.source, link.line)
            for image in context.images:
                if image.asset_path is None:
                    continue
                size_kib = image.asset_path.stat().st_size / 1024
                if size_kib > model.config.max_image_kib:
                    problems.append(Problem("warning", image.source, image.line, "image-size",
                                            f"{repo_relative(image.asset_path)} is {size_kib:.0f} KiB "
                                            f"(limit {model.config.max_image_kib})"))
                if not image.alt.strip():
                    problems.append(Problem("warning", image.source, image.line, "image-alt",
                                            f"{repo_relative(image.asset_path)} has no alt text"))
    for language, language_decks in decks.items():
        for deck in language_decks.values():
            if model.languages[language].decks[deck.module].is_fallback:
                continue
            for link in deck.links:
                if link.target_page:
                    problems += check_anchor(ids, language, link.target_page, link.anchor, link.source, link.line)
    return problems


def check_anchor(ids: dict, language: str, target: str, anchor: str | None, source: str, line: int) -> list[Problem]:
    if not anchor or anchor.startswith(FOOTNOTE_ANCHOR_PREFIXES):
        return []
    known = ids.get((language, target), set())
    if anchor in known:
        return []
    return [Problem("error", source, line, "broken-anchor", f"#{anchor} is not a heading of {target} ({language})")]


def review_problems(model: ContentModel, today: datetime.date) -> list[Problem]:
    problems = []
    for page in model.languages[model.config.source_language].pages.values():
        source = repo_relative(page.source_file)
        reviewed = page.front.get("reviewed")
        if not isinstance(reviewed, datetime.date):
            problems.append(Problem("warning", source, 1, "reviewed-missing", "no reviewed: date in front matter"))
            continue
        limit = int(page.front.get("review_every", model.config.stale_after_months))
        age = months_between(reviewed, today)
        if age >= limit:
            problems.append(Problem("warning", source, 1, "reviewed-stale",
                                    f"reviewed {reviewed.isoformat()}, {age} months ago (review every {limit})"))
    return problems


def todo_problems(model: ContentModel) -> list[Problem]:
    """Pending work left in the content as <!-- TODO: ... --> comments."""
    problems = []
    for language in model.languages.values():
        for page in language.pages.values():
            if page.is_fallback:
                continue
            for offset, line in enumerate(page.body.split("\n")):
                if "<!-- TODO" in line:
                    note = line.split("<!-- TODO", 1)[1].split("-->", 1)[0].strip(" :")
                    problems.append(Problem("warning", repo_relative(page.source_file), page.body_start_line + offset,
                                            "todo", note))
    return problems
