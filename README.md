# 公众号IP文创作工厂

一套把个人经验、行业认知和素材，拆成可发布公众号文章的内容系统。

它不是让 AI 代替你写观点，而是帮你把自己的想法拆开、理顺、补齐，再变成适合公众号发布的内容。

## 当前版本

```text
0.2.0
```

这一版包含 public-generic Profile 模板、新用户冒烟测试和公开发布级 onboarding 文档。

## 一句话理解

如果你已经有行业观察、真实案例、踩坑复盘或方法论，但每次写公众号都从零开始，这套工具可以帮你把“想法 → 文章结构 → 标题 → 发布资产 → 手动发布包 / 草稿箱准备”变成一条可重复流程。

## 适合谁

- 对某个行业、岗位、产品或业务问题有真实观察的人
- 已经有判断，但还没写成文章的人
- 有案例、踩坑、复盘、方法论，但表达比较散的人
- 想把个人认知沉淀成长期输出的公众号 IP 作者

## 不适合什么情况

- 不适合用来伪装专业经验
- 不适合把没有认知、没有一手经验的内容直接包装成权威观点
- 如果缺少行业理解，这套流程最多只能辅助你整理资料和做学习笔记

## 核心原则

公众号内容最有价值的部分，来自作者自己的行业认知、真实经验和长期观察。

AI 的作用是放大表达效率，不是替代经验本身。

## 能做什么

- 提炼核心判断
- 拆解文章结构
- 补齐论证链路
- 生成标题候选
- 整理草稿、摘要、配图提示和发布资产
- 协作扩写半成稿或直接整理成发布版

## 包含什么

- 公众号文章发布 skill：`skills/wechat-article-publisher/`
- 运行时同步 skill：`skills/skill-runtime-sync/`
- 内容工厂模板：`templates/content-factory/`
- 轻量写作资产模板：`templates/writing-assets/`
- 完整 public-generic Profile 模板：`skills/wechat-article-publisher/profiles/public-generic/`
- 虚构 demo：`examples/demo-article/`
- 安装脚本：`scripts/install-skills.sh`
- 自检脚本：`scripts/check-public-profile.py`、`scripts/smoke-new-user.py`

## 前置条件

- 本机能运行 Bash 和 Python 3
- 使用支持本地 skill 的 agent，例如 Codex CLI、Claude Code 或兼容运行时
- 有一个用于存放内容工厂的本地目录，推荐是 Obsidian vault

公众号 API 不是必需条件。没有公众号 API 时，默认输出手动发布包。

## 快速开始

安装 skill：

```bash
bash scripts/install-skills.sh
```

这个脚本只会安装本仓库提供的 skill，不会删除你本机 `~/.codex/skills`、`~/.agents/skills` 或 `~/.claude/skills` 里已有的其他 skill。

检查公开模板：

```bash
python3 -X utf8 scripts/check-public-profile.py
```

做一次从零用户视角冒烟测试：

```bash
python3 -X utf8 scripts/smoke-new-user.py
```

这个测试使用临时 HOME 和临时 vault，不会改你的真实 Obsidian vault。

## 初始化自己的工作区

轻量方式：

```bash
cp -R templates/content-factory /path/to/your-vault/content-factory
cp -R templates/writing-assets /path/to/your-vault/writing-assets
```

完整方式：

```bash
cp -R templates/content-factory /path/to/your-vault/content-factory
cp -R skills/wechat-article-publisher/profiles/public-generic /path/to/your-vault/profiles/my-profile
```

轻量方式适合先跑通流程。完整方式适合长期维护个人 IP 写作资产，包括作者身份、风格、故事、已发布链接、固定引用链接、research brief 和 `article.json` 模板。

## 第一次怎么调用

把你的想法、素材、截图或半成稿放进内容工厂或 Obsidian 笔记后，对 agent 说类似下面的话：

```text
使用 wechat-article-publisher，把这段素材扩写成公众号文章。先做输入诊断和方向卡，不要直接写终稿。
```

如果你已经有完整草稿：

```text
使用 wechat-article-publisher，按成稿发布模式检查这篇文章，生成标题候选、发布版、article.json 和手动发布清单。我没有公众号 API。
```

## 推荐工作流

- 先写下你的原始想法、行业判断、案例和素材
- 用写作资产模板补充定位、表达风格、常用故事和观点边界
- 调用 `wechat-article-publisher`，把想法拆成文章结构
- 检查标题、观点、个人故事、配图和发布资产
- 没有公众号 API 时，生成手动发布包
- 有公众号 API 时，再接入自己的草稿箱创建链路
- 人工确认后，才算正式发布

## 边界

- 默认只到草稿和人工确认，不自动群发
- 草稿箱推送依赖公众号官方 API；很多人没有这个权限，所以公开版默认不强依赖这一步
- 没有公众号 API 时，依然可以产出完整的手动发布包
- 公开版不包含任何私人素材、真实发布记录或账号凭据
- `已创建草稿` 不等于 `已正式发布`

## 目录说明

```text
skills/                      # 可安装到 agent 运行时的 skills
templates/                   # 可复制到个人内容工作区的模板
examples/demo-article/       # 虚构 demo，不含真实账号或真实链接
scripts/install-skills.sh    # 增量安装 skills
scripts/check-public-profile.py
scripts/smoke-new-user.py
```

## Demo

查看 `examples/demo-article/` 可以看到一个最小闭环：

```text
source.md
→ title-candidates.md
→ publish.md
→ content.html
→ article.json
```

这个 demo 的状态是 `manual_package_ready`，不是 `published`。
