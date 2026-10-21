import textwrap

from content_model import Deck, load_content
from slides_render import load_vocabulary, render_deck, section_html, split_slides


def make_deck(model, body: str) -> Deck:
    source_file = model.languages["es"].pages["prompts/index.md"].source_file.with_name("slides.md")
    return Deck("es", "prompts", source_file, {}, textwrap.dedent(body).lstrip("\n"), 3, False)


def test_separator_is_ignored_inside_fences_and_without_blank_lines():
    body = textwrap.dedent("""
        <!-- .slide: id="a" -->
        ## A

        ```yaml
        x: 1

        ---

        y: 2
        ```

        ---

        <!-- .slide: id="b" -->
        Título
        ---
        texto
        """).lstrip("\n")
    slides = split_slides(body, 1)
    assert [slide.attributes["id"] for slide in slides] == ["a", "b"]
    assert "y: 2" in slides[0].text
    assert "Título\n---" in slides[1].text


def test_notes_start_at_column_zero_outside_fences():
    body = "<!-- .slide: id=\"a\" -->\n## A\n\n```text\nNotas: esto es un prompt\n```\n\n  Notas: sangrado\n\nNotas:\n**Demo** paso 1\n"
    slide = split_slides(body, 1)[0]
    assert "Notas: esto es un prompt" in slide.text
    assert "Notas: sangrado" in slide.text
    assert slide.notes == "**Demo** paso 1"


def test_rendered_slide_has_namespaced_id_layout_and_notes(config, content_dir):
    model = load_content(config, content_dir)
    deck = make_deck(model, """
        <!-- .slide: id="rol" class="comparison fragments" -->
        ## Rol

        ### Mal
        Uno

        ### Mejor
        Dos

        Notas:
        Comentario
        """)
    rendered = render_deck(deck, model, load_vocabulary())
    assert not [problem for problem in rendered.problems if problem.level == "error"]
    slide = rendered.slides[0]
    html = section_html("prompts", slide)
    assert '<section id="prompts--rol" class="layout-comparison is-fragments" data-module="prompts">' in html
    assert html.count('<div class="region fragment">') == 2
    assert '<aside class="notes"><p>Comentario</p>' in html


def test_list_items_become_fragments_without_regions(config, content_dir):
    model = load_content(config, content_dir)
    deck = make_deck(model, '<!-- .slide: id="a" class="fragments" -->\n## A\n\n- uno\n- dos\n  - anidado\n')
    html = render_deck(deck, model, load_vocabulary()).slides[0].html
    assert html.count('<li class="fragment">') == 2


def test_slide_errors_are_reported(config, content_dir):
    model = load_content(config, content_dir)
    deck = make_deck(model, """
        <!-- .slide: class="bullets inventada" -->
        ## Sin id

        ---

        <!-- .slide: id="x" class="two-col cards" style="color:red" -->
        ## Dos layouts

        ---

        <!-- .slide: id="x" -->
        ## Repetida
        """)
    codes = {problem.code for problem in render_deck(deck, model, load_vocabulary()).problems}
    assert {"slide-id", "slide-class", "slide-layouts", "slide-attribute", "slide-id-duplicate"} <= codes


def test_slide_links_open_in_a_new_tab_and_point_to_pages(config, content_dir):
    model = load_content(config, content_dir)
    deck = make_deck(model, '<!-- .slide: id="a" -->\n## A\n\n[Ejemplos](ejemplos.md)\n')
    html = render_deck(deck, model, load_vocabulary()).slides[0].html
    assert 'href="/sitio/prompts/ejemplos/"' in html and 'target="_blank"' in html
