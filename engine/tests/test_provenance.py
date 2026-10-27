import subprocess
from pathlib import Path

import pytest

import provenance
from provenance import all_statuses, blob_hash, moves, normalised_bytes, source_diff, stamp


def git(repo: Path, *arguments: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *arguments], check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    git(tmp_path, "init", "-q")
    (tmp_path / ".gitattributes").write_text("* text=auto eol=lf\n")
    content = tmp_path / "content"
    (content / "es" / "prompts").mkdir(parents=True)
    (content / "gl" / "prompts").mkdir(parents=True)
    (content / "nav.yaml").write_text("sections:\n  - id: a\n    modules: [prompts]\n")
    (content / "es" / "_ui.yaml").write_text("site_title: Sitio\n")
    (content / "gl" / "_ui.yaml").write_text("site_title: Sitio\n")
    (content / "es" / "prompts" / "index.md").write_text("---\ntitle: Prompts\nreviewed: 2026-04-30\n---\n## Uno\n\nTexto.\n")
    (content / "gl" / "prompts" / "index.md").write_text("---\ntitle: Prompts\n---\n## Un\n\nTexto.\n")
    monkeypatch.setattr(provenance, "CONTENT_DIR", content)
    monkeypatch.setattr(provenance, "REPO_ROOT", tmp_path)
    return tmp_path


def state_of(path: str) -> str:
    return next(status.state for status in all_statuses() if status.path == path)


def test_blob_hash_matches_git_also_for_crlf_input(repo):
    source = repo / "content" / "es" / "prompts" / "index.md"
    assert blob_hash(normalised_bytes(source)) == git(repo, "hash-object", str(source))
    crlf = repo / "crlf.md"
    crlf.write_bytes(b"linea uno\r\nlinea dos\r\n")
    assert blob_hash(normalised_bytes(crlf)) == git(repo, "hash-object", str(crlf))


def test_bom_is_rejected(repo):
    bom = repo / "bom.md"
    bom.write_bytes(b"\xef\xbb\xbfhola\n")
    with pytest.raises(ValueError):
        normalised_bytes(bom)


def test_stamp_keeps_the_rest_of_the_file_and_quotes_the_hash(repo):
    target = repo / "content" / "gl" / "prompts" / "index.md"
    assert state_of("gl/prompts/index.md") == "unstamped"
    stamp(target, if_trivial=False)
    text = target.read_text()
    expected_hash = blob_hash(normalised_bytes(repo / "content" / "es" / "prompts" / "index.md"))
    assert text.startswith("---\ntitle: Prompts\nderived_from:\n")
    assert f'  es/prompts/index.md: "{expected_hash}"\n---\n## Un\n' in text
    stamp(target, if_trivial=False)
    assert target.read_text() == text
    assert state_of("gl/prompts/index.md") == "up-to-date"


def test_stamp_adds_front_matter_with_a_blank_line_to_a_new_deck(repo):
    deck = repo / "content" / "es" / "prompts" / "slides.md"
    deck.write_text('<!-- .slide: id="uno" -->\n## Uno\n')
    stamp(deck, if_trivial=False)
    text = deck.read_text()
    assert text.startswith("---\nderived_from:\n  es/prompts/index.md: \"")
    assert text.endswith('"\n---\n\n<!-- .slide: id="uno" -->\n## Uno\n')


def test_source_change_makes_it_stale_and_diff_shows_the_change(repo):
    source = repo / "content" / "es" / "prompts" / "index.md"
    target = repo / "content" / "gl" / "prompts" / "index.md"
    stamp(target, if_trivial=False)
    recorded = provenance.read_recorded(target)["es/prompts/index.md"]
    source.write_text(source.read_text().replace("Texto.", "Texto nuevo."))
    assert state_of("gl/prompts/index.md") == "stale"
    diff = source_diff("es/prompts/index.md", recorded)
    assert "-Texto.\n" in diff and "+Texto nuevo.\n" in diff


def test_diff_without_the_old_blob_asks_for_a_full_comparison(repo):
    assert "not in this git repository" in source_diff("es/prompts/index.md", "0" * 40)


def test_if_trivial_stamps_only_non_translatable_changes(repo):
    source = repo / "content" / "es" / "prompts" / "index.md"
    target = repo / "content" / "gl" / "prompts" / "index.md"
    stamp(target, if_trivial=False)
    source.write_text(source.read_text().replace("2026-04-30", "2026-10-22"))
    assert state_of("gl/prompts/index.md") == "trivial"
    assert stamp(target, if_trivial=True) == 0
    assert state_of("gl/prompts/index.md") == "up-to-date"
    source.write_text(source.read_text().replace("Texto.", "Otro texto."))
    assert stamp(target, if_trivial=True) == 1
    assert state_of("gl/prompts/index.md") == "stale"


def test_missing_translation_and_deck_sources(repo):
    deck = repo / "content" / "es" / "prompts" / "slides.md"
    deck.write_text("---\n---\n<!-- .slide: id=\"a\" -->\n## A\n")
    statuses = {status.path: status for status in all_statuses()}
    assert statuses["es/prompts/slides.md"].state == "unstamped"
    assert statuses["es/prompts/slides.md"].changed_sources == ["es/prompts/index.md"]
    assert statuses["gl/prompts/slides.md"].state == "missing"


def test_renamed_source_is_suggested_as_a_move(repo):
    source = repo / "content" / "es" / "prompts" / "index.md"
    target = repo / "content" / "gl" / "prompts" / "index.md"
    stamp(target, if_trivial=False)
    (repo / "content" / "es" / "tecnicas").mkdir()
    source.rename(repo / "content" / "es" / "tecnicas" / "index.md")
    assert moves() == [("gl/prompts/index.md", "gl/tecnicas/index.md")]
