English | [中文](README.zh-CN.md)

# Desktop Taste Skills

Desktop Taste Skills is a Codex plugin containing portable desktop UI/UX taste skills for upgrading AI-built macOS and Windows application interfaces.

It helps Codex produce stronger window composition, layout, typography, motion, spacing, native feel, interaction states, and product expression instead of generic, template-like UI or SaaS dashboards pasted into desktop windows.

The project is Agent-oriented, but currently only supports Codex. It is not a general desktop engineering handbook; it is a design-quality layer for Agents that generate, revise, critique, or document desktop application UI.

## What this is for

Use Desktop Taste Skills when a coding Agent needs to design, implement, redesign, or critique desktop application UI for macOS or Windows.

The suite helps the Agent reason about:

- desktop brief gates before large UI changes
- visual or evidence targets such as screenshots, running windows, code paths, `DESIGN.md`, references, or selected art direction
- app type and workflow context
- macOS, Windows, or cross-platform expectations
- native-feeling windows, sidebars, toolbars, inspectors, menus, dialogs, popovers, command palettes, tables, and workbench layouts
- information density and long-session comfort
- typography hierarchy and spacing rhythm
- interaction feel, motion, feedback, and state design
- product-level brand expression inside desktop UI
- anti-slop critique before and after implementation

The intended outcome is not simply “correct UI”. The intended outcome is desktop UI with taste: useful, durable, distinctive, coherent, and implementation-ready.

## Skills

- `desktop-taste`: entry Skill for desktop UI/UX task recognition, boundary checks, and route selection.
- `desktop-design-read`: pre-implementation desktop brief gate covering platform, app type, user, session context, density, interaction model, evidence target, risks, and next routes.
- `desktop-art-direction`: produces 2-3 concrete desktop art directions with thesis, fit, anti-patterns, and signature moments.
- `desktop-native-feel`: checks whether macOS or Windows UI feels like real desktop software instead of a web shell.
- `desktop-layout-composition`: chooses desktop window layouts, zones, and component tradeoffs for real workflows and data.
- `desktop-typography-density`: calibrates type hierarchy, spacing, text roles, tables, lists, and density levels.
- `desktop-motion-interaction`: designs and reviews desktop motion, interaction states, feedback, undo/redo, and reduced-motion behavior.
- `desktop-brand-system`: keeps product expression inside useful desktop UI rather than turning the app into marketing surface.
- `desktop-audit`: audits existing desktop UI and produces diagnosis, preservation guidance, fixes, and implementation checks.
- `desktop-redesign`: turns audit findings into implementable layout, component, state, interaction, and visual strategy.
- `desktop-qa`: checks implemented desktop UI before handoff against Desktop Read, evidence targets, native feel, layout, density, states, keyboard path, real data, and themes.
- `desktop-design-md`: creates or updates a desktop-focused `DESIGN.md` for user projects.

Reusable templates live in `templates/` for desktop `DESIGN.md`, Desktop Read, critique, and anti-slop checks.

## What this is not for

Desktop Taste Skills is not a general engineering handbook, a mobile or web design toolkit, or a brand/marketing design system without desktop app UI context.

It may include lightweight implementation guardrails when they help produce feasible UI, but its center of gravity is desktop UI/UX taste.

## Vision

The target capability map is maintained in [VISION.md](VISION.md).

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/MC-and-his-Agents/Desktop-Taste-Skills.git
   ```

2. Install the repository root with your Codex plugin installer. The plugin
   manifest must stay at `.codex-plugin/plugin.json`.
3. Confirm Codex lists the plugin as `Desktop Taste`.
4. Run the local validator:

   ```sh
   python3 scripts/validate_repo.py
   python3 scripts/smoke_plugin_install.py
   ```

If Codex cannot find the plugin, first confirm you installed the repository
root, not `.codex-plugin/`, and then run the validator to catch invalid
versions, missing files, or manifest paths that point outside the repository.

## Upgrade

1. Pull the latest repository changes with `git pull --ff-only`.
2. Read [CHANGELOG.md](CHANGELOG.md) for install, upgrade, migration, and
   breaking-change notes.
3. Refresh or reinstall the plugin in Codex from the same repository root.
4. Re-run `python3 scripts/validate_repo.py`.
5. Re-run `python3 scripts/smoke_plugin_install.py`.

Each published Skill lives in `skills/<name>/SKILL.md`, and its frontmatter
must include `name`, `description`, and `version`.

## Platform handling

Desktop Taste Skills targets macOS and Windows.

The Agent should:

- state when a decision is macOS-specific, Windows-specific, or cross-platform
- preserve platform expectations when they improve usability
- allow tasteful cross-platform compromise when the product requires it
- avoid flattening macOS and Windows into a generic web-like UI
- explain the principle behind native-feeling patterns instead of copying screenshots blindly

## Versioning

The plugin and each published Skill are versioned separately. See [VERSIONING.md](VERSIONING.md).
Release-visible changes are tracked in [CHANGELOG.md](CHANGELOG.md).

## Influences

Desktop Taste Skills is influenced by:

- `Leonxlnx/taste-skill` for portable anti-slop UI taste skills for coding Agents
- `yetone/native-feel-skill` for native-feeling cross-platform desktop app principles
- `VoltAgent/awesome-design-md` for Agent-readable design handoff ideas
- `Dimillian/Skills` for focused, single-purpose skill organization
- Apple Human Interface Guidelines for macOS platform expectations
- Microsoft Windows app design guidelines and Fluent Design for Windows platform expectations

These references inform method and structure. Desktop Taste Skills should define its own desktop-specific design behavior rather than copying web, mobile, or brand-site patterns.
