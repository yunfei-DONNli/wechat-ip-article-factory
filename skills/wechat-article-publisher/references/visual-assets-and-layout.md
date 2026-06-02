# 配图与排版规则

这部分解决两个问题：

- 文章视觉资产是否完整
- 微信排版是否接近作者既有风格

## 视觉资产目录

正式视觉源目录：

```text
visual-assets/YYYY-MM-DD_主题/
├── image-prompts.md
├── cover.png
├── illustration-01.png
└── illustration-02.png
```

发布包目录：

```text
publish-packages/YYYY-MM-DD_主题/
├── article.json
├── content.html
├── cover.png
└── images/
```

## 资产角色

- `visual-assets/`：源资产区
- `publish-packages/cover.png`：上传副本
- `publish-packages/images/`：正文实际使用图片
- HTML：最终引用层

## 正文图规则

发布包初始化时先创建 `images/` 子目录。

封面完成不等于视觉闭环完成。

插图决策必须前置到方案卡或发布计划阶段：先判断要不要正文图、需要几张、每张服务哪个段落。

封面是单选资产；正文图可以多选，不要把多图需求硬压成一张图。

正文配图先判断角色，不先生成图片。默认分三类：

- **证据截图**：证明事件、网页、价格、后台状态、用户附件真实存在；不生成 AI 图替代；默认 `screenshot_thumbnail`；细节交给点击放大。
- **结构解释图**：讲清流程、系统、层级、模块关系；沿用现有商务信息图风格；允许更多文字，但每张图只服务一个结构问题；只有横向复杂结构才允许 `full_width_allowed`。
- **认知隐喻图**：承接文章最关键判断、误区或情绪转折；用白底、手绘、固定角色、少文字、大留白、一图一动作形成记忆点；不复制 Ian Xiaohei 的“小黑”IP，可发展作者自己的视觉角色，例如“author mascot / AI workshop worker”。

长文默认检查是否需要：

- 新闻截图
- 证据截图
- 结构解释图
- 认知隐喻图
- 引用卡片
- 过渡图

正文配图不能停留在“还没决定”。发布包进入 ready 前，必须二选一：

- 正文图已经真实落地到 `publish-packages/images/`，并被最终 HTML 用 `images/xxx.png` 相对路径引用
- 或在 `article.json.visual_assets` 中明确写 `skip: true` 和 `reason`

截图驱动文章不能直接走第二项。如果文章开头、标题、主论证或素材池写了“截图 / 图里 / 用户附件 / 如图 / 看到一张图”，这张截图就是证据图，必须先追踪原图。找不到原图时要停下说明“找不到哪些路径”，不能只用 OCR 文字替代，也不能生成 AI 概念图冒充截图证据。

如果用户要求正文配图，不能只生成 `image-prompts.md`，必须有实际图片落地。正文需要多张图时，一次性产出并保留多个候选，再按文章结构落位。

如果最后不用正文图，必须记录原因；截图驱动文章还必须记录用户明确确认跳过。

## 视觉提示词规则

生成封面或正文图前，先探测可用图片生成能力。作者私有工作流优先检查 your private image-generation config `~/.config/orbitos/secrets/image2.env`、`~/.config/orbitos/secrets/*image*.env`、`~/.config/orbitos/secrets/*generate*.env` 与当前环境中的 `IMAGE2_API_KEY`，并优先调用 `scripts/image2_generate.py`；默认接口为 `<your-image-api-base-url>` + `/v1/images/generations`。检查 secrets 时只看文件存在、权限和变量名是否 `SET`，不得打印 key；如果当前 shell 没有变量但 secrets 文件存在，先在子 shell 中 source 后再判断，不要直接降级到 Pillow。如果用户在对话里提供 image2 key，只能落到 `~/.config/orbitos/secrets/image2.env` 和本机运行时环境，不能写入 vault / skill / git。image2 不可用时再检查用户指定 API、其他项目脚本和既有素材。若仍不可用，直接降级到用户截图、既有素材、Pillow / HTML / SVG 程序化封面或明确无 AI 插图，不连续试错多个不可用 skill。降级结果必须记录到视觉决策和 publish-notes。

