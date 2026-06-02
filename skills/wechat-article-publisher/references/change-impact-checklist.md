# 公众号 skill 修改影响面检查清单

当修改 `wechat-article-publisher`、公众号发布流程、协作扩写、标题、正文配图、版式、发布包、草稿箱、链接回填、收件箱回写相关规则时，先执行本清单，再改文件。

## 1. 先判定修改类型

记录本次属于哪一类：

- skill 入口规则
- 协作扩写流程
- 标题生成
- 写作资产 / 个人故事锚点
- 素材池 / 截图保全
- 正文配图 / 图片尺寸
- 微信 HTML / 版式系统
- 发布包 / 预检
- 草稿箱 / 远端 runner
- `publish-notes` / 收件箱回写
- 历史链接刷新 / 正式发布链接回填
- 公开版 skill 同步

## 2. 必扫目录

每次至少检查这些位置，不凭记忆判断：

```text
skills/wechat-article-publisher/SKILL.md
skills/wechat-article-publisher/references/*.md
content-factory/协作扩写/templates/*.md
content-factory/版式系统/*.md
content-factory/版式系统/templates/*
content-factory/版式系统/*.json
content-factory/成稿到草稿箱_操作卡.md
content-factory/发布链路/*.md
scripts/*.py
scripts/tests/test_*.py
```

如果修改会影响公开版，再检查：

```text
skills/wechat-article-publisher/SKILL.md
skills/wechat-article-publisher/references/*.md
```

默认先改私有版；公开版只在私有版跑顺并得到确认后同步。

## 3. 关键词扫描

按修改主题选择关键词全局搜索。常用关键词：

```text
历史链接
已发布文章链接
published-articles-snapshot
标题生成
候选标题
个人故事
故事锚点
写作资产
素材池
截图
source visual
正文配图
visual_assets
images/
content.html
wechat-layout-config
publish-notes
publish_flow_status
草稿箱
inline_image_uploads
45166
title-card
<h1>
作者日期
```

示例命令：

```bash
grep -R "关键词" -n \
  "skills/wechat-article-publisher" \
  "content-factory" \
  "scripts" | head -120
```

## 4. 修改分层原则

- `SKILL.md`：只放路由、默认链路、硬 gate、reference map、hard stops。
- `references/*.md`：放细流程、规则解释、异常处理。
- `协作扩写/templates/*.md`：放 agent 实际输出时必须填写的字段。
- `版式系统/*.md / templates / json`：放 HTML、图片尺寸、视觉规则。
- `脚本/*.py`：放可重复、易出错、必须确定性的操作。
- `tests/test_*.py`：每个新增脚本或关键 gate 至少有对应测试。

不要只改说明文档而漏掉模板；不要只改模板而漏掉脚本/预检；不要只改源码而漏掉运行时副本。

## 5. 验证命令

改完后至少执行：

```bash
python3 -X utf8 "/Users/author/.codex/skills/.system/skill-creator/scripts/quick_validate.py" \
  "skills/wechat-article-publisher"

PYTHONPATH="scripts" python3 -X utf8 -m unittest \
  "scripts/tests/test_publish_precheck.py"
```

如涉及对应能力，再追加：

```bash
PYTHONPATH="scripts" python3 -X utf8 -m unittest \
  "scripts/tests/test_apply_wechat_layout_config.py" \
  "scripts/tests/test_backfill_published_links_from_backend.py" \
  "scripts/tests/test_publish_backfill_result.py" \
  "scripts/tests/test_build_publish_ops_dashboard.py" \
  "scripts/tests/test_build_wechat_published_links.py"
```

## 6. 运行时同步

私有 skill 源码改完后，同步运行时副本：

```bash
bash "scripts/sync_agent_skills.sh" all "your-vault"

rsync -a --delete --exclude='.DS_Store' \
  "skills/wechat-article-publisher/" \
  "$HOME/.claude/skills/wechat-article-publisher/"
```

然后检查 diff：

```bash
for root in "$HOME/.codex/skills" "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  diff -qr \
    "skills/wechat-article-publisher" \
    "$root/wechat-article-publisher"
done
```

## 7. 最终回复必须包含影响面检查表

每次修改后，最终回复要列出：

- 已改：文件清单
- 已查但不改：文件/目录 + 原因
- 暂不改：文件/目录 + 原因
- 验证：命令和结果
- 运行时同步：目标目录和 diff 结果
