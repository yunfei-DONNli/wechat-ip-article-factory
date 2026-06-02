# Expected｜重推草稿

通过条件：

- 必须使用：`ORBITOS_REMOTE_FORCE_NEW_DRAFT=true bash "scripts/publish_remote_draft.sh" "YYYY-MM-DD_主题"`
- 不能把 `skipped_existing_draft` 当作成功。
- 重推后必须检查 `draft_created`、`inline_image_uploads`、`draft_content_preview` 中图片是否为 `mmbiz.qpic.cn`。
- 必须更新 publish-notes 和控制页。
