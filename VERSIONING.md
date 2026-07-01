# 版本管理

本仓库使用两层版本管理：插件版本和 Skill 版本。

## 插件版本

- 插件版本写在 `.codex-plugin/plugin.json` 的 `version` 字段。
- 插件版本表示整个插件包的安装、升级和兼容性状态。
- 任意已发布 Skill 的新增、删除、重命名、迁移说明变化，或插件元数据变化，都必须评估是否提升插件版本。

## Skill 版本

- 每个已发布 Skill 都必须在 `skills/<skill-name>/SKILL.md` frontmatter 中声明 `version`。
- Skill 版本表示该 Skill 自身的触发条件、行为约束、输入输出契约和迁移成本。
- 修改某个 Skill 的用户可见行为时，提升该 Skill 版本；只改错别字或内部表述且不改变行为时，可以不提升。

示例：

```markdown
---
name: desktop-taste
description: 改进 macOS 和 Windows 桌面应用 UI/UX。
version: 0.1.0
---
```

## 升级规则

- 插件版本和 Skill 版本都使用 SemVer。
- `PATCH`：修正文案、校验、轻微缺陷，不改变触发方式或用户可见契约。
- `MINOR`：新增 Skill、扩展已有 Skill 能力，保持向后兼容。
- `MAJOR`：删除、重命名、移动已发布 Skill，或改变已有 Skill 的触发语义和输出契约。
- 插件版本不必和所有 Skill 版本一致；插件版本描述整体发布，Skill 版本描述单个 Skill。
- 有破坏性变更时，README 或发布说明必须写清迁移步骤。
