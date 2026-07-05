---
name: report-generator
description: 根据用户提供的主题和数据来源，生成结构化的分析报告 Markdown 文件，保存到 reports-md/ 目录。报告含 front-matter 元数据，便于后续 page-builder skill 转换为 HTML。
trigger_keywords: ["生成报告", "写分析报告", "整理报告", "调研报告", "分析报告"]
---

# 📝 report-generator - 分析报告生成 Skill

## 1. 用途

根据用户输入的主题、数据来源和目标受众，产出一份结构化的分析报告 Markdown 文件，保存到 `reports-md/` 目录。生成的 md 文件包含 front-matter 元数据，便于后续 `page-builder` skill 转换为 HTML 页面。

## 2. 输入参数

| 参数 | 必填 | 说明 | 示例 |
|------|------|------|------|
| `topic` | ✅ | 报告主题 | "2026 中国新能源汽车市场分析" |
| `data_sources` | ⚪ | 数据来源（公开报告、新闻、研究等） | "中汽协、工信部、企业财报" |
| `audience` | ⚪ | 目标读者 | "投资人 / 产品经理 / 决策者" |
| `depth` | ⚪ | 报告深度（brief / standard / deep） | "standard" |
| `tags` | ⚪ | 预设标签（tech/market/data/strategy） | ["market", "data"] |

## 3. 输出格式

### 3.1 文件路径

```
reports-md/{slug}.md
```

`slug` 由主题生成（kebab-case，仅小写字母、数字、连字符）。

### 3.2 文件结构

```markdown
---
title: {报告标题}
description: {简短描述，用于首页卡片}
date: {YYYY-MM-DD}
author: {作者}
icon: {emoji 图标}
tags: [{标签数组}]
slug: {slug}
---

# {emoji} {报告标题}

> **核心摘要**
> {一段话总结}

## 1. {章节标题}
{正文内容}

### 关键数据
| 指标 | 数据 | 备注 |
|------|------|------|
| ... | ... | ... |

## 2. {章节标题}
...

## N. 展望与建议
> **核心建议**
> 1. ...
> 2. ...

---
*免责声明：本报告仅供参考，不构成任何投资建议。*
```

## 4. 工作流

1. **澄清需求** — 与用户确认主题、深度、目标受众
2. **收集信息** — 使用 `search_web` / `fetch_web` 工具调研公开信息
3. **整理数据** — 提取关键数据点、行业趋势、竞争格局
4. **撰写报告** — 按 3.2 模板生成 Markdown
5. **保存文件** — 写入 `reports-md/{slug}.md`
6. **更新进展** — 在 `Progress/changelog.md` 追加记录

## 5. 质量要求

- ✅ 数据需注明来源（脚注或行内链接）
- ✅ 章节结构清晰（1. → 2. → 3. …），含「展望与建议」收尾
- ✅ 表格、引用块、高亮框等组件按模板规范使用
- ✅ 字数：brief 约 800 字、standard 约 1500 字、deep 约 3000 字
- ❌ 不编造数据，无法找到的数据应明确标注「数据待补充」

## 6. 示例

参见 [`reports-md/sample-report.md`](../../reports-md/sample-report.md) — 完整示范了 front-matter、章节、表格、引用块等元素。

## 7. 与其他 skill 的衔接

完成后建议立即调用 [`page-builder`](../page-builder/SKILL.md) skill 将 md 转换为 HTML 页面并注册到首页。
