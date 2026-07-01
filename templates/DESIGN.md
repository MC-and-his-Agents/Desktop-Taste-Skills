# DESIGN.md

这是一份桌面应用设计契约模板，用于 macOS / Windows 应用。它应记录可执行的设计判断，让后续 Agent 能延续同一套窗口结构、密度、状态和交互规则。

## 使用规则

- 先写文字：每节先用 1-3 句自然语言写清设计意图、边界和取舍，再列规则或 token。
- 从 `Desktop Read` 开始写：必须引用平台、应用类型、用户、使用场景、密度、主要交互和风险。
- 只写桌面应用结构：窗口、标题栏、工具栏、侧边栏、split view、Inspector、表格、命令面板、状态栏、popover、dialog、菜单和快捷键。
- 不生成 Web hero、CTA、landing sections、responsive web breakpoints、marketing card grid、SaaS dashboard 或品牌官网文案。
- 不把本文件写成研究资料、灵感墙或组件库全集；只保留当前产品需要遵守的判断。

## 来源判断

- source_read: <引用 Desktop Read 的关键判断或链接>
- platform: <macOS / Windows / cross-platform>
- app_archetype: <工具 / 编辑器 / 工作台 / 控制台 / 数据库客户端 / 创作工具等>
- user_role: <用户角色>
- session_context: <短任务 / 长时间工作 / 批量处理 / 深度创作等>
- density: <calm / standard / dense / control-room>
- primary_interaction: <鼠标 / 键盘 / command-first / drag-and-drop / multi-pane / multi-window>
- main_risks: <网页壳 / dashboard 化 / 过度留白 / 平台感缺失 / 状态缺失 / 真实数据下失效>

## 1. 桌面设计主张

<用一段话说明这个桌面应用应该给人的工作感受、设计主张和反面参照。不要只写“现代、干净、高级”。>

- should_feel_like: <具体软件类型、工作台或专业场景>
- should_not_feel_like: <明确反模式>
- signature_moment: <用户会在核心工作流里反复感知的一个产品瞬间>

## 2. 平台目标

<说明目标平台策略：macOS 优先、Windows 优先，还是 cross-platform 折中。跨平台不等于 Web UI。>

- macOS: <窗口 chrome、菜单、toolbar、快捷键、系统材质和 focus 规则>
- Windows: <title bar、command bar、context menu、快捷键、Mica/Acrylic 或系统主题规则>
- shared_rules: <两平台共享的信息架构和状态语义>
- platform_differences: <必须分平台处理的行为>

## 3. 窗口与表面系统

<说明窗口和表面如何组成桌面工作区。先决定窗口角色，再决定表面层级。>

- primary_window: <主窗口职责、最小尺寸、默认尺寸、恢复行为>
- title_bar: <窗口标题、文档状态、拖拽区域、窗口控制边界>
- toolbar: <高频命令、搜索、过滤、视图切换和禁用态>
- sidebar: <导航或对象集合；选中态、空态、折叠策略>
- main_workspace: <主工作区承载的对象和动作>
- inspector: <当前选择对象的属性、诊断或上下文操作；无选择时的空态>
- bottom_panel: <日志、输出、诊断或队列；展开、关闭和持久化规则>
- status_bar: <连接、同步、选中数量、后台任务、权限或环境状态>
- popover_dialog_sheet: <非阻塞选择、阻塞确认、危险操作和关闭行为>

## 4. 布局语法

<说明布局类型和区域关系。不要默认 card grid 或 dashboard。>

- chosen_layout: <utility window / sidebar app / two-pane / three-pane / editor workbench / creative canvas / data cockpit / monitoring console / settings / tray popover / tabbed workspace>
- rejected_layouts:
  - <layout>: <为什么不用>
- zone_map:
  - stable_navigation: <位置和职责>
  - object_list_or_tree: <是否存在，和主对象关系>
  - detail_or_editor: <主工作区规则>
  - contextual_panel: <Inspector 或 side panel 规则>
  - transient_panel: <command palette、popover、bottom panel 规则>
- resize_rules: <splitter、最小宽度、折叠、滚动和窄窗口退化>
- data_stress_rules: <0、1、10、100+ 条记录，长文本，多选，错误和加载时如何成立>

## 5. 排版

<说明文字层级如何服务桌面扫描、比较、编辑或监控，不服务营销冲击。>

- font_stack: <系统字体或项目字体；何时使用 monospace>
- hierarchy:
  - app_title: <处理>
  - window_title: <处理>
  - toolbar_label: <处理>
  - section_label: <处理>
  - sidebar_item: <处理>
  - body: <处理>
  - metadata: <处理>
  - table_or_list_row: <处理>
  - code_or_log: <处理>
  - caption: <处理>
  - status: <处理>
  - error: <处理>
- truncation_wrapping: <长路径、长名称、日志和表格单元格规则>

## 6. 间距与密度

