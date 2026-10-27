"""The annex on the Xunta training deck must account for every content page of that deck, in both languages."""
import re
from pathlib import Path

import pytest

CONTENT_DIR = Path(__file__).resolve().parents[2] / "content"
ANNEX = "etica-legal/anexo-formacion-xunta.md"
# Pages 1, 2 and 74 are the cover, the index and the closing slide: nothing to map.
CONTENT_PAGES = set(range(3, 74))
PAGE_RANGE = re.compile(r"^(\d+)(?:[–-](\d+))?$")


def covered_pages(annex: Path) -> set[int]:
    pages: set[int] = set()
    for line in annex.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 4 and (match := PAGE_RANGE.match(cells[1])):
            first, last = int(match[1]), int(match[2] or match[1])
            pages.update(range(first, last + 1))
    return pages


@pytest.mark.parametrize("language", ["es", "gl"])
def test_annex_maps_every_content_page_of_the_deck(language):
    annex = CONTENT_DIR / language / ANNEX
    if language != "es" and not annex.exists():
        pytest.skip("translation not written yet")
    missing = sorted(CONTENT_PAGES - covered_pages(annex))
    assert not missing, f"{language}: deck pages without a row in the annex table: {missing}"
