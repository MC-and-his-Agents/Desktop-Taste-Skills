# Desktop Taste Skills 目标状态能力清单

## 1. 插件核心能力

### 1.1 桌面 UI 任务识别能力

插件应能识别用户任务是否属于桌面应用 UI/UX 场景。

应触发的场景包括：

- 设计 macOS / Windows 桌面应用界面
- 优化 Electron / Tauri / SwiftUI / AppKit / WinUI / WPF 应用 UI
- 重设计已有桌面应用
- 让界面更原生、更有品味、更不像网页壳
- 生成桌面应用设计规范
- 优化局部桌面 UI：侧边栏、工具栏、设置页、命令面板、表格、工作台、Inspector、状态栏等

不应触发的场景包括：

- Web landing page
- Mobile app
- 品牌官网
- 通用后端工程
- Electron / Tauri 工程架构问题
- 发布、签名、安装、自动更新等工程问题

---

## 2. 设计分析能力

插件必须要求 agent 在写 UI 之前先完成桌面设计判断，而不是直接开始写代码。

核心分析应覆盖：

- 目标平台：macOS、Windows、cross-platform
- 应用类型：工具、编辑器、工作台、启动器、控制台、数据库客户端、创作工具、AI workspace 等
- 用户类型：普通用户、专业用户、开发者、创作者、研究人员、运营人员等
- 使用场景：短任务、长时间工作、频繁切换、后台监控、批量处理、深度创作
- 信息密度：calm、standard、dense、control-room
- 主要交互：鼠标优先、键盘优先、command-first、drag-and-drop、multi-window、multi-pane
- 设计风险：网页壳、dashboard 化、过度留白、假高级感、平台感缺失、状态缺失

核心输出可以是：

```text
Desktop Read:
This is a <macOS / Windows / cross-platform> <app archetype>
for <user role>,
used in <session context>,
with <density level>,
where the interface should feel <design thesis>,
not like <anti-pattern>.
```

---

## 3. Art Direction 能力

插件不能只让 agent 做出“干净现代”的平均 UI，而要让它提出明确设计主张。

应提供能力：

- 为桌面应用提出 2–3 个不同设计方向
- 判断哪个方向最适合产品
- 明确这个应用应该“像什么”，不应该“像什么”
- 定义视觉气质：calm、technical、studio-grade、native、industrial、editorial、premium、focused
- 定义一个或多个 signature moment
- 防止 agent 只做安全、普通、模板化设计

每个 art direction 至少应包含：

- 设计主张
- 适用场景
- 不适用场景
- 布局策略
- 字体策略
- 密度策略
- 动效策略
- 品牌表达方式
- 典型反模式
- signature moment

---

## 4. 桌面原生感能力

插件应帮助 agent 判断界面是否像真实 macOS / Windows 应用，而不是网页包壳。

应覆盖：

- 窗口结构
- 标题栏
- 工具栏
- 菜单栏 / 应用菜单
- 右键菜单
- 弹窗、sheet、dialog、popover
- 侧边栏
- split view
- inspector
- 状态栏
- 系统主题
- 系统 accent color
- reduced motion
- high contrast
- 键盘焦点
- hover / focus / selected / active / disabled 状态
- 拖拽反馈
- 加载、空状态、错误状态

目标不是机械复制 Apple / Microsoft 规范，而是让 agent 能判断：

```text
这个 UI 为什么不像桌面应用？
这个模式应该更接近 macOS、Windows，还是做跨平台折中？
哪些部分应该保留原生习惯？
哪些部分可以表达产品自己的设计语言？
```

---

## 5. 布局与构图能力

插件应提供桌面应用布局判断能力，避免默认 card grid、dashboard、网页式页面结构。

应支持的布局类型包括：

- utility window
- sidebar app
- two-pane split view
- three-pane workspace
- inspector layout
- command-first layout
- editor workbench
- creative canvas
- data cockpit
- monitoring console
- settings window
- tray / menu bar style popover
- multi-document interface
- tabbed workspace

应指导 agent 判断：

- 何时使用侧边栏
- 何时使用 split view
- 何时使用 inspector
- 何时使用 toolbar
- 何时使用 bottom panel
- 何时使用 command palette
- 何时使用 table / list / tree
- 何时需要 status bar
- 何时需要多窗口或多文档结构
- 如何避免桌面空间浪费
- 如何让真实数据填充后仍然成立

---

## 6. 字体、间距、密度能力

插件应提供桌面应用的 typography、spacing 和 density 判断能力。

应覆盖：

