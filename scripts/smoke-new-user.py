#!/usr/bin/env python3
"""Run a new-user smoke test for the public WeChat IP article factory.

The test uses temporary HOME and vault directories. It verifies that:
- install-skills.sh installs repository skills without deleting unrelated existing skills;
- the public-generic profile is present after installation;
- the public profile validator passes;
- a fresh user can copy content-factory templates, writing assets, public profile templates, and the demo article into a new workspace.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: list[str], *, cwd: Path, env: dict[str, str] | None = None) -> None:
    printable = " ".join(cmd)
    print(f"$ {printable}")
    subprocess.run(cmd, cwd=cwd, env=env, check=True)


def copytree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def assert_exists(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"missing expected path: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run public package new-user smoke test.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    with tempfile.TemporaryDirectory(prefix="wechat-ip-smoke-") as tmp:
        tmp_path = Path(tmp)
        fake_home = tmp_path / "home"
        fake_vault = tmp_path / "vault"
        fake_home.mkdir()
        fake_vault.mkdir()

        for runtime in [".codex/skills", ".agents/skills", ".claude/skills"]:
            existing = fake_home / runtime / "existing-skill"
            existing.mkdir(parents=True)
            (existing / "SKILL.md").write_text("---\nname: existing-skill\ndescription: keep me\n---\n", encoding="utf-8")

        env = os.environ.copy()
        env["HOME"] = str(fake_home)
        run(["bash", "scripts/install-skills.sh"], cwd=root, env=env)

        for runtime in [".codex/skills", ".agents/skills", ".claude/skills"]:
            runtime_root = fake_home / runtime
            assert_exists(runtime_root / "existing-skill/SKILL.md")
            assert_exists(runtime_root / "wechat-article-publisher/SKILL.md")
            assert_exists(runtime_root / "wechat-article-publisher/profiles/public-generic/EXTEND.md")
            assert_exists(runtime_root / "skill-runtime-sync/SKILL.md")

        run([sys.executable, "-X", "utf8", "scripts/check-public-profile.py", "--root", str(root)], cwd=root)

        copytree(root / "templates/content-factory", fake_vault / "content-factory")
        copytree(root / "templates/writing-assets", fake_vault / "writing-assets-light")
        copytree(root / "skills/wechat-article-publisher/profiles/public-generic", fake_vault / "profiles/public-generic")
        copytree(root / "examples/demo-article", fake_vault / "content-factory/demo-article")

        expected_vault_paths = [
            "content-factory/README.md",
            "content-factory/选题索引.md",
            "writing-assets-light/作者身份基线模板.md",
            "profiles/public-generic/EXTEND.md",
            "profiles/public-generic/templates/article-json-template.json",
            "profiles/public-generic/templates/research-brief-template.md",
            "content-factory/demo-article/source.md",
            "content-factory/demo-article/publish.md",
            "content-factory/demo-article/article.json",
        ]
        for rel in expected_vault_paths:
            assert_exists(fake_vault / rel)

        print("New-user smoke test passed")
        print(f"temp_home={fake_home}")
        print(f"temp_vault={fake_vault}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError) as exc:
        print(f"New-user smoke test failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
