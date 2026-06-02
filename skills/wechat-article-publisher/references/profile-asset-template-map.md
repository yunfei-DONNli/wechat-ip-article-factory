# Profile Asset Template Map

Use this reference when splitting the WeChat article workflow into a shared core plus private/public profiles. The goal is to keep one reusable publishing system while making private Author assets replaceable by public templates.

## Purpose

- Keep the private and public versions aligned through one shared core workflow.
- Do not publish Author's real identity, story, style, history, links, backend data, credentials, or source materials.
- Share reusable asset structures, field schemas, placeholder examples, and setup guidance instead of empty folders.
- Use this map as the migration contract before creating `core/`, `profiles/author-private/`, or `profiles/public-generic/`.

## Design Principle

- `core/` contains reusable workflow rules, gates, scripts, tests, and profile-agnostic references.
- `profiles/author-private/` contains real Author assets, local OrbitOS paths, credentials pointers, integrations, and private style/story material.
- `profiles/public-generic/` contains templates, placeholder examples, setup instructions, and fake sample data.
- Every private asset must be classified as one of:
  - `template`: publish its structure with fake examples.
  - `schema-only`: publish field definitions but no content examples that could reveal private data.
  - `private-only`: do not publish; optionally provide a synthetic sample asset.
  - `core-candidate`: move to shared core if it has no private content and applies to all users.

## Mapping Table

| Private asset | Role in private workflow | Public template | Share level | Notes |
|---|---|---|---|---|
| `content-factory/writing-assets/作者身份基线.md` | Author identity, credibility, and qualification baseline | `profiles/public-generic/templates/author-identity-template.md` | `template` | Keep structure and prompts; replace real career details with fake examples. |
| `content-factory/writing-assets/作者基线.md` | Supplemental author background and recurring viewpoint baseline | `profiles/public-generic/templates/author-baseline-template.md` | `template` | May later merge with author identity if fields overlap. |
| `content-factory/writing-assets/作者身份调用卡.md` | Runtime card for deciding when and how to invoke identity | `profiles/public-generic/templates/author-positioning-card-template.md` | `template` | Share the decision structure, not Author's actual authority claims. |
| `content-factory/writing-assets/作者公众号风格基线.md` | Voice, rhythm, argument style, and article texture | `profiles/public-generic/templates/writing-style-baseline-template.md` | `template` | Use generic/fake excerpts; do not expose real unpublished examples. |
| `content-factory/writing-assets/表达禁改规则.md` | Expressions, terms, and judgment boundaries that should not be rewritten | `profiles/public-generic/templates/expression-guardrails-template.md` | `template` | Public value is the guardrail method and categories. |
| `content-factory/writing-assets/修改规律.md` | Learning rules from AI draft to Author final draft | `profiles/public-generic/templates/revision-rules-template.md` | `template` | Provide synthetic before/after examples; keep real revision patterns private if they reveal style assets. |
| `content-factory/writing-assets/故事素材库.md` | Index of personal stories available for article anchors | `profiles/public-generic/templates/personal-story-bank-template.md` | `template` | Publish fields and fictional samples only. |
| `content-factory/writing-assets/个人故事/向前奔跑的人.md` | A concrete Author personal story asset | `profiles/public-generic/templates/personal-story-template.md` | `template` | Do not publish real story text; provide a fictional sample story. |
| `content-factory/writing-assets/published-links-index.md` | Historical published-link pool for related-link backfill | `profiles/public-generic/templates/published-links-template.md` | `schema-only` | Use fake URLs and document how to fill after publishing. |
| `content-factory/writing-assets/公众号固定引用链接池.md` | Stable reference links repeatedly inserted into articles | `profiles/public-generic/templates/fixed-reference-links-template.md` | `template` | Use generic links or placeholders. |
| `content-factory/writing-assets/published-articles-snapshot.md` | Backend/export snapshot of WeChat published articles | `profiles/public-generic/templates/published-article-snapshot-template.md` | `schema-only` | Do not publish backend data. Public version should describe fields and import path. |
| `content-factory/writing-assets/published-articles-snapshot.json` | Machine-readable backend/export snapshot if present | `profiles/public-generic/templates/published-article-snapshot-template.json` | `schema-only` | Include empty array or fake minimal records only. |
| `content-factory/writing-assets/风格复盘/*.md` | Per-article style reflection and learning evidence | `profiles/public-generic/templates/style-reflection-template.md` | `template` | Publish reflection structure with fake article samples. |
| `content-factory/writing-assets/原始素材/*.docx` | Private raw source material | `profiles/public-generic/examples/source-material-sample.md` | `private-only` | Do not publish originals; use synthetic source notes if examples are needed. |
| `content-factory/writing-assets/原始素材/向前奔跑的人.docx` | Private long-form autobiographical source | `profiles/public-generic/examples/personal-source-sample.md` | `private-only` | Never publish the document or converted text. |
| `content-factory/writing-assets/published-articles-snapshot.md` + `published-links-index.md` | Startup Links Gate data source | `profiles/public-generic/templates/link-refresh-setup-template.md` | `schema-only` | Public package should explain that WeChat API/backend access is optional and many users will only maintain links manually. |

