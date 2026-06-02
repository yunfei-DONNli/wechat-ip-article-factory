# 公众号文章执行可靠性规则

这份规则处理文章质量之外的工程执行问题：路径、预检、图片降级、双源交接、修订学习和历史链接失败处理。

## 1. 路径落点规则

当前工作目录通常是 `/path/to/your-workspace`，真实 vault 根是 `your-vault/`。

所有内容工厂文件必须写到：

```text
content-factory/...
```

不要在当前工作目录下直接写：

```text
content-factory/...
```

第一批文件写入后必须立即验证物理落点，例如：

```bash
find "content-factory" -path "*YYYY-MM-DD_主题*" -maxdepth 6 -print
ls -la "content-factory/publish-packages/YYYY-MM-DD_主题"
```

如果发现同一主题同时出现在 `50_资源/...` 和 `your-vault/50_资源/...`，先停下整理 source of truth，不要继续生成发布包。

最终回复的相关产物同步检查中要报告：

- source of truth 路径
- 成稿区路径
- 发布版路径
- 发布包路径
- 是否存在错误落点

## 2. article.json 字段前置

生成 `article.json` 前，先看 `publish_precheck.py` 的字段依赖，不要靠记忆补字段。

最小字段必须包含：

```json
{
  "package_id": "YYYY-MM-DD_主题",
  "status": "ready_for_draft",
  "title": "...",
  "author": "作者",
  "digest": "...",
  "content_file": "content.html",
  "cover_file": "cover.png",
  "source_note": "...",
  "publish_note": "...",
  "allow_auto_publish": false,
  "visual_assets": {
    "cover": "...",
    "body_images": [],
    "skip": false,
    "reason": ""
  },
  "truth_check": {
    "triggered": true,
    "research_brief": "...",
    "publish_preflight_review": true,
    "unverified_claims": [],
    "downgraded_claims": [],
    "central_unverified_blockers": [],
    "human_confirmation_required": []
  }
}
```

正文有本地图片时，`visual_assets.body_images[]` 每项还必须写：

- `path`
- `type`
- `purpose`
- `position`

建议在发布包骨架完成后先跑一次预检，让缺字段早暴露；最终 HTML、封面、正文图和发布记录都完成后再跑最终预检。

## 3. 图片生成可用性前置

生成封面或正文插图前，先做一次图片生成能力探测，不要连续尝试多个不可用 skill。

作者私有公众号工作流的首选 AI 生图通道是：

```bash
python3 -X utf8 "scripts/image2_generate.py" \
  --prompt-file "content-factory/visual-assets/YYYY-MM-DD_主题/image-prompts.md" \
  --section "封面" \
  --output "content-factory/visual-assets/YYYY-MM-DD_主题/cover.png" \
  --size "1536x864"
```

必需运行时环境变量：

```text
IMAGE2_API_KEY=本机私有凭据，不写入 vault / skill / git
IMAGE2_BASE_URL=<your-image-api-base-url>
IMAGE2_SUBMIT_PATH=/v1/images/generations
IMAGE2_STATUS_PATH_TEMPLATE=/v1/images/generations/{task_id}
IMAGE2_MODEL=gpt-image-1
```

如果用户在对话中提供 image2 key 和 base URL，agent 应把它落到本机私有环境，而不是只留在聊天上下文里。允许写入的位置只有：

```text
~/.config/orbitos/secrets/image2.env
```

写入要求：

- 文件权限必须是 `600` / `-rw-------`。
- 只写环境变量，不写入 vault、skill、发布包、文章、日志、git。
- 同步追加到 `~/.zshrc` 的只能是 source 语句，不直接写 key。
- 可用 `launchctl setenv` 注入当前 macOS GUI 会话，但最终回复不得回显真实 key。
- 验证时只输出 `SET`、长度、base URL、submit path，不输出 key 原文。
- 已运行中的 Claude Code / Codex 可能读不到新变量，需提醒重启或新开 agent。

推荐配置命令形状：

```bash
mkdir -p "$HOME/.config/orbitos/secrets"
umask 077
cat > "$HOME/.config/orbitos/secrets/image2.env" <<'EOF'
export IMAGE2_API_KEY='...redacted...'
export IMAGE2_BASE_URL='<your-image-api-base-url>'
export IMAGE2_SUBMIT_PATH='/v1/images/generations'
export IMAGE2_STATUS_PATH_TEMPLATE='/v1/images/generations/{task_id}'
export IMAGE2_MODEL='gpt-image-1'
EOF
chmod 600 "$HOME/.config/orbitos/secrets/image2.env"
```

检查顺序：

探测逻辑不是“找 agent 认识的标准 API”，而是“先找 OrbitOS 已配置的可用图片生成能力”。作者私有工作流中，`~/.config/orbitos/secrets/` 是优先探测范围。

1. 先检查 OrbitOS 私有基础设施路径；只允许检查文件是否存在、权限和变量名是否 `SET`，不得打印 key：
   - `~/.config/orbitos/secrets/image2.env`
   - `~/.config/orbitos/secrets/*image*.env`
   - `~/.config/orbitos/secrets/*generate*.env`
