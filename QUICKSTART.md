# Quickstart

目标：用 10 分钟确认公开包能安装、能自检，并能准备一个新用户工作区。

当前版本：`0.3.1`

## 1. 安装 skill

```bash
bash scripts/install-skills.sh
```

安装脚本是增量安装，不会清空你现有的其他 skill。

它会同步到本机已经存在的运行时目录：

```text
~/.codex/skills
~/.agents/skills
~/.claude/skills
```

## 2. 检查公开 Profile 模板

```bash
python3 -X utf8 scripts/check-public-profile.py
```

这个检查验证公开模板完整性、JSON 有效性和明显隐私泄露，不需要公众号 API。

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

轻量方式适合快速试用。完整方式适合长期维护作者身份、风格、故事、链接和发布元数据。

## 5. 准备写作资产

至少准备：

- 作者身份和定位
- 作者风格基线
- 故事素材库
- 表达边界规则
- 已发布文章链接或历史标题参考，如果有

完整方式按 `profiles/my-profile/EXTEND.md` 填写。

不要让 AI 编造你的经历、身份、项目或结果。

## 6. 放入第一份输入

输入可以是：

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

## 8. 检查关键 gates

第一次使用时，重点看这些 gate 是否被执行：

- 输入诊断：不要一上来直接写终稿
- 方向卡：粗素材要先给方向选择
- 开头阅读体验：首屏要讲清文章有什么
- 标题：生成 3-5 个候选，只推荐 1 个
- 个人故事：判断型文章要检查真实锚点
- 事实校验：经验、观点、事实要分开
- 正文配图：封面不等于视觉闭环
- 发布包：HTML、`article.json`、图片路径要一致

## 9. 生成发布资产

按需要输出：

- 标题候选和推荐标题
- 发布版 Markdown
- 封面 / 正文图 / 截图清单
- 发布包 HTML
- `article.json`
- 手动发布清单或草稿箱准备材料

## 10. 处理草稿箱或手动发布

- 有公众号 API 权限：创建草稿箱草稿
- 没有公众号 API 权限：输出完整手动发布包

公开包默认不要求公众号 API。

## 11. 做收尾

- 回写 publish 状态
- 回写 source note / inbox 记录，如果有
- 保存 AI 初稿和作者终稿
- 沉淀 revision learning
- 正式发布后再回填最终 URL

## 12. 不要混淆状态

- `已创建草稿` 不等于 `已正式发布`
- `手动发布包 ready` 不等于 `已发布`
- 只有拿到最终发布 URL 或后台确认，才算发布完成
