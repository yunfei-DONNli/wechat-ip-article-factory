#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for runtime in "$HOME/.codex/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  mkdir -p "$runtime"
  for skill in "$ROOT/skills"/*; do
    [ -d "$skill" ] || continue
    name="$(basename "$skill")"
    target="$runtime/$name"
    rm -rf "$target"
    cp -R "$skill" "$target"
  done
  find "$runtime" -name '.DS_Store' -delete
  echo "synced $runtime"
done
