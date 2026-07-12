# 📊 AnalystReport

> 多维度数据分析报告中心 · 通过 GitHub Pages 静态呈现

## 🌐 在线访问

- **网站**：https://gl-universe.github.io/AnalystReport
- **仓库**：https://github.com/GL-Universe/AnalystReport

---

## 📁 项目目录与文件定位

项目按"代码 / 源文件 / 文档"分离原则组织。每个目录与文件有明确职责，避免内容重复。

### 顶层目录

| 目录 | 定位 | 时间维度 |
|------|------|---------|
| `frontend/` | 静态前端代码（GitHub Pages 根目录） | 静态 |
| `reports-md/` | Markdown 报告源文件 | 静态 |
| `scripts/` | 构建脚本（md → HTML） | 静态 |
| `wiki/` | 结构维度文档（架构、工作流、案例研究） | 静态 |
| `Progress/` | 时间维度文档（变更日志、任务追踪） | 倒序累积 |
| `white-paper-research/` | 白皮书的关键点特点 | 静态 |
| `reference/` | 白皮书撰写期的原始来源 outline 与转录稿 | 静态 |
| `.github/workflows/` | CI/CD（Pages 自动部署） | 静态 |

### 关键文件定位

| 文件 | 唯一职责 | 不做什么 |
|------|---------|---------|
| `README.md`（本文件） | 项目入口 + 目录与文件定位说明 + 快速开始 + 文档导航 | 不重复 wiki 详细架构/工作流 |
| `wiki/architecture.md` | 静态架构说明（目录结构、模块职责、数据流向） | 不记录时间线变更 |
| `wiki/workflow.md` | 静态工作流说明（报告生成→页面搭建→部署） | 不记录具体某次白皮书的构建过程 |
| `wiki/media-citation-patterns.md` | 媒体引用模式研究 + 评测报告大纲模板 | — |
| `wiki/whitepaper-build-guide.md` | GPT-5.5 白皮书构建案例研究（某次具体构建的结构化总结） | 不替代通用工作流 |
| `wiki/README.md` | wiki 文档索引 | — |
| `Progress/changelog.md` | 倒序变更日志（每次版本变更的详细记录） | 不重复 todo 的待办清单 |
| `Progress/todo.md` | 任务追踪（待办+已完成） | 已完成事项不再列详细描述，指向 changelog |
| `Progress/README.md` | Progress 索引（当前状态 + 版本概览表） | 不重复 architecture 的静态描述 |
| `frontend/data/reports.json` | 报告元数据注册表（首页卡片渲染来源） | — |
| `.github/workflows/deploy-pages.yml` | 推送 `main` 时自动部署 `frontend/` 到 Pages | — |

### wiki/ 与 Progress/ 的分工

- **`wiki/`** = 结构维度：项目的"是什么"（架构、工作流、案例研究），静态文档
- **`Progress/`** = 时间维度：项目的"变了什么"（变更日志、任务追踪），倒序累积

两者不合并，以保持"静态结构"与"时间变更"的清晰区分。

---

## 🔄 核心工作流概览

```
[1] 撰写 Markdown 报告源            →  reports-md/*.md（单篇或多章节）
[2] scripts/build_report.py           →  多章节 NN-*.md 批量合并为 frontend/reports/*.html
[2'] 单篇报告手动转 HTML              →  frontend/reports/*.html + 更新 reports.json
[3] git push                          →  GitHub Actions 自动部署到 Pages
[4] Progress/changelog.md             →  追加变更记录
```

详见 [`wiki/workflow.md`](./wiki/workflow.md)。

---

## 🚀 快速开始

### 在线查看

访问 **https://gl-universe.github.io/AnalystReport** 即可浏览所有报告。

### 本地预览

```bash
git clone git@github.com:GL-Universe/AnalystReport.git
cd AnalystReport
cd frontend && python3 -m http.server 8080
# 访问 http://localhost:8080
```

---

## ✍️ 如何添加新报告

### 方式 1：手动操作（单篇报告）

1. 在 `reports-md/` 创建 `{slug}.md`（参考 [`sample-report.md`](./reports-md/sample-report.md)）
2. 在 `frontend/reports/` 创建对应的 `{slug}.html`（参考 [`sample-report.html`](./frontend/reports/sample-report.html)）
3. 在 `frontend/data/reports.json` 追加条目
4. `git add . && git commit && git push`

### 方式 2：多章节合并型报告

参考 [`wiki/whitepaper-build-guide.md`](./wiki/whitepaper-build-guide.md) 中"GPT-5.5 评测白皮书"的构建方式。

---

## 📚 文档导航

### wiki/（结构维度，静态）

- 📖 [项目架构](./wiki/architecture.md)
- 🔄 [工作流说明](./wiki/workflow.md)
- 📰 [媒体引用模式研究](./wiki/media-citation-patterns.md)
- 📝 [白皮书构建指南](./wiki/whitepaper-build-guide.md)

### Progress/（时间维度，倒序）

- 📈 [变更日志](./Progress/changelog.md)
- 📋 [任务追踪](./Progress/todo.md)
- 📊 [项目进展索引](./Progress/README.md)

### 其他

- 📋 [评测报告大纲 v1](./report-outline-v1.md)

---

## 🛠️ 技术栈

- 纯静态 HTML/CSS/JavaScript（零依赖）
- Markdown + front-matter 内容源
- GitHub Actions 自动部署
- GitHub Pages 免费托管

## 📄 License

MIT
