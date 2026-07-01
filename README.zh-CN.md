[English](README.md) | 中文

# Desktop Taste Skills

Desktop Taste Skills 是一个 Codex 插件，包含多项可移植的桌面 UI/UX 品味 SKILL，用于升级 AI 构建的 macOS 和 Windows 应用界面。

它帮助 Codex 产出更强的窗口构成、布局、排版、动态效果、间距、原生感、交互状态和产品表达，而不是千篇一律的模板式 UI，或塞进桌面窗口的通用 SaaS 后台。

本项目面向 Agent，但目前仅支持 Codex。它不是通用桌面工程手册，而是用于生成、修改、评审或文档化桌面应用 UI 的设计质量层。

## 适用场景

当 coding Agent 需要为 macOS 或 Windows 桌面应用设计、实现、重设计或评审 UI 时，使用 Desktop Taste Skills。

这套 SKILL 帮助 Agent 推理：

- 应用类型与工作流上下文
- macOS、Windows 或跨平台预期
- 具有原生感的窗口、侧边栏、工具栏、检查器、菜单、对话框、弹出层、命令面板、表格和工作台布局
- 信息密度与长时间使用舒适性
- 排版层级与间距节奏
- 交互手感、动效、反馈和状态设计
- 桌面产品 UI 内部的品牌表达
- 实现前后的 anti-slop 评审

预期结果不是简单的“正确 UI”，而是有品味的桌面 UI：有用、耐用、有辨识度、一致，并且可以落地实现。

## 不适用场景

Desktop Taste Skills 不是通用工程手册，不是移动或 Web 设计工具，也不是脱离桌面应用 UI 上下文的品牌 / 营销设计系统。

它可以在有助于产出可实现 UI 时加入轻量实现护栏，但重心始终是桌面 UI/UX 品味。

## 愿景

目标状态能力清单维护在 [VISION.md](VISION.md)。

## 安装

1. 克隆本仓库：

   ```sh
   git clone https://github.com/MC-and-his-Agents/Desktop-Taste-Skills.git
   ```

2. 在 Codex 插件安装入口中选择本仓库根目录。插件 manifest 必须保留在 `.codex-plugin/plugin.json`。
3. 确认 Codex 中显示插件名 `Desktop Taste`。
4. 运行本地校验：

   ```sh
   python3 scripts/validate_repo.py
   ```

如果 Codex 找不到插件，先确认安装的是仓库根目录，而不是 `.codex-plugin/` 子目录；再运行校验脚本，排查无效版本、缺失文件或指向仓库外部的 manifest 路径。

## 升级

1. 使用 `git pull --ff-only` 拉取最新仓库变更。
2. 阅读 [CHANGELOG.md](CHANGELOG.md)，确认安装、升级、迁移和破坏性变更说明。
3. 在 Codex 中从同一个仓库根目录刷新或重新安装插件。
4. 重新运行 `python3 scripts/validate_repo.py`。

当前仓库允许没有 `skills/` 目录，或 `skills/` 目录为空。一旦发布 Skill，其 `skills/<name>/SKILL.md` frontmatter 必须包含 `name`、`description` 和 `version`。

## 平台处理

Desktop Taste Skills 面向 macOS 与 Windows。

Agent 应：

- 说明某个决策是 macOS 特定、Windows 特定，还是跨平台折中
- 当平台预期能提升可用性时，保留平台预期
- 当产品必须跨平台发布时，允许有品味的跨平台折中
- 避免把 macOS 和 Windows 压平成通用的 Web 式 UI
- 解释原生感模式背后的设计原则，而不是盲目复制截图

## 版本管理

插件和每个已发布 Skill 分别管理版本。见 [VERSIONING.md](VERSIONING.md)。
对发布可见的变更记录在 [CHANGELOG.md](CHANGELOG.md)。

## 参考来源

Desktop Taste Skills 受到以下项目和规范启发：

- `Leonxlnx/taste-skill`：面向 coding Agent 的可移植 anti-slop UI 品味 SKILL
- `yetone/native-feel-skill`：具有原生感的跨平台桌面应用原则
- `VoltAgent/awesome-design-md`：Agent 可读的设计交接思路
- `Dimillian/Skills`：聚焦、单一职责的 SKILL 组织方式
- Apple Human Interface Guidelines：macOS 平台预期
- Microsoft Windows app design guidelines 与 Fluent Design：Windows 平台预期

这些参考影响方法和结构。Desktop Taste Skills 应定义自己的桌面特定设计行为，而不是复制 Web、移动端或品牌站模式。
