---
name: wechat-article-publisher
description: Use when the user wants to turn ideas, notes, or source material into a publish-ready WeChat Official Account article through a structured workflow with title generation, writing assets, story anchors, fact checking, layout, images, publish package creation, and draft-box closeout.
---

# WeChat Article Publisher

Use this skill to move source material into a publish-ready WeChat Official Account article.

## Core Principle

This is a closed-loop publishing workflow, not a single formatting task.

Default chain:

```text
inputs
→ 素材池
→ 协作扩写
→ 成稿区
→ 发布版
→ 配图区
→ 发布包
→ 预检
→ 草稿箱
→ 回填
→ 已发布
```

## Required Inputs

- source notes or article draft
- title reference
- writing assets
- image needs
- publish target

## Mandatory Gates

- writing assets gate
- title gate
- story anchor gate
- screenshot preservation gate
- body-image gate
- WeChat compatibility gate
- inbox/source closeout gate
- post-publish archive gate

## Reference Files

Load these references when needed:

- `references/title-generation.md`
- `references/writing-assets-and-story-anchors.md`
- `references/visual-assets-and-layout.md`
- `references/publish-closeout-checklist.md`
- `references/runtime-targets.md`

## Output Rule

When working this skill, make clear:

- source of truth
- publish title status
- what is missing before package readiness
- whether images and HTML are ready
- whether draft-box closeout has been completed
