"""Builds the site into engine/_build: pages, the composable deck, assets and the search index.

Usage: uv run engine/build.py [--drafts] [--no-search] [--strict] [--base-path /x/] [--serve [--port 8000]]
"""

import argparse
import datetime
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import quoteattr

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup

from content_model import (ASSETS_DIR, ENGINE_DIR, REPO_ROOT, ContentModel, Page, Problem, SiteConfig,
                           load_config, load_content)
from markdown_render import RenderContext, pygments_css, render_markdown
from redirects import Redirect, load_legacy_routes, load_redirect_map, plan_redirects
from slides_render import RenderedDeck, load_vocabulary, module_title_section, render_deck, section_html
from validation import heading_ids, validate_rendered

OUTPUT_DIR = ENGINE_DIR / "_build"
TEMPLATES_DIR = ENGINE_DIR / "templates"
THEME_DIR = ENGINE_DIR / "theme"
VENDOR_DIR = ENGINE_DIR / "vendor"
SHORT_URL = "i.gal/ia-edu"
LOCALES = {"es": "es_ES", "gl": "gl_ES"}


@dataclass
class RenderedPage:
    page: Page
    html: str
    toc: list
    has_mermaid: bool
    context: RenderContext


@dataclass
class BuildResult:
    problems: list[Problem]
    page_count: int
    slide_count: int
    redirect_count: int


def css_string(value: str) -> Markup:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("<", "\\3c ")
    return Markup(f'"{escaped}"')


def make_environment() -> Environment:
    environment = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "j2"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["css_string"] = css_string
    return environment


def format_date(value: datetime.date, ui: dict) -> str:
    month = ui["months"][value.month - 1]
    return ui["labels"]["date_format"].format(day=value.day, month=month, year=value.year)


def months_between(earlier: datetime.date, later: datetime.date) -> int:
    return (later.year - earlier.year) * 12 + later.month - earlier.month


def render_pages(model: ContentModel, problems: list[Problem]) -> dict[str, dict[str, RenderedPage]]:
    rendered: dict[str, dict[str, RenderedPage]] = {}
    source_language = model.config.source_language
    source_heading_ids: dict[str, list[str]] = {}
    for language in [source_language, *(lang for lang in model.config.languages if lang != source_language)]:
        content = model.languages[language]
        rendered[language] = {}
        for relative_path, page in content.pages.items():
            inherited = None if language == source_language or page.is_fallback else source_heading_ids.get(relative_path)
            context = RenderContext(model=model, language=language, source_file=page.source_file, ui=content.ui,
                                    line_offset=page.body_start_line - 1, inherited_heading_ids=inherited)
            result = render_markdown(page.body, context)
            if language == source_language:
                source_heading_ids[relative_path] = [heading.id for heading in context.headings]
            if not page.is_fallback:
                problems.extend(context.problems)
            toc = [heading for heading in context.headings if heading.level in (2, 3)]
            rendered[language][relative_path] = RenderedPage(page, result.html, toc, context.has_mermaid, context)
    return rendered


def render_decks(model: ContentModel, problems: list[Problem]) -> dict[str, dict[str, RenderedDeck]]:
    vocabulary = load_vocabulary()
    decks: dict[str, dict[str, RenderedDeck]] = {}
    for language, content in model.languages.items():
        decks[language] = {}
        for module, deck in content.decks.items():
            rendered = render_deck(deck, model, vocabulary)
            if not deck.is_fallback:
                problems.extend(rendered.problems)
            decks[language][module] = rendered
    return decks


