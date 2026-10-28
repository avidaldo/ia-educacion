"""Every route of the old Docusaurus site keeps resolving: it is a page of the new site or a bridge page to one."""

from build import render_pages, write_redirects
from content_model import load_config, load_content
from redirects import Redirect, load_legacy_routes, load_redirect_map, plan_redirects
from validation import heading_ids


def plan(model, legacy_routes, redirect_map):
    return plan_redirects(model, heading_ids(render_pages(model, [])), legacy_routes, redirect_map)


def test_every_legacy_route_of_the_real_site_resolves():
    model = load_content(load_config())
    legacy_routes = load_legacy_routes()
    redirects, problems = plan(model, legacy_routes, load_redirect_map())
    assert not problems, [problem.message for problem in problems]
    # The two home pages are still served by the new site itself; every other old route gets a bridge page.
    assert {redirect.route for redirect in redirects} == set(legacy_routes) - {"", "gl/"}


def test_the_prefix_chooses_the_language_and_the_anchor_is_resolved_in_it(config, content_dir):
    (content_dir / "es" / "_ui.yaml").write_text(
        (content_dir / "es" / "_ui.yaml").read_text(encoding="utf-8").replace(
            "labels: {prompt: Prompt}", "labels: {prompt: Prompt, deck_picker_link: Presentaciones}"),
        encoding="utf-8")
    model = load_content(config, content_dir)
    redirects, problems = plan(model, ["", "gl/", "docs/prompt/", "gl/docs/prompt/", "en/", "it/docs/old-deck/"],
                               {"docs/prompt/": "prompts/#qué-es-un-prompt", "docs/old-deck/": "presentacion/"})
    assert not problems
    assert [(redirect.route, redirect.language, redirect.target_url, redirect.target_title)
            for redirect in redirects] == [
        ("docs/prompt/", "es", "/sitio/prompts/#qué-es-un-prompt", "Prompts"),
        ("gl/docs/prompt/", "gl", "/sitio/gl/prompts/#qué-es-un-prompt", "Prompts (gl)"),
        ("en/", "es", "/sitio/", "Inicio"),
        ("it/docs/old-deck/", "es", "/sitio/presentacion/", "Presentaciones"),
    ]


def test_missing_entries_and_targets_are_reported_once_each(config, content_dir):
    model = load_content(config, content_dir)
    _, problems = plan(model, ["docs/a/", "en/docs/a/", "docs/b/", "it/docs/b/", "docs/c/"],
                       {"docs/b/": "no-existe/", "docs/c/": "prompts/#no-existe"})
    assert sorted((problem.code, problem.message) for problem in problems) == [
        ("redirect-missing", "no entry for the old route 'docs/a/'"),
        ("redirect-target", "docs/b/: 'no-existe/' is not a page of the site"),
        ("redirect-target", "docs/c/: 'prompts/#no-existe': #no-existe is not a heading of prompts/index.md (es)"),
    ]


def test_bridge_page_keeps_the_old_anchor_only_when_the_target_has_none(tmp_path):
    model = load_content(load_config())
    write_redirects(model, [Redirect("docs/prompt/", "es", "/ia-educacion/prompts/", "Prompts"),
                            Redirect("gl/docs/etica/", "gl", "/ia-educacion/gl/etica-legal/#sesgos", "Ética")],
                    tmp_path)
    plain = (tmp_path / "docs" / "prompt" / "index.html").read_text(encoding="utf-8")
    anchored = (tmp_path / "gl" / "docs" / "etica" / "index.html").read_text(encoding="utf-8")
    assert 'location.replace("/ia-educacion/prompts/" + location.hash);' in plain
    assert 'location.replace("/ia-educacion/gl/etica-legal/#sesgos");' in anchored
    assert '<meta name="robots" content="noindex">' in plain
    assert '<html lang="gl">' in anchored and "Esta páxina cambiou de enderezo:" in anchored
