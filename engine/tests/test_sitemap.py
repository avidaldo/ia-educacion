"""The sitemap lists what each language really has, and links translations to each other."""

import xml.etree.ElementTree as ElementTree

from build import sitemap_xml
from content_model import load_content

SITEMAP = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
XHTML = "{http://www.w3.org/1999/xhtml}"


def alternates_by_page(config, content_dir) -> dict[str, dict[str, str]]:
    root = ElementTree.fromstring(sitemap_xml(load_content(config, content_dir)))
    return {entry.find(f"{SITEMAP}loc").text: {link.get("hreflang"): link.get("href")
                                               for link in entry.findall(f"{XHTML}link")}
            for entry in root.findall(f"{SITEMAP}url")}


def test_untranslated_pages_are_listed_only_in_their_own_language(config, content_dir):
    pages = alternates_by_page(config, content_dir)
    assert set(pages) == {
        "https://example.org/sitio/", "https://example.org/sitio/prompts/",
        "https://example.org/sitio/prompts/ejemplos/", "https://example.org/sitio/tests-moodle/",
        "https://example.org/sitio/gl/prompts/",
        "https://example.org/sitio/presentacion/", "https://example.org/sitio/gl/presentacion/",
    }
    assert pages["https://example.org/sitio/prompts/ejemplos/"] == {"es": "https://example.org/sitio/prompts/ejemplos/"}


def test_translations_point_at_each_other(config, content_dir):
    pages = alternates_by_page(config, content_dir)
    both = {"es": "https://example.org/sitio/prompts/", "gl": "https://example.org/sitio/gl/prompts/"}
    assert pages["https://example.org/sitio/prompts/"] == both
    assert pages["https://example.org/sitio/gl/prompts/"] == both
