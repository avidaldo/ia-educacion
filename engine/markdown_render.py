"""The Markdown dialect shared by pages and slides: markdown-it + GFM, localised alerts, chats, resolved links and images."""

import re
import shlex
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

from markdown_it import MarkdownIt
from markdown_it.common.utils import escapeHtml
from markdown_it.rules_core import StateCore
from markdown_it.token import Token
from mdit_py_plugins.attrs import attrs_block_plugin, attrs_plugin
from mdit_py_plugins.container import container_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.gfm import gfm_plugin
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

from content_model import ASSETS_DIR, CONTENT_DIR, ContentModel, Problem, repo_relative

ALLOWED_ATTRIBUTES = ("id", "class", "alt", "width", "loading")
CONTENT_IMAGE_CLASSES = {"narrow", "wide", "border"}
EXTERNAL_LINK = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
PLAIN_FENCE_LANGUAGES = {"", "text", "plain", "gift", "aiken", "prompt"}
CODE_FORMATTER = HtmlFormatter(cssclass="highlight", wrapcode=True)


@dataclass
class Heading:
    level: int
    text: str
    id: str


@dataclass
class LinkReference:
    source: str
    line: int
    target_page: str | None
    anchor: str | None


@dataclass
class ImageReference:
    source: str
    line: int
    asset_path: Path | None
    alt: str


@dataclass
class RenderContext:
    model: ContentModel
    language: str
    source_file: Path
    ui: dict
    line_offset: int = 0
    inherited_heading_ids: list[str] | None = None
    slide_mode: bool = False
    slide_regions: bool = False
    slide_fragments: bool = False
    headings: list[Heading] = field(default_factory=list)
    links: list[LinkReference] = field(default_factory=list)
    images: list[ImageReference] = field(default_factory=list)
    problems: list[Problem] = field(default_factory=list)
    has_mermaid: bool = False

    @property
    def source_label(self) -> str:
        return repo_relative(self.source_file)

    def line_of(self, token: Token | None) -> int:
        return (token.map[0] if token is not None and token.map else 0) + self.line_offset + 1

    def problem(self, level: str, token: Token | None, code: str, message: str) -> None:
        self.problems.append(Problem(level, self.source_label, self.line_of(token), code, message))


@dataclass
class RenderedMarkdown:
    html: str
    context: RenderContext


def slugify(text: str) -> str:
    """GitHub-style ids: lower case, accents kept, punctuation dropped, spaces to hyphens."""
    lowered = text.strip().lower()
    without_punctuation = re.sub(r"[^\w\s-]", "", lowered)
    return re.sub(r"\s+", "-", without_punctuation).strip("-")


def ui_text(ui: dict, *keys: str, default: str = "") -> str:
    value: object = ui
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return str(value)


def plain_text(inline_token: Token) -> str:
    return "".join(child.content for child in inline_token.children or [] if child.type in ("text", "code_inline"))


def parse_container_params(info: str) -> tuple[list[str], dict[str, str]]:
    words = shlex.split(info.strip())[1:]
    flags = [word for word in words if "=" not in word]
    params = dict(word.split("=", 1) for word in words if "=" in word)
    return flags, params


def find_closing(tokens: list[Token], opening_index: int) -> int:
    opening_type = tokens[opening_index].type
    closing_type = opening_type.removesuffix("_open") + "_close"
    depth = 0
    for index in range(opening_index, len(tokens)):
        if tokens[index].type == opening_type:
            depth += 1
        elif tokens[index].type == closing_type:
            depth -= 1
            if depth == 0:
                return index
    return -1


def render_chat(renderer, tokens: list[Token], index: int, options, env: dict) -> str:
    token = tokens[index]
    if token.nesting == -1:
        return "</figure>\n"
    _, params = parse_container_params(token.info)
    meta = " · ".join(escapeHtml(params[key]) for key in ("model", "date") if params.get(key))
    caption = f'<figcaption class="chat-meta">{meta}</figcaption>\n' if meta else ""
    return f'<figure class="chat">\n{caption}'


