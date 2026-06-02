# 微信草稿兼容性

本文件专门防止“本地生成正常，但微信草稿失败”。

## 完成标准

只有满足以下条件，才可视为真正完成：

- 远端 draft 创建成功
- `publish-notes` 已回写最新信息
- 最新 draft 可在后台继续人工核对

本地文件生成、HTML 生成、发布包生成，都不等于真正完成。

## 高风险兼容性问题

重点检查：

- HTML 中残留 Markdown 语法，如 `**粗体**`
- 不稳定链接、错误链接、临时链接
- 相关链接缺 `<a href>`
- `text-decoration: none` 误用于延伸阅读链接
- HTML 结构退化成 body-only
- 模板结构与既有 accepted style 偏差太大
- 图片路径仍指向本地临时路径
- 正文插图放在发布包根目录，而不是 `publish-packages/images/`
- HTML 引用了 `./xxx.png`、绝对路径或本地路径，导致远端 runner 无法上传

## 标题与元信息去重

公众号后台通常已经在页面顶部展示标题、作者和日期。生成正文 HTML 时必须检查：

- 不在正文顶部卡片重复同一个标题
- 不重复展示作者和日期
- 顶部卡片如存在，必须是金句、导语或观点卡
- 金句卡内容不能与标题完全相同

如果预览截图里出现“标题重复”或“作者日期重复”，必须回到 HTML 模板重建，而不是只手工删远端草稿。

## HTML 硬门槛

必须包含：

- 680px 外层 wrapper
- 顶部导语/金句/观点卡：`data-component="lead-card"` / `gold-sentence-card` / `viewpoint-card`
- 如使用内容索引，应使用独立 `data-component="content-index"`，不要把目录写成标题卡或金句卡
- 编号 section-title
- 紧凑段落
- 蓝色下划线延伸阅读链接，或直接展示完整明文 URL

正文 HTML 禁止包含：

- `<h1>`：公众号后台已经承载标题
- 重复的标题文本：顶部卡片不能等于 `article.json.title`
- 重复的作者 / 日期行：不要在正文内再写“作者：作者 · 日期”
- `data-component="title-card"`：旧标题卡已废弃

## 固定链接块

公众号后台可能吞掉 `text-decoration: underline`。外部链接默认优先展示完整明文 URL；需要样式时，可用 `<u>` 包裹并加 `!important`，但不能只依赖样式表达链接。

固定 10 篇链接要满足：

- 真正的 `<a href>`
- 蓝色
- 下划线或明文 URL 可复制
- 链接可回溯到 publish record 或 published_url

## 45166 排查思路

如果远端创建草稿失败：

1. 先怀疑 HTML 内容兼容性，不先怀疑整体流程
2. 先查粗体残留、工作台标记残留、异常链接、锚点结构、图片相对路径
3. 若 `inline_image_uploads` 为空，优先检查正文图片是否在 `publish-packages/images/` 且 HTML 是否引用 `images/xxx.png`
4. 必要时做最小化替换 / 分段 bisect
5. 修复后重新跑 draft wrapper，而不是手工绕过主脚本

## 重建规则

如果用户明确要求重建新 draft，或已有草稿后本地发布包发生任何会影响草稿预览的变化（标题、正文、HTML、封面、正文图、`article.json`）：

```bash
ORBITOS_REMOTE_FORCE_NEW_DRAFT=true \
bash "scripts/publish_remote_draft.sh" "YYYY-MM-DD_主题"
```

除非 wrapper 坏了，否则不要直接手工 SSH 绕过。

重建后必须确认返回状态不是 `skipped_existing_draft`；有正文图时还要确认 `inline_image_uploads` 非空。

## HTML 生成脚本规则

复杂 HTML 不要用 shell 内联 Python f-string 拼接。优先写入稳定脚本文件，用普通字符串拼接或模板文件渲染，避免花括号和引号转义导致语法错误。
