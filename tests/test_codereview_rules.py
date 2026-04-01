import re


def test_exists_codereview_test_rules_file():
    import pathlib

    path = pathlib.Path(__file__).parent.parent / "codereview_test_rules.py"
    assert path.exists(), "codereview_test_rules.py should exist"


def test_contains_all_expected_rule_markers():
    path = __import__("pathlib").Path(__file__).parent.parent / "codereview_test_rules.py"
    content = path.read_text(encoding="utf-8")

    markers = [
        "SEC001",
        "SEC002",
        "SEC003",
        "PERF001",
        "PERF002",
        "PERF003",
        "STYLE001",
        "STYLE002",
        "STYLE003",
        "STYLE004",
        "STYLE005",
        "SYS001",
        "SYS002",
        "TODO",
        "print(\"DEBUG:\"",
        "requests.get",
        "open(path",
        "while True",
        "% user_input",
        "<div>{user_input}</div>",
    ]

    missing = [m for m in markers if m not in content]
    assert not missing, f"Missing rule markers in file: {missing}"


def test_main_runs_without_uncaught_errors(monkeypatch):
    import sys
    import pathlib

    repo_root = pathlib.Path(__file__).parent.parent
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    from codereview_test_rules import main

    # Prevent external dependency calls from making real network requests by monkeypatching requests.get
    class FakeResponse:
        text = "ok"

        def raise_for_status(self):
            return None

    def fake_get(*args, **kwargs):
        return FakeResponse()

    import requests

    monkeypatch.setattr(requests, "get", fake_get)

    assert main() == 0 

    