def make_message_renderer(role: str):
    def render_message(renderer, tokens: list[Token], index: int, options, env: dict) -> str:
        token = tokens[index]
        context: RenderContext = env["context"]
        if token.nesting == -1:
            return "</div></details>\n" if token.meta.get("collapsed") else "</div></div>\n"
        flags, _ = parse_container_params(token.info)
        role_label = escapeHtml(ui_text(context.ui, "chat", role, default=role))
        if "collapsed" in flags:
            closing_index = find_closing(tokens, index)
            if closing_index != -1:
                tokens[closing_index].meta["collapsed"] = True
            expand_label = escapeHtml(ui_text(context.ui, "chat", "expand"))
            return (f'<details class="chat-message chat-{role}"><summary class="chat-role">{role_label}'
                    f' <span class="chat-expand">{expand_label}</span></summary>\n<div class="chat-body">\n')
        return f'<div class="chat-message chat-{role}"><div class="chat-role">{role_label}</div>\n<div class="chat-body">\n'
    return render_message


def render_fence(renderer, tokens: list[Token], index: int, options, env: dict) -> str:
    token = tokens[index]
    context: RenderContext = env["context"]
    language = token.info.strip().split(" ")[0].lower() if token.info else ""
    if language == "mermaid":
        context.has_mermaid = True
        return f'<pre class="mermaid">{escapeHtml(token.content)}</pre>\n'
    label = ui_text(context.ui, "labels", "prompt") if language in ("text", "prompt") else language.upper()
    label_attribute = f' data-label="{escapeHtml(label)}"' if label else ""
    if language not in PLAIN_FENCE_LANGUAGES:
        try:
            lexer = get_lexer_by_name(language)
        except ClassNotFound:
            lexer = None
        if lexer is not None:
            highlighted = highlight(token.content, lexer, CODE_FORMATTER)
            return f'<div class="code-block" data-lang="{escapeHtml(language)}"{label_attribute}>{highlighted}</div>\n'
    return (f'<div class="code-block" data-lang="{escapeHtml(language or "text")}"{label_attribute}>'
            f'<pre><code>{escapeHtml(token.content)}</code></pre></div>\n')


def localise_alerts(tokens: list[Token], context: RenderContext) -> list[Token]:
    kept: list[Token] = []
    skip_until = -1
    for index, token in enumerate(tokens):
        if index <= skip_until:
            continue
        kept.append(token)
        if token.type != "alert_title_open":
            continue
        alert_open = next((candidate for candidate in reversed(kept) if candidate.type == "alert_open"), None)
        kind = str(alert_open.meta.get("kind", "") if alert_open else "").lower()
        title_inline = tokens[index + 1]
        label = ui_text(context.ui, "alerts", kind, default=kind.capitalize())
        title_inline.children = [make_text_token(label)]
        title_inline.content = label
        paragraph_index = index + 3
        if paragraph_index + 2 < len(tokens) and tokens[paragraph_index].type == "paragraph_open":
            body_inline = tokens[paragraph_index + 1]
            promoted = split_leading_strong(body_inline)
            if promoted is not None:
                title_children, remaining = promoted
                title_inline.children = title_children
                title_inline.content = "".join(child.content for child in title_children)
                body_inline.children = remaining
                if not remaining:
                    kept.append(tokens[index + 1])
                    kept.append(tokens[index + 2])
                    skip_until = paragraph_index + 2
    return kept


def make_text_token(content: str) -> Token:
    token = Token("text", "", 0)
    token.content = content
    return token


def split_leading_strong(inline_token: Token) -> tuple[list[Token], list[Token]] | None:
    children = [child for child in inline_token.children or [] if not (child.type == "text" and not child.content)]
    if not children or children[0].type != "strong_open":
        return None
    closing = next((i for i, child in enumerate(children) if child.type == "strong_close"), -1)
    if closing == -1:
        return None
    rest = children[closing + 1:]
    if rest and rest[0].type not in ("softbreak", "hardbreak"):
        return None
    return children[1:closing], rest[1:] if rest else []


