# Quickstart

目标：用 10 分钟确认这套公开包能安装、能自检、能准备一个新用户工作区。

当前版本：`0.2.0`

## 1. 安装 skill

```bash
bash scripts/install-skills.sh
```

这个安装脚本是增量安装，不会清空你现有的其他 skill。

安装后会同步到这些目录中已经存在的运行时：

```text
~/.codex/skills
~/.agents/skills
~/.claude/skills
```

## 2. 检查公开 Profile 模板

```bash
python3 -X utf8 scripts/check-public-profile.py
```

这个检查只验证公开模板完整性、JSON 有效性和明显隐私泄露，不需要公众号 API。

## 3. 做一次新用户冒烟测试

```bash
python3 -X utf8 scripts/smoke-new-user.py
```

这个测试会使用临时 HOME 和临时 vault，不会改你的真实技能目录或真实 Obsidian vault。

## 4. 初始化内容工厂

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

轻量方式适合快速试用。完整方式适合长期维护自己的作者身份、风格、故事、链接和发布元数据。

## 5. 准备写作资产

轻量方式至少准备：

- 作者风格基线
- 作者身份基线
- 故事素材库
- 表达边界规则

完整方式按 `profiles/my-profile/EXTEND.md` 填写：

- 作者身份
- 作者基线
- 风格基线
- 表达边界
- 个人故事库
- 已发布链接
- 固定引用链接
- research brief
- `article.json`

不要让 AI 编造你的经历、身份、项目或结果。

## 6. 放入第一份输入

把你的输入放进素材区：

- 原始想法
- 行业判断
- 文章半稿
- 截图 / 链接 / 事件线索
- 现成文章草稿

## 7. 调用 skill

粗输入：

```text
使用 wechat-article-publisher，把这段素材扩写成公众号文章。先做输入诊断和方向卡，不要直接写终稿。
```

现成成稿：

```text
使用 wechat-article-publisher，按成稿发布模式检查这篇文章，生成标题候选、发布版、article.json 和手动发布清单。我没有公众号 API。
```

## 8. 先做输入诊断

先判断这份输入属于哪类：

- 观点种子
- 事件扩写
- 素材成文
- 半成稿
- 已完成草稿

不要一上来就直接写终稿。

## 9. 生成发布资产

按需要输出：

- 标题候选和推荐标题
- 发布版 Markdown
- 配图 / 封面 / 正文图
- 发布包 HTML
- `article.json`
- 手动发布清单或草稿箱准备材料

## 10. 处理草稿箱或手动发布

- 有公众号 API 权限：创建草稿箱草稿
- 没有公众号 API 权限：输出完整手动发布包

公开包默认不要求公众号 API。

## 11. 做收尾

- 回写 publish 状态
- 回写 source note / inbox 记录（如果有）
- 人工确认后再算正式发布

## 12. 不要混淆状态

- `已创建草稿` 不等于 `已正式发布`
- `手动发布包 ready` 不等于 `已发布`
- 只有拿到最终发布 URL 或后台确认，才算发布完成