def nav_tree(model: ContentModel, language: str, current: Page | None,
             decks: dict[str, RenderedDeck]) -> list[dict]:
    pages = model.languages[language].pages
    ui = model.languages[language].ui
    tree = []
    for section in model.nav:
        modules = []
        for module in section.modules:
            index_path = f"{module.slug}/index.md"
            if index_path not in pages:
                continue
            index_page = pages[index_path]
            is_current_module = current is not None and current.module == module.slug
            subpages = [
                {"title": pages[f"{module.slug}/{sub}.md"].title,
                 "url": model.url_for(language, f"{module.slug}/{sub}.md"),
                 "current": current is not None and current.relative_path == f"{module.slug}/{sub}.md"}
                for sub in module.subpages if f"{module.slug}/{sub}.md" in pages
            ]
            deck = decks.get(module.slug)
            modules.append({
                "slug": module.slug,
                "title": index_page.title,
                "description": index_page.front.get("description", ""),
                "url": model.url_for(language, index_path),
                "current": is_current_module,
                "current_page": current is not None and current.relative_path == index_path,
                "open": is_current_module,
                "advanced": module.advanced,
                "subpages": subpages,
                "deck_url": model.deck_url(language, [module.slug]) if deck and deck.slides else None,
                "slide_count": len(deck.slides) + 1 if deck else 0,
            })
        if modules:
            tree.append({"label": ui["nav"].get(section.id, section.id), "modules": modules})
    return tree


def alternates_for(model: ContentModel, relative_path: str | None) -> list[dict]:
    alternates = []
    for language in model.config.languages:
        ui = model.languages[language].ui
        url = model.url_for(language, relative_path) if relative_path is not None else model.deck_url(language)
        alternates.append({"lang": language, "url": url, "absolute_url": model.config.site_url + url,
                           "code": language.upper(), "name": ui["language_name"]})
    return alternates


def common_context(model: ContentModel, language: str, build_date: str) -> dict:
    ui = model.languages[language].ui
    base_path = model.config.base_path
    return {
        "lang": language,
        "content_lang": language,
        "ui": ui | {"locale": LOCALES.get(language, language)},
        "base_path": base_path,
        "engine_url": base_path + "_engine/",
        "vendor_url": base_path + "_engine/vendor/reveal.js-6.0.2/",
        "home_url": model.language_root(language),
        "deck_index_url": model.deck_url(language),
        "mermaid_url": model.config.mermaid_url,
        "build_date": format_date(datetime.date.fromisoformat(build_date), ui),
        "short_url": SHORT_URL,
        "noindex": False,
        "indexable": True,
        "has_mermaid": False,
    }


def write_html(output_dir: Path, url: str, base_path: str, html: str) -> None:
    relative = url.removeprefix(base_path).split("?")[0]
    target = output_dir / relative / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def write_pages(model: ContentModel, rendered: dict[str, dict[str, RenderedPage]],
                decks: dict[str, dict[str, RenderedDeck]], output_dir: Path, search_enabled: bool,
                build_date: str) -> int:
    environment = make_environment()
    page_template = environment.get_template("page.html.j2")
    home_template = environment.get_template("home.html.j2")
    today = datetime.date.today()
    count = 0
    for language, pages in rendered.items():
        ui = model.languages[language].ui
        ordered = model.ordered_pages(language)
        for position, page in enumerate(ordered):
            rendered_page = pages[page.relative_path]
            context = common_context(model, language, build_date)
            reviewed = page.front.get("reviewed")
            review_every = int(page.front.get("review_every", model.config.stale_after_months))
            deck = decks[language].get(page.module) if page.is_module_index else None
            module_index = model.languages[language].pages.get(f"{page.module}/index.md") if page.module else None
            context |= {
                "page_title": page.title if page.relative_path != "index.md" else "",
                "description": page.front.get("description", ui["site_tagline"]),
                "canonical": model.config.site_url + model.url_for(language, page.relative_path),
                "alternates": alternates_for(model, page.relative_path),
                "nav_tree": nav_tree(model, language, page, decks[language]),
                "content_html": rendered_page.html,
                "toc": rendered_page.toc,
                "has_mermaid": rendered_page.has_mermaid,
                "is_fallback": page.is_fallback,
                "content_lang": model.config.source_language if page.is_fallback else language,
                "indexable": not page.is_fallback,
                "search_enabled": search_enabled,
                "reviewed": format_date(reviewed, ui) if isinstance(reviewed, datetime.date) else "",
                "reviewed_iso": reviewed.isoformat() if isinstance(reviewed, datetime.date) else "",
                "reviewed_stale": isinstance(reviewed, datetime.date) and months_between(reviewed, today) >= review_every,
                "breadcrumb": ({"title": module_index.title, "url": model.url_for(language, module_index.relative_path)}
                               if module_index and not page.is_module_index else None),
                "deck": ({"slide_count": len(deck.slides) + 1, "url": model.deck_url(language, [page.module]),
                          "frame_url": model.deck_url(language, [page.module]) + "&frame=1"}
                         if deck and deck.slides else None),
                "previous_page": page_link(model, language, ordered[position - 1]) if position > 0 else None,
                "next_page": page_link(model, language, ordered[position + 1]) if position + 1 < len(ordered) else None,
            }
            template = home_template if page.relative_path == "index.md" else page_template
            write_html(output_dir, model.url_for(language, page.relative_path), model.config.base_path,
                       template.render(context))
            count += 1
    return count


