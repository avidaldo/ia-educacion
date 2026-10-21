"""Checks the content without writing the site: links and anchors, assets, slides, translation parity,
provenance (what the skills still have to update) and review dates.

Usage: uv run engine/check.py [--strict] [--only CATEGORY ...] [--lang gl] [--json]
Exit status: 0 clean, 1 errors, 2 warnings with --strict.
"""

import argparse
import datetime
import json
import sys
from dataclasses import asdict

from build import render_decks, render_pages
from content_model import Problem, load_config, load_content
from provenance import all_statuses
from validation import CATEGORIES, category_of, review_problems, todo_problems, validate_rendered


def provenance_problems() -> list[Problem]:
    messages = {"stale": "its sources changed: {sources}",
                "trivial": "only non-translatable keys changed in {sources}: run provenance.py stamp --if-trivial", "unstamped": "has no derived_from yet (made from {sources})",
                "missing": "does not exist yet (to be made from {sources})"}
    return [Problem("warning", f"content/{status.path}", 1, status.state,
                    f"{status.kind}: " + messages[status.state].format(sources=", ".join(status.changed_sources)))
            for status in all_statuses() if status.state != "up-to-date"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--only", nargs="+", choices=sorted(CATEGORIES))
    parser.add_argument("--lang", help="keep only findings for files of this language")
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args()

    model = load_content(load_config())
    problems = list(model.problems)
    rendered = render_pages(model, problems)
    decks = render_decks(model, problems)
    problems += validate_rendered(model, rendered, decks)
    problems += review_problems(model, datetime.date.today())
    problems += provenance_problems()
    problems += todo_problems(model)
    if arguments.only:
        problems = [problem for problem in problems if category_of(problem.code) in arguments.only]
    if arguments.lang:
        problems = [problem for problem in problems if f"/{arguments.lang}/" in f"/{problem.path}"]
    problems.sort(key=lambda problem: (problem.level != "error", category_of(problem.code), problem.path, problem.line))

    if arguments.json:
        print(json.dumps([asdict(problem) | {"category": category_of(problem.code)} for problem in problems],
                         ensure_ascii=False, indent=2))
    else:
        for problem in problems:
            print(f"{problem.level.upper():7} [{category_of(problem.code)}/{problem.code}] "
                  f"{problem.path}:{problem.line} {problem.message}")
    errors = sum(problem.level == "error" for problem in problems)
    warnings = len(problems) - errors
    if not arguments.json:
        print(f"{errors} errors, {warnings} warnings")
    if errors:
        return 1
    return 2 if arguments.strict and warnings else 0


if __name__ == "__main__":
    sys.exit(main())
