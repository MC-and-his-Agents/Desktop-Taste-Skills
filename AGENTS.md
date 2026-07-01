# AGENTS.md

本文件只约束本仓库中 Desktop Taste Skills / plugin 的开发方向。它不是需求文档、研究记录或待办池。

## 方向性约束

- 所有变更都必须服务于一个目标：让 coding agent 生成更高质量的 macOS / Windows 桌面应用 UI/UX。
- 本仓库开发的是 SKILLS / plugin 本体，不是用户项目、示例应用或通用桌面开发框架。
- 优先沉淀 agent 可执行的设计判断、分析方法、反模式、预检清单和实现指导；不要写泛泛的设计文章。
- 始终保持桌面应用视角：窗口、标题栏、工具栏、侧边栏、面板、表格、命令面板、焦点、选择状态、键鼠路径、信息密度、原生感和交互手感。
- 只面向 macOS 和 Windows；不要扩展到 Web、Mobile、Linux 或纯品牌设计，除非用户明确要求。
- 不要把本仓库扩展成 Electron / Tauri / SwiftUI / WinUI / 后端 / 发布 / 签名 / 安装工程手册；工程内容只在影响 UI/UX 可实现性时保留。
- `DESIGN.md` 是插件可生成的用户项目输出物；本仓库只定义生成和使用它的方法，不把 DESIGN.md 风格库当作核心产品。
- 新增或修改 Skill 时，必须保证它单一职责、可触发、可执行，并能真实改变 agent 的设计或实现行为。
- Skill 内容应直接约束 agent 如何分析、设计、实现和检查桌面 UI；避免堆概念、堆研究结论或重复 README。
- 默认使用中文撰写仓库文档；保留必要的英文标识符、frontmatter key、API 名、代码和命令名。
- 编辑后检查 `git status --short`，确认只包含有意变更。
