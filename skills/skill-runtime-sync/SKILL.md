---
name: skill-runtime-sync
description: Use when the user wants to audit, sync, install, or verify custom skills from a source-of-truth folder into local runtime skill folders for Codex, Claude Code, or agents.
---

# Skill Runtime Sync

Use this skill to keep custom skills consistent across the source folder and local runtime copies.

## Core Principle

Source folder is the source of truth. Runtime folders are copies only.

## Runtime targets

```text
~/.codex/skills/{skill}/
~/.agents/skills/{skill}/
~/.claude/skills/{skill}/
```

## Standard Workflow

1. Identify the skill.
2. Compare source and runtime copies.
3. Sync with delete semantics.
4. Verify no diff remains.
