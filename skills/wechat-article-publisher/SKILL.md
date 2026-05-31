---
name: wechat-article-publisher
description: Use when the user wants to turn ideas, notes, source material, rough drafts, or finished drafts into a publish-ready WeChat Official Account article through collaborative expansion, writing-asset based drafting, title generation, story anchors, fact checking, visual asset packaging, WeChat layout, optional draft-box creation, and source closeout.
---

# WeChat Article Publisher

Use this skill to turn source material into a publish-ready WeChat Official Account article.

## Core Principle

Treat this as a **closed-loop article workflow**, not a single formatting task and not a single API-upload task.

This skill does not replace the author's expertise. It helps the author拆解自己的想法, clarify the core judgment, structure the argument, preserve real experience, and package the article for WeChat publishing.

Default chain:

```text
input / source material
→ input diagnosis
→ material pool
→ collaborative expansion or direct publish mode
→ candidate draft
→ publish version
→ title candidates → title lock
→ visual assets
→ WeChat layout / HTML
→ publish package
→ precheck
→ optional draft-box creation
→ source closeout
→ human confirmation / formal publish
```

## Routing Boundary

Use this skill when the input is primarily:

- a personal idea or judgment seed
- a core paragraph
- a rough note
- a half draft
- a finished article draft
- a publish-ready article that needs title, layout, images, package, or closeout

Do not treat this skill as the default processor for generic source collection such as PDFs, slide decks, webpages, OCR pages, or large screenshot batches. Those should first be compiled into article material unless the user explicitly asks to turn them into a WeChat article.

## Input Diagnosis

Before writing, diagnose the input mode:

- `idea_seed`: only a core thought or judgment exists
- `rough_material`: notes, screenshots, fragments, links, or scattered evidence
- `half_draft`: article direction exists but structure or voice is incomplete
- `finished_draft`: full draft exists and needs publishing work
- `publish_input`: article is ready and needs package / layout / draft-box / closeout

The diagnosis determines the mode. Do not jump directly to publish package creation when the input is still rough.

## Two Modes

### 1. Collaborative Expansion Mode

Use this when the input is an idea seed, rough material, screenshots, fragments, or a half draft.

Default behavior:

- diagnose the input mode
- identify the writing basis and source of truth
- check writing assets before drafting
- propose 2-3 direction cards when the thesis or angle is not locked
- wait for user selection unless the user explicitly authorizes full automation
- then produce or update the candidate draft

### 2. Direct Publish Mode

Use this when the user provides a finished draft or clearly authorizes full automation.

Default behavior:

- verify the source of truth
- check title, writing assets, story anchor, visual assets, and WeChat compatibility
- create or update the publish package
- optionally create a WeChat draft-box entry when API credentials and permission exist
- write closeout notes and wait for human confirmation before claiming formal publish

## Required Inputs

Minimum useful inputs:

- source note, idea, or article draft
- author writing assets or voice guidance
- target audience / publishing account context
- title reference or title preference
- image needs or screenshot/source-visual material
- publish target and whether draft-box API is available

If some inputs are missing, continue with explicit assumptions only when safe. Do not invent professional experience, facts, or personal stories.


## Public Profile Templates

This public package includes a fillable generic profile under:

```text
skills/wechat-article-publisher/profiles/public-generic/
```

Use `profiles/public-generic/EXTEND.md` when adapting the workflow for a new author. It contains templates and synthetic examples only. Users should copy these templates into their own private workspace and fill them with their real identity, style, story, link, and publishing metadata.

Do not treat missing public-template fields as permission to skip gates. Missing profile data means the user must fill the template or the agent must draft conservatively without inventing expertise, facts, or personal stories.

## Mandatory Gates

These gates are hard requirements before claiming package readiness.

### A. Writing Assets Gate

Before candidate drafting, publish-version locking, or draft-box creation, check the available writing assets:

- author voice baseline
- author identity / positioning baseline
- industry cognition or first-hand experience
- story material library
- expression boundaries and forbidden claims

If this is a judgment-heavy article and a real story anchor exists, default to landing at least one story anchor unless the user explicitly asks not to or the anchor would distort the core judgment.

If writing assets are missing, say what is missing and draft conservatively. Do not fabricate expertise.

### B. Concept Coverage Gate

Any concept, viewpoint, or example explicitly requested by the user must appear in the final article, or the omission must be explained.

### C. Title Generation Gate

Treat title as part of the publish input, not as an optional final polish step.

Before publish version lock, package readiness, or draft-box creation:

