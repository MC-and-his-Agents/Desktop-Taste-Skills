# 变更记录

本文件记录对安装、升级和发布说明有影响的变更。每个版本保留以下分类：插件变更、Skill 变更、修复、破坏性变更、迁移要求。

## [0.7.0] - 2026-07-02

### 插件变更

- 新增 Desktop Visual Draft 能力：在缺少视觉目标或用户要求设计稿时，为 macOS / Windows 桌面应用生成 3 张独立 ImageGen 窗口设计稿。
- 将 selected visual draft 纳入桌面证据目标链路，后续 redesign、`DESIGN.md` 和 QA 可以引用它，但不得把它当作像素级实现规范。
- 更新插件说明和默认提示，加入 visual draft 路由与 selected visual draft 证据目标。

### Skill 变更

- 新增 `desktop-visual-draft@0.1.0`，定义设计稿触发边界、ImageGen prompt、尺寸、窗口状态、三方案输出和选择交接。
- 更新 `desktop-taste@0.4.0`，加入 visual draft 路由、target surface / draft state / draft dimensions 与 selected visual draft 证据目标。
- 更新 `desktop-design-read@0.4.0`，增加 `target_surface`、`draft_state`、`draft_dimensions` 字段，并扩展 `evidence_target` 与 `next_routes`。
- 更新 `desktop-art-direction@0.3.0`，输出 draft-ready brief 和 visual draft handoff 片段。
- 更新 `desktop-redesign@0.4.0`，消费 selected visual draft，并用 `adopt / adapt / reject` 防止照抄不可实现细节。
- 更新 `desktop-design-md@0.3.0`，记录 selected visual draft 的来源、适用窗口、选择理由和不可照抄边界。
- 更新 `desktop-qa@0.3.0`，增加 selected visual draft 与实现截图 / runtime evidence 的非 pixel-perfect 对齐检查。
- 新增 `templates/desktop-visual-draft.md`，并更新 Desktop Read、DESIGN.md、critique 和 anti-slop 模板的设计稿证据字段。

### 修复

- 无。

### 破坏性变更

- 无。

### 迁移要求

- 无。

## [0.6.0] - 2026-07-02

### 插件变更

- 增加 macOS Native Depth 能力：Desktop Taste 仍覆盖 macOS 与 Windows，但允许 macOS 侧更深，尤其是 Liquid Glass、SwiftUI scene/window、toolbar、sidebar、Inspector 和 AppKit 边界。
- 明确 Liquid Glass 是现代 macOS UI 的一等材料策略；它不是跨平台默认风格，也不能牺牲内容可读性、状态语义或真实工作流。
- 更新插件说明和默认提示，加入 macOS Native Depth 路由提示。

### Skill 变更

- 更新 `desktop-taste@0.3.0` 和 `desktop-design-read@0.3.0`，加入 macOS-first、Windows-first 和 cross-platform desktop 的平台深度判断。
- 更新 `desktop-native-feel@0.2.0`，加入 Liquid Glass、SwiftUI first 和 AppKit narrow bridge 规则。
- 更新 `desktop-layout-composition@0.2.0`，加入 macOS scene/window 角色、toolbar、sidebar、Inspector 和 command 取舍。
- 更新 `desktop-typography-density@0.2.0` 和 `desktop-motion-interaction@0.2.0`，加入 macOS source-list、Inspector、toolbar label、focus、command 和 panel reveal 规则。
- 更新 `desktop-brand-system@0.2.0`，加入 Liquid Glass / fake glass 材料护栏。
- 更新 `desktop-redesign@0.3.0` 和 `desktop-design-md@0.2.0`，加入窗口生命周期、AppKit 边界与所有权规则。
- 更新 `desktop-qa@0.2.0`，加入 macOS Native Depth 检查项，并要求不误伤 Windows 目标。

### 修复

- 无。

### 破坏性变更

- 无。

### 迁移要求

- 无。

## [0.5.0] - 2026-07-02

### 插件变更

