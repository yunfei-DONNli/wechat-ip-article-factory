# 发布收尾检查单

用于发布前后最后一轮闭环检查。

## 新文章启动前

新文章启动前先刷新历史已发布链接池，避免正文固定链接、历史文章引用和标题参考继续使用旧数据。

```bash
python3 -X utf8 "scripts/sync_wechat_published_backend.py" \
  --root "your-vault" \
  --json-output "content-factory/writing-assets/published-articles-snapshot.json"

python3 -X utf8 "scripts/backfill_published_links_from_backend.py" --root "your-vault"
```

检查结果：

- `content-factory/writing-assets/published-articles-snapshot.json` 已尽量刷新，或已记录后台不可用原因
- 缺失 `published_url` 的历史 `publish-notes` 已尽量由后台快照回填
- `content-factory/writing-assets/published-links-index.md` 已重建或明确沿用现有版本
- `content-factory/发布链路/公众号发布观察面板.md` 已重建或明确沿用现有版本

## 发布前

至少检查：

- 路径落点已验证：所有成稿、发布版、发布包、素材池都在 `content-factory/...` 下；没有误写到当前工作目录的 `50_资源/...`。
- 第一批文件写入后已用 `find` 或 `ls` 验证物理路径，不靠记忆判断文件存在。

- 标题已锁定，并且候选标题、推荐理由、参考来源已有记录
- 标题已同步到发布版 Markdown、`article.json`、公众号 HTML 标题区、发布包 HTML 和草稿标题
- 发布版 Markdown 已更新
- AI 原稿和用户终稿已分别保存；不能用终稿覆盖原稿
- 双稿齐全时，`revision-diff.md`、`revision-learning.md` 已生成，或已记录暂不生成原因
- `修改规律.md` 已记录文章级学习索引，或已记录暂不更新原因
- 素材池 `source.md` 已更新，记录 source of truth、素材处理结果和写作资产调用
- 如文章触发真实性核验条件，素材池或工作台已有 `research-brief.md`，并记录已核验事实、用户判断 / 个人体验、未核验项和降级写法
- 发布版正文、标题、摘要、顶部卡片、内容索引中的确定性事实已回到 `research-brief.md` 或用户原始材料
- 截图描述已和实际截图逐张对应；截图 OCR 不被当作外部事实核验
- `article.json.truth_check` 已记录 triggered、research_brief 或未触发原因、publish_preflight_review、未核验项和降级 / 人工确认记录
- 个人故事锚点已检查：文章能回答“为什么由作者来说”；如未使用，已有原因
- HTML 粘贴版已更新
- 顶部卡片已检查：不重复标题，金句/导语不等于标题
- 开头阅读体验已检查：前 300 字说明讲什么 / 为什么现在读 / 读完得到什么
- 如使用内容索引，已明确索引类型；用户说“内容索引”时默认目录型索引，列出全篇部分和每部分作用
- 作者和日期元信息只出现一次
- 发布包已更新
- cover.png 来自配图区正式版本，且封面只锁定 1 张
- `publish-packages/images/` 子目录存在
- 截图清点表已完成，原始截图数量与处理结果数量一致
- 截图驱动文章已追踪原图：入文，或已记录找不到路径并由用户确认跳过
- 正文配图已完成二选一：`publish-packages/images/` 已有实际资源，或 `article.json.visual_assets.skip=true + reason`；截图驱动文章不得无确认 skip
- 如果文章需要多张正文图，`publish-packages/images/` 和 HTML 已引用全部选中图片
- `article.json` 已记录 visual_assets
- 固定 10 篇链接完整，外部链接优先展示明文 URL

## 预检

运行：

预检前先确认 `article.json` 已按 `publish_precheck.py` 字段依赖写齐：`status`、`content_file`、`cover_file`、`source_note`、`publish_note`、`allow_auto_publish=false`、`visual_assets`、`truth_check`。正文有本地图片时，`visual_assets.body_images[]` 必须包含 `path/type/purpose/position`。

```bash
cd "your-vault"
python3 -X utf8 "scripts/publish_precheck.py" --root "." --package-id "YYYY-MM-DD_主题"
```

仅当 `overall_status = ready` 时进入远端草稿创建。

同时检查 material pool update 已完成。

同时检查 HTML 中不得残留 `📍`、`✏️`、`⚠️`、残破的 `️` 或内部批注标记。

## 远端草稿创建

默认首次创建：

