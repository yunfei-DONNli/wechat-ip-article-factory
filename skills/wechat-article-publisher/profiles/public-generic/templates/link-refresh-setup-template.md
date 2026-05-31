# Link Refresh Setup Template

Use this to decide how historical published links are refreshed before a new article.

## Mode

Choose one:

- manual: maintain `published-links-template.md` by hand.
- backend-export: import from your own backend or WeChat data export.
- API-runner: use a private script or remote runner with credentials.

## Public User Note

Many users do not have WeChat Official Account API access. The public profile should work with manual mode by default.

## Required Local Fields

- link_index_path:
- export_json_path:
- refresh_command:
- fallback_when_unavailable:

## Fake Example

- link_index_path: `profiles/my-profile/assets/links/published-links.md`
- mode: manual
- fallback_when_unavailable: continue with the existing local link index and record that no backend refresh happened.
