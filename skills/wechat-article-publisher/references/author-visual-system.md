# 作者公众号视觉系统

目标：让公众号视觉稳定、克制、有记忆点。先做视觉判断，再写 prompt 或生成 HTML。

## 基本原则

- 文章是主角，图片服务证据、理解和记忆，不抢正文。
- 截图证明真实，结构图讲清系统，隐喻图让人记住判断。
- 不把所有图都做成 PPT 信息图。
- 不复制外部角色 IP；可吸收“白底手绘、一图一动作、少文字”的方法。
- 每张图只能承担一个任务：证明、解释、转场、记忆点，不能全都要。

## 正文图类型矩阵

| 类型 | 用途 | 默认风格 | 默认尺寸 | 禁止 |
|---|---|---|---|---|
| 证据截图 | 证明事情真实发生 | 原图保全 + 轻边框 | `screenshot_thumbnail` | AI 图替代、裁到看不出来源 |
| 结构解释图 | 讲流程、系统、层级、模块关系 | 商务信息图 / 蓝橙 / 低噪声 | `normal_illustration`；复杂才 `detail_readable` 或 `full_width_allowed` | 一张图塞完整文章 |
| 认知隐喻图 | 承接核心判断、误区、情绪转折 | 白底手绘 / 固定小角色 / 大留白 / 少文字 | `normal_illustration` | 复制“小黑”IP、画成流程全图 |
| 引用卡 | 承接金句、概念定义、强判断 | 文字卡 / 克制强调 | HTML 组件优先 | 变成第二个标题 |
| 过渡图 | 段落节奏切换 | 极简场景 / 低信息密度 | `normal_illustration` | 无意义装饰 |

## 视觉预设

### 1. 商务结构蓝橙

用于：系统结构、流程闭环、企业 AI、工具链、方法论框架。

特征：

- 背景浅色或白色
- 主色 `#0F4C81`，点缀 `#D88A4A`
- 少量卡片、箭头、层级线
- 中文文字尽量少，复杂说明放正文

适合：结构解释图、部分封面。

### 2. 白底手绘认知隐喻

用于：文章最重要的认知转折、误区纠偏、反常识判断。

特征：

- 白底、大留白、细线条
- 一个固定小角色，可称“author mascot / AI workshop worker”
- 一图一动作：推门、搬箱子、接线、看仪表盘、踩坑、拆墙、搭桥
- 可有 1 个短标签，不写长句

适合：认知隐喻图。不要用于证据截图和复杂结构图。

### 3. 编辑部杂志感

用于：开头情绪、行业观察、个人经历、趋势判断。

特征：

- 真实或半写实场景
- 克制光影，少科技噪声
- 人物不正脸摆拍，避免广告感
- 不出现大段文字和 logo

适合：封面、过渡图、少量正文图。

### 4. 截图缩略证据

用于：用户附件、后台页面、价格、排名、网页、聊天记录。

特征：

- 保留原始截图主体
- 正文缩略展示，点击放大看细节
- 可加轻边框、圆角、图注
- 不重新设计成概念图

适合：证据截图。

## 选择规则

按顺序判断：

1. 这张图是不是证明材料？是 → 证据截图。
2. 读者是否需要看结构才能理解？是 → 结构解释图。
3. 是否存在一个最想让读者记住的判断？是 → 认知隐喻图。
4. 是否只是段落节奏需要停顿？是 → 过渡图。
5. 都不是 → 不要配图。

## Prompt 生成规则

生成正文图 prompt 时，必须记录：

- 图片类型
- 使用的视觉预设
- 服务的段落
- 画面动作 / 结构问题
- 尺寸策略
- 生成通道：优先 `image2_generate.py`；不可用时记录降级原因

认知隐喻图 prompt 模板：

```text
minimal white-background hand-drawn editorial illustration, one small original Orbit worker character [具体动作], [一个可见冲突或反差], lots of whitespace, thin ink lines, subtle blue and warm orange accents, no logo, no brand character, no complex diagram, optional one short Chinese label
```

结构解释图 prompt 模板：

```text
clean business system diagram, white background, restrained blue and warm orange palette, [具体结构：三层/五步/左右对比/闭环], minimal Chinese labels, clear hierarchy, low visual noise, not a presentation slide screenshot
```

编辑部杂志感 prompt 模板：

```text
cinematic editorial illustration, [具体人物/场景], quiet professional atmosphere, restrained blue and warm amber light, premium magazine composition, no logo, no large text
```

## 预检关注点

发布包 ready 前检查：

- 每张 `article.json.visual_assets.body_images[]` 都有 `type`、`purpose`、`position`。
- 证据截图对应的 HTML 图片应使用缩略证据图尺寸。
- 认知隐喻图不能包含复杂流程、满屏文字或外部角色 IP。
- 结构解释图如果使用满宽，必须有可读性理由。
- 文章没有正文图时，必须有 `skip=true + reason`；截图驱动文章还要有用户确认。
