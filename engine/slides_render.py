"""Turns a module's slides.md into reveal.js <section> elements, using the same Markdown dialect as the pages."""

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from markdown_it.common.utils import escapeHtml

from content_model import ENGINE_DIR, ContentModel, Deck, Problem, repo_relative
from markdown_render import LinkReference, RenderContext, render_markdown

LAYOUTS_FILE = ENGINE_DIR / "theme" / "layouts.yaml"
DEFAULT_LAYOUT = "bullets"
SLIDE_COMMENT = re.compile(r"^\s*<!--\s*\.slide:(?P<attributes>.*?)-->\s*$")
SLIDE_ATTRIBUTE = re.compile(r'(?P<name>[a-z-]+)="(?P<value>[^"]*)"')
SLIDE_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NOTES_MARKER = re.compile(r"^Notas:\s?(?P<rest>.*)$")
FENCE_OPENING = re.compile(r"^\s{0,3}(?P<marker>`{3,}|~{3,})")
BULLET_LINE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


@dataclass(frozen=True)
class Vocabulary:
    layouts: dict[str, dict]
    modifiers: dict[str, dict]


def load_vocabulary(path: Path = LAYOUTS_FILE) -> Vocabulary:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return Vocabulary(layouts=raw["layouts"], modifiers=raw["modifiers"])


@dataclass
class RawSlide:
    text: str
    start_line: int
    notes: str = ""
    attributes: dict[str, str] = field(default_factory=dict)


@dataclass
class RenderedSlide:
    slide_id: str
    layout: str
    modifiers: list[str]
    html: str
    notes_html: str
    start_line: int


@dataclass
class RenderedDeck:
    module: str
    language: str
    slides: list[RenderedSlide]
    problems: list[Problem]
    links: list[LinkReference] = field(default_factory=list)


def split_slides(body: str, first_line: int) -> list[RawSlide]:
    """Splits on a lone '---' line between blank lines, never inside fenced code."""
    lines = body.split("\n")
    slides: list[RawSlide] = []
    current: list[str] = []
    current_start = first_line
    fence_marker: str | None = None
    for index, line in enumerate(lines):
        fence_match = FENCE_OPENING.match(line)
        if fence_marker is None and fence_match:
            fence_marker = fence_match.group("marker")
        elif fence_marker is not None and line.strip().startswith(fence_marker[0] * len(fence_marker)) \
                and set(line.strip()) == {fence_marker[0]}:
            fence_marker = None
        is_separator = (
            fence_marker is None and line.strip() == "---"
            and (index == 0 or not lines[index - 1].strip())
            and (index + 1 == len(lines) or not lines[index + 1].strip())
        )
        if is_separator:
            slides.append(RawSlide("\n".join(current), current_start))
            current = []
            current_start = first_line + index + 1
        else:
            current.append(line)
    slides.append(RawSlide("\n".join(current), current_start))
    return [split_notes_and_attributes(slide) for slide in slides if slide.text.strip()]


def split_notes_and_attributes(slide: RawSlide) -> RawSlide:
    lines = slide.text.split("\n")
    fence_marker: str | None = None
    for index, line in enumerate(lines):
        fence_match = FENCE_OPENING.match(line)
        if fence_marker is None and fence_match:
            fence_marker = fence_match.group("marker")
            continue
        if fence_marker is not None:
            if set(line.strip()) == {fence_marker[0]} and len(line.strip()) >= len(fence_marker):
                fence_marker = None
            continue
        if (notes_match := NOTES_MARKER.match(line)):
            slide.notes = "\n".join([notes_match.group("rest"), *lines[index + 1:]]).strip()
            lines = lines[:index]
            break
    content_lines = []
    for line in lines:
        if (comment := SLIDE_COMMENT.match(line)) and not slide.attributes:
            slide.attributes = {m.group("name"): m.group("value") for m in SLIDE_ATTRIBUTE.finditer(comment.group("attributes"))}
        else:
            content_lines.append(line)
    slide.text = "\n".join(content_lines).strip("\n")
    return slide


def count_words_and_bullets(text: str) -> tuple[int, int]:
    words = bullets = 0
    in_fence = False
    for line in text.split("\n"):
        if FENCE_OPENING.match(line):
            in_fence = not in_fence
            continue
        if in_fence or line.lstrip().startswith(("<!--", ":::")):
            continue
        if BULLET_LINE.match(line):
            bullets += 1
        visible = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
        visible = re.sub(r"\]\([^)]*\)", "]", visible)
        words += len(re.findall(r"\w+", visible))
    return words, bullets