<说明密度档位为什么适合这个产品。桌面密度必须来自真实工作流。>

- density: <calm / standard / dense / control-room>
- reason: <一句话说明>
- toolbar_density: <高度、间距、图标/标签策略>
- sidebar_density: <行高、分组、选中态和缩进>
- table_list_density: <行高、列间距、批量选择和扫描规则>
- panel_spacing: <Inspector、settings、dialog、popover 的节奏>
- hit_targets: <鼠标、触控板和键盘路径下的可操作尺寸>

## 7. 色彩与材质

<说明颜色和材质如何表达层级、状态和平台感。品牌色不能覆盖语义色。>

- surface_system: <window、sidebar、toolbar、panel、popover、dialog 的表面规则>
- accent: <选择态、焦点、主操作、进度或关键标记的使用位置>
- semantic_colors:
  - success: <规则>
  - warning: <规则>
  - error: <规则>
  - danger: <规则>
  - info: <规则>
- material_rules: <macOS vibrancy / Windows Mica-Acrylic / 自定义材质的使用边界>
- theme_rules: <light、dark、high contrast、system accent 的适配>

## 8. 组件

<只列当前产品必须稳定的桌面组件规则，不写通用组件百科。>

- command_palette: <打开、搜索、分组、快捷键、空结果和关闭规则>
- menus_context_menus: <菜单项命名、快捷键、禁用条件和对象范围>
- toolbar_buttons: <图标、标签、tooltip、selected/active/disabled>
- sidebar_items: <hover、selected、focus、badge、空态>
- tables_lists_trees: <排序、筛选、列、选择、多选、空态、错误态>
- inspector_fields: <分组、编辑、验证、恢复路径>
- forms_settings: <分类、保存、取消、危险操作>
- notifications_feedback: <inline、status bar、system notification 的使用边界>

## 9. 动效与交互手感

<说明动效如何服务操作确认、状态变化和空间理解。没有操作意图的动画不要保留。>

- interaction_states:
  - hover: <语义>
  - focus: <语义和键盘路径>
  - selected: <语义，窗口失焦时如何保留>
  - active: <语义>
  - disabled: <语义和原因暴露>
  - loading: <短等待、中等待、长任务规则>
  - error: <恢复路径>
- spatial_transitions: <command palette、panel、inspector、popover 的来源、关闭和焦点恢复>
- drag_resize: <drag start/over/drop、splitter hover/active、尺寸约束>
- undo_redo: <对象级确认和状态栏反馈>
- reduced_motion: <保留的反馈和替代的大位移动效>

## 10. 品牌表达

<说明品牌如何进入桌面工作流，而不是变成品牌官网或广告页。>

- brand_reference: <具体参考物、工作场所或产品场景>
- brand_role: <识别产品 / 区分状态 / 降低空态尴尬 / 解释 onboarding / 强化核心操作>
- carriers:
  - <app icon / accent / empty state / microcopy / signature interaction 等，2-3 项>
- voice_rules:
  - empty_state: <语气和下一步动作>
  - onboarding: <语气、可跳过和任务导向>
  - command_palette: <命令命名和空结果>
- visual_rules:
  - icon_language: <小尺寸成立的图标语言>
  - illustration_style: <仅在哪些屏幕使用>
  - product_motif: <一个产品 motif 及禁用方式>

## 11. Anti-Slop 规则

<列出这个项目最容易滑向的桌面 UI 反模式，以及最小修正。>

- no_web_shell: <如何避免网页壳>
- no_hero_or_cta: <禁止 hero、CTA、landing sections 的具体边界>
- no_marketing_card_grid: <哪些区域不能做成卡片墙>
- no_dashboard_by_default: <何时必须用 table/list/tree/workbench>
- no_fake_native_chrome: <窗口控制、标题栏和系统菜单边界>
- no_missing_states: <必须实现的 loading、empty、error、selected、disabled、undo>
- no_unreadable_density: <过松、过密和小字号风险>
- no_brand_overreach: <品牌色、材质、插画和文案的禁区>

## 12. Agent 实现指南

<告诉后续 Agent 怎么延续设计，而不是重新发明界面。>

- before_editing:
  - 先读取本文件和最新 Desktop Read。
  - 明确要改的窗口区域、状态和用户路径。
  - 不要为了局部改动引入 Web 页面结构。
- implementation_rules:
  - 优先修改现有桌面组件和布局边界。
  - UI、业务逻辑、数据访问和外部 API 不混在同一模块。
  - 每个可操作状态至少覆盖 hover、focus、selected 或 disabled 中相关项。
  - 表格、列表、树和 Inspector 必须用真实数据压力检查。
- review_checklist:
  - 窗口结构是否仍像桌面应用。
  - 平台快捷键、菜单、焦点和系统主题是否成立。
  - 真实数据、长文本、空态、错误、权限和后台任务是否可用。
  - 是否出现 hero、CTA、landing section、marketing card grid 或 dashboard 化。