- load `references/title-generation.md`
- judge the current title as `keep`, `tweak`, or `rewrite`
- generate 3-5 title candidates before locking the title; do not jump straight to one polished title
- even if the user already supplied a title, still re-evaluate and regenerate candidates when the title is only a work title or no longer fits the article
- mark exactly one recommended title
- keep the title faithful to the article's core judgment
- sync the selected title to draft, publish version, HTML, package, and draft-box title

### D. Personal Story Anchor Gate

For judgment-heavy articles, evaluate whether at least one personal story anchor should be inserted.

If inserted, it must support trust and argument clarity. If skipped, record the reason.

### E. Screenshot and Source Material Preservation Gate

Do not silently drop user-provided screenshots, diagrams, or source visuals.

Each source visual must end in one of these outcomes:

- used in cover
- used in body image
- converted into article evidence or summary
- archived as source material
- skipped with a concrete reason

### F. Body Image Gate

A cover is not enough. Explicitly check whether the article needs in-body images.

Cover is single-select: lock exactly one final cover asset.
Body images are multi-select: if the article benefits from multiple in-body visuals, land more than one rather than forcing a single image.

Before package readiness, this gate must end in exactly one outcome:

- body images are landed and referenced by the final article / HTML
- or the package records `skip=true` with a concrete reason

If body-image generation is needed, actual image assets must be produced. Prompt files alone are not a completed body-image outcome.

### G. Fact and Claim Check Gate

Separate three types of statements:

- personal experience or opinion
- source-backed factual claim
- uncertain claim requiring validation

Do not turn uncertain claims into authoritative statements. If a central factual claim cannot be verified, stop and ask or mark it clearly.

### H. WeChat Compatibility Gate

Before draft-box creation or final package handoff:

- load `references/wechat-draft-compatibility.md`
- check WeChat-safe HTML and layout constraints
- check links, anchors, images, and style compatibility
- rebuild the draft package if compatibility fails

### I. Draft-box Dependency Gate

Draft-box creation is optional and depends on WeChat Official Account API access.

Many users do not have this permission. If API credentials or permission are missing, produce a manual publishing package instead of treating the workflow as failed.

### J. Source Closeout Gate

When the article originates from an inbox, source note, issue, or source page, remote draft success is not the end.

Write back a closeout record without deleting or moving the source unless the user explicitly configured an archive rule.

Minimum closeout fields:

- `publish_flow_status`
- `package_id`
- `publish_note`
- `publish_version`
- `publish_flow_updated`
- links to publish package / draft / final article when available

### K. Formal Publish Gate

Never claim the article is formally published unless the user provides the final WeChat URL or confirms backend publication.

`draft created` is not the same as `published`.

## Reference Files

Load these references only when needed:

### `references/collaboration-writing-flow.md`

Use for input diagnosis, collaborative expansion, direction cards, candidate draft creation, and promotion from rough material to publish version.

### `references/writing-assets-and-story-anchors.md`

Use for writing assets, voice protection, story-anchor decisions, and original-experience preservation.

### `references/title-generation.md`

Use for title judgment, 3-5 candidates, recommended title, and title sync requirements.

### `references/visual-assets-and-layout.md`

Use for cover/body-image decisions, screenshot preservation, visual assets, and layout baseline.

### `references/wechat-draft-compatibility.md`

Use for WeChat HTML compatibility, draft-box limitations, rebuild rules, and manual publishing fallback.

### `references/publish-closeout-checklist.md`

Use for precheck, package readiness, draft creation sequence, closeout fields, and final human confirmation checklist.

### `references/runtime-targets.md`

Use for deciding whether the current runtime can create a draft-box entry or should only produce a manual package.

## Output Rule

When working in collaborative expansion mode, make clear:

- input diagnosis
- source of truth
- writing-basis priority
- whether writing assets are sufficient
- whether external fact validation is needed
- proposed direction cards or next drafting action

When working in direct publish mode, make clear:

- source of truth
- publish title status
- title candidate coverage and final selection
- missing items before package readiness
- body-image decision
- whether body images are single-select or multi-select
- WeChat compatibility status
- whether draft-box API is available
- closeout status

## Hard Stops

Stop and ask or wait when any of these is true:

- input mode cannot be diagnosed
- core thesis is ambiguous
- collaboration mode needs user direction selection
- key factual claim cannot be verified but is central to the article
- writing assets are missing and the article would otherwise imply false expertise
- the user says the draft does not sound like them
- draft-box creation is requested but API credentials or permission are missing
- compatibility failure cannot be fixed safely

## Completion Rule

The workflow can be called complete only when one of these is true:

- a manual publishing package is ready and all required gates are resolved
- a WeChat draft-box entry is created and source closeout is written
- the user confirms formal publication or provides the final public WeChat URL

Do not confuse these three states.
