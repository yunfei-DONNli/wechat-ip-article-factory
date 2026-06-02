# 公众号IP文创作工厂

把你的行业认知、真实经验、案例素材和零散想法，拆成一篇能发布的公众号文章。

这不是一个“AI 代写观点”的工具。它更像一个公众号文章生产流程：帮你诊断输入、拆结构、生成标题候选、保护作者口吻、保留个人故事、处理截图和配图、做事实校验，最后整理成手动发布包或草稿箱准备材料。

## 当前版本

```text
0.3.1
```

v0.3.1 在 v0.3.0 的工作流 gates 基础上，重写了公开 README 和新用户引导：开头阅读体验、标题、风格对齐、正文配图、事实校验、修订学习、执行可靠性、多代理交接和公开 eval 用例。

## 一句话理解

如果你已经有行业观察、真实案例、踩坑复盘或方法论，但每次写公众号都从零开始，这套工具可以把：

```text
想法 / 素材 / 半成稿
→ 方向卡
→ 候选稿
→ 发布版
→ 标题候选
→ 配图和 HTML
→ 手动发布包 / 草稿箱准备
→ 发布后回填和归档
```

变成一条可重复流程。

## 适合谁

- 对某个行业、岗位、产品或业务问题有真实观察的人
- 已经有判断，但还没写成文章的人
- 有案例、踩坑、复盘、方法论，但表达比较散的人
- 想把个人认知沉淀成长期公众号 IP 的作者
- 希望把公众号写作从“灵感驱动”变成“流程驱动”的个人或团队

## 不适合什么情况

- 不适合伪装专业经验
- 不适合把没有认知、没有一手经验的内容包装成权威观点
- 不适合跳过事实校验直接制造判断
- 不适合把“创建草稿”误当成“正式发布”

如果缺少行业理解，这套流程最多只能帮你整理资料和做学习笔记。文章真正有价值的部分，仍然来自作者自己的经验、判断和长期观察。

## v0.3.1 核心能力

### 输入诊断和协作扩写

先判断输入属于哪类：观点种子、粗素材、截图线索、半成稿、完成稿或发布输入。

粗输入不会直接写终稿，而是先生成方向卡，让作者选择角度，再进入候选稿。

### 开头阅读体验 Gate

发布前检查首屏是否回答清楚：

- 这篇文章讲什么
- 为什么现在值得读
- 读完能得到什么

如果文章较长，会要求目录型内容索引，而不是只给几个空泛观点。

### 标题 Gate

标题不是最后随手润色。

默认生成 3-5 个候选标题，只标记 1 个推荐标题，并同步到 Markdown、HTML、`article.json` 和草稿标题。

### 写作资产和个人故事

文章必须尽量对齐作者身份、风格、表达边界和真实故事。

判断型文章需要回答一个问题：

```text
为什么这件事由你来说是可信的？
```

如果有真实故事锚点，就优先低干扰插入；如果没有，就保守表达，不编造经历。

### 风格对齐 Gate

如果文章“太 AI”“不像作者”“没人味”，流程会回到写作资产和修订记录，而不是只做表面口语化。

### 正文配图 Gate

封面不等于视觉闭环。

正文图分为几类：

- 证据截图：证明事情真实发生，不用 AI 图替代
- 结构解释图：讲清流程、系统和层级
- 认知隐喻图：让核心判断更容易被记住
- 引用卡 / 过渡图：服务节奏和阅读体验

正文图可以多选。只生成 prompt 不算完成，必须有真实图片落地，或明确记录为什么跳过。

### 事实校验 Gate

流程会区分：

- 作者经验和观点
- 有来源支撑的事实
- 需要验证的不确定说法

中央事实无法验证时，不能强行写成确定结论。

### 修订学习闭环

如果有 AI 初稿和作者终稿，需要保存差异，沉淀“作者怎么改 AI 稿”的规律。

长期看，这比单篇润色更重要。

### 执行可靠性

v0.3.1 保留了 v0.3.0 补齐的工程坑位：

- 文件落点检查
- `article.json` 字段前置
- 图片生成能力探测和降级
- HTML / WeChat 兼容性
- 相关产物一致性检查
- 多代理 / 双源 draft 交接
- 发布包变更后强制重建草稿
- 发布后 URL 回填和源文件 closeout

## 核心工作流

```text
输入 / 素材
→ 输入诊断
→ 素材池
→ 方向卡
→ 作者选择
→ 候选稿
→ 作者修订
→ 发布版
→ 标题候选和锁定
→ 事实校验
→ 配图和视觉资产
→ WeChat HTML / 发布包
→ 预检
→ 手动发布包或草稿箱准备
→ 人工确认
→ 正式发布后回填 URL
→ 源素材 closeout / 归档
→ 修订学习
```

## 包含什么

```text
skills/wechat-article-publisher/     # 公众号文章工作流 skill
skills/skill-runtime-sync/           # skill 运行时同步工具
templates/content-factory/           # 内容工厂模板
templates/writing-assets/            # 轻量写作资产模板
examples/demo-article/               # 虚构 demo，不含真实账号或真实链接
scripts/install-skills.sh            # 增量安装 skills
scripts/check-public-profile.py      # 公开 profile 自检
scripts/smoke-new-user.py            # 新用户冒烟测试
```

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

这个脚本是增量安装，只同步本仓库提供的 skill，不会删除你本机已有的其他 skill。

检查公开模板：

```bash
python3 -X utf8 scripts/check-public-profile.py
```

做一次从零用户视角冒烟测试：

```bash
python3 -X utf8 scripts/smoke-new-user.py
```

冒烟测试使用临时 HOME 和临时 vault，不会改你的真实 Obsidian vault。

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

如果你只有想法、素材、截图或半成稿：

```text
使用 wechat-article-publisher，把这段素材扩写成公众号文章。先做输入诊断和方向卡，不要直接写终稿。
```

如果你已经有完整草稿：

```text
使用 wechat-article-publisher，按成稿发布模式检查这篇文章，生成标题候选、发布版、article.json 和手动发布清单。我没有公众号 API。
```

如果你想走完整流程：

```text
使用 wechat-article-publisher，把这篇文章从素材到发布包完整跑一遍。先确认 source of truth、标题、事实校验、正文配图和手动发布包。
```

## 没有公众号 API 怎么办

很多人没有公众号草稿箱 API 权限。公开版默认不强依赖这一步。

没有 API 时，流程应该产出：

- 发布版 Markdown
- 公众号 HTML / 粘贴版内容
- `article.json`
- 标题候选和锁定标题
- 封面 / 正文图 / 截图清单
- 手动发布清单
- closeout 记录

有 API 时，可以在你自己的私有工作流里接入草稿箱创建。公开版不会包含账号凭据、服务器信息或真实后台数据。

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

## 验证命令

```bash
python3 -X utf8 scripts/check-public-profile.py
python3 -X utf8 scripts/smoke-new-user.py
```

## Release

当前最新发行版：

```text
v0.3.1
```

GitHub Release 页面会自动提供源码 zip 和 tar.gz。

## 隐私和边界

- 公开版不包含私人素材
- 公开版不包含真实公众号链接
- 公开版不包含 API key
- 公开版不包含真实草稿编号、后台数据或服务器配置
- 不要让 AI 编造你的经历、身份、项目或结果
- `draft created` 不是 `published`
- 只有拿到最终发布 URL 或后台确认，才算正式发布
