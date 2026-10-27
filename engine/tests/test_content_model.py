import datetime

import pytest

from content_model import load_content, slug_path_for, split_front_matter


def test_front_matter_is_split_and_body_line_is_counted():
    front, body, body_start_line = split_front_matter("---\ntitle: T\nreviewed: 2026-01-02\n---\n## A\n")
    assert front == {"title": "T", "reviewed": datetime.date(2026, 1, 2)}
    assert body == "## A\n"
    assert body_start_line == 5


def test_empty_front_matter_and_missing_front_matter():
    assert split_front_matter("---\n---\nx") == ({}, "x", 3)
    assert split_front_matter("x") == ({}, "x", 1)


def test_unclosed_front_matter_is_an_error():
    with pytest.raises(ValueError):
        split_front_matter("---\ntitle: T\n## A\n")


@pytest.mark.parametrize("relative_path, expected", [
    ("index.md", ""), ("prompts/index.md", "prompts/"), ("prompts/ejemplos.md", "prompts/ejemplos/"),
])
def test_slug_paths(relative_path, expected):
    assert slug_path_for(relative_path) == expected


def test_translation_inherits_review_date_and_missing_pages_fall_back(config, content_dir):
    model = load_content(config, content_dir)
    galician = model.languages["gl"]
    assert galician.pages["prompts/index.md"].front["reviewed"] == datetime.date(2026, 4, 30)
    assert not galician.pages["prompts/index.md"].is_fallback
    assert galician.pages["tests-moodle/index.md"].is_fallback
    assert galician.ui["alerts"]["tip"] == "Consello"
    assert galician.ui["alerts"]["warning"] == "Atención"


def test_urls_put_the_source_language_at_the_root(config, content_dir):
    model = load_content(config, content_dir)
    assert model.url_for("es", "prompts/ejemplos.md") == "/sitio/prompts/ejemplos/"
    assert model.url_for("gl", "index.md") == "/sitio/gl/"
    assert model.deck_url("gl", ["prompts", "tests-moodle"]) == "/sitio/gl/presentacion/?m=prompts,tests-moodle"


def test_orphan_translation_and_unlisted_page_are_reported(config, content_dir):
    (content_dir / "gl" / "vieja.md").write_text("---\ntitle: V\n---\n", encoding="utf-8")
    (content_dir / "es" / "suelta.md").write_text("---\ntitle: S\n---\n", encoding="utf-8")
    codes = {problem.code for problem in load_content(config, content_dir).problems}
    assert {"orphan-translation", "not-in-nav"} <= codes


def test_drafts_are_skipped_unless_requested(config, content_dir):
    path = content_dir / "es" / "tests-moodle" / "index.md"
    path.write_text("---\ntitle: M\ndraft: true\n---\n", encoding="utf-8")
    assert "tests-moodle/index.md" not in load_content(config, content_dir).languages["es"].pages
    assert "tests-moodle/index.md" in load_content(config, content_dir, include_drafts=True).languages["es"].pages


def test_reserved_module_slug_is_an_error(config, content_dir):
    (content_dir / "nav.yaml").write_text("sections:\n  - id: x\n    modules: [assets]\n", encoding="utf-8")
    problems = load_content(config, content_dir).problems
    assert any(problem.code == "reserved-slug" and problem.level == "error" for problem in problems)