2. 再检查当前环境中的 `IMAGE2_API_KEY`。如果当前 shell 没有变量，但 `image2.env` 存在，应在子 shell 中先 `source ~/.config/orbitos/secrets/image2.env`，再运行 `image2_generate.py --dry-run` 或正式生成。不要因为当前 shell 缺少变量就降级到 Pillow。
3. 确认 `IMAGE2_BASE_URL` 和提交路径；缺省按 `<your-image-api-base-url>` 与 `/v1/images/generations`。
4. 用 `--dry-run` 或小图 prompt 做一次轻量探测；不要输出或记录真实 key。
5. image2 不可用时，再检查用户明确指定的其他图片 API / 脚本。
6. 都不可用时，直接降级：
   - 使用用户截图 / 既有素材
   - 生成程序化封面（Pillow / HTML / SVG）
   - 或明确记录“本篇仅用截图证据，不生成 AI 插图”

降级不是失败，但必须写进视觉决策和 publish-notes。不要把 3 个图片 skill 都试失败后才降级。也不要因为当前 shell 缺少 `IMAGE2_API_KEY` 就认定用户没有 image2；应说明“当前运行时未加载 image2，但已检查 OrbitOS secrets 路径 / 或记录未发现该路径”。

图片生成可用不等于封面有效。若 image2 已可用但首版封面偏抽象、偏装饰、和正文内容不贴合，不要归因于 API；应先回到文章的三个核心元素重写 prompt，例如“主题对象 / 关键场景 / 读者应该记住的判断”。封面 prompt 必须从文章内容锚定出发，再选择视觉路线，不能先堆“network nodes / data panels / abstract charts / professional feeling”这类泛专业词。

## 4. 修订学习不可跳过

只要用户对候选稿或发布稿做了关键修改，就必须保存 AI 原稿和用户终稿，并在发布包 ready 前生成：

- `revision-diff.md`
- `revision-learning.md`

关键修改包括但不限于：

- 标题被用户替换
- 开头被用户重写
- 用户补入个人经历、年龄、身份、利益相关、现场感
- 用户把居高临下的判断改成自我警告或自我坦白
- 用户删掉 AI 腔、模板句、空泛升维

例如“按年龄算我也到了别人眼中的老登阶段”这类自我坦白段，必须进入 `revision-learning.md`，因为它是跨篇可复用的信任策略。WorkBuddy 文章里的标题替换、“上周我跑了一个新工具”、“专家管理”等用户修订，同样属于必须沉淀的跨篇学习信号。

没有明显差异时也不能空文件结束，按 `revision-learning-quality.md` 记录 `no-signal`、keep / avoid / watch。

发布包 ready / 远端草稿前必须做一次修订学习状态检查：

- 如果存在 AI 原稿 + 用户终稿：必须生成 `revision-diff.md` 和 `revision-learning.md`。
- 如果用户明确修改过标题、开头、个人锚点、核心概念或表达方式，但文件链路里缺少用户终稿：先补保存用户终稿，再生成学习文件。
- 如果确实没有用户修订：在候选稿 / publish-notes / 最终同步检查中记录 `no-user-revision`，不能留空。
- 不得因为已经进入“成稿发布 / 草稿箱”阶段就跳过修订学习；这是发布前 gate，不是发布后复盘项。

## 5. 双源初稿交接不可简化

只要正文由 Claude Code / Multica / 外部 agent 参与，必须走正式 handoff：

```bash
python3 -X utf8 "scripts/check_multica_handoff.py" \
  --root "your-vault" \
  --issue "DON-xx" \
  --handoff "content-factory/协作扩写/workbench/YYYY-MM-DD_主题/handoff.md"
```

没有 `handoff.md` 或脚本未返回 `ready_to_collect`，不得声称双源流程规范完成。

如果用户或流程要求“双源初稿”，但实际只 spawn 了 Claude Code / Multica agent、没有创建 `handoff.md`、没有运行校验脚本，必须记录为 `handoff_not_completed`，不能写成 Gate 已通过。正文质量好不等于交接合规。

本地无真实 Multica issue 时，仍应创建本地 `handoff.md`，至少记录 Codex 稿路径、Claude Code 稿路径、融合依据、已改文件、阻塞项，并运行能覆盖本地文件存在性的等价检查；否则成稿发布前必须在相关产物同步检查中列为阻塞或明确例外。

## 6. Startup Links 失败处理

历史链接刷新失败时，必须区分三种情况：

- 后台 / CDP / 登录不可用，但文章不依赖最新链接：记录原因，沿用现有链接池。
- 文章依赖最新历史文章链接：提示用户打开浏览器、登录公众号后台或启动 CDP，再重试。
- 用户不想中断：继续写作，但在 publish-notes 中记录“历史链接池未刷新”。

不能只写“失败”然后假装已刷新；也不能在需要最新链接时静默沿用旧索引。
