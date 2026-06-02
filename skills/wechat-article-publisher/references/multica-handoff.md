# Multica / Claude Code 正文写作交接规则

当正文由外部 agent（例如 Multica 中的 Claude Code agent）撰写时，公众号 skill 仍然负责前置方案和后续成稿发布闭环。

## 适用场景

- 本 skill 已完成素材池、方案卡、标题方向、个人锚点策略和配图策略。
- 用户希望 Claude Code / Multica agent 负责正文初稿，或工作流要求双源初稿对照。
- 需要跨 agent 接力，但不希望靠聊天记忆传递上下文。

## handoff 文件位置

推荐位置：

```text
content-factory/协作扩写/workbench/YYYY-MM-DD_主题/handoff.md
```

## handoff.md 必填字段

```text
package_id:
当前阶段:
正文写作 agent:
source_of_truth:
素材池路径:
方案卡路径:
三方向证据路径:
标题候选路径:
风格对齐记录:
写作资产记录:
个人故事锚点策略:
截图 / 正文图处理要求:
正文输出路径:
Codex 直写稿路径:
Claude Code / Multica 稿路径:
融合稿路径:
用户终稿路径:
已改文件:
阻塞项:
下一步:
```

## 交给 Multica agent 的边界

外部正文写作 agent 只负责：

- 读取 handoff、素材池、方案卡、标题候选和风格记录
- 写 Claude Code / Multica 稿，不覆盖 Codex 直写稿
- 更新 handoff.md
- 在 Multica issue 评论交付文件路径和阻塞项

不得负责：

- 发布包
- HTML
- 远端草稿箱
- Git 提交推送
- publish-notes / 控制页 / 收件箱回写
- 正式发布 URL 回填

这些由本 skill 的“成稿发布模式”继续执行。


## 双源初稿规则

本 skill 接手成稿前，应至少能看到两份 AI 初稿：

- Codex 直写稿：当前 agent 根据同一方案直接生成。
- Claude Code / Multica 稿：外部 agent 根据 handoff 生成。

最终候选稿不是简单拼接，而是基于两稿对比做融合。融合记录至少说明：

- 以哪一稿为主。
- 另一稿贡献了哪些结构、句子、边界或截图处理。
- 舍弃了哪些内容，原因是什么。

如果只生成了一份稿，必须在 handoff 和最终同步检查中说明原因。

## Multica issue 建议格式

```bash
multica issue create   --title "撰写公众号正文：YYYY-MM-DD_主题"   --description-file "content-factory/协作扩写/workbench/YYYY-MM-DD_主题/handoff.md"   --assignee "author-wechat-draft-writer"
```


## 自动巡检脚本

创建 Multica issue 后，必须使用脚本巡检，而不是只靠 agent 记忆或单次查看。

如果没有真实 Multica issue，也必须创建本地 `handoff.md` 并运行能覆盖本地路径检查的等价校验；否则只能记录为“外部稿已收到，但正式 handoff 未完成”，不能写成 Gate 已通过。

```bash
python3 -X utf8 "scripts/check_multica_handoff.py" \
  --root "your-vault" \
  --issue "DON-71" \
  --handoff "content-factory/协作扩写/workbench/YYYY-MM-DD_主题/handoff.md" \
  --wait 600 \
  --interval 30
```

只有脚本返回 `status: ready_to_collect`，才能进入“成稿发布模式”。

脚本同时检查：

- Multica issue 状态是否进入 `in_review` / 完成态
- handoff.md 的 `已改文件` 是否不再是“待 agent 回填”
- Claude Code / Multica 稿路径文件是否真实存在
- issue 是否已有 agent 完成评论
- handoff.md 的 `阻塞项` 是否为空

不得只凭正文文件存在就进入成稿发布，也不得只凭 issue 状态进入成稿发布。

## 回收检查

外部 agent 完成后，本 skill 接手前必须检查：

- handoff.md 已更新
- Codex 直写稿路径存在，或已记录无法生成原因
- Claude Code / Multica 稿路径存在
- 融合稿、候选稿或正文路径存在
- 标题状态明确
- 截图 / 正文图处理状态明确
- 阻塞项为空或已说明

接手后进入“成稿发布模式”，只跳过协作扩写，不跳过标题、配图、发布包、precheck、草稿和回写 gate。


## Smoke Test Result

- Test issue: `DON-71`
- Agent: `author-wechat-draft-writer`
- Result: passed
- Evidence:
  - AI draft created at `content-factory/final-drafts/2026-05-31_multica-handoff-smoke-test/ai-draft-v1.md`
  - `handoff.md` updated with changed file and no blockers
  - Multica issue received agent completion comment
  - Issue status moved to `in_review`
- Note: this smoke test did not run 成稿发布模式 or remote draft creation.
