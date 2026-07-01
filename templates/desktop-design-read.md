# 桌面设计前置判断模板

用于在实现、重设计、审计或生成 `DESIGN.md` 前固定桌面设计判断。它是后续 Skill 的输入，不是视觉研究材料。

## 使用规则

- 先输出 Desktop Read，再写 UI 方案或代码。
- 信息不足时做保守判断，并在 `assumptions` 中标注。
- 字段名保持稳定，方便后续 Skill 直接引用。
- 只覆盖 macOS / Windows 桌面 UI；Web、Mobile、品牌官网和发布工程不进入本模板。

## 输出格式

```text
Desktop Read:
- platform: <macOS / Windows / cross-platform>
- app_archetype: <tool / editor / workbench / launcher / console / database client / creative tool / AI workspace / settings / tray popover>
- user_role: <普通用户 / 专业用户 / 开发者 / 创作者 / 研究人员 / 运营人员等>
- session_context: <短任务 / 长时间工作 / 频繁切换 / 后台监控 / 批量处理 / 深度创作>
- density: <calm / standard / dense / control-room>
- primary_interaction: <mouse-first / keyboard-first / command-first / drag-and-drop / multi-window / multi-pane>
- design_thesis: <一句话说明界面应该给人的工作感受>
- anti_pattern: <一句话说明明确不要像什么>
- main_risks:
  - <web shell / dashboard 化 / 过度留白 / 平台感缺失 / 状态缺失 / 真实数据下失效>
- next_routes:
  - <audit / redesign / native feel / layout / typography / motion / brand / DESIGN.md>
- assumptions:
  - <only if needed>
```

## 字段规则

- `platform`: 必须说明 macOS、Windows 或 cross-platform；cross-platform 仍需保留平台差异。
- `app_archetype`: 写真实桌面应用类型，不写“页面”“网站”“dashboard”。
- `session_context`: 决定密度、状态反馈和窗口持久化。
- `density`: 不因为“高级感”默认 `calm`；开发者工具、数据工具、控制台常用 `dense` 或 `control-room`。
- `primary_interaction`: 写主路径；可以组合，但不要把所有交互都列上。
- `design_thesis`: 必须具体到产品工作流，避免“干净现代、简洁高级”。
- `anti_pattern`: 明确拒绝 Web hero、CTA、landing sections、marketing card grid、SaaS dashboard 或网页壳。
- `main_risks`: 只列会影响实现或评审的风险。
- `next_routes`: 只列后续实际需要的 Skill 路由。
- `assumptions`: 只有信息不足时出现；不要把已知事实重复放入这里。

## 最小示例

```text
Desktop Read:
- platform: cross-platform
- app_archetype: developer workbench
- user_role: 开发者
- session_context: 长时间工作、频繁切换、多面板排错
- density: dense
- primary_interaction: keyboard-first, multi-pane
- design_thesis: 界面应像稳定的本地开发工作台，优先让命令、日志和当前对象保持可见。
- anti_pattern: 不要像 Web SaaS dashboard、landing hero 或卡片墙。
- main_risks:
  - 平台感缺失
  - 状态缺失
  - 真实日志和长路径下失效
- next_routes:
  - layout
  - typography
  - motion
- assumptions:
  - 目标平台未指定，先按 cross-platform 处理。
```

## 自检

- 是否先判断桌面应用类型，而不是网页页面类型。
- 是否明确密度、主要交互和平台策略。
- 是否给后续 Skill 留下可执行输入。
- 是否避免把输出写成 moodboard、研究摘录或泛泛设计原则。
