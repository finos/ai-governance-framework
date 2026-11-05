"""Checks the upstream watch's decisions against stubbed GitHub API answers.

scripts/check_upstream_release.py asks the GitHub API about
finos/ai-governance-framework. These tests replace its one network call, `_get`, with
a table of answers, so they run offline.
"""

import importlib.util
import json
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
HEAD = "f" * 40


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's cached answers."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _stub(watch, monkeypatch, tree=None, head=None, tags=("v1", "v2")):
    """Answer as the API does: main at `head`, holding `tree` when it has moved."""
    head = head or watch.PINNED_COMMIT
    tree = watch.pins() if tree is None else tree
    answers = {
        f"{watch.API}/commits/{watch.BRANCH}": {"sha": head},
        f"{watch.API}/tags?per_page=100": [{"name": t} for t in tags],
        f"{watch.API}/git/trees/{head}?recursive=1": {
            "tree": [{"path": p, "sha": s, "type": "blob"} for p, s in tree.items()]
        },
    }

    def fake(url):
        return json.dumps(answers[url]).encode()

    monkeypatch.setattr(watch, "_get", fake)


def test_nothing_moved(watch, monkeypatch, capsys):
    _stub(watch, monkeypatch)
    assert watch.main([]) == 0
    assert "has not moved" in capsys.readouterr().out


def test_main_moved_outside_what_the_schema_reads(watch, monkeypatch, capsys):
    tree = dict(watch.pins())
    tree["docs/_layouts/risk.html"] = "a" * 40
    _stub(watch, monkeypatch, tree=tree, head=HEAD)
    assert watch.main([]) == 0
    assert "no file the schema reads" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("change", "says"),
    [
        (lambda t: t.update({"docs/_config.yml": "a" * 40}), "changes 1 file"),
        (lambda t: t.pop("docs/_config.yml"), "drops 1 file"),
        (lambda t: t.update({"docs/_risks/ri-99_new.md": "a" * 40}), "adds 1 file"),
        (
            lambda t: t.update({"docs/_data/references/new.yml": "a" * 40}),
            "adds 1 file",
        ),
        (lambda t: t.update({"LICENSE": "a" * 40}), "changes the licence"),
    ],
)
def test_main_changes_what_the_schema_reads(watch, monkeypatch, capsys, change, says):
    tree = dict(watch.pins())
    change(tree)
    _stub(watch, monkeypatch, tree=tree, head=HEAD)
    assert watch.main([]) == 1
    assert says in capsys.readouterr().out


def test_a_new_tag(watch, monkeypatch, capsys):
    _stub(watch, monkeypatch, tags=("v1", "v2", "v3"))
    assert watch.main([]) == 1
    assert "`v3`" in capsys.readouterr().out


def test_a_drifted_copy(watch, monkeypatch, capsys):
    pins = dict(watch.pins())
    pins["README.md"] = "a" * 40
    monkeypatch.setattr(watch, "pins", lambda: pins)
    _stub(watch, monkeypatch, tree=pins)
    assert watch.main([]) == 1
    assert "`README.md`" in capsys.readouterr().out


def test_a_failed_fetch_is_reported(watch, monkeypatch, capsys):
    def fail(url):
        raise urllib.error.URLError("no route")

    monkeypatch.setattr(watch, "_get", fail)
    assert watch.main([]) == 1
    assert "could not finish" in capsys.readouterr().out


def test_server_text_is_quoted(watch, monkeypatch, capsys):
    _stub(watch, monkeypatch, tags=("v1", "v2", "@someone`"))
    assert watch.main([]) == 1
    assert "`@someone'`" in capsys.readouterr().out


def test_the_report_is_written(watch, monkeypatch, tmp_path):
    _stub(watch, monkeypatch)
    report = tmp_path / "report.md"
    assert watch.main(["--report", str(report)]) == 0
    assert "has not moved" in report.read_text(encoding="utf-8")


def test_a_redirect_off_the_api_is_refused(watch):
    """A redirect is followed only to another https address of the GitHub API."""
    handler = watch._HttpsApiOnly()
    req = urllib.request.Request(f"{watch.API}/tags")
    for elsewhere in (
        "http://api.github.com/repos/finos/ai-governance-framework/tags",
        "https://example.org/tags",
        "https://api.github.com.example.org/tags",
    ):
        with pytest.raises(urllib.error.HTTPError):
            handler.redirect_request(req, None, 302, "Found", {}, elsewhere)
    followed = handler.redirect_request(
        req, None, 302, "Found", {}, f"{watch.API_ORIGIN}/repositories/1/tags"
    )
    assert followed.full_url == f"{watch.API_ORIGIN}/repositories/1/tags"


@pytest.mark.parametrize("path", ["../outside.md", "docs/../../x", "/etc/passwd"])
def test_a_manifest_path_outside_the_tree_is_refused(
    watch, monkeypatch, tmp_path, path
):
    manifest = tmp_path / "upstream_tree.tsv"
    manifest.write_text(f"{'a' * 40}\t{path}\n", encoding="utf-8")
    monkeypatch.setattr(watch, "MANIFEST", manifest)
    with pytest.raises(ValueError):
        watch.pins()