- app title
- window title
- toolbar label
- section label
- sidebar item
- body text
- metadata
- table text
- list row text
- code / log text
- caption
- status text
- error text

应提供密度判断：

- calm：写作、阅读、轻工具
- standard：通用生产力应用
- dense：开发者工具、数据工具、研究工具
- control-room：监控、运维、交易、日志、分析面板

应避免：

- 网页 landing page 式大标题
- 过宽行距
- 过大留白
- 卡片之间空得像营销页
- 表格行高过大
- 小字号不可读
- 元信息层级混乱
- 所有文本都像 body copy

---

## 7. Motion 与交互手感能力

插件应区分“网页动效”和“桌面交互反馈”。

应覆盖：

- hover feedback
- focus movement
- selected state
- active state
- command palette reveal
- panel reveal
- inspector transition
- drag-and-drop feedback
- resize splitter behavior
- loading feedback
- task completion feedback
- error recovery feedback
- undo / redo feedback
- reduced motion fallback

原则：

- 桌面动效应服务操作确认、状态变化和空间理解
- 不应使用营销页式大面积滚动动效
- 动效应该快、清楚、克制
- 专业工具优先保证响应感和可预测性

---

## 8. 品牌表达能力

插件应让品牌感进入桌面应用，而不是把应用做成营销页面。

应覆盖：

- app icon language
- accent color
- illustration style
- empty state tone
- onboarding tone
- command palette personality
- loading state
- signature interaction
- window material
- microcopy
- semantic color rules
- product-specific visual motifs

应避免：

- 品牌色到处乱用
- 大渐变背景
- 过度玻璃拟态
- hero section 化
- marketing copy 进入工具界面
- 品牌表达压倒可用性

---

## 9. 桌面反模式识别能力

插件应有强 anti-slop 能力，阻止 agent 生成常见低质桌面 UI。

必须识别和避免：

- Web dashboard inside desktop window
- landing page inside app
- giant hero inside application UI
- generic rounded cards everywhere
- 3-column SaaS card grid
- fake glassmorphism
- low-density tables
- no real data state
- empty state 好看但 populated state 不可用
- sidebar as website navigation
- command palette as modal form
- no keyboard path
- no focus state
- no selected / active distinction
- platform-neutral UI that feels native nowhere
- brand decoration without product meaning
- overly safe “clean modern” average design

---

## 10. Redesign / Audit 能力

插件应能用于已有桌面应用的设计审计和重设计。

应能分析：

- 为什么这个界面像网页壳
- 为什么这个界面像 demo
- 为什么这个界面不够专业
- 为什么这个界面信息密度不对
- 为什么这个界面平台感不足
- 为什么这个界面品牌感弱
- 为什么这个界面真实数据下会崩
- 哪些状态缺失
- 哪些交互不符合桌面习惯

应输出：

- 问题诊断
- redesign direction
- 保留什么
- 改什么
- 不该改什么
- 最小可行改法
- 高水平改法
- 实现后检查项

---

## 11. DESIGN.md 生成能力

插件应能在用户需要时生成桌面版 `DESIGN.md`。

`DESIGN.md` 是用户项目中的输出物，不是插件本体。

桌面版 `DESIGN.md` 应覆盖：

```markdown
# DESIGN.md

## 1. Desktop Design Thesis
## 2. Platform Targets
## 3. Window & Surface System
## 4. Layout Grammar
## 5. Typography
## 6. Spacing & Density
## 7. Color & Materials
## 8. Components
## 9. Motion & Interaction Feel
## 10. Brand Expression
## 11. Anti-Slop Rules
## 12. Agent Implementation Guide
```

它应记录：

- 当前桌面应用的设计主张
- macOS / Windows 平台策略
- 窗口和表面系统
- 布局语法
- 字体系统
- 间距和密度
- 颜色和材质
- 组件规则
- 状态规则
- 动效规则
- 品牌表达
- 反模式
- 后续 agent 应如何延续设计

它不应默认生成 Web 式内容：

- hero section
- CTA
- landing page sections
- responsive web breakpoints
- marketing card grid
- brand-site copywriting

---

## 12. 实现指导能力

插件不是只给设计建议，还要指导 coding agent 如何落地。

应提供：

- 实现前需要做哪些设计判断
- UI 代码应体现哪些层级
- 组件如何拆分才符合桌面结构
- 哪些状态必须实现
- 哪些交互路径必须考虑
- 哪些布局不应硬编码
- 表格、侧边栏、工具栏、命令面板等应如何变成可维护组件
- 如何在不破坏功能的情况下做 redesign

