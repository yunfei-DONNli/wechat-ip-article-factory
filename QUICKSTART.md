# Quickstart

## 1. 安装 skill

```bash
bash scripts/install-skills.sh
```

这个安装脚本是增量安装，不会清空你现有的其他 skill。

## 2. 初始化内容工厂

复制 `templates/content-factory/` 到你的 Obsidian vault，或者按你的本地目录结构使用同等目录。

## 3. 准备写作资产

轻量方式：填写 `templates/writing-assets/` 里的模板，至少准备：

- 作者风格基线
- 作者身份基线
- 故事素材库
- 表达边界规则

完整方式：复制 `skills/wechat-article-publisher/profiles/public-generic/` 到你的私有工作区，再按 `EXTEND.md` 填写作者身份、风格、故事、已发布链接、固定引用链接、research brief 和 `article.json` 模板。

## 4. 检查公开 Profile 模板

```bash
python3 -X utf8 scripts/check-public-profile.py
```

这个检查只验证公开模板完整性、JSON 有效性和明显隐私泄露，不需要公众号 API。

## 5. 放入第一份输入

把你的输入放进素材区：

- 原始想法
- 行业判断
- 文章半稿
- 截图 / 链接 / 事件线索
- 现成文章草稿

## 6. 先做输入诊断

先判断这份输入属于哪类：

- 观点种子
- 事件扩写
- 素材成文
- 半成稿
- 已完成草稿

不要一上来就直接写终稿。

## 7. 选择工作模式

- 粗输入：先协作扩写，再进入候选稿
- 现成成稿：直接进入标题、配图、发布包和收尾检查

## 8. 生成发布资产

按需要输出：

- 标题候选和推荐标题
- 发布版 Markdown
- 配图 / 封面 / 正文图
- 发布包 HTML
- `article.json`
- 手动发布清单或草稿箱准备材料

## 9. 处理草稿箱或手动发布

- 有公众号 API 权限：创建草稿箱草稿
- 没有公众号 API 权限：输出完整手动发布包

## 10. 做收尾

- 回写 publish 状态
- 回写 source note / inbox 记录（如果有）
- 人工确认后再算正式发布

## 11. 不要混淆状态

- `已创建草稿` 不等于 `已正式发布`
- `手动发布包 ready` 不等于 `已发布`
- 只有拿到最终发布 URL 或后台确认，才算发布完成
