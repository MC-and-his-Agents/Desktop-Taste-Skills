# 桌面 Anti-Slop 检查清单

用于 macOS / Windows 桌面应用的 audit 和 redesign。先确认目标平台、应用类型、信息密度和主要交互方式，再逐项记录 `通过 / 失败 / 证据 / 最小修正`。不要把它当视觉偏好表；只有影响桌面可用性、信息密度或平台感时才标记失败。

## 使用方式

1. 引用已有 Desktop Read；没有时先补齐平台、用户、场景、密度和主要风险。
2. 用真实窗口和真实数据检查：空态、1 条、10 条、100+ 条、长名称、错误、加载、多选和窗口缩放。
3. 每个失败项给出最小修正方向；redesign 只扩展已失败的项，不新增无关范围。
4. 若出现阻断项，不要标记桌面 UI 已就绪。

## 检查清单

| 反模式信号 | 失败判定 | 最小修正方向 |
| --- | --- | --- |
| `Web dashboard inside desktop window` | 主界面只是 KPI 卡片、图表摘要或后台 dashboard；用户无法围绕对象选择、编辑、比较、排错或执行命令。 | 改成匹配工作流的桌面布局：sidebar / split view / table / inspector / status bar；让主对象、主动作、过滤和状态同屏可用。 |
| `landing page inside app` | 应用窗口出现 hero、营销文案、巨大标题、feature cards、过度留白或装饰渐变，真实任务入口被推到下方。 | 用任务工作区替代 hero：窗口标题、toolbar、主列表/表格/画布、紧凑空态和一个主要动作。 |
| `generic cards` | 所有内容都被包进相同圆角卡片，卡片只提供装饰边界，不能表达选择、层级、批量操作或平台控件。 | 先换成 list / table / tree / split pane / inspector；只在重复对象确实需要独立边界时保留卡片。 |
| `low-density table` | 表格行高、内边距或列间距过大；一屏看不到足够记录；缺少排序、筛选、选择、状态、错误或批量路径。 | 降低行高并收紧列；补齐表头、排序/筛选、选中态、键盘行导航、空态/错误态和必要的横向溢出策略。 |
| `no keyboard path` | 关键任务只能鼠标完成；Tab 顺序、方向键、快捷键、`Esc`、type-ahead 或 command palette 缺失。 | 为核心任务定义键盘路径：Tab 到控件、方向键移动列表/表格、Enter 执行、Esc 取消/关闭、平台快捷键触发高频命令。 |
| `no focus state` | 键盘移动时当前位置不可见，或 focus 只复用 hover 样式；高对比/深色模式下焦点消失。 | 使用平台风格 focus ring 或等效焦点层；逐屏测试键盘遍历，保证焦点不被裁切、不被 hover 覆盖。 |
| `no selected/active distinction` | hover、focus、selected、active、disabled 使用同一种颜色或 opacity；窗口失焦后当前选择无法识别。 | 明确状态语义：selected 表示持久选择，active 表示按下/执行中，focus 表示键盘位置，hover 只表示指针经过。 |
| `platform-neutral` | macOS 和 Windows 共用一套窗口控制、菜单、快捷键、焦点、滚动条、字体和 dialog 行为，结果两边都不像桌面应用。 | 写明平台策略：macOS 优先、Windows 优先或 cross-platform 折中；保留对应窗口 chrome、菜单/命令、快捷键、系统字体、accent、reduced motion 和 high contrast。 |

## 审计输出模板

```text
Desktop Anti-Slop:
- target: <screen/window/flow>
- platform_strategy: <macOS / Windows / cross-platform>
- density: <calm / standard / dense / control-room>
- result: <pass / fail>
- blockers:
  - <signal>: <evidence> -> <minimum fix>
- redesign_scope:
  - keep: <保留的桌面结构或行为>
  - change: <只改失败项>
  - avoid: <不要扩大到品牌、工程或无关页面>
```
