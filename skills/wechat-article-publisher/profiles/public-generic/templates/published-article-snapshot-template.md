# Published Article Snapshot Template

This is a schema description for a WeChat published-article export. Do not publish real backend exports in a public profile.

## Fields

- title: exact published title
- url: final WeChat URL
- published_at: local publish time
- digest: WeChat digest/summary if available
- cover_url: optional cover URL
- tags: optional topic tags
- source: backend / manual / import

## Markdown Example With Fake Data

```json
[
  {
    "title": "Fake sample article",
    "url": "https://example.com/wechat/fake-example",
    "published_at": "2026-01-01 09:00",
    "digest": "A fake sample used to show the schema.",
    "tags": ["AI workflow"],
    "source": "manual"
  }
]
```
