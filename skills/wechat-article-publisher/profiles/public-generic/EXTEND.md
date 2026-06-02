# Public Generic Profile

This profile is for public sharing of the WeChat article workflow. It contains fillable templates and synthetic examples only.

## Scope

Use this profile for public documentation, onboarding, template generation, and release-package preparation. Do not use it for real private author article drafting.

## Template Roots

```text
template_root: profiles/public-generic/templates/
example_root: profiles/public-generic/examples/
```

## Templates

| Need | Template |
|---|---|
| author identity | `profiles/public-generic/templates/author-identity-template.md` |
| author baseline | `profiles/public-generic/templates/author-baseline-template.md` |
| identity invocation card | `profiles/public-generic/templates/author-positioning-card-template.md` |
| style baseline | `profiles/public-generic/templates/writing-style-baseline-template.md` |
| expression guardrails | `profiles/public-generic/templates/expression-guardrails-template.md` |
| revision rules | `profiles/public-generic/templates/revision-rules-template.md` |
| story bank | `profiles/public-generic/templates/personal-story-bank-template.md` |
| personal story | `profiles/public-generic/templates/personal-story-template.md` |
| published link index | `profiles/public-generic/templates/published-links-template.md` |
| fixed reference links | `profiles/public-generic/templates/fixed-reference-links-template.md` |
| published article snapshot | `profiles/public-generic/templates/published-article-snapshot-template.md` |
| published article snapshot JSON | `profiles/public-generic/templates/published-article-snapshot-template.json` |
| style reflection | `profiles/public-generic/templates/style-reflection-template.md` |
| link refresh setup | `profiles/public-generic/templates/link-refresh-setup-template.md` |
| research brief | `profiles/public-generic/templates/research-brief-template.md` |
| article metadata | `profiles/public-generic/templates/article-json-template.json` |

## Examples

| Need | Example |
|---|---|
| generic source material | `profiles/public-generic/examples/source-material-sample.md` |
| fictional personal source | `profiles/public-generic/examples/personal-source-sample.md` |

## Public User Defaults

- Historical links: default to manual maintenance unless the user has their own WeChat backend/API access.
- Credentials: never included; users must configure their own private runner or skip draft-box automation.
- Personal stories: use fictional examples until the user fills their own private profile.
- Style: public templates describe structure; users must add their own voice samples in a private copy.

## Rules

- Keep all examples synthetic.
- Do not include real WeChat article URLs, API keys, backend exports, private screenshots, or personal documents.
- Public profile gaps must be shown as fields to fill, not silently skipped.
- Core workflow gates still apply: truth check, title, screenshot/body image, HTML compatibility, precheck, and publication boundary.
