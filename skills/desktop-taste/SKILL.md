---
name: desktop-taste
description: 识别 macOS 和 Windows 桌面 UI/UX 任务并路由到合适的桌面设计能力。
version: 0.1.0
---

# Desktop Taste 入口

这是 Desktop Taste Skills 的入口 Skill。它只负责判断任务是否属于 macOS / Windows 桌面应用 UI/UX，说明不适用边界，并把任务路由给后续能力。不要在这里展开完整专项规则。

## 触发条件

当用户要设计、实现、重设计、审计或文档化桌面应用 UI 时使用本 Skill。典型信号包括：

- macOS、Windows、Electron、Tauri、SwiftUI、AppKit、WinUI、WPF 桌面应用界面
- 让应用更原生、更像真实桌面软件、更不像网页壳
- 调整窗口、标题栏、工具栏、侧边栏、表格、Inspector、命令面板、设置页、状态栏
- 生成或维护桌面应用的 `DESIGN.md`
- 在写 UI 前判断平台、密度、布局、状态和交互风险

## 不适用场景

遇到以下任务时不要使用 Desktop Taste Skills；如果任务混合了桌面 UI 与非 UI 工程，只处理桌面 UI/UX 部分：

- Web landing page、营销站、品牌官网、SaaS 官网
- Mobile app、响应式移动页面、iOS / Android 原生移动界面
- 通用后端、数据库、API、认证、队列、部署、CI
- Electron / Tauri / SwiftUI / WinUI 的工程架构、打包、签名、发布、自动更新
- 纯品牌识别、logo、海报、社媒视觉，且没有桌面应用 UI 载体

边界处理：

- 用户只问工程问题：直接回答工程问题，不加载本插件。
- 用户问桌面应用里的品牌、文案或图标：只评估它们如何服务窗口、导航、状态和工作流。
- 用户要求 Web 和 Desktop 同时做：先拆出桌面应用 UI 目标，Web 部分交给对应能力。

## 固定入口流程

1. 先判断是否属于桌面 UI/UX。
2. 若属于，先运行 `desktop-design-read`，产出可引用的 Desktop Read。
3. 再按下方路由选择后续能力。若对应专项 Skill 尚未存在或未安装，只记录路由需求，不假装已经加载。
4. 最后实现、审计或文档化时，保持 macOS / Windows 桌面应用视角。

## 路由表

| 路由 | 触发条件 | 不适用条件 | 行动 |
| --- | --- | --- | --- |
| `audit` | 用户要求 review、critique、audit、检查现有桌面 UI | 只检查代码质量或性能 | 输出问题诊断、风险、最小修正路径 |
| `redesign` | 用户要求重设计已有桌面应用界面 | 没有现有界面或截图，且只要新建页面 | 先保留有效工作流，再提出改法 |
| `native feel` | 用户说不像原生、像网页壳，或涉及窗口、菜单、系统状态 | 纯工程选型或发布问题 | 聚焦平台习惯、窗口结构、输入反馈、系统状态 |
| `layout` | 涉及侧边栏、split view、Inspector、表格、工作台、信息架构 | 只是颜色或文案调整 | 判断桌面布局类型和真实数据承载能力 |
| `typography` | 涉及字号、层级、行高、密度、长时间阅读 | 只是品牌字体展示 | 校准桌面字号层级、信息密度和可读性 |
| `motion` | 涉及 hover、focus、selection、panel reveal、drag、loading、undo | 营销滚动动效或装饰动画 | 保证动效服务操作确认和空间理解 |
| `brand` | 涉及产品气质、accent color、empty state、图标语言、微文案 | 品牌站、logo 系统或广告视觉 | 让品牌表达进入桌面工作流，不压倒可用性 |
| `DESIGN.md` | 用户要求生成、更新或遵循桌面设计规范 | Web 设计规范或通用品牌手册 | 生成桌面应用设计契约，不生成模板目录 |

## 输出格式

先给出路由判断，再进入后续工作：

```text
Desktop Taste Routing:
- applies: yes/no
- reason: <一句话说明>
- desktop_read: required/skipped
- routes: <audit/redesign/native feel/layout/typography/motion/brand/DESIGN.md>
- out_of_scope: <不处理的非桌面范围>
```

如果 `applies: no`，停止使用本 Skill，并说明应改用什么能力或直接处理原问题。
