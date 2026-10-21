"""A tiny content tree in tmp_path, with the render modules pointed at it."""

import textwrap
from pathlib import Path

import pytest

import content_model
import markdown_render
from content_model import SiteConfig


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip("\n"), encoding="utf-8")


@pytest.fixture
def config() -> SiteConfig:
    return SiteConfig(
        base_path="/sitio/", site_url="https://example.org", languages=["es", "gl"], source_language="es",
        stale_after_months=6, max_image_kib=300, deck_slide_width=1280, deck_slide_height=720,
        mermaid_url="https://example.org/mermaid.mjs",
        reserved_slugs=["gl", "assets", "presentacion"],
    )


@pytest.fixture
def content_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    content = tmp_path / "content"
    write(content / "nav.yaml", """
        sections:
          - id: fundamentos
            modules:
              - prompts: [ejemplos]
              - tests-moodle
        """)
    write(content / "es" / "_ui.yaml", """
        site_title: Sitio
        alerts: {tip: Consejo, warning: Atención}
        chat: {user: Docente, assistant: Asistente, expand: (ver)}
        labels: {prompt: Prompt}
        """)
    write(content / "gl" / "_ui.yaml", """
        alerts: {tip: Consello}
        """)
    write(content / "es" / "index.md", """
        ---
        title: Inicio
        ---
        Hola.
        """)
    write(content / "es" / "prompts" / "index.md", """
        ---
        title: Prompts
        reviewed: 2026-04-30
        ---
        ## Qué es un *prompt*

        Texto.
        """)
    write(content / "es" / "prompts" / "ejemplos.md", """
        ---
        title: Ejemplos
        ---
        ## Uno
        """)
    write(content / "es" / "tests-moodle" / "index.md", """
        ---
        title: Moodle
        ---
        ## GIFT
        """)
    write(content / "gl" / "prompts" / "index.md", """
        ---
        title: Prompts (gl)
        ---
        ## Que é un *prompt*

        Texto.
        """)
    (content / "assets" / "prompts").mkdir(parents=True)
    (content / "assets" / "prompts" / "captura.webp").write_bytes(b"RIFF")
    (content / "assets" / "prompts" / "captura.gl.webp").write_bytes(b"RIFF")
    monkeypatch.setattr(content_model, "CONTENT_DIR", content)
    monkeypatch.setattr(content_model, "ASSETS_DIR", content / "assets")
    monkeypatch.setattr(content_model, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(markdown_render, "CONTENT_DIR", content)
    monkeypatch.setattr(markdown_render, "ASSETS_DIR", content / "assets")
    return content
