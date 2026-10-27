"""Discovers pages and decks under content/, applies language fallback and inheritance, and maps them to URLs."""

import tomllib
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
ENGINE_DIR = REPO_ROOT / "engine"
ASSETS_DIR = CONTENT_DIR / "assets"

DECK_FILE_NAME = "slides.md"
INHERITED_KEYS = ("reviewed", "review_every", "draft")


@dataclass(frozen=True)
class SiteConfig:
    base_path: str
    site_url: str
    languages: list[str]
    source_language: str
    stale_after_months: int
    max_image_kib: int
    deck_slide_width: int
    deck_slide_height: int
    mermaid_url: str
    reserved_slugs: list[str]


def load_config(path: Path = ENGINE_DIR / "config.toml", base_path_override: str | None = None) -> SiteConfig:
    values = tomllib.loads(path.read_text(encoding="utf-8"))
    if base_path_override is not None:
        values["base_path"] = base_path_override
    base_path = "/" + values["base_path"].strip("/") + "/" if values["base_path"].strip("/") else "/"
    values["base_path"] = base_path
    return SiteConfig(**values)


@dataclass(frozen=True)
class Problem:
    level: str  # "error" or "warning"
    path: str
    line: int
    code: str
    message: str


def split_front_matter(text: str) -> tuple[dict, str, int]:
    """Returns the front matter, the body, and the 1-based line number where the body starts."""
    if not text.startswith("---\n"):
        return {}, text, 1
    closing = text.find("\n---\n", 3)
    if closing == -1 and text.endswith("\n---"):
        closing = len(text) - len("\n---")
    if closing == -1:
        raise ValueError("front matter is not closed with ---")
    front_text = text[4:closing]
    body = text[closing + len("\n---\n"):]
    front = yaml.safe_load(front_text) or {}
    if not isinstance(front, dict):
        raise ValueError("front matter must be a mapping")
    front_line_count = front_text.count("\n") + 1 if front_text else 0
    body_start_line = front_line_count + 3
    return front, body, body_start_line


def slug_path_for(relative_path: str) -> str:
    """'index.md' -> '', 'prompts/index.md' -> 'prompts/', 'prompts/ejemplos.md' -> 'prompts/ejemplos/'."""
    path = PurePosixPath(relative_path)
    parts = list(path.parent.parts) if path.name == "index.md" else [*path.parent.parts, path.stem]
    return "".join(f"{part}/" for part in parts)


@dataclass
class Page:
    language: str
    relative_path: str
    source_file: Path
    front: dict
    body: str
    body_start_line: int
    is_fallback: bool

    @property
    def slug_path(self) -> str:
        return slug_path_for(self.relative_path)

    @property
    def module(self) -> str | None:
        parts = PurePosixPath(self.relative_path).parts
        return parts[0] if len(parts) > 1 else None

    @property
    def title(self) -> str:
        return str(self.front.get("title", ""))

    @property
    def is_module_index(self) -> bool:
        return self.module is not None and PurePosixPath(self.relative_path).name == "index.md"


@dataclass
class Deck:
    language: str
    module: str
    source_file: Path
    front: dict
    body: str
    body_start_line: int
    is_fallback: bool


@dataclass
class NavModule:
    slug: str
    subpages: list[str]
    advanced: bool


@dataclass
class NavSection:
    id: str
    modules: list[NavModule]


@dataclass
class LanguageContent:
    language: str
    ui: dict
    pages: dict[str, Page] = field(default_factory=dict)
    decks: dict[str, Deck] = field(default_factory=dict)


@dataclass
class ContentModel:
    config: SiteConfig
    nav: list[NavSection]
    languages: dict[str, LanguageContent]
    problems: list[Problem]

    def url_for(self, language: str, relative_path: str) -> str:
        return self.language_root(language) + slug_path_for(relative_path)

    def language_root(self, language: str) -> str:
        prefix = "" if language == self.config.source_language else f"{language}/"
        return self.config.base_path + prefix

    def deck_url(self, language: str, modules: list[str] | None = None) -> str:
        query = f"?m={','.join(modules)}" if modules else ""
        return self.language_root(language) + "presentacion/" + query

    def nav_modules(self) -> list[NavModule]:
        return [module for section in self.nav for module in section.modules]

    def ordered_pages(self, language: str) -> list[Page]:
        """Home first, then every module index followed by its sub-pages, in nav order."""
        pages = self.languages[language].pages
        ordered = [pages["index.md"]] if "index.md" in pages else []
        for module in self.nav_modules():
            for relative_path in [f"{module.slug}/index.md", *(f"{module.slug}/{sub}.md" for sub in module.subpages)]:
                if relative_path in pages:
                    ordered.append(pages[relative_path])
        return ordered