- 引入桌面工作流门禁：Desktop Read 现在作为 brief gate，要求大范围 UI 变更前确认平台、目标窗口、真实数据、主要交互、证据目标和约束。
- 明确桌面视觉 / 证据目标规则：截图、运行中窗口、UI 代码路径、`DESIGN.md`、平台参考、用户描述或已选 art direction 可作为实现、审计、redesign 和 QA 的依据。
- 更新插件说明和默认提示，加入 post-implementation QA 路由。

### Skill 变更

- 新增 `desktop-qa@0.1.0`，用于桌面 UI 实现后交付前检查。
- 更新 `desktop-taste@0.2.0`，加入上下文复用、brief gate、证据目标和 QA 路由。
- 更新 `desktop-design-read@0.2.0`，加入 question / playback mode、hard boundary 和 `evidence_target` 字段。
- 更新 `desktop-art-direction@0.2.0`，允许在缺少视觉目标时作为已确认设计方向来源。
- 更新 `desktop-audit@0.2.0`，强化 evidence / limits / minimum fix 绑定。
- 更新 `desktop-redesign@0.2.0`，要求大范围 redesign 前具备桌面视觉 / 证据目标。

### 修复

- 无。

### 破坏性变更

- 无。

### 迁移要求

- 无。

## [0.4.0] - 2026-07-01

### 插件变更

- 新增桌面评审、重设计和 `DESIGN.md` 输出模板，覆盖 `templates/DESIGN.md`、`templates/desktop-design-read.md`、`templates/critique.md` 和 `templates/desktop-anti-slop.md`。
- 增强 CI 与本地校验：检查 Skill 内容结构，并新增干净安装树的插件发现冒烟测试。

### Skill 变更

- 新增 `desktop-audit@0.1.0`，用于审计已有桌面 UI 并输出问题诊断、保留项、修正项和实现后检查项。
- 新增 `desktop-redesign@0.1.0`，用于把审计诊断转成可实现的桌面重设计策略和实施顺序。
- 新增 `desktop-design-md@0.1.0`，用于生成或更新用户项目中的桌面版 `DESIGN.md`。

### 修复

- 安装冒烟测试现在会在存在 `templates/` 目录时检查模板目录和模板文件，避免模板路径空通过。

### 破坏性变更

- 无。

### 迁移要求

- 无。

## [0.3.0] - 2026-07-01

### 插件变更

- 发布第一批桌面专项 Skill，覆盖 art direction、native feel、layout、typography、motion 和 brand 六条路线。

### Skill 变更

- 新增 `desktop-art-direction@0.1.0`，用于提出 2-3 个桌面应用设计方向并定义设计主张。
- 新增 `desktop-native-feel@0.1.0`，用于判断 macOS / Windows 桌面应用是否像真实原生软件。
- 新增 `desktop-layout-composition@0.1.0`，用于选择桌面窗口布局类型、区域结构和关键组件取舍。
- 新增 `desktop-typography-density@0.1.0`，用于校准桌面应用排版、间距和信息密度。
- 新增 `desktop-motion-interaction@0.1.0`，用于设计和审查桌面动效、状态反馈与交互手感。
- 新增 `desktop-brand-system@0.1.0`，用于把品牌表达限制在桌面工作流和产品 UI 内。

### 修复

- 无。

### 破坏性变更

- 无。

### 迁移要求

- 无。

## [0.2.0] - 2026-07-01

### 插件变更

- 在 manifest 中声明真实存在的 `skills/` 目录。
- 更新插件说明和默认提示，使入口 Skill 与设计前置判断成为可发现能力。

### Skill 变更

- 新增 `desktop-taste@0.1.0`，用于桌面 UI/UX 任务识别、边界判断和路由。
- 新增 `desktop-design-read@0.1.0`，用于在实现、审计或生成 `DESIGN.md` 前产出桌面设计判断。

### 修复

- 无。

### 破坏性变更

- 无。

### 迁移要求

- 无。

## [0.1.0] - 2026-07-01

### 插件变更

- 建立 Desktop Taste 插件 manifest、README、愿景文档、版本规则和轻量 CI 校验入口。
- 补充安装、升级、校验和排障说明。

### Skill 变更

- 暂无已发布 Skill。

### 修复

- 无。

### 破坏性变更

- 无。

### 迁移要求

- 无。
