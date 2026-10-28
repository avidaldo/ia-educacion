"""Plans the bridge pages that send each route of the old Docusaurus site to its new address.

engine/legacy-urls.txt lists the old routes and engine/redirects.yaml maps them; build.py writes the pages."""

from dataclasses import dataclass
from pathlib import Path

import yaml

from content_model import ENGINE_DIR, ContentModel, Problem

LEGACY_URLS_FILE = ENGINE_DIR / "legacy-urls.txt"
REDIRECTS_FILE = ENGINE_DIR / "redirects.yaml"
REDIRECTS_SOURCE = "engine/redirects.yaml"
# The old site's translations: English and Italian were machine translations, so they land on the Spanish source.
LEGACY_LANGUAGE_PREFIXES = {"gl/": "gl", "en/": "es", "it/": "es"}
DECK_PATH = "presentacion/"


@dataclass(frozen=True)
class Redirect:
    route: str  # the old route, relative to base_path: "gl/docs/prompt/"
    language: str
    target_url: str  # "/ia-educacion/gl/prompts/", with the #anchor if the map gives one
    target_title: str


def load_legacy_routes(path: Path = LEGACY_URLS_FILE) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip().removeprefix("/") for line in lines if line.strip() and not line.startswith("#")]


def load_redirect_map(path: Path = REDIRECTS_FILE) -> dict[str, str]:
    entries = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(old_path): str(target or "") for old_path, target in entries.items()}


def resolve_target(model: ContentModel, heading_ids: dict[tuple[str, str], set[str]], language: str,
                   target: str) -> tuple[str, str] | str:
    """Returns (url, title) of the target in this language, or the reason it does not exist."""
    path, _, anchor = target.partition("#")
    ui = model.languages[language].ui
    if path == DECK_PATH and not anchor:
        return model.deck_url(language), ui["labels"]["deck_picker_link"]
    page = next((page for page in model.languages[language].pages.values() if page.slug_path == path), None)
    if page is None:
        return f"{target!r} is not a page of the site"
    if anchor and anchor not in heading_ids.get((language, page.relative_path), set()):
        return f"{target!r}: #{anchor} is not a heading of {page.relative_path} ({language})"
    url = model.url_for(language, page.relative_path) + (f"#{anchor}" if anchor else "")
    return url, page.title or ui["site_title"]


def plan_redirects(model: ContentModel, heading_ids: dict[tuple[str, str], set[str]], legacy_routes: list[str],
                   redirect_map: dict[str, str]) -> tuple[list[Redirect], list[Problem]]:
    base_path = model.config.base_path
    served = {model.url_for(language, page.relative_path).removeprefix(base_path)
              for language, content in model.languages.items() for page in content.pages.values()}
    served |= {model.deck_url(language).removeprefix(base_path) for language in model.languages}
    redirects: list[Redirect] = []
    problems: dict[str, Problem] = {}  # keyed by message: an old page reached from three prefixes is one problem
    for route in legacy_routes:
        if route in served:
            continue
        prefix = next((prefix for prefix in LEGACY_LANGUAGE_PREFIXES if route.startswith(prefix)), "")
        language = LEGACY_LANGUAGE_PREFIXES.get(prefix, model.config.source_language)
        old_path = route.removeprefix(prefix)
        # An old language root (/en/, /it/) goes to the home page without needing an entry.
        target = "" if old_path == "" else redirect_map.get(old_path)
        if target is None:
            message = f"no entry for the old route {old_path!r}"
            problems[message] = Problem("error", REDIRECTS_SOURCE, 1, "redirect-missing", message)
            continue
        resolved = resolve_target(model, heading_ids, language, target)
        if isinstance(resolved, str):
            message = f"{old_path}: {resolved}"
            problems[message] = Problem("error", REDIRECTS_SOURCE, 1, "redirect-target", message)
            continue
        target_url, target_title = resolved
        redirects.append(Redirect(route, language, target_url, target_title))
    return redirects, list(problems.values())