生成封面或正文图提示词前，先读取 `creative-runtime.md`，用“稳定核心 + 可控偏离”生成 2-3 个视觉方向。方向差异应来自画面路线，而不是抽象商业词堆叠。

生成提示词时，不要先解释文章概念，再让模型翻译成图。先确定画面，再补概念。

默认顺序：

1. 先提取文章三个内容锚点：主题对象、关键场景、读者应记住的判断。
2. 再定图的角色：封面、证据截图、结构解释图、认知隐喻图、引用卡、过渡图。
3. 再定视觉路线：真实场景、杂志感、电影感、抽象隐喻、手绘线稿、科技克制风。
4. 再写可见画面：人物、环境、构图、光线、色彩、材质。
5. 最后才补文章概念，只作为画面服务，不做概念说明书。

封面 prompt 必须服务文章内容，不服务“专业感”本身。像 WorkBuddy / 股票分析这类文章，画面要锚定“股票页面、AI 专家分工、投资分析现场”等内容元素；不要写成泛化的 network nodes、abstract charts、data panels。首版图如果只显得科技但看不出文章主题，应判定为 prompt 失败并重写，不算封面完成。

认知隐喻图的提示词要先写场景，不写抽象概念：

- 只保留一个动作、一个冲突或一个反差
- 不让一张图解释完整文章
- 默认白底、手绘、少文字、固定角色、大留白
- 角色属于作者自己的视觉系统，不使用“小黑”、Ian Xiaohei 角色或可识别 IP
- 画面可以有一句短标签，但不要做流程全图或 PPT 标题页

写 prompt 时优先：

- 用具体画面，不用抽象口号
- 少写“平台、系统、放大器、认知升级”这类解释词
- 给风格参考，但不要堆太多限制词
- 允许一次产出 2-3 个不同视觉方向候选
- 正文图优先服务段落情绪，而不是把整篇逻辑一次讲完

不推荐的 prompt 写法：

- 让模型“画出平台 + AI + 工作流放大器的概念图”
- 用一串抽象商业词堆出说明书式提示词
- 同时要求太多风格、对象、构图和信息点

推荐的 prompt 写法：

- `cinematic editorial illustration of a solitary creator in front of a modular workflow wall, quiet automation behind glass, dark blue and warm orange, no text, premium magazine feel`
- `minimal hand-drawn business sketch, one person, one desk, three linked panels, calm hierarchy, white background, blue accent, no logo, no text`

如果用户明确要“好看一点”，优先用画面路线重写 prompt，而不是继续堆概念词。

## 用户截图保全

用户提供截图时，先做截图清点表，再决定是否入文。

截图追踪顺序：

1. 当前收件箱源 note 的 `![[...]]` wiki embed
2. `00_收件箱/附件待归档/` 中同名或近似文件
3. 素材池 `assets/` 或 `source.md` 记录
4. 已有发布包 `images/`
5. 若仍找不到，记录搜索命令、候选路径和阻塞原因

只要文章以截图事件切入，默认处理结果必须是“入文”或“用户确认跳过”，不能默认“转文字后跳过原图”。

截图清点表至少包含：

| 序号 | 来源位置 | 文件/链接 | 内容识别 | 处理结果 | 文章位置/跳过理由 |
|---|---|---|---|---|---|

硬规则：

- 不能静默丢失
- 收件箱有几张截图，清点表就必须有几行
- 要记录已使用 / 转化参考 / 仅归档 / 明确排除
- 如果被文章使用，必须同步到最终引用链路
- 如果不入文，必须写清楚原因，例如重复、低清、无关、版权风险、只作事实线索
- 发布前做数量对账：已使用 + 仅归档 + 跳过 = 原始截图总数

## 图片路径硬规则

- 正文插图必须放在 `publish-packages/images/` 子目录
- HTML 只引用 `images/文件名.png` 这类相对路径
- 不把正文插图放在发布包根目录
- 远端 runner 上传结果里必须能看到 inline image uploads；否则不算完成

