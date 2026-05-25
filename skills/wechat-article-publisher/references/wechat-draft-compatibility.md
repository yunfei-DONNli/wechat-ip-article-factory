# WeChat Draft Compatibility

## Purpose

Make the final article package safe for WeChat Official Account editing and draft-box creation.

## Checkpoints

- Title is locked and synced.
- HTML uses WeChat-safe structure.
- Images have stable local/package references before upload.
- Body images are either landed or explicitly skipped with reason.
- Links and anchors are valid.
- Unsupported layout styles are avoided.
- Draft-box API availability is confirmed before remote creation.

## API Dependency

Draft-box creation requires WeChat Official Account API credentials and sufficient account permission.

If unavailable, produce a manual publishing package instead:

- final Markdown or HTML
- title
- summary
- cover suggestion or cover asset
- body-image decision
- publish notes
- manual copy/paste checklist

## Rebuild Rule

If WeChat compatibility fails, rebuild the publish package from the selected publish version. Do not silently patch only the remote draft while leaving the local package inconsistent.

## Completion Boundary

`draft created` means the article exists in the account draft box.

`published` means the user confirms publication or provides the public article URL.
