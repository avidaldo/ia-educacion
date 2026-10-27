"""Local preview: serves engine/_build under the site's base path and rebuilds when content/ or engine/ change."""

import functools
import http.server
import subprocess
import sys
import threading
from collections.abc import Callable
from pathlib import Path

from content_model import CONTENT_DIR, ENGINE_DIR, SiteConfig

WATCHED_DIRS = (CONTENT_DIR, ENGINE_DIR)
IGNORED_PARTS = {"_build", "_screens", "__pycache__", ".pytest_cache", "tests"}


def latest_source_change() -> float:
    newest = 0.0
    for directory in WATCHED_DIRS:
        for path in directory.rglob("*"):
            if path.is_file() and not IGNORED_PARTS.intersection(path.parts):
                newest = max(newest, path.stat().st_mtime)
    return newest


class BasePathHandler(http.server.SimpleHTTPRequestHandler):
    base_path = "/"
    rebuild_if_needed: Callable[[], None] = staticmethod(lambda: None)

    def do_GET(self) -> None:
        if self.path in ("/", "") and self.base_path != "/":
            self.send_response(302)
            self.send_header("Location", self.base_path)
            self.end_headers()
            return
        if not self.path.startswith(self.base_path):
            self.send_error(404, f"outside {self.base_path}")
            return
        if self.path.split("?")[0].endswith(("/", ".html")):
            self.rebuild_if_needed()
        self.path = "/" + self.path.removeprefix(self.base_path)
        super().do_GET()

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, format: str, *args) -> None:
        return


def serve(config: SiteConfig, output_dir: Path, port: int, build_arguments: list[str]) -> int:
    """Each rebuild runs build.py in a fresh interpreter, so changes to the engine itself are picked up too."""
    lock = threading.Lock()
    state = {"built_at": 0.0}
    build_command = [sys.executable, str(ENGINE_DIR / "build.py"), "--out", str(output_dir), *build_arguments]

    def rebuild_if_needed() -> None:
        with lock:
            if latest_source_change() <= state["built_at"]:
                return
            state["built_at"] = latest_source_change()
            subprocess.run(build_command, check=False)

    rebuild_if_needed()
    handler = functools.partial(type("Handler", (BasePathHandler,), {
        "base_path": config.base_path, "rebuild_if_needed": staticmethod(rebuild_if_needed)}),
        directory=str(output_dir))
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
        print(f"Serving http://127.0.0.1:{port}{config.base_path}  (Ctrl+C to stop; rebuilds on change)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0
