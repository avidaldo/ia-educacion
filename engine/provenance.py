"""Provenance of derived files: Galician pages and decks, and every deck, record the git blob hash of the
Spanish text they were made from (`derived_from`), so the skills can redo only what changed.

Usage:
  uv run engine/provenance.py status [--json]          what is stale, trivial (only non-translatable keys
                                                       changed: just stamp --if-trivial), unstamped or missing
  uv run engine/provenance.py diff <derived-file>      how each source changed since the derived file was made
  uv run engine/provenance.py stamp <derived-file> [--if-trivial]
                                                       record the current source hashes (after updating it)
  uv run engine/provenance.py moves                    orphan translations that look like renamed sources

Paths may be given relative to the repository root or to content/. Hashes are always written by this script.
"""

import argparse
import difflib
import hashlib
import json
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

from content_model import (CONTENT_DIR, DECK_FILE_NAME, INHERITED_KEYS, REPO_ROOT, load_config, load_nav,
                           split_front_matter)

UI_FILE_NAME = "_ui.yaml"
NON_TRANSLATABLE_KEYS = {*INHERITED_KEYS, "derived_from"}


def normalised_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"{path} starts with a UTF-8 BOM; save it without one")
    return data.replace(b"\r\n", b"\n")


def blob_hash(data: bytes) -> str:
    """The id git gives this content as a blob: the same with or without git, committed or not."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def content_key(path: Path) -> str:
    return path.resolve().relative_to(CONTENT_DIR.resolve()).as_posix()


def resolve_argument(argument: str) -> Path:
    candidate = Path(argument)
    for base in (Path.cwd(), REPO_ROOT, CONTENT_DIR):
        if (base / candidate).exists():
            return (base / candidate).resolve()
    raise SystemExit(f"no such file: {argument}")


@dataclass
class DerivedFile:
    path: str
    kind: str  # "translation", "deck", "deck-translation", "ui-translation"
    default_sources: list[str]
    recorded: dict[str, str] = field(default_factory=dict)

    @property
    def sources(self) -> list[str]:
        return list(self.recorded) if self.recorded else self.default_sources


@dataclass
class Status:
    path: str
    kind: str
    state: str  # "up-to-date", "trivial", "stale", "unstamped", "missing"
    changed_sources: list[str]


def read_recorded(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if path.name == UI_FILE_NAME:
        front = yaml.safe_load(text) or {}
    else:
        front = split_front_matter(text)[0]
    recorded = front.get("derived_from") or {}
    return {str(key): str(value) for key, value in recorded.items()}


def module_source_pages(module: str) -> list[str]:
    nav = load_nav(CONTENT_DIR, [])
    for section in nav:
        for nav_module in section.modules:
            if nav_module.slug == module:
                return [f"es/{module}/index.md", *(f"es/{module}/{sub}.md" for sub in nav_module.subpages)]
    return [f"es/{module}/index.md"]


def derived_files(source_language: str, target_languages: list[str]) -> list[DerivedFile]:
    """Every file that should exist as a derivation of Spanish text, whether it exists yet or not."""
    source_dir = CONTENT_DIR / source_language
    derived: list[DerivedFile] = []
    for deck in sorted(source_dir.glob(f"*/{DECK_FILE_NAME}")):
        key = content_key(deck)
        existing = [page for page in module_source_pages(deck.parent.name) if (CONTENT_DIR / page).exists()]
        derived.append(DerivedFile(key, "deck", existing, read_recorded(deck)))
    for language in target_languages:
        for source in sorted(source_dir.rglob("*.md")):
            source_key = content_key(source)
            target = CONTENT_DIR / language / source.relative_to(source_dir)
            kind = "deck-translation" if source.name == DECK_FILE_NAME else "translation"
            derived.append(DerivedFile(content_key(target) if target.exists() else f"{language}/{source.relative_to(source_dir).as_posix()}",
                                       kind, [source_key], read_recorded(target)))
        ui_target = CONTENT_DIR / language / UI_FILE_NAME
        derived.append(DerivedFile(f"{language}/{UI_FILE_NAME}", "ui-translation",
                                   [f"{source_language}/{UI_FILE_NAME}"], read_recorded(ui_target)))
    return derived


def current_hash(source_key: str) -> str | None:
    path = CONTENT_DIR / source_key
    return blob_hash(normalised_bytes(path)) if path.exists() else None


def status_of(item: DerivedFile) -> Status:
    if not (CONTENT_DIR / item.path).exists():
        return Status(item.path, item.kind, "missing", item.default_sources)
    if not item.recorded:
        return Status(item.path, item.kind, "unstamped", item.default_sources)
    changed = [source for source, recorded in item.recorded.items() if current_hash(source) != recorded]
    new_sources = [source for source in item.default_sources if source not in item.recorded]
    if not changed and not new_sources:
        return Status(item.path, item.kind, "up-to-date", [])
    if not new_sources and only_trivial_changes(item):
        return Status(item.path, item.kind, "trivial", changed)
    return Status(item.path, item.kind, "stale", changed + new_sources)


def all_statuses() -> list[Status]:
    config = load_config()
    targets = [language for language in config.languages if language != config.source_language]
    return [status_of(item) for item in derived_files(config.source_language, targets)]


def find_derived(path: Path) -> DerivedFile:
    key = content_key(path)
    config = load_config()
    targets = [language for language in config.languages if language != config.source_language]
    for item in derived_files(config.source_language, targets):
        if item.path == key:
            return item
    raise SystemExit(f"{key} is not a derived file (a Galician page, deck or _ui.yaml, or a Spanish deck)")


def git_blob_text(blob: str) -> str | None:
    result = subprocess.run(["git", "-C", str(REPO_ROOT), "cat-file", "-p", blob], capture_output=True)
    return result.stdout.decode("utf-8") if result.returncode == 0 else None


def store_blob(path: Path) -> None:
    subprocess.run(["git", "-C", str(REPO_ROOT), "hash-object", "-w", str(path)], check=True, capture_output=True)


def source_diff(source_key: str, recorded_hash: str | None) -> str:
    current_path = CONTENT_DIR / source_key
    if not current_path.exists():
        return f"### {source_key}\nThe source no longer exists: it was deleted or renamed (see `provenance.py moves`).\n"
    current_text = normalised_bytes(current_path).decode("utf-8")
    if recorded_hash is None:
        return f"### {source_key}\nNo recorded version: compare the whole source with the derived file.\n"
    if recorded_hash == blob_hash(current_text.encode("utf-8")):
        return ""
    old_text = git_blob_text(recorded_hash)
    if old_text is None:
        return (f"### {source_key}\nThe recorded version ({recorded_hash[:10]}) is not in this git repository "
                "(never committed here, or pruned): compare the whole source with the derived file.\n")
    lines = difflib.unified_diff(old_text.splitlines(keepends=True), current_text.splitlines(keepends=True),
                                 fromfile=f"{source_key} (when derived)", tofile=f"{source_key} (now)", n=2)
    return f"### {source_key}\n" + "".join(lines)


def translatable_view(text: str, is_ui: bool) -> tuple[dict, str]:
    if is_ui:
        mapping = yaml.safe_load(text) or {}
        return {k: v for k, v in mapping.items() if k not in NON_TRANSLATABLE_KEYS}, ""
    front, body, _ = split_front_matter(text)
    return {k: v for k, v in front.items() if k not in NON_TRANSLATABLE_KEYS}, body


def only_trivial_changes(item: DerivedFile) -> bool:
    for source, recorded in item.recorded.items():
        current = current_hash(source)
        if current == recorded:
            continue
        old_text = git_blob_text(recorded)
        if old_text is None or current is None:
            return False
        is_ui = source.endswith(UI_FILE_NAME)
        new_text = normalised_bytes(CONTENT_DIR / source).decode("utf-8")
        if translatable_view(old_text, is_ui) != translatable_view(new_text, is_ui):
            return False
    return True


def render_derived_from(hashes: dict[str, str]) -> str:
    lines = ["derived_from:"] + [f'  {source}: "{value}"' for source, value in hashes.items()]
    return "\n".join(lines) + "\n"


def without_key_block(lines: list[str], key: str) -> list[str]:
    kept: list[str] = []
    skipping = False
    for line in lines:
        if line.startswith(f"{key}:"):
            skipping = True
            continue
        if skipping and (line.startswith((" ", "\t")) or not line.strip()):
            continue
        skipping = False
        kept.append(line)
    return kept


def write_derived_from(path: Path, hashes: dict[str, str]) -> None:
    """Rewrites only the derived_from block, leaving every other byte of the file as it was."""
    text = path.read_text(encoding="utf-8")
    block = render_derived_from(hashes)
    if path.name == UI_FILE_NAME:
        lines = without_key_block(text.splitlines(keepends=True), "derived_from")
        new_text = "".join(lines).rstrip("\n") + "\n" + block
    elif text.startswith("---\n"):
        closing = text.find("\n---\n", 3)
        if closing == -1:
            raise SystemExit(f"{path}: front matter is not closed")
        front_lines = without_key_block(text[4:closing + 1].splitlines(keepends=True), "derived_from")
        front = "".join(front_lines)
        new_text = "---\n" + front + block + text[closing + 1:]
    else:
        new_text = "---\n" + block + "---\n" + text
    path.write_text(new_text, encoding="utf-8")


def stamp(path: Path, if_trivial: bool) -> int:
    item = find_derived(path)
    if if_trivial and not only_trivial_changes(item):
        print(f"{item.path}: the sources changed in translatable text; update it first, then stamp without --if-trivial")
        return 1
    sources = [source for source in item.sources if (CONTENT_DIR / source).exists()]
    sources += [source for source in item.default_sources if source not in sources and (CONTENT_DIR / source).exists()]
    hashes = {}
    for source in sources:
        source_path = CONTENT_DIR / source
        store_blob(source_path)
        hashes[source] = blob_hash(normalised_bytes(source_path))
    write_derived_from(path, hashes)
    print(f"{item.path}: stamped from {', '.join(sources)}")
    return 0


def moves() -> list[tuple[str, str]]:
    """Derived files whose recorded source is gone but whose recorded hash matches an existing source."""
    config = load_config()
    by_hash = {}
    for source in (CONTENT_DIR / config.source_language).rglob("*.md"):
        by_hash[blob_hash(normalised_bytes(source))] = content_key(source)
    suggestions = []
    for language in config.languages:
        if language == config.source_language:
            continue
        for derived in (CONTENT_DIR / language).rglob("*.md"):
            for source, recorded in read_recorded(derived).items():
                if not (CONTENT_DIR / source).exists() and recorded in by_hash:
                    new_source = by_hash[recorded]
                    target = f"{language}/" + new_source.split("/", 1)[1]
                    suggestions.append((content_key(derived), target))
    return suggestions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    status_parser = commands.add_parser("status")
    status_parser.add_argument("--json", action="store_true")
    status_parser.add_argument("--all", action="store_true", help="also list up-to-date files")
    diff_parser = commands.add_parser("diff")
    diff_parser.add_argument("derived")
    stamp_parser = commands.add_parser("stamp")
    stamp_parser.add_argument("derived", nargs="+")
    stamp_parser.add_argument("--if-trivial", action="store_true",
                              help="stamp only if the sources changed in non-translatable keys only")
    commands.add_parser("moves")
    arguments = parser.parse_args()

    if arguments.command == "status":
        statuses = [s for s in all_statuses() if arguments.all or s.state != "up-to-date"]
        if arguments.json:
            print(json.dumps([asdict(s) for s in statuses], ensure_ascii=False, indent=2))
        else:
            for item in statuses:
                detail = f" <- {', '.join(item.changed_sources)}" if item.changed_sources else ""
                print(f"{item.state:10} {item.kind:16} {item.path}{detail}")
            if not statuses:
                print("everything is up to date")
        return 0
    if arguments.command == "diff":
        item = find_derived(resolve_argument(arguments.derived))
        sources = list(dict.fromkeys([*item.sources, *item.default_sources]))
        output = "".join(source_diff(source, item.recorded.get(source)) for source in sources)
        print(output or f"{item.path}: no source has changed")
        return 0
    if arguments.command == "stamp":
        return max(stamp(resolve_argument(path), arguments.if_trivial) for path in arguments.derived)
    suggestions = moves()
    for old, new in suggestions:
        print(f"git mv content/{old} content/{new}")
    if not suggestions:
        print("no moved sources detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
