# 发布收尾检查单

用于发布前后最后一轮闭环检查。

## 发布前

至少检查：

- 标题已锁定，并且候选标题、推荐理由、参考来源已有记录
- 标题已同步到发布版 Markdown、`article.json`、公众号 HTML 标题区、发布包 HTML 和草稿标题 / 手动发布清单
- 发布版 Markdown 已更新
- HTML 粘贴版已更新
- 发布包已更新
- cover.png 来自配图区正式版本或已有明确封面建议，且封面只锁定 1 张
- 正文配图已完成二选一：`发布包/images/` 已有实际资源，或 `article.json.visual_assets.skip=true + reason`
- 如果文章需要多张正文图，`发布包/images/` 和 HTML 已引用全部选中图片
- `article.json` 已记录 visual_assets
- 固定链接或延伸阅读链接完整

## 预检

公开版不强制固定脚本，但预检至少覆盖：

- package id 存在
- title 存在且同步
- publish version 存在
- HTML 存在
- cover 或 cover decision 存在
- body-image decision 完成，且已明确正文图是多选落位还是跳过
- source closeout target 明确
- draft-box API 依赖已判断

仅当预检 ready 时进入草稿箱创建或手动发布包交付。

## 草稿箱创建

如果用户有公众号 API 权限：

- 创建前先确认凭据来源和权限
- 创建前先确保本地发布包已完成
- 创建后记录 draft id / media id / run result 等信息

如果用户没有公众号 API 权限：

- 不创建远端草稿
- 输出手动发布包
- 保留人工检查清单

## 草稿创建后

必须核对：

- draft id 或等价草稿记录
- cover upload 状态，如果启用了上传
- updated 时间
- run result 路径或日志
- 单篇发布控制页是否同步，如果项目有控制页
- 若来源于 inbox / source note，源文件是否已回写：
  - `publish_flow_status`
  - `package_id`
  - `publish_note`
  - `publish_version`
  - `publish_flow_updated`
  - `## 处理状态`

## 最终人工确认

提醒用户去微信后台核对：

- 标题
- 封面
- 开头
- 配图
- 排版
- 事实与链接
- IP / 版权风险
- 最终是否正式群发

## 正式发布后归档

只有在用户回填 `published_url`，或明确确认公众号后台已经正式发布后，才执行已发布归档。

归档时建议同步：

- publish notes：写入 `published_url`、`published_at`，并切到已发布状态
- `已发布/YYYY-MM/主题.md`：保存最终内容资产
- `已发布/README.md`：补充归档索引
- 已发布文章链接索引：补充正式链接

不要把“草稿已创建”当成“已发布归档”。

## 不得误报完成

除非用户给出最终发布 URL 或明确说已在后台发布，否则不能声称“已正式发布”。

## 收件箱收尾边界

- 自动回写状态：允许
- 自动补充链路链接：允许
- 覆盖内容编译器或其他上游系统的 `status`：禁止
- 自动删除原收件箱笔记：禁止
- 自动移动原收件箱笔记：默认禁止，除非另有明确归档规则
