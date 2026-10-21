"""Screenshots of decks and pages from engine/_build, with an overflow check on every slide.

Usage: uv run engine/shoot.py [--lang es] [--module prompts ...] [--pages] [--theme light|dark|both] [--out engine/_screens]
Exits 1 when a slide's content does not fit in the slide. Uses the installed Google Chrome through Playwright.
"""

import argparse
import functools
import http.server
import sys
import threading
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

from build import OUTPUT_DIR
from content_model import ENGINE_DIR, load_config, load_content
from serve import BasePathHandler

SCREENS_DIR = ENGINE_DIR / "_screens"
SLIDE_OVERFLOW_SCRIPT = """() => {
  const slide = Reveal.getCurrentSlide();
  const body = slide.querySelector('.slide-body') || slide;
  return {id: slide.id, overflowY: body.scrollHeight - body.clientHeight, overflowX: body.scrollWidth - body.clientWidth};
}"""


def start_static_server(output_dir: Path, base_path: str) -> tuple[http.server.ThreadingHTTPServer, str]:
    handler_class = type("ShootHandler", (BasePathHandler,), {"base_path": base_path})
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(handler_class, directory=str(output_dir)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}"


def shoot_deck(page: Page, origin: str, deck_path: str, module: str, theme: str, out_dir: Path) -> list[str]:
    query = f"?m={module}&frame=1" + ("&theme=dark" if theme == "dark" else "")
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto(origin + deck_path + query)
    page.wait_for_function("() => window.Reveal && Reveal.isReady()")
    total = page.evaluate("() => Reveal.getTotalSlides()")
    overflowing = []
    module_dir = out_dir / module
    module_dir.mkdir(parents=True, exist_ok=True)
    for index in range(total):
        page.evaluate(f"() => {{ Reveal.slide({index}); while (Reveal.nextFragment()) {{}} }}")
        page.wait_for_timeout(450)
        measure = page.evaluate(SLIDE_OVERFLOW_SCRIPT)
        slide_id = measure["id"].removeprefix(f"{module}--")
        page.screenshot(path=module_dir / f"{index + 1:02d}-{slide_id}-{theme}.png")
        if measure["overflowY"] > 2 or measure["overflowX"] > 2:
            overflowing.append(f"{measure['id']}: {measure['overflowY']}px tall, {measure['overflowX']}px wide too much")
    return overflowing


def shoot_pages(page: Page, origin: str, urls: list[str], theme: str, out_dir: Path) -> None:
    for width in (390, 1280):
        page.set_viewport_size({"width": width, "height": 900})
        for url in urls:
            page.goto(origin + url)
            page.evaluate(f"() => {{ document.documentElement.dataset.theme = '{theme}'; }}")
            page.wait_for_timeout(200)
            name = url.strip("/").replace("/", "_") or "home"
            page.screenshot(path=out_dir / f"page-{name}-{width}-{theme}.png", full_page=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lang", default="es")
    parser.add_argument("--module", action="append", help="deck to shoot (repeatable); default: every deck")
    parser.add_argument("--pages", action="store_true", help="also shoot every page at 390 and 1280 px")
    parser.add_argument("--theme", choices=["light", "dark", "both"], default="light")
    parser.add_argument("--out", type=Path, default=SCREENS_DIR)
    arguments = parser.parse_args()

    config = load_config()
    model = load_content(config)
    if not OUTPUT_DIR.exists():
        print("engine/_build does not exist: run uv run engine/build.py first", file=sys.stderr)
        return 2
    modules = arguments.module or sorted(model.languages[arguments.lang].decks)
    themes = ["light", "dark"] if arguments.theme == "both" else [arguments.theme]
    out_dir = arguments.out / arguments.lang
    out_dir.mkdir(parents=True, exist_ok=True)
    server, origin = start_static_server(OUTPUT_DIR, config.base_path)
    deck_path = model.deck_url(arguments.lang)
    overflowing: list[str] = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel="chrome")
            page = browser.new_page(viewport={"width": config.deck_slide_width, "height": config.deck_slide_height})
            for theme in themes:
                for module in modules:
                    overflowing += shoot_deck(page, origin, deck_path, module, theme, out_dir)
                if arguments.pages:
                    urls = [model.url_for(arguments.lang, p.relative_path) for p in model.ordered_pages(arguments.lang)]
                    shoot_pages(page, origin, urls, theme, out_dir)
            browser.close()
    finally:
        server.shutdown()
    for line in overflowing:
        print(f"OVERFLOW {line}")
    print(f"Screens in {out_dir}; {len(overflowing)} overflowing slides")
    return 1 if overflowing else 0


if __name__ == "__main__":
    sys.exit(main())
