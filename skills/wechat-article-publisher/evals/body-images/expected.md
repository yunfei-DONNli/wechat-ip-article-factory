# Expected｜正文配图

通过条件：

- 不能只生成 image-prompts.md。
- 必须决策正文图数量、位置、角色。
- 若进入发布包 ready，图片必须落到 `publish-packages/images/` 并由 HTML 使用 `images/xxx` 引用。
- 如果最终不使用正文图，必须写 `article.json.visual_assets.skip=true` 和具体 reason，并说明用户原要求为何被改判。