def deep_merge(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_yaml_file(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_nav(content_dir: Path, problems: list[Problem]) -> list[NavSection]:
    raw = load_yaml_file(content_dir / "nav.yaml")
    advanced = set(raw.get("advanced", []))
    sections = []
    for raw_section in raw.get("sections", []):
        modules = []
        for entry in raw_section.get("modules", []):
            if isinstance(entry, str):
                slug, subpages = entry, []
            elif isinstance(entry, dict) and len(entry) == 1:
                slug, subpages = next(iter(entry.items()))
            else:
                problems.append(Problem("error", "content/nav.yaml", 0, "nav-entry", f"invalid module entry: {entry!r}"))
                continue
            modules.append(NavModule(slug=slug, subpages=list(subpages or []), advanced=slug in advanced))
        sections.append(NavSection(id=raw_section["id"], modules=modules))
    return sections


def read_markdown(path: Path, problems: list[Problem]) -> tuple[dict, str, int] | None:
    try:
        return split_front_matter(path.read_text(encoding="utf-8"))
    except (ValueError, yaml.YAMLError) as error:
        problems.append(Problem("error", repo_relative(path), 1, "front-matter", str(error)))
        return None


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def source_markdown_files(language_dir: Path) -> list[Path]:
    return sorted(
        path for path in language_dir.rglob("*.md")
        if path.name != DECK_FILE_NAME and not path.name.startswith("_")
    )


def load_content(config: SiteConfig, content_dir: Path = CONTENT_DIR, include_drafts: bool = False) -> ContentModel:
    problems: list[Problem] = []
    nav = load_nav(content_dir, problems)
    source_language = config.source_language
    source_dir = content_dir / source_language
    source_ui = load_yaml_file(source_dir / "_ui.yaml")

    source_pages: dict[str, Page] = {}
    for path in source_markdown_files(source_dir):
        parsed = read_markdown(path, problems)
        if parsed is None:
            continue
        front, body, body_start_line = parsed
        relative_path = path.relative_to(source_dir).as_posix()
        if front.get("draft") and not include_drafts:
            continue
        source_pages[relative_path] = Page(source_language, relative_path, path, front, body, body_start_line, False)

    source_decks: dict[str, Deck] = {}
    for path in sorted(source_dir.glob(f"*/{DECK_FILE_NAME}")):
        parsed = read_markdown(path, problems)
        if parsed is None:
            continue
        front, body, body_start_line = parsed
        module = path.parent.name
        if f"{module}/index.md" in source_pages:
            source_decks[module] = Deck(source_language, module, path, front, body, body_start_line, False)

    languages = {source_language: LanguageContent(source_language, source_ui, source_pages, source_decks)}

    for language in config.languages:
        if language == source_language:
            continue
        language_dir = content_dir / language
        ui = deep_merge(source_ui, load_yaml_file(language_dir / "_ui.yaml"))
        content = LanguageContent(language, ui)
        for relative_path, source_page in source_pages.items():
            translated_file = language_dir / relative_path
            if translated_file.exists() and (parsed := read_markdown(translated_file, problems)):
                front, body, body_start_line = parsed
                for key in INHERITED_KEYS:
                    if key in source_page.front:
                        front.setdefault(key, source_page.front[key])
                content.pages[relative_path] = Page(language, relative_path, translated_file, front, body, body_start_line, False)
            else:
                content.pages[relative_path] = Page(
                    language, relative_path, source_page.source_file, source_page.front, source_page.body,
                    source_page.body_start_line, True,
                )
        for module, source_deck in source_decks.items():
            translated_file = language_dir / module / DECK_FILE_NAME
            if translated_file.exists() and (parsed := read_markdown(translated_file, problems)):
                front, body, body_start_line = parsed
                content.decks[module] = Deck(language, module, translated_file, front, body, body_start_line, False)
            else:
                content.decks[module] = Deck(
                    language, module, source_deck.source_file, source_deck.front, source_deck.body,
                    source_deck.body_start_line, True,
                )
        for path in source_markdown_files(language_dir) if language_dir.exists() else []:
            relative_path = path.relative_to(language_dir).as_posix()
            if relative_path not in source_pages:
                problems.append(Problem("warning", repo_relative(path), 1, "orphan-translation",
                                        f"no {source_language} page {relative_path} for this translation"))
        languages[language] = content

    check_nav_against_pages(nav, source_pages, config, problems)
    return ContentModel(config, nav, languages, problems)


def check_nav_against_pages(nav: list[NavSection], pages: dict[str, Page], config: SiteConfig,
                            problems: list[Problem]) -> None:
    listed: set[str] = {"index.md"}
    for section in nav:
        for module in section.modules:
            if module.slug in config.reserved_slugs:
                problems.append(Problem("error", "content/nav.yaml", 0, "reserved-slug",
                                        f"module slug '{module.slug}' is reserved"))
            index_path = f"{module.slug}/index.md"
            listed.add(index_path)
            if index_path not in pages:
                problems.append(Problem("warning", "content/nav.yaml", 0, "nav-missing-page",
                                        f"module '{module.slug}' has no {index_path} yet"))
            for sub in module.subpages:
                listed.add(f"{module.slug}/{sub}.md")
                if f"{module.slug}/{sub}.md" not in pages:
                    problems.append(Problem("warning", "content/nav.yaml", 0, "nav-missing-page",
                                            f"sub-page '{module.slug}/{sub}.md' does not exist yet"))
    for relative_path, page in pages.items():
        if relative_path not in listed:
            problems.append(Problem("warning", repo_relative(page.source_file), 1, "not-in-nav",
                                    f"{relative_path} is not listed in content/nav.yaml"))
