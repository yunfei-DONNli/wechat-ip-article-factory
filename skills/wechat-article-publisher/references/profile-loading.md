# Profile Loading

Use this reference when an agent needs to locate writing assets for the Author WeChat article workflow or prepare the same workflow for public reuse.

## Principle

The publishing workflow has one core behavior. Profiles provide data, assets, paths, and integration pointers. Profiles must not redefine safety gates, publish prechecks, screenshot preservation, truth review, title behavior, or WeChat compatibility rules.

## Default Profile

For the private OrbitOS vault, use:

```text
profiles/author-private/EXTEND.md
```

This profile points to the current private writing assets under:

```text
content-factory/writing-assets/
```

Do not copy private assets into the skill folder unless a later migration explicitly requires it.

## Public Template Profile

For public release preparation, use:

```text
profiles/public-generic/EXTEND.md
```

This profile points to fillable templates and synthetic examples under:

```text
profiles/public-generic/templates/
profiles/public-generic/examples/
```

Use this profile to explain how others can adapt the workflow. Do not use it to write Author's private articles.

## Loading Order

When a task requires writing assets, load in this order:

1. Core gate/reference needed for the current stage.
2. Active profile `EXTEND.md`.
3. Only the concrete asset/template files named by the active profile and needed for the current stage.

Do not bulk-load every template or every private asset.

## Active Profile Selection

Use `author-private` when:

- the task is inside this Obsidian vault,
- the user asks to generate or publish Author's WeChat article,
- the workflow needs real writing assets, personal stories, historical links, or OrbitOS content factory paths.

Use `public-generic` when:

- the user asks to publish/share the skill publicly,
- the task is documentation, packaging, onboarding, or template generation for other users,
- private assets must be excluded.

If the user explicitly names a profile, use that profile.

## Asset Categories

| Need | Private source | Public source |
|---|---|---|
| author identity | `profiles/author-private/EXTEND.md` → identity assets | `profiles/public-generic/templates/author-identity-template.md` |
| style baseline | private style assets | `writing-style-baseline-template.md` |
| expression guardrails | private expression rules | `expression-guardrails-template.md` |
| personal stories | private story bank and story files | `personal-story-bank-template.md`, `personal-story-template.md` |
| revision learning | private modification rules and reflections | `revision-rules-template.md`, `style-reflection-template.md` |
| published links | private published-link index/export | `published-links-template.md`, `published-article-snapshot-template.*` |
| fixed references | private fixed-link pool | `fixed-reference-links-template.md` |
| research brief | article workbench/publish package | `research-brief-template.md` |
| article metadata | publish package `article.json` | `article-json-template.json` |

## Safety Rules

- Never publish private profile files as part of a public release.
- Never replace private profile paths with public templates during a real Author article run.
- Never let public template gaps weaken the core workflow; missing public data means the public user must fill templates, not skip gates.
- If a private source path is unavailable, report the missing path and continue only when the current stage can safely use existing records or a user-approved fallback.

## Validation

After modifying `profiles/author-private/EXTEND.md`, `profiles/public-generic/EXTEND.md`, or public profile templates, run:

```bash
python3 -X utf8 "skills/wechat-article-publisher/scripts/check_profiles.py" --vault-root "your-vault"
```

This checks private target paths, public template paths, JSON validity, and obvious public-profile privacy leaks.

## Migration Status

Current status: profile indirection is documented, but the private workflow still reads existing OrbitOS paths directly. This is intentional. Actual path migration should happen only after the loading contract is stable and tested on real article runs.
