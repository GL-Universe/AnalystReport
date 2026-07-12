# 📊 AnalystReport

> 多维度数据分析报告中心 · 通过 GitHub Pages 静态呈现

## 🌐 在线访问

- **网站**：https://gl-universe.github.io/AnalystReport
- **仓库**：https://github.com/GL-Universe/AnalystReport

## 📁 项目结构

```
AnalystReport/
├── frontend/              # 🚀 前端代码（GitHub Pages 根目录）
│   ├── index.html          #    首页：报告列表
│   ├── assets/             #    样式与脚本
│   │   ├── css/style.css            #     首页 + 示例报告样式
│   │   ├── css/github-markdown.css  #     多章节合并报告样式（GitHub 风格）
│   │   └── js/main.js               #     卡片动态加载脚本
│   ├── data/reports.json   #    报告注册表
│   └── reports/            #    HTML 报告详情页
│       ├── sample-report.html
│       └── gpt-5.5-evaluation-whitepaper.html  # GPT-5.5 评测白皮书
│
├── reports-md/             # 📝 Markdown 报告源文件
│   ├── 00-executive-summary.md ~ 12-appendix.md  # GPT-5.5 白皮书 13 章
│   └── sample-report.md
│
├── scripts/               # 🧰 构建脚本
│   └── build_report.py     #   将 reports-md/NN-*.md 合并为 HTML 报告
│
├── skills/                 # 🛠️ AI 技能集合
│   ├── report-generator/   #    报告生成 skill
│   └── page-builder/       #    页面搭建 skill
│
├── wiki/                   # 📚 项目文档（架构、工作流）
├── Progress/               # 📈 项目进展记录
└── .github/workflows/      # ⚙️ GitHub Pages 自动部署
```

详见 [`wiki/architecture.md`](./wiki/architecture.md)。

## 🔄 核心工作流

```
[1] report-generator skill  →  产出 reports-md/*.md（单篇报告）
[2] page-builder skill      →  md 转 frontend/reports/*.html + 更新 reports.json（单篇报告）
[2'] scripts/build_report.py →  多章节 NN-*.md 批量合并为 frontend/reports/*.html（多章节报告）
[3] git push                →  GitHub Actions 自动部署到 Pages
[4] Progress/changelog.md   →  追加变更记录
```

详见 [`wiki/workflow.md`](./wiki/workflow.md)。

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

## ✍️ 如何添加新报告

### 方式 1：使用 AI Skill（推荐）

对 AI 说：
> 「帮我生成一份关于 XX 的分析报告，并发布上线。」

AI 会自动调用 `report-generator` 生成 md，再调用 `page-builder` 转换为 HTML 并注册到首页。

### 方式 2：手动操作

1. 在 `reports-md/` 创建 `{slug}.md`（参考 [`sample-report.md`](./reports-md/sample-report.md)）
2. 在 `frontend/reports/` 创建对应的 `{slug}.html`（参考 [`sample-report.html`](./frontend/reports/sample-report.html)）
3. 在 `frontend/data/reports.json` 追加条目
4. `git add . && git commit && git push`

## 📚 文档导航

- 📖 [项目架构](./wiki/architecture.md)
- 🔄 [工作流说明](./wiki/workflow.md)
- 🛠️ [AI Skills](./skills/README.md)
- 📈 [项目进展](./Progress/README.md)

## 🛠️ 技术栈

- 纯静态 HTML/CSS/JavaScript（零依赖）
- Markdown + front-matter 内容源
- AI Skill 驱动内容生产
- GitHub Actions 自动部署
- GitHub Pages 免费托管

## 📄 License

MIT
