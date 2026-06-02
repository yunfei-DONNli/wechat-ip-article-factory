# 公众号文章生成一致性检查清单

生成、扩写、改稿、定题、配图、发布版整理或重建公众号草稿时，不能只改当前可见正文。每次关键变更后，都要检查相关产物是否需要同步。

## 1. 触发场景

以下变更必须触发一致性检查：

- 核心判断、文章主线、结构顺序变化
- 标题、摘要、开头、结尾变化
- 用户新增或删除必须覆盖的概念
- 个人故事锚点变化
- 事实、数据、价格、公司 / 产品信息变化
- 截图、正文配图、封面、图注变化
- 历史文章链接、外部链接变化
- 从候选稿升级到成稿 / 发布版 / 发布包
- AI 原稿、用户终稿、修订学习记录变化
- 重建 HTML、重建发布包、重建远端草稿
- 正式发布后链接回填

## 2. 文章生成产物影响面

按当前阶段检查相关产物，不要求不存在的阶段提前创建，但已经存在的相关产物必须同步。

### 素材层

```text
content-factory/material-pool/YYYY-MM-DD_主题/source.md
content-factory/material-pool/YYYY-MM-DD_主题/research-brief.md
content-factory/material-pool/YYYY-MM-DD_主题/assets/
```

检查：

- 核心判断、写作方向、素材处理结果是否同步
- 截图 / 源图清点数量是否一致
- 事实核验结论是否同步到 `research-brief.md`
- 写作资产和个人锚点调用是否记录

### 协作扩写层

```text
content-factory/协作扩写/workbench/YYYY-MM-DD_主题/
content-factory/协作扩写/templates/*.md
```

检查：

- MECE、金字塔、方案卡、候选稿是否反映最新主线
- 用户选择的方案是否与最终稿一致
- 用户点名概念是否在候选稿和 coverage check 中出现

### 成稿 / 发布版层

```text
content-factory/final-drafts/YYYY-MM-DD_主题/
content-factory/publish-versions/YYYY-MM-DD_主题.md
content-factory/publish-versions/YYYY-MM-DD_主题_公众号精排版.md
content-factory/publish-versions/YYYY-MM-DD_主题_公众号后台粘贴版.html
```

检查：

- AI 原稿是否保留，用户终稿是否另存，不能互相覆盖
- `revision-diff.md`、`revision-learning.md` 是否在双稿齐全后生成
- `writing-assets/修改规律.md` 是否记录文章级学习索引或有暂不更新原因
- 标题、摘要、正文、结尾是否一致
- 工作台标记是否清除
- 顶部卡片不是标题重复
- 个人锚点是否保留
- 图文承接、图注、历史链接是否同步

### 配图 / 发布包层

```text
content-factory/visual-assets/YYYY-MM-DD_主题/
content-factory/publish-packages/YYYY-MM-DD_主题/article.json
content-factory/publish-packages/YYYY-MM-DD_主题/content.html
content-factory/publish-packages/YYYY-MM-DD_主题/cover.png
content-factory/publish-packages/YYYY-MM-DD_主题/images/
```

检查：

- `article.json.title/digest/visual_assets` 是否同步
- `content.html` 是否同步最新正文和图片
- `cover.png` 是否来自配图区正式封面
- 正文图片是否在 `images/` 下，并以 `images/xxx` 引用
- 截图驱动文章是否已追踪原图，不能只保留 OCR/文字复述
- 图片尺寸是否已按 `wechat-layout-config.json` 应用，截图证据图默认是缩略尺寸，不是大图铺满

### 发布记录 / 草稿层

```text
content-factory/数据区/YYYY-MM-DD_主题_publish-notes.md
content-factory/publish-versions/YYYY-MM-DD_主题_发布控制页.md
00_收件箱/源文件.md
```

检查：

- `publish_status`、`draft_media_id`、`cover_media_id`、`inline_image_uploads` 是否同步
- 发布包变更后重推是否强制新建草稿，而不是复用旧 `draft_media_id`
- 来源收件箱是否写入 `publish_flow_status/package_id/publish_note/publish_version/publish_flow_updated`
- 不覆盖内容编译器使用的 `status`

### 发布后链接层

```text
content-factory/writing-assets/published-links-index.md
content-factory/发布链路/公众号发布观察面板.md
content-factory/已发布/YYYY-MM/主题.md
```

检查：

- 正式发布 URL 是否写入 `publish-notes`
- 链接索引和观察面板是否重建
- 已发布归档是否同步

## 3. 修改后执行动作

根据改动类型选择：

- 改标题：同步发布版、精排版、HTML、`article.json`、远端草稿标题
- 改正文：同步成稿 / 发布版 / HTML / 发布包 `content.html`；如用户终稿已形成，同步修订学习记录
- 改配图：同步素材池清点、配图区、发布包 `images/`、HTML、`article.json.visual_assets`
- 改事实：同步 `research-brief.md`、正文、图注、链接
- 改发布状态：同步 `publish-notes`、控制页、观察面板、收件箱源文件
- 回填正式链接：同步 `publish-notes`、链接索引、观察面板、已发布归档

## 4. 最小输出要求

生成或修改文章后，最终回复必须包含一段“相关产物同步检查”：

- 已同步：列出实际改动过的产物
- 已检查无需同步：列出已存在但无需改的产物和原因
- 待人工确认：只列微信后台正式发布、事实/IP/版权等必须人工确认项
- 阻塞项：缺少素材、缺少权限、缺少最终链接等

不要只说“文章已改好”。