## Public Template Package

When the public profile is created, prefer this folder shape:

```text
profiles/public-generic/templates/
├── author-identity-template.md
├── author-baseline-template.md
├── author-positioning-card-template.md
├── writing-style-baseline-template.md
├── expression-guardrails-template.md
├── revision-rules-template.md
├── personal-story-bank-template.md
├── personal-story-template.md
├── published-links-template.md
├── fixed-reference-links-template.md
├── published-article-snapshot-template.md
├── published-article-snapshot-template.json
├── style-reflection-template.md
├── link-refresh-setup-template.md
├── research-brief-template.md
└── article-json-template.json
```

The public package should not be an empty folder. It should include fillable files with:

- required fields,
- optional fields,
- one short fake example,
- instructions for what not to include,
- expected runtime path or profile override key.

## Private Profile Package

When the private profile is created, prefer this folder shape:

```text
profiles/author-private/
├── EXTEND.md
├── assets/
│   ├── author/
│   ├── style/
│   ├── stories/
│   ├── revision-learning/
│   └── links/
└── integrations/
    ├── obsidian-content-factory.md
    ├── tencent-cloud-runner.md
    └── image-api.md
```

Initial migration should point to existing OrbitOS paths instead of moving files immediately. Move real assets only after the profile loader and private article workflow have passed at least two successful runs.

## Core / Profile Boundary

Move to shared core when the rule is profile-agnostic:

- option-card evidence preservation,
- creative runtime method,
- truth and fact-checking gate,
- title generation method,
- body image inventory and WeChat image landing rules,
- HTML compatibility rules,
- publish precheck contract,
- revision learning workflow,
- profile asset lookup protocol.

Keep in private profile when it contains Author-specific content:

- author identity and credentials,
- Author style baseline,
- expression no-change rules,
- personal story text,
- article history and published URLs,
- backend export snapshots,
- local OrbitOS content-factory paths that cannot exist for other users,
- API credentials or private runner details.

Publish as public profile templates when the structure is useful but the content is private:

- author baseline,
- story bank,
- style baseline,
- revision rules,
- link index,
- source-material examples,
- article metadata examples.

## Migration Rules

- Do not split the current private skill immediately just because this map exists.
- First create this map and use it as the review contract.
- Then create public templates from the mapped structures.
- Then introduce a profile-loading reference or `EXTEND.md` that tells agents where to find private/public assets.
- Then run two private article workflows successfully with the profile indirection.
- Only after the private workflow is stable, regenerate the public release package.
- Never let the public profile redefine core gates differently from the private profile; differences should be data/assets, not workflow safety.