def render_deck(deck: Deck, model: ContentModel, vocabulary: Vocabulary) -> RenderedDeck:
    ui = model.languages[deck.language].ui
    problems: list[Problem] = []
    source_label = repo_relative(deck.source_file)
    rendered: list[RenderedSlide] = []
    links: list[LinkReference] = []
    seen_ids: set[str] = set()
    for raw in split_slides(deck.body, deck.body_start_line):
        slide_id = raw.attributes.get("id", "")
        if not SLIDE_ID.match(slide_id):
            problems.append(Problem("error", source_label, raw.start_line, "slide-id",
                                    f"every slide needs an ascii kebab-case id; got {slide_id!r}"))
            slide_id = slide_id or f"slide-{len(rendered) + 1}"
        if slide_id in seen_ids:
            problems.append(Problem("error", source_label, raw.start_line, "slide-id-duplicate",
                                    f"duplicate slide id {slide_id!r}"))
        seen_ids.add(slide_id)
        unknown_attributes = set(raw.attributes) - {"id", "class"}
        if unknown_attributes:
            problems.append(Problem("error", source_label, raw.start_line, "slide-attribute",
                                    f"only id and class are allowed on slides; got {sorted(unknown_attributes)}"))
        classes = raw.attributes.get("class", "").split()
        layouts = [name for name in classes if name in vocabulary.layouts]
        modifiers = [name for name in classes if name in vocabulary.modifiers]
        unknown_classes = [name for name in classes if name not in vocabulary.layouts and name not in vocabulary.modifiers]
        if unknown_classes:
            problems.append(Problem("error", source_label, raw.start_line, "slide-class",
                                    f"classes not in engine/theme/layouts.yaml: {unknown_classes}"))
        if len(layouts) > 1:
            problems.append(Problem("error", source_label, raw.start_line, "slide-layouts",
                                    f"one layout per slide; got {layouts}"))
        layout = layouts[0] if layouts else DEFAULT_LAYOUT
        layout_spec = vocabulary.layouts[layout]
        expected_regions = int(layout_spec.get("regions", 0))
        region_count = len(re.findall(r"^###\s", raw.text, flags=re.MULTILINE))
        if expected_regions and not 2 <= region_count <= max(expected_regions, 2):
            problems.append(Problem("warning", source_label, raw.start_line, "slide-regions",
                                    f"layout {layout} expects up to {expected_regions} ### regions; found {region_count}"))
        words, bullets = count_words_and_bullets(raw.text)
        if words > int(layout_spec.get("max_words", 10_000)):
            problems.append(Problem("warning", source_label, raw.start_line, "slide-words",
                                    f"{words} words exceeds {layout_spec['max_words']} for layout {layout}"))
        if bullets > int(layout_spec.get("max_bullets", 10_000)):
            problems.append(Problem("warning", source_label, raw.start_line, "slide-bullets",
                                    f"{bullets} bullets exceeds {layout_spec['max_bullets']} for layout {layout}"))
        context = RenderContext(
            model=model, language=deck.language, source_file=deck.source_file, ui=ui,
            line_offset=raw.start_line - 1, slide_mode=True, slide_regions=expected_regions > 0,
            slide_fragments="fragments" in modifiers,
        )
        html = render_markdown(raw.text, context).html
        notes_context = RenderContext(model=model, language=deck.language, source_file=deck.source_file, ui=ui,
                                      line_offset=raw.start_line - 1, slide_mode=True)
        notes_html = render_markdown(raw.notes, notes_context).html if raw.notes else ""
        problems.extend(context.problems)
        problems.extend(notes_context.problems)
        links.extend(context.links)
        rendered.append(RenderedSlide(slide_id, layout, modifiers, html, notes_html, raw.start_line))
    return RenderedDeck(deck.module, deck.language, rendered, problems, links)


def section_html(module: str, slide: RenderedSlide) -> str:
    classes = " ".join([f"layout-{slide.layout}", *(f"is-{modifier}" for modifier in slide.modifiers)])
    notes = f'\n<aside class="notes">{slide.notes_html}</aside>' if slide.notes_html else ""
    return (f'<section id="{module}--{slide.slide_id}" class="{classes}" data-module="{module}">\n'
            f'<div class="slide-body">\n{slide.html}</div>{notes}\n</section>')


def module_title_section(module: str, title: str, description: str, kicker: str) -> str:
    description_html = f'<p class="subtitle">{escapeHtml(description)}</p>' if description else ""
    return (f'<section id="{module}--inicio" class="layout-section is-module-title" data-module="{module}">\n'
            f'<div class="slide-body"><p class="kicker">{escapeHtml(kicker)}</p>'
            f'<h2>{escapeHtml(title)}</h2>{description_html}</div>\n</section>')