def page_link(model: ContentModel, language: str, page: Page) -> dict:
    title = page.title or model.languages[language].ui["site_title"]
    return {"title": title, "url": model.url_for(language, page.relative_path)}


def write_decks(model: ContentModel, decks: dict[str, dict[str, RenderedDeck]], output_dir: Path,
                build_date: str) -> int:
    template = make_environment().get_template("deck.html.j2")
    total_slides = 0
    for language, language_decks in decks.items():
        ui = model.languages[language].ui
        pages = model.languages[language].pages
        modules = []
        for section in model.nav:
            for nav_module in section.modules:
                deck = language_decks.get(nav_module.slug)
                index_page = pages.get(f"{nav_module.slug}/index.md")
                if deck is None or index_page is None or not deck.slides:
                    continue
                kicker = ui["nav"].get(section.id, section.id)
                sections = [module_title_section(nav_module.slug, index_page.title,
                                                 index_page.front.get("description", ""), kicker)]
                sections += [section_html(nav_module.slug, slide) for slide in deck.slides]
                modules.append({"slug": nav_module.slug, "title": index_page.title, "slide_count": len(sections),
                                "sections_html": "\n".join(sections),
                                "page_url": model.url_for(language, index_page.relative_path)})
                total_slides += len(sections)
        context = common_context(model, language, build_date) | {
            "modules": modules,
            "deck_data": {"modules": [{key: module[key] for key in ("slug", "title", "slide_count", "page_url")}
                                      for module in modules],
                          "width": model.config.deck_slide_width, "height": model.config.deck_slide_height},
        }
        write_html(output_dir, model.deck_url(language), model.config.base_path, template.render(context))
    return total_slides


def write_redirects(model: ContentModel, redirects: list[Redirect], output_dir: Path) -> None:
    template = make_environment().get_template("redirect.html.j2")
    for redirect in redirects:
        html = template.render(lang=redirect.language, ui=model.languages[redirect.language].ui,
                               target_url=redirect.target_url, target_title=redirect.target_title,
                               absolute_url=model.config.site_url + redirect.target_url,
                               keeps_hash="#" not in redirect.target_url)
        write_html(output_dir, model.config.base_path + redirect.route, model.config.base_path, html)


def write_not_found(model: ContentModel, decks: dict[str, dict[str, RenderedDeck]], output_dir: Path,
                    search_enabled: bool, build_date: str) -> None:
    """One 404.html at the site root, which GitHub Pages serves for every missing address under it."""
    language = model.config.source_language
    messages = [{"lang": lang, "title": content.ui["labels"]["not_found_title"],
                 "text": content.ui["labels"]["not_found_text"], "home_label": content.ui["labels"]["not_found_home"],
                 "home_url": model.language_root(lang)}
                for lang, content in model.languages.items()]
    context = common_context(model, language, build_date) | {
        "page_title": messages[0]["title"],
        "description": model.languages[language].ui["site_tagline"],
        "canonical": "",
        "alternates": alternates_for(model, "index.md"),
        "nav_tree": nav_tree(model, language, None, decks[language]),
        "messages": messages,
        "noindex": True,
        "indexable": False,
        "search_enabled": search_enabled,
    }
    html = make_environment().get_template("404.html.j2").render(context)
    (output_dir / "404.html").write_text(html, encoding="utf-8")