def assign_heading_ids(tokens: list[Token], context: RenderContext) -> None:
    used: dict[str, int] = {}
    inherited = context.inherited_heading_ids
    heading_positions = [i for i, token in enumerate(tokens) if token.type == "heading_open"]
    use_inherited = inherited is not None and len(inherited) == len(heading_positions)
    if inherited is not None and not use_inherited:
        context.problem("warning", None, "heading-parity",
                        f"{len(heading_positions)} headings here vs {len(inherited)} in the source page: anchors not aligned")
    for position, index in enumerate(heading_positions):
        token = tokens[index]
        text = plain_text(tokens[index + 1])
        heading_id = token.attrGet("id")
        if not heading_id:
            heading_id = inherited[position] if use_inherited else slugify(text)
            count = used.get(heading_id, 0)
            used[heading_id] = count + 1
            if count:
                heading_id = f"{heading_id}-{count}"
            token.attrSet("id", heading_id)
        context.headings.append(Heading(int(token.tag[1]), text, str(heading_id)))
        if token.tag == "h1" and not context.slide_mode:
            context.problem("warning", token, "body-h1", "the page title comes from front matter; start the body at ##")


def resolve_relative(context: RenderContext, target: str) -> Path:
    return (context.source_file.parent / target).resolve()


def content_relative_page(path: Path, model: ContentModel) -> str | None:
    for language in model.config.languages:
        language_dir = (CONTENT_DIR / language).resolve()
        if path.is_relative_to(language_dir):
            return path.relative_to(language_dir).as_posix()
    return None


def rewrite_links_and_images(tokens: list[Token], context: RenderContext) -> None:
    model = context.model
    source_pages = model.languages[model.config.source_language].pages
    for block_token in tokens:
        for token in block_token.children or []:
            if token.type == "link_open":
                rewrite_link(token, block_token, context, source_pages)
            elif token.type == "image":
                rewrite_image(token, block_token, context)


def rewrite_link(token: Token, block_token: Token, context: RenderContext, source_pages: dict) -> None:
    href = str(token.attrGet("href") or "")
    if context.slide_mode:
        token.attrSet("target", "_blank")
    if EXTERNAL_LINK.match(href):
        token.attrSet("rel", "noopener")
        return
    if href.startswith("#"):
        context.links.append(LinkReference(context.source_label, context.line_of(block_token), None, href[1:]))
        if context.slide_mode:
            context.problem("warning", block_token, "slide-anchor-link", "slide links must point to a page, not to #anchor")
        return
    path_part, _, anchor = href.partition("#")
    if not path_part.endswith(".md"):
        context.problem("error", block_token, "link-not-md", f"internal link must point to a .md source file: {href}")
        return
    relative_page = content_relative_page(resolve_relative(context, path_part), context.model)
    if relative_page is None or relative_page not in source_pages:
        context.problem("error", block_token, "broken-link", f"link target does not exist: {href}")
        return
    context.links.append(LinkReference(context.source_label, context.line_of(block_token), relative_page, anchor or None))
    url = context.model.url_for(context.language, relative_page)
    token.attrSet("href", url + (f"#{anchor}" if anchor else ""))


