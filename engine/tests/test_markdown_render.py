from content_model import load_content
from markdown_render import RenderContext, render_markdown, slugify


def render(model, text, language="es", source="prompts/index.md", **options):
    source_file = model.languages[language].pages[source].source_file
    context = RenderContext(model=model, language=language, source_file=source_file,
                            ui=model.languages[language].ui, **options)
    return render_markdown(text, context).html, context


def codes(context):
    return {problem.code for problem in context.problems}


def test_alert_title_is_localised(config, content_dir):
    model = load_content(config, content_dir)
    html, _ = render(model, "> [!TIP]\n> Texto.\n", language="gl")
    assert '<p class="markdown-alert-title">Consello</p>' in html


def test_leading_bold_line_becomes_the_alert_title(config, content_dir):
    model = load_content(config, content_dir)
    html, _ = render(model, "> [!WARNING]\n> **Ojo con esto**\n> Detalle.\n")
    assert '<p class="markdown-alert-title">Ojo con esto</p>' in html
    assert "<strong>" not in html
    assert "Detalle." in html


def test_bold_only_alert_body_leaves_no_empty_paragraph(config, content_dir):
    model = load_content(config, content_dir)
    html, _ = render(model, "> [!TIP]\n> **Solo título**\n")
    assert "<p></p>" not in html


def test_unknown_alert_kind_stays_a_blockquote(config, content_dir):
    model = load_content(config, content_dir)
    html, _ = render(model, "> [!FOO]\n> Texto.\n")
    assert "<blockquote>" in html


def test_chat_container_renders_messages_and_collapsed_replies(config, content_dir):
    model = load_content(config, content_dir)
    text = (":::: chat model=\"ChatGPT\" date=2025-04-25\n::: user\nHola\n:::\n"
            "::: assistant collapsed\nAdiós\n:::\n::::\n")
    html, _ = render(model, text)
    assert '<figure class="chat">' in html and "ChatGPT · 2025-04-25" in html
    assert '<div class="chat-message chat-user"><div class="chat-role">Docente</div>' in html
    assert '<details class="chat-message chat-assistant">' in html and "</div></details>" in html


def test_source_links_become_urls_in_the_rendering_language(config, content_dir):
    model = load_content(config, content_dir)
    html, context = render(model, "[a](ejemplos.md#uno) [b](../tests-moodle/index.md)", language="gl")
    assert 'href="/sitio/gl/prompts/ejemplos/#uno"' in html
    assert 'href="/sitio/gl/tests-moodle/"' in html
    assert [(link.target_page, link.anchor) for link in context.links] == [
        ("prompts/ejemplos.md", "uno"), ("tests-moodle/index.md", None)]


def test_broken_and_non_markdown_internal_links_are_errors(config, content_dir):
    model = load_content(config, content_dir)
    _, context = render(model, "[a](no-existe.md) [b](../tests-moodle/)")
    assert {"broken-link", "link-not-md"} <= codes(context)


def test_images_resolve_to_assets_with_language_variants(config, content_dir):
    model = load_content(config, content_dir)
    text = "![Captura](../../assets/prompts/captura.webp){.narrow}"
    html_es, _ = render(model, text)
    html_gl, _ = render(model, text, language="gl")
    assert 'src="/sitio/assets/prompts/captura.webp"' in html_es and 'class="narrow"' in html_es
    assert 'src="/sitio/assets/prompts/captura.gl.webp"' in html_gl


def test_missing_image_and_unknown_image_class_are_errors(config, content_dir):
    model = load_content(config, content_dir)
    _, missing = render(model, "![x](../../assets/prompts/nada.webp)")
    _, styled = render(model, "![x](../../assets/prompts/captura.webp){.gigante}")
    assert "missing-asset" in codes(missing)
    assert "image-class" in codes(styled)


def test_inline_style_is_rejected_outside_code_only(config, content_dir):
    model = load_content(config, content_dir)
    _, prose = render(model, '<span style="color:red">x</span>\n')
    _, fenced = render(model, '```html\n<span style="color:red">x</span>\n```\n')
    assert "inline-style" in codes(prose)
    assert "inline-style" not in codes(fenced)


def test_heading_ids_keep_accents_and_deduplicate(config, content_dir):
    model = load_content(config, content_dir)
    html, context = render(model, "## Diseño de *prompts*\n\n## Diseño de *prompts*\n")
    assert [heading.id for heading in context.headings] == ["diseño-de-prompts", "diseño-de-prompts-1"]
    assert 'id="diseño-de-prompts"' in html


def test_translated_headings_inherit_the_source_ids(config, content_dir):
    model = load_content(config, content_dir)
    _, context = render(model, "## Que é\n\n## Outro\n", language="gl", inherited_heading_ids=["que-es", "otro"])
    assert [heading.id for heading in context.headings] == ["que-es", "otro"]
    _, mismatched = render(model, "## Só un\n", language="gl", inherited_heading_ids=["que-es", "otro"])
    assert "heading-parity" in codes(mismatched)


def test_template_braces_and_mermaid_pass_through(config, content_dir):
    model = load_content(config, content_dir)
    html, context = render(model, "Expresión n8n: `{{ $json.nombre }}`\n\n```mermaid\ngraph TD; A-->B\n```\n")
    assert "{{ $json.nombre }}" in html
    assert '<pre class="mermaid">graph TD; A--&gt;B\n</pre>' in html
    assert context.has_mermaid


def test_text_fences_are_labelled_as_prompts(config, content_dir):
    model = load_content(config, content_dir)
    html, _ = render(model, "```text\nHola\n```\n")
    assert 'data-lang="text" data-label="Prompt"' in html


def test_slugify_drops_punctuation():
    assert slugify("*Metaprompting*: pedirle a la IA") == "metaprompting-pedirle-a-la-ia"


def test_problems_report_the_file_line(config, content_dir):
    model = load_content(config, content_dir)
    _, context = render(model, "Texto.\n\n[roto](nada.md)\n", line_offset=4)
    assert [problem.line for problem in context.problems if problem.code == "broken-link"] == [7]


def test_broken_anchor_is_found_by_validation(config, content_dir):
    from build import render_decks, render_pages
    from validation import validate_rendered
    (content_dir / "es" / "tests-moodle" / "index.md").write_text(
        "---\ntitle: M\n---\n## GIFT\n\n[ok](../prompts/index.md#qué-es-un-prompt) [mal](../prompts/index.md#no-existe)\n",
        encoding="utf-8")
    model = load_content(config, content_dir)
    problems = []
    rendered = render_pages(model, problems)
    found = validate_rendered(model, rendered, render_decks(model, problems))
    assert [problem.message for problem in found if problem.code == "broken-anchor"] == [
        "#no-existe is not a heading of prompts/index.md (es)"]
