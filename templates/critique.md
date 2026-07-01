# 桌面评审模板

用于审计 macOS / Windows 桌面 UI 的输出格式。它优先给出可修复发现，不堆研究材料，不写营销审美点评。

## 使用规则

- 发现优先：先列影响用户或实现的具体问题；没有问题时明确写 `无阻断发现`。
- 每条发现必须包含证据、影响和最小修正。
- 只评审桌面 UI/UX：窗口结构、平台感、布局、排版密度、交互状态、真实数据承载和长期使用。
- 不把 Web landing、Mobile、品牌官网、发布工程、打包签名或后端架构混入评审。
- 严重度保持稳定：`P0` 阻断使用，`P1` 明显破坏核心工作流，`P2` 降低质量或可维护性，`P3` 小修小补。

## 输出格式

```text
Desktop Critique:
- source: <screenshot / running app / code path / PR / DESIGN.md>
- scope: <本次评审覆盖的窗口、流程或组件>
- platform: <macOS / Windows / cross-platform>
- desktop_read: <引用 Desktop Read 的关键判断；没有则写 assumptions>
- verdict: <pass / needs work / fail>

Findings:
1. [P1] <area>: <问题一句话>
   - evidence: <看到的具体界面、代码或行为>
   - impact: <对桌面工作流、平台感、可读性、状态或真实数据的影响>
   - fix: <最小可行修正>

2. [P2] <area>: <问题一句话>
   - evidence: <具体证据>
   - impact: <具体影响>
   - fix: <最小可行修正>

What works:
- <保留的窗口结构、工作流、状态或视觉判断>

Desktop Checks:
- native_feel: <pass / needs work / fail + note>
- layout_composition: <pass / needs work / fail + note>
- typography_density: <pass / needs work / fail + note>
- motion_interaction: <pass / needs work / fail + note>
- state_completeness: <pass / needs work / fail + note>
- real_data_readiness: <pass / needs work / fail + note>
- brand_expression: <pass / needs work / fail + note>

Out of scope:
- <本次未评审的非桌面、工程、发布或业务范围>

Next:
- <最小修正顺序；不超过 3 条>
```

## 发现区域

- `window`: 窗口角色、标题栏、toolbar、菜单、系统窗口控制。
- `native feel`: 平台习惯、快捷键、context menu、focus ring、系统主题。
- `layout`: sidebar、split view、Inspector、bottom panel、status bar、真实数据布局。
- `typography`: 字号层级、行高、表格/列表密度、metadata、状态和错误文案。
- `spacing`: 留白、对齐、面板间距、命中目标和窗口缩放。
- `interaction`: hover、focus、selected、active、disabled、drag、resize、keyboard path。
- `states`: loading、empty、error、success、offline、permission、undo/redo。
- `data`: 长文本、0/1/10/100+ 条记录、多选、排序、筛选、溢出。
- `brand`: accent、semantic color、材质、图标、empty state、microcopy、signature moment。

## 护栏

- 不用总分掩盖问题；分数可省略，发现不可省略。
- 不把个人偏好写成结论；必须连接到桌面工作流或平台预期。
- 不建议“大改全部视觉系统”，除非 P0/P1 证明当前结构无法承载任务。
- 不把 hero、CTA、landing sections、marketing card grid 当成桌面改进建议。
- 修正建议优先最小路径：改共享状态语义、窗口结构或密度规则，而不是重做整套 UI。