def rewrite_image(token: Token, block_token: Token, context: RenderContext) -> None:
    source = str(token.attrGet("src") or "")
    alt = "".join(child.content for child in token.children or [])
    if EXTERNAL_LINK.match(source):
        context.problem("error", block_token, "external-image", f"images must be local assets: {source}")
        return
    asset_path = resolve_relative(context, source)
    assets_root = ASSETS_DIR.resolve()
    if not asset_path.is_relative_to(assets_root) or not asset_path.exists():
        context.problem("error", block_token, "missing-asset", f"image not found under content/assets: {source}")
        context.images.append(ImageReference(context.source_label, context.line_of(block_token), None, alt))
        return
    variant = asset_path.with_name(f"{asset_path.stem}.{context.language}{asset_path.suffix}")
    if context.language != context.model.config.source_language and variant.exists():
        asset_path = variant
    context.images.append(ImageReference(context.source_label, context.line_of(block_token), asset_path, alt))
    token.attrSet("src", context.model.config.base_path + "assets/" + asset_path.relative_to(assets_root).as_posix())
    token.attrSet("loading", "lazy")
    token.attrSet("decoding", "async")
    unknown_classes = set(str(token.attrGet("class") or "").split()) - CONTENT_IMAGE_CLASSES
    if unknown_classes:
        context.problem("error", block_token, "image-class", f"unknown image classes: {sorted(unknown_classes)}")


def wrap_slide_regions(tokens: list[Token], context: RenderContext) -> list[Token]:
    if not context.slide_regions:
        return tokens
    region_class = "region fragment" if context.slide_fragments else "region"
    wrapped: list[Token] = []
    open_region = False
    for token in tokens:
        if token.type == "heading_open" and token.tag == "h3" and token.level == 0:
            if open_region:
                wrapped.append(make_html_block("</div>\n"))
            wrapped.append(make_html_block(f'<div class="{region_class}">\n'))
            open_region = True
        wrapped.append(token)
    if open_region:
        wrapped.append(make_html_block("</div>\n"))
    return wrapped


def mark_list_fragments(tokens: list[Token], context: RenderContext) -> None:
    if not context.slide_fragments or context.slide_regions:
        return
    for token in tokens:
        if token.type == "list_item_open" and token.level == 1:
            token.attrJoin("class", "fragment")


def make_html_block(content: str) -> Token:
    token = Token("html_block", "", 0)
    token.content = content
    return token


def postprocess(state: StateCore) -> None:
    context: RenderContext | None = state.env.get("context")
    if context is None:
        return
    tokens = localise_alerts(state.tokens, context)
    assign_heading_ids(tokens, context)
    rewrite_links_and_images(tokens, context)
    mark_list_fragments(tokens, context)
    state.tokens = wrap_slide_regions(tokens, context)


def make_markdown() -> MarkdownIt:
    markdown = MarkdownIt("commonmark", {"html": True, "typographer": False}).use(gfm_plugin, front_matter=True)
    markdown.use(attrs_plugin, allowed=ALLOWED_ATTRIBUTES).use(attrs_block_plugin, allowed=ALLOWED_ATTRIBUTES)
    markdown.use(deflist_plugin)
    markdown.use(container_plugin, name="chat", render=render_chat)
    markdown.use(container_plugin, name="user", render=make_message_renderer("user"))
    markdown.use(container_plugin, name="assistant", render=make_message_renderer("assistant"))
    markdown.add_render_rule("fence", render_fence)
    markdown.core.ruler.after("inline", "ia_edu_postprocess", postprocess)
    return markdown


MARKDOWN = make_markdown()


def render_markdown(text: str, context: RenderContext) -> RenderedMarkdown:
    if re.search(r"\bstyle\s*=", strip_fenced_code(text)):
        context.problem("error", None, "inline-style", "style= is not allowed in content; use the theme's classes")
    html = MARKDOWN.render(text, {"context": context})
    return RenderedMarkdown(html, context)


def strip_fenced_code(text: str) -> str:
    return re.sub(r"^(```|~~~).*?^\1\s*$", "", text, flags=re.MULTILINE | re.DOTALL)


def pygments_css() -> str:
    light = HtmlFormatter(style="default").get_style_defs(".highlight")
    dark = HtmlFormatter(style="github-dark").get_style_defs(":root[data-theme='dark'] .highlight")
    return f"/* Generated by the build from Pygments. */\n{light}\n{dark}\n"


def module_of(relative_path: str) -> str | None:
    parts = PurePosixPath(relative_path).parts
    return parts[0] if len(parts) > 1 else None
