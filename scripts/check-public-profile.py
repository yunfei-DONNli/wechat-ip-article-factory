#!/usr/bin/env python3
"""Validate the public generic profile shipped in this repository."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_PATHS = [
    "skills/wechat-article-publisher/profiles/public-generic/EXTEND.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/author-identity-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/author-baseline-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/author-positioning-card-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/writing-style-baseline-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/expression-guardrails-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/revision-rules-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/personal-story-bank-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/personal-story-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/published-links-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/fixed-reference-links-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/published-article-snapshot-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/published-article-snapshot-template.json",
    "skills/wechat-article-publisher/profiles/public-generic/templates/style-reflection-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/link-refresh-setup-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/research-brief-template.md",
    "skills/wechat-article-publisher/profiles/public-generic/templates/article-json-template.json",
    "skills/wechat-article-publisher/profiles/public-generic/examples/source-material-sample.md",
    "skills/wechat-article-publisher/profiles/public-generic/examples/personal-source-sample.md",
]

PRIVATE_PATTERNS = [
    re.compile(pattern)
    for pattern in [
        r"云飞",
        r"lidong",
        r"DONNli",
        r"api-cn\.hi-code\.cc",
        r"sk-[A-Za-z0-9]",
        r"mp\.weixin\.qq\.com/s/",
    ]
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public generic profile templates.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()
    root = Path(args.root)
    profile_root = root / "skills/wechat-article-publisher/profiles/public-generic"
    failures: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            failures.append(f"missing: {rel}")

    if profile_root.exists():
        for path in profile_root.rglob("*.json"):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                failures.append(f"invalid json: {path.relative_to(root)}: {exc}")

        for path in profile_root.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in PRIVATE_PATTERNS:
                if pattern.search(text):
                    failures.append(f"privacy term: {path.relative_to(root)} contains {pattern.pattern}")

    if failures:
        print("Public profile check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Public profile check passed")
    print(f"required_paths={len(REQUIRED_PATHS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
