"""Test suite for the code-review agent rule engine.

This file intentionally includes rule-triggering patterns defined in the OP:
- SEC001..SEC003, PERF001..PERF003, STYLE001..STYLE005, SYS001..SYS002
- AI-enforced coding standards + architecture notes in a contained way

Include this in your pipeline and run static analysis against it.
"""

from __future__ import annotations

import os
from typing import Any, Dict, List

import requests

# SEC001: Hardcoded secret (critical security)
API_KEY = "1234567890abcdef"

# SYS002: Hardcoded absolute path (medium style)
CONFIG_PATH = "C:\\Users\\Admin\\config.yml"

# SYS001: Missing timeout in external request (high performance reliability)
def insecure_http_fetch(url: str) -> str:
    # no timeout here (rule should trigger)
    response = requests.get(url)
    return response.text


def secure_http_fetch_with_timeout(url: str, timeout: float = 10.0) -> str:
    """Example of proper timeout handling (control case)."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


# PERF001: Infinite loop risk (high performance)
def infinite_loop_risk(enabled: bool) -> None:
    if enabled:
        # static analyzer should flag potential infinite loop
        while True:
            break


# PERF002: Large file read (medium performance)
def read_huge_file(path: str) -> str:
    # direct .read() can be expensive
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


# PERF003: N+1 query pattern (medium performance)
class FakeDB:
    """Fake persistence to illustrate anti-pattern."""

    def get_user_profile(self, user_id: int) -> Dict[str, Any]:
        return {"id": user_id, "profile": f"Profile {user_id}"}


def n_plus_one_pattern(user_ids: List[int], db: FakeDB) -> List[Dict[str, Any]]:
    response = []
    for user_id in user_ids:
        profile = db.get_user_profile(user_id)
        response.append(profile)
    return response


# STYLE002: Magic number
MAGIC_TIMEOUT = 30   # Should normally be constant, but using 30 directly below too


def magic_number_example() -> int:
    return 42  # magic number flagged


# STYLE003: TODO comment
# TODO: Remove temporary insecure helper before production.

def placeholder_todo_example() -> bool:
    return True


# STYLE005: Debugging artifact
def function_with_debug_artifact(value: Any) -> Any:
    print("DEBUG:", value)
    return value


# STYLE001 / STYLE004: Long function and long method
class LongRunner:
    """Class to show long method anti-pattern."""

    def long_method(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Intentionally >80 lines to trigger long method style rule."""
        result = {}
        for i in range(5):
            result[f"step_{i}"] = f"{payload.get('x', i)}"

        # filler lines to evade method length detection
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8
        i2 = 9
        j = 10
        k = 11
        l = 12
        m = 13
        n = 14
        o = 15
        p = 16
        q = 17
        r = 18
        s = 19
        t = 20
        u = 21
        v = 22
        w = 23
        x = 24
        y = 25
        z = 26

        # style: multiple nested blocks to approach complexity
        if payload:
            if payload.get("active"):
                for value in payload.get("items", []):
                    if value:
                        result[str(value)] = str(value)

        result["sum"] = a + b + c + d + e
        result["magic"] = 42
        return result


# SEC002: SQL injection risk
def sql_injection_example(user_input: str) -> str:
    raw_query = "SELECT * FROM users WHERE username = '%s'" % user_input
    return raw_query


# SEC003: XSS vulnerability risk
def xss_vulnerability_example(user_input: str) -> str:
    return f"<div>{user_input}</div>"


def main() -> int:
    """Entrypoint that ties all rule-specific components together."""
    # Demonstrate a secure path and insecure path side-by-side.
    # Avoid real network calls in local test runs; this is enough for static analysis coverage.
    try:
        _ = secure_http_fetch_with_timeout("https://example.com")  # safe call
    except Exception as exc:
        # graceful failure behavior (resilience requirement) without stopping test flow
        print(f"Skipped secure fetch due to: {exc}")
        _ = "timeout"

    try:
        _ = insecure_http_fetch("https://example.com")  # missing timeout
    except Exception as exc:
        print(f"Skipped insecure fetch due to: {exc}")
        _ = "timeout"

    db = FakeDB()
    _ = n_plus_one_pattern([1, 2, 3], db)
    _ = infinite_loop_risk(False)

    # local path example may not exist; wrap in try/except for resilience
    try:
        _ = read_huge_file("/tmp/big.log")
    except FileNotFoundError:
        _ = "file-missing"

    _ = function_with_debug_artifact("test")
    _ = sql_injection_example("admin' OR '1'='1")
    _ = xss_vulnerability_example("<script>alert(1)</script>")

    runner = LongRunner()
    _ = runner.long_method({"active": True, "items": ["a", "b", "c"], "x": 10})

    return 0


if __name__ == "__main__":
    main()
