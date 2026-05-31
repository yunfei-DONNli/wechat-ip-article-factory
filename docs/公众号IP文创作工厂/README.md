# 公众号IP文创作工厂

这是一个把个人经验、行业认知和素材，协作生产成可发布公众号文章的内容系统。

它的目标不是让 AI 代替作者写观点，而是把作者自己的想法拆开、理顺、补齐，再变成可发布内容。

## 核心模块

```text
素材池
→ 协作扩写
→ 成稿区
→ 发布版
→ 配图区
→ 发布包
→ 草稿箱 / 手动发布包
→ 已发布
→ 数据区
```

## 需要的 skill

- `wechat-article-publisher`
- `skill-runtime-sync`

## 公开 Profile

公开版内置一个可填写的通用 Profile：

```text
skills/wechat-article-publisher/profiles/public-generic/
```

它包含作者身份、风格、表达边界、个人故事、已发布链接、固定引用链接、research brief 和 `article.json` 模板。

公开 Profile 只包含模板和合成示例，不包含真实个人素材、真实公众号链接、草稿编号、后台数据或凭据。

## 使用方式

1. 把 skill 同步到本机运行时目录。
2. 初始化内容工厂目录。
3. 复制轻量写作资产模板，或复制完整 public-generic Profile 到自己的私有工作区。
4. 先写素材，再进入协作扩写。
5. 生成标题、发布版、配图和发布包。
6. 如果有公众号 API，就创建草稿箱草稿；如果没有，就生成手动发布包。
7. 正式发布后回填公开链接，再归档到 `已发布/`。

## 自检命令

```bash
python3 -X utf8 scripts/check-public-profile.py
python3 -X utf8 scripts/smoke-new-user.py
```

## 公开版边界

- 可以公开 skill、模板、文档和虚构 demo
- 不公开真实收件箱内容、真实草稿编号、真实链接、账号凭据和服务器信息
- 没有公众号 API 时，仍然可以完成完整的手动发布闭环
- `draft created` 不是 `published`
