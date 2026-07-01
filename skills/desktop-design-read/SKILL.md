---
name: desktop-design-read
description: 在编写或修改桌面 UI 前产出可复用的桌面设计判断。
version: 0.1.0
---

# Desktop Design Read

在写 macOS / Windows 桌面 UI 代码、做重设计、审计或生成 `DESIGN.md` 前，先产出 Desktop Read。它是后续 Skill 和实现工作的设计输入，不是完整设计稿。

## 触发条件

- 入口 `desktop-taste` 判断任务属于桌面 UI/UX
- 用户要新建、修改、重设计或审计桌面应用界面
- 用户要求更原生、更专业、更有品味、更适合长期使用
- 需要生成或更新桌面应用 `DESIGN.md`

## 不适用场景

- Web landing、品牌官网、Mobile app
- 后端、发布、签名、安装、自动更新等工程问题
- 只修复不影响 UI/UX 的纯逻辑 bug
- 用户明确要求不要做设计判断，只要机械改动

## 判断维度

必须覆盖以下字段。信息不足时做保守推断，并标注 `assumption`：

- `platform`: macOS、Windows 或 cross-platform
- `app_archetype`: 工具、编辑器、工作台、启动器、控制台、数据库客户端、创作工具、AI workspace 等
- `user_role`: 普通用户、专业用户、开发者、创作者、研究人员、运营人员等
- `session_context`: 短任务、长时间工作、频繁切换、后台监控、批量处理、深度创作
- `density`: calm、standard、dense、control-room
- `primary_interaction`: 鼠标优先、键盘优先、command-first、drag-and-drop、multi-window、multi-pane
- `main_risks`: 网页壳、dashboard 化、过度留白、平台感缺失、状态缺失、真实数据下失效
- `design_thesis`: 这个界面应该给人的一句话感受
- `anti_pattern`: 明确不要像什么
- `next_routes`: audit、redesign、native feel、layout、typography、motion、brand、DESIGN.md 中的后续路由

## 输出格式

```text
Desktop Read:
- platform: <macOS / Windows / cross-platform>
- app_archetype: <type>
- user_role: <role>
- session_context: <context>
- density: <calm / standard / dense / control-room>
- primary_interaction: <interaction model>
- design_thesis: <one sentence>
- anti_pattern: <one sentence>
- main_risks:
  - <risk>
- next_routes:
  - <route>
- assumptions:
  - <only if needed>
```

## 使用规则

- Desktop Read 必须先于 UI 实现或 redesign 方案出现。
- 后续实现、审计和 `DESIGN.md` 必须引用 Desktop Read 的平台、密度、交互和风险判断。
- 不要把 Desktop Read 写成视觉风格库；它只决定方向和边界。
- 不要默认选择 `calm` 或大留白。开发者工具、数据工具、研究工具和控制台通常需要更高密度。
- 发现任务其实不是桌面 UI/UX 时，回到 `desktop-taste` 的不适用处理。

## 快速自检

交付前确认：

- 是否明确平台策略，而不是把 macOS 和 Windows 压成通用 Web UI
- 是否明确桌面应用类型和真实用户工作流
- 是否选择了合理密度
- 是否指出网页壳、dashboard 化、平台感缺失、状态缺失等主要风险
- 是否给后续路由留下可执行输入