## 正文插图尺寸规则

正文插图默认不要撑满整篇宽度。公众号正文是文字主导，图片服务证据和节奏，不抢正文面积。

尺寸真相源是：`content-factory/版式系统/wechat-layout-config.json`。生成或改动发布 HTML 后，运行：

```bash
python3 -X utf8 "scripts/apply_wechat_layout_config.py" --root "your-vault" "content-factory/publish-packages/YYYY-MM-DD_主题/content.html"
```

图片尺寸分类：

- `normal_illustration`：普通正文插图，默认 `82% / 520px`
- `screenshot_thumbnail`：截图、聊天记录、网页截图、后台截图等证据图，默认 `42% / 300px`，让读者知道来源，细节点击放大
- `detail_readable`：价格表、排名表、关键结构图等正文必须直接读细节的图片，才允许 `68% / 460px`，并记录理由
- `full_width_allowed`：横向结构复杂且缩小不可读时才用，必须记录理由

默认样式：

```html
<img src="images/xxx.png" style="display: block; width: 82%; max-width: 520px; height: auto; margin: 0 auto; border-radius: 14px; border: 1px solid #E3EDF7;" />
```

截图、价格表、后台页面这类信息密集图，默认按“可点击缩略证据图”处理：正文只让读者大概知道有这个证据，详细内容交给点击放大查看。

```html
<img src="images/xxx.png" style="display: block; width: 42%; max-width: 300px; height: auto; margin: 0 auto; border-radius: 10px; border: 1px solid #E3EDF7;" />
```

只有当图片本身承担正文阅读任务（例如关键价格表、横向结构图、缩小后无法理解核心信息），才允许使用 `detail_readable` 尺寸：`width: 68%; max-width: 460px`，并在图注或素材池记录可读性理由。

只有当图本身是横向结构图、信息过多且缩小后不可读，才允许使用 `width: 100%; max-width: 640px`，并在图注或素材池记录原因。

## 顶部卡片语义规则

公众号正文里的顶部视觉卡片不是标题重复区。

如果微信后台或页面顶部已经显示文章标题，HTML 正文内不要再次用大字号重复同一个标题。顶部卡片只能承担以下角色之一：

- 金句卡：提取全篇最有传播力的一句话
- 导语卡：浓缩文章主判断，但不能逐字等于标题
- 观点卡：用一句新表达承接正文，不重复标题

内容索引不是顶部金句卡。若需要内容索引，应作为独立 `content-index` 组件放在金句/导语卡之后，默认使用目录型索引：列出全篇分几部分、每部分讲什么、解决什么读者问题。

顶部卡片选择规则：

- 优先选正文中已经存在的强判断句
- 其次从正文主结论改写一句 20-35 字金句
- 不把标题原样复制进卡片
- 如果没有合适金句，宁可取消卡片，不硬塞标题

作者、日期、原创等元信息只出现一次。

如果微信后台标题区已经显示作者和日期，正文 HTML 卡片内不要再重复“作者 · 日期”。如模板需要署名，只保留正文内唯一一处，不做双重展示。

## 微信版式基线

优先复用既有模板，不现场发明新样式：

- canonical template：`版式系统/templates/作者商业评论.inline.html`
- accepted reference：`2026-05-10_怎么判断AI培训是不是割韭菜_公众号后台粘贴版.html`

## 关键样式约束

- 外层宽度：680px
- 正文色：`#2F3437`
- 蓝色强调：`#0F4C81`
- 点缀色：`#D88A4A`
- 行高：`1.72`
- 段落间距：从 `margin: 0 0 5px` 开始
- 小节标题：`data-component="section-title"`

## 强调句规则

使用：

```html
<strong style="font-weight: 800; color: #0F4C81;">重点句</strong>
```

每篇 3-5 句即可，不要整篇染蓝。

## 工作台标记清理

生成 HTML 前必须清理草稿工作标记：`📍`、`✏️`、`⚠️`、残留的 `️`、批注前缀、内部说明。小标题和段落开头不得保留这些标记。