但不应变成完整工程手册。

---

## 13. 质量评估能力

插件应提供一套桌面 UI 质量评价维度，帮助 agent 在实现后自检。

建议维度：

```text
Native feel
Layout composition
Typography hierarchy
Spacing discipline
Interaction feel
State completeness
Information density
Brand expression
Visual originality
Real-data readiness
Long-session comfort
Signature moment
```

每个维度不一定都要打分，但 agent 应能据此判断：

```text
这个 UI 是只是能用，还是有品味？
它是否像真实桌面应用？
它是否能承载真实数据？
它是否适合用户每天长时间使用？
它是否有自己的产品气质？
```

---

# 插件应包含的内容

## 1. 插件入口说明

仓库应包含清晰的入口文档，说明：

- 这个插件是什么
- 它解决什么问题
- 它不解决什么问题
- 支持哪些平台
- 适合哪些 coding agent
- 何时使用
- 何时不要使用
- 如何安装或接入
- 如何在用户项目中使用

---

## 2. Plugin manifest

如果目标 agent 支持 plugin manifest，仓库应包含对应入口文件，例如：

```text
plugin.json
```

它应声明：

- 插件名称
- 插件描述
- 包含的 skills
- skill 路径
- 入口说明
- 资源路径
- 版本信息

manifest 只能声明真实存在的能力和路径，不能有占位字段或本机绝对路径。

---

## 3. Skills

目标状态下，插件至少应包含这些 Skill：

```text
skills/
  desktop-taste/
    SKILL.md

  desktop-art-direction/
    SKILL.md

  desktop-native-feel/
    SKILL.md

  desktop-layout-composition/
    SKILL.md

  desktop-typography-density/
    SKILL.md

  desktop-motion-interaction/
    SKILL.md

  desktop-brand-system/
    SKILL.md

  desktop-design-md/
    SKILL.md
```

每个 `SKILL.md` 应至少包含：

- name / description
- 触发条件
- 不适用场景
- 分析方法
- 最佳实践
- 反模式
- 实现指导
- preflight checklist
- 输出格式

---

## 4. Templates

插件应包含可复用模板，例如：

```text
templates/
  DESIGN.md
  desktop-design-read.md
  critique.md
```

模板不是需求池，而是 agent 可直接生成或复用的输出格式。

---

## 5. References

可选包含精简参考文件，但必须是 agent 可执行的规则，不是研究材料堆积。

例如：

```text
references/
  macos-design-notes.md
  windows-design-notes.md
  desktop-anti-patterns.md
```

每个 reference 应满足：

- 简短
- 可执行
- 面向 agent
- 不复制官方规范全文
- 不变成文章库

---

## 6. Examples

插件应包含少量高质量示例，展示如何使用它。

例如：

```text
examples/
  macos-research-workspace.md
  windows-developer-tool.md
  cross-platform-database-client.md
  desktop-design-md-output.md
```

示例应展示：

- 输入 prompt
- agent 应做的 design read
- 设计方向
- 关键 UI 决策
- 反模式检查
- 可选 DESIGN.md 输出

示例数量不宜过多，质量比数量重要。

---

## 7. Validation / Lint

目标状态下可以有轻量校验能力，确保插件自身结构正确。

可校验：

- 每个 skill 是否有 `SKILL.md`
- frontmatter 是否存在
- manifest 路径是否真实
- README 链接是否有效
- `DESIGN.md` 模板是否存在
- 是否出现明显占位内容
- 是否引入不支持平台

这不是自动测试框架，而是插件内容完整性检查。

---

# 总结

目标状态下，这个插件应该提供三类能力：

## 1. 设计判断能力

让 agent 在写 UI 前知道：

- 这是哪类桌面应用
- 应该是什么气质
- 应该遵守哪些平台习惯
- 应该使用什么布局和密度
- 应该避免哪些模板化模式

## 2. 设计落地能力

让 agent 在写 UI 时知道：

- 怎么组织窗口和面板
- 怎么处理字体、间距、状态、动效
- 怎么处理品牌表达
- 怎么避免网页壳和 dashboard 化
- 怎么让 UI 承载真实数据和长时间使用

## 3. 设计沉淀能力

让 agent 在必要时输出：

- redesign audit
- preflight critique
- desktop-aware `DESIGN.md`
- 后续 agent 可复用的设计规则

最终它应该成为：

> 一套让 coding agent 生成高水平 macOS / Windows 桌面应用 UI/UX 的品味插件，而不是一个桌面开发教程、需求池或设计文章合集。