def sitemap_xml(model: ContentModel) -> str:
    """Every translated page and the deck, each with its alternates; untranslated fallbacks stay out."""
    languages = model.config.languages
    translated = {language: [page.relative_path for page in model.ordered_pages(language) if not page.is_fallback]
                  for language in languages}
    entries = [(model.url_for(language, relative_path),
                {other: model.url_for(other, relative_path) for other in languages if relative_path in translated[other]})
               for language in languages for relative_path in translated[language]]
    entries += [(model.deck_url(language), {other: model.deck_url(other) for other in languages})
                for language in languages]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, alternates in entries:
        lines.append(f"<url><loc>{model.config.site_url}{url}</loc>")
        lines += [f'<xhtml:link rel="alternate" hreflang={quoteattr(language)} '
                  f'href={quoteattr(model.config.site_url + alternate)}/>' for language, alternate in alternates.items()]
        lines.append("</url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def copy_static(output_dir: Path) -> None:
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, output_dir / "assets", dirs_exist_ok=True)
    engine_output = output_dir / "_engine"
    shutil.copytree(THEME_DIR, engine_output / "theme", dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("*.yaml"))
    shutil.copytree(VENDOR_DIR, engine_output / "vendor", dirs_exist_ok=True)
    (engine_output / "theme" / "pygments.css").write_text(pygments_css(), encoding="utf-8")


def run_search_index(output_dir: Path) -> None:
    subprocess.run([sys.executable, "-m", "pagefind", "--site", str(output_dir), "--quiet"], check=True)


def build(config: SiteConfig, output_dir: Path = OUTPUT_DIR, include_drafts: bool = False,
          search_enabled: bool = True) -> BuildResult:
    model = load_content(config, include_drafts=include_drafts)
    problems = list(model.problems)
    rendered = render_pages(model, problems)
    decks = render_decks(model, problems)
    problems += validate_rendered(model, rendered, decks)
    redirects, redirect_problems = plan_redirects(model, heading_ids(rendered), load_legacy_routes(),
                                                  load_redirect_map())
    problems += redirect_problems
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    build_date = datetime.date.today().isoformat()
    page_count = write_pages(model, rendered, decks, output_dir, search_enabled, build_date)
    slide_count = write_decks(model, decks, output_dir, build_date)
    write_redirects(model, redirects, output_dir)
    write_not_found(model, decks, output_dir, search_enabled, build_date)
    (output_dir / "sitemap.xml").write_text(sitemap_xml(model), encoding="utf-8")
    copy_static(output_dir)
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")
    if search_enabled:
        run_search_index(output_dir)
    return BuildResult(problems, page_count, slide_count, len(redirects))


def report(result: BuildResult) -> tuple[int, int]:
    errors = [problem for problem in result.problems if problem.level == "error"]
    warnings = [problem for problem in result.problems if problem.level == "warning"]
    for problem in sorted(result.problems, key=lambda p: (p.level != "error", p.path, p.line)):
        print(f"{problem.level.upper():7} {problem.path}:{problem.line} [{problem.code}] {problem.message}")
    print(f"{result.page_count} pages, {result.slide_count} slides, {result.redirect_count} redirects; "
          f"{len(errors)} errors, {len(warnings)} warnings")
    return len(errors), len(warnings)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--base-path", default=None, help="override base_path from engine/config.toml")
    parser.add_argument("--drafts", action="store_true", help="include pages with draft: true")
    parser.add_argument("--no-search", action="store_true", help="skip the Pagefind index")
    parser.add_argument("--strict", action="store_true", help="fail on warnings too")
    parser.add_argument("--serve", action="store_true", help="serve the build and rebuild on changes")
    parser.add_argument("--port", type=int, default=8000)
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    config = load_config(base_path_override=arguments.base_path)
    if arguments.serve:
        from serve import serve
        build_arguments = [flag for flag, enabled in (("--drafts", arguments.drafts), ("--no-search", arguments.no_search))
                           if enabled]
        if arguments.base_path:
            build_arguments += ["--base-path", arguments.base_path]
        return serve(config, arguments.out, arguments.port, build_arguments)
    result = build(config, arguments.out, arguments.drafts, not arguments.no_search)
    errors, warnings = report(result)
    print(f"Output: {arguments.out.relative_to(REPO_ROOT) if arguments.out.is_relative_to(REPO_ROOT) else arguments.out}")
    return 1 if errors or (arguments.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
