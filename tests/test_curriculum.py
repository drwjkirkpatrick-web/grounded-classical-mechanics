#!/usr/bin/env python3
"""test_curriculum.py — the full verification suite for the repository.

Run: python -m pytest tests/ -q
Every test runs against the live files; no fixtures, no mocks.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"

data = json.loads(MAP.read_text(encoding="utf-8"))
ALL_LESSONS = [l for u in data["units"] for l in u["lessons"]]


def test_map_has_365_lessons():
    assert data["total"] == 365
    assert len(ALL_LESSONS) == 365
    assert [l["n"] for l in ALL_LESSONS] == list(range(1, 366))


def test_map_is_regenerated_from_units():
    """The committed map must match what build_map.py would produce."""
    r = subprocess.run([sys.executable, "tools/build_map.py", "--check"], cwd=ROOT,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_all_lesson_files_exist_and_are_unique():
    paths = [ROOT / l["filename"] for l in ALL_LESSONS]
    missing = [str(p) for p in paths if not p.exists()]
    assert not missing, f"{len(missing)} lesson files missing, e.g. {missing[:3]}"
    assert len(set(paths)) == 365


def test_lint_all_lessons():
    r = subprocess.run([sys.executable, "tools/lint_lessons.py", "--all"], cwd=ROOT,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:]


def test_every_lesson_has_project_when_tagged():
    for l in ALL_LESSONS:
        text = (ROOT / l["filename"]).read_text(encoding="utf-8")
        if l["project"]:
            assert "**Project:**" in text, f"{l['filename']} missing Project line"


def test_cbe_coverage_check():
    r = subprocess.run([sys.executable, "tools/coverage.py", "--check"], cwd=ROOT,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_pre_post_mirror():
    """Post-test Q1-2 must mirror pre-test items so growth is measurable."""
    spot = [l for l in ALL_LESSONS if l["n"] % 37 == 0]  # deterministic sample of 10
    for l in spot:
        text = (ROOT / l["filename"]).read_text(encoding="utf-8")
        pre = re.search(r"## Pre-Test\n(.*?)(?=\n## )", text, re.S)
        post = re.search(r"## Post-Test\n(.*?)(?=\n## )", text, re.S)
        assert pre and post, l["filename"]
        assert "mirror" in post.group(1).lower() or "pre-test" in post.group(1).lower(), (
            f"{l['filename']}: post-test should mark mirrored items")


def test_no_forbidden_materials():
    """Materials must stay local and low-cost — no lab-supply-only kit."""
    banned = ["vernier calliper set supplier", "laboratory bench", "oscilloscope",
              "bunsen", "retort stand", "voltmeter"]
    for l in ALL_LESSONS:
        text = (ROOT / l["filename"]).read_text(encoding="utf-8").lower()
        for b in banned:
            assert b not in text, f"{l['filename']} uses non-local material: {b}"
