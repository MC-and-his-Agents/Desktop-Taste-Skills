# 桌面设计稿生成模板

用于把 Desktop Read 和 art direction 转成 3 张可评审的 macOS / Windows 桌面应用设计稿。它是 ImageGen 前的输出结构和后续实现 / QA 的事实载体，不是像素级实现规范。

## 使用规则

- 先确认 Desktop Read，再生成设计稿。
- 默认生成 3 张独立图像，不生成拼贴板、九宫格或小缩略图集合。
- cross-platform 任务至少覆盖 macOS-forward、Windows-forward 和 cross-platform compromise 三种取舍。
- 每张图必须绑定同一个 `target_surface`、`draft_state` 和 `draft_dimensions`，除非明确说明状态差异。
- macOS-first 可以强调 Liquid Glass，但只用于合适的系统表面；Windows-first 必须保留 Windows title bar、command bar、context menu、系统主题和 Fluent / Mica / Acrylic 预期。
- 设计稿被选中后，作为后续 redesign、`DESIGN.md` 和 QA 的 selected visual draft；实现时只吸收结构、密度、状态和材料边界，不照抄随机文字、系统 chrome 或不可实现细节。

## 输出格式

```text
Desktop Visual Draft:
- source_read:
  - platform: <macOS / Windows / cross-platform>
  - platform_depth: <macOS-first / Windows-first / cross-platform desktop>
  - app_archetype: <tool / editor / workbench / launcher / console / creative tool>
  - density: <calm / standard / dense / control-room>
  - primary_interaction: <mouse-first / keyboard-first / command-first / drag-and-drop / multi-pane>
- target_surface: <main window / settings / inspector / popover / dialog / tray popover / specific window>
- draft_state: <populated / selected item / empty / loading / error / editing / permission denied>
- draft_dimensions: <width x height / ratio / window chrome included>
- art_direction_source: <chosen direction / assumption / not available>
- evidence_target: <art direction / draft-ready brief / visual draft / reference / screenshot / runtime / DESIGN.md / code / user description>

Draft Variants:
1. <variant name>
   - thesis: <一句话说明这个视觉稿的桌面主张>
   - best_for: <适用场景>
   - platform_material_strategy: <Liquid Glass / Mica / Acrylic / native surfaces / custom surface boundary>
   - image_prompt: <可直接交给 ImageGen 的完整 prompt>
   - size: <recommended dimensions>
   - negative_prompt: <Web landing, mobile UI, browser chrome, marketing hero, generic cards, fake glass, unreadable text>
   - implementation_notes:
     - <后续可吸收的结构、密度、状态或组件规则>

2. <variant name>
   - thesis: ...
   - best_for: ...
   - platform_material_strategy: ...
   - image_prompt: ...
   - size: ...
   - negative_prompt: ...
   - implementation_notes:
     - ...

3. <variant name>
   - thesis: ...
   - best_for: ...
   - platform_material_strategy: ...
   - image_prompt: ...
   - size: ...
   - negative_prompt: ...
   - implementation_notes:
     - ...

Selection Handoff:
- selected_visual_draft: <variant name / image id / file path / pending user choice>
- carry_forward:
  - <layout / density / component state / material boundary / signature moment>
- do_not_copy:
  - <random generated text / exact pixels / fake system chrome / unreadable blur / non-product assets>
- next_routes:
  - <redesign / DESIGN.md / QA / implementation-specific route>
- out_of_scope:
  - <non-desktop or engineering scope>
```

## 自检

- 是否生成的是桌面应用窗口，而不是网页页面或品牌视觉。
- 是否每个方案都可用真实数据、状态和桌面组件实现。
- 是否明确哪些内容可传递给实现，哪些只是生成图像里的随机细节。
- 是否能让 QA 对照实现截图检查窗口、状态、密度和平台材料边界。