```bash
bash "scripts/publish_remote_draft.sh" "YYYY-MM-DD_主题"
```

如果已有草稿后又改了标题、正文、HTML、封面、`article.json` 或正文图，必须强制新建草稿：

```bash
ORBITOS_REMOTE_FORCE_NEW_DRAFT=true bash "scripts/publish_remote_draft.sh" "YYYY-MM-DD_主题"
```

创建前先检查 SSH/GitHub 连通性，例如 `ssh -T git@github.com`。

创建前先 commit + push，因为远端 runner 读 GitHub。

## 草稿创建后

必须核对：

- `publish-notes` 中的 `draft_media_id`
- `cover_media_id`
- inline image upload 状态；正文有图时 `inline_image_uploads` 不能是空
- 如果本次是重推，远端返回不能是 `skipped_existing_draft`，必须是 `draft_created`
- `draft_content_preview` 中正文图片 URL 已替换为 `mmbiz.qpic.cn`，且截图缩略图尺寸符合配置
- `updated`
- run result 路径
- 单篇发布控制页是否同步
- 若来源于 `00_收件箱`，收件箱源文件是否已回写：
  - `publish_flow_status`
  - `package_id`
  - `publish_note`
  - `publish_version`
  - `publish_flow_updated`
  - `## 处理状态`

## 草稿创建后收件箱回写核查

草稿创建后，如果来源于 `00_收件箱`，必须执行固定核查表：

| 检查项 | 要求 |
|---|---|
| `publish-notes` frontmatter | 已写入草稿状态、媒体 ID、时间等关键字段 |
| 收件箱源文件回写 | 已写入 `publish_flow_status`、`package_id`、`publish_note`、`publish_version`、`publish_flow_updated` |
| Wikilink 断链 | 指向 `publish_note`、`publish_version` 的 wikilink 可解析；发现断链要修复后再结束 |
| 草稿状态段与 frontmatter 一致 | `## 处理状态` 中的发布链路阶段与 frontmatter 保持一致 |
| 内容编译器 `status` 未被覆盖 | 只写 `publish_flow_status`，不得改动编译器使用的 `status` 字段 |
| 收件箱源文件未自动删除 / 移动 | 草稿创建后只回写，不删除、不移动；除非后续正式发布归档规则单独触发 |

这 6 项必须写入最终“相关产物同步检查”。如果有一项失败，只能报告草稿已创建，不能报告收尾完成。

## 最终人工确认

提醒用户去微信后台核对：

- 标题
- 封面
- 开头
- 配图
- 排版
- 事实与链接
- IP / 版权风险
- 最终是否正式群发

## 正式发布后链接回填与归档

本节只处理“当前这篇文章正式发布后”的单篇回填；历史链接池刷新属于“新文章启动前”步骤。

只有在用户提供正式发布 URL，或明确确认公众号后台已经正式发布且可从后台抓取到 URL 后，才执行发布后回填。

回填链接是执行 agent 的责任，不让用户手工改 Markdown。必须执行：

```bash
python3 -X utf8 "scripts/publish_backfill_result.py" \
  --root "your-vault" \
  --package-id "YYYY-MM-DD_主题" \
  --published-url "https://mp.weixin.qq.com/s/<article-id>" \
  --published-at "YYYY-MM-DD HH:MM" \
  --operator "作者"

python3 -X utf8 "scripts/build_wechat_published_links.py" --root "your-vault"
python3 -X utf8 "scripts/build_publish_ops_dashboard.py" --root "your-vault"
```

回填后必须核对：

- `publish-notes`：已写入 `published_url`、`published_at`，并切到 `publish_status: 已发布`
- `content-factory/writing-assets/published-links-index.md`：已出现该正式链接
- `content-factory/发布链路/公众号发布观察面板.md`：已显示已发布链接
- 来源收件箱笔记：`publish_flow_status` 已同步为已发布

归档时再同步：

- `content-factory/已发布/YYYY-MM/主题.md`：保存最终内容资产
- `content-factory/已发布/README.md`：补充归档索引

不要把“草稿已创建”当成“已发布归档”。

## 不得误报完成

除非用户给出最终发布 URL 或明确说已在后台发布，否则不能声称“已正式发布”。

## 收件箱收尾边界

- 自动回写状态：允许
- 自动补充链路链接：允许
- 覆盖内容编译器 `status`：禁止
- 自动删除原收件箱笔记：禁止
- 自动移动原收件箱笔记：默认禁止，除非另有明确归档规则
