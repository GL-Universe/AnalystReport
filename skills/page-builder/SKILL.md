---
name: page-builder
description: 将 reports-md/ 目录下的 Markdown 报告转换为前端可访问的 HTML 静态页面，整合到 frontend/ 项目中，并自动更新 reports.json 注册表。调用后即可在 GitHub Pages 首页看到新报告。
trigger_keywords: ["发布报告", "md转html", "整合报告", "页面搭建", "上首页"]
---

# 🏗️ page-builder - 报告页面搭建 Skill

## 1. 用途

将 `reports-md/*.md` 文件转换为 `frontend/reports/*.html` 静态页面，并更新 `frontend/data/reports.json` 注册表，使新报告出现在首页卡片列表中。转换后只需 `git push`，GitHub Pages 即自动上线。

## 2. 输入参数

| 参数 | 必填 | 说明 | 示例 |
|------|------|------|------|
| `md_file` | ✅ | md 文件路径 | "reports-md/sample-report.md" |
| `template` | ⚪ | 使用的 HTML 模板 | "frontend/reports/sample-report.html" |

## 3. 转换规则

### 3.1 front-matter → reports.json 条目

读取 md 文件顶部的 YAML front-matter，提取以下字段：

```yaml
---
title: ...        → reports.json 条目的 "title"
description: ...   → "description"
date: ...          → "date"
author: ...        → "author"
icon: ...          → "icon"
tags: [...]        → "tags"
slug: ...          → "file": "reports/{slug}.html"
---
```

生成条目追加到 `frontend/data/reports.json` 的 `reports` 数组。

### 3.2 Markdown body → HTML body

按映射规则将 Markdown 语法转换为 HTML（套用模板样式）：

| Markdown | HTML（带样式类） |
|----------|-----------------|
| `# 标题` | `<h1>...</h1>` |
| `## 章节` | `<h2>...</h2>` |
| `### 子标题` | `<h3>...</h3>` |
| `> **核心摘要**` 段 | `<div class="highlight-box"><h3>📌 核心摘要</h3><p>...</p></div>` |
| `> **核心建议**` 列表 | `<div class="highlight-box"><h3>🎯 核心建议</h3><ol>...</ol></div>` |
| `>` 引用（其他） | `<blockquote>...</blockquote>` |
| `\|...\|` 表格 | `<table>...</table>` |
| `- **xxx：**` 列表 | `<ul><li><strong>xxx：</strong>...</li></ul>` |
| 普通段落 | `<p>...</p>` |
| `---` 分隔线 | `<hr>` + 免责声明样式 |

### 3.3 套用模板

以 [`frontend/reports/sample-report.html`](../../frontend/reports/sample-report.html) 为模板：
- 保留 `<head>` 部分（标题改为 front-matter 中的 title）
- 保留 `<header class="report-header">` 结构（注入 title、date、author、tags）
- 替换 `<article class="report-content">` 内的内容为转换后的 HTML body
- 保留 `<footer>` 不变

## 4. 工作流

1. **读取 md** — 解析 front-matter 与 body
2. **生成 HTML body** — 按转换规则映射
3. **套用模板** — 注入到 `frontend/reports/template.html` 骨架
4. **保存 HTML** — 写入 `frontend/reports/{slug}.html`
5. **更新 reports.json** — 在数组中添加新条目（按日期降序插入）
6. **校验** — 用浏览器或 `curl` 检查 HTML 渲染正常
7. **更新进展** — 在 `Progress/changelog.md` 追加记录

## 5. 输出示例

### 5.1 生成的 `frontend/data/reports.json` 条目

```json
{
  "title": "2026 上半年科技行业趋势分析",
  "description": "涵盖人工智能、云计算、半导体等关键领域的市场趋势",
  "date": "2026-07-01",
  "author": "AnalystReport",
  "icon": "📈",
  "tags": ["tech", "market"],
  "file": "reports/sample-report.html"
}
```

### 5.2 生成的 HTML 结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <title>{title} - AnalystReport</title>
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="report-page">
  <main class="report-container">
    <header class="report-header">
      <a href="../index.html" class="report-back">← 返回报告列表</a>
      <h1>{icon} {title}</h1>
      <div class="report-date">发布日期：{date} · 作者：{author}</div>
      <div class="tags">{tags}</div>
    </header>
    <article class="report-content">
      {转换后的 HTML body}
    </article>
  </main>
  <footer class="site-footer">...</footer>
</body>
</html>
```

## 6. 边界情况

| 情况 | 处理 |
|------|------|
| md 中无 `slug` 字段 | 从 title 生成 kebab-case slug |
| reports.json 已有同 slug 条目 | 更新而非新增 |
| md 含未支持的语法 | 转为纯文本保留内容，记录警告 |
| tags 含未定义标签 | 在 CSS 中自动追加 `.tag-{name}` 默认样式 |

## 7. 与其他 skill 的衔接

- 上游：[`report-generator`](../report-generator/SKILL.md) 生成的 `reports-md/*.md`
- 下游：`git push` → GitHub Actions 自动部署 → Pages 上线

## 8. 校验清单

- [ ] HTML 文件可在浏览器正常打开
- [ ] 首页 `frontend/index.html` 卡片显示新报告
- [ ] 卡片点击跳转到详情页正常
- [ ] 返回按钮可回到首页
- [ ] 表格、引用块样式渲染正常
