# 🏗️ 项目架构说明

## 1. 设计原则

- **职责分离**：前端代码、Markdown 源、AI skill、文档、进展记录各自独立
- **零依赖**：前端纯静态 HTML/CSS/JS，无需构建工具
- **可自动化**：通过 GitHub Actions 自动部署，AI skill 自动化内容生产
- **可追溯**：所有变更记录在 `Progress/changelog.md`

## 2. 顶层目录结构

```
AnalystReport/
├── frontend/              # 前端代码（GitHub Pages 根目录）
│   ├── index.html         # 首页：报告列表
│   ├── assets/            # 静态资源
│   │   ├── css/
│   │   │   ├── style.css          # 首页 + 示例报告样式
│   │   │   └── github-markdown.css# 多章节合并报告样式（GitHub 风格精简）
│   │   └── js/main.js            # 异步加载 reports.json 渲染卡片
│   ├── data/reports.json  # 报告元数据注册表
│   └── reports/           # 转换后的 HTML 报告
│       ├── sample-report.html
│       └── gpt-5.5-evaluation-whitepaper.html  # 多章节合并白皮书
│
├── reports-md/            # Markdown 报告源文件
│   ├── 00-executive-summary.md ... 12-appendix.md  # GPT-5.5 白皮书 13 章
│   └── sample-report.md                              # 单篇示例
│
├── scripts/              # 构建脚本
│   └── build_report.py   # 将 reports-md/NN-*.md 合并为 frontend/reports/*.html
│
├── skills/                # AI 技能集合
│   ├── report-generator/  # 报告生成 skill
│   └── page-builder/      # 页面搭建 skill
│
├── wiki/                  # 项目文档
│   ├── architecture.md    # 本文件
│   └── workflow.md        # 工作流说明
│
├── Progress/              # 项目进展记录
│   └── changelog.md       # 变更日志
│
├── .github/workflows/     # CI/CD
│   └── deploy-pages.yml   # Pages 自动部署
│
└── README.md              # 项目主入口
```

## 3. 模块职责

### 3.1 `frontend/` - 前端代码

**职责**：托管在 GitHub Pages 的静态网站，呈现所有分析报告。

**关键文件**：

| 文件 | 作用 |
|------|------|
| `index.html` | 首页，展示报告卡片列表 |
| `assets/css/style.css` | 首页 + 示例报告样式（含渐变/卡片/阴影） |
| `assets/css/github-markdown.css` | 多章节合并报告样式（GitHub README 风格，约 180 行） |
| `assets/js/main.js` | 异步加载 `data/reports.json` 渲染卡片 |
| `data/reports.json` | 报告注册表，决定首页显示哪些报告 |
| `reports/*.html` | 单个报告详情页 |

**数据流向**：
```
reports.json ──fetch──> main.js ──渲染──> index.html 卡片
                                       │
                                       └──点击──> reports/*.html
```

**报告样式分发**：

| 报告类型 | 引用 CSS |
|----------|---------|
| 单篇示例（`sample-report.html`） | `style.css`（卡片渐变样式） |
| 多章节合并（`gpt-5.5-evaluation-whitepaper.html`） | `github-markdown.css`（GitHub README 风格） |

### 3.2 `reports-md/` - Markdown 报告源

**职责**：保存 AI 生成的分析报告 Markdown 源文件。

**两种组织模式**：

1. **单篇模式**：一个 `.md` 文件对应一份报告，含 YAML front-matter 元数据 + 正文
   - 命名规范：`{slug}.md`（如 `sample-report.md`）
   - 由 `page-builder` skill 转换为 `frontend/reports/{slug}.html`

2. **多章节模式**：一个目录下的多个 `NN-*.md` 文件按文件名顺序合并为一份完整报告
   - 命名规范：`NN-{chapter-name}.md`（如 `00-executive-summary.md`）
   - 由 `scripts/build_report.py` 合并并转换为 `frontend/reports/{slug}.html`
   - 当前示例：`reports-md/00-*.md` ~ `12-*.md` → `frontend/reports/gpt-5.5-evaluation-whitepaper.html`

### 3.3 `scripts/` - 构建脚本

**职责**：将多章节 Markdown 合并为完整 HTML 报告。

| 脚本 | 输入 | 输出 |
|------|------|------|
| `build_report.py` | `reports-md/NN-*.md`（自动按文件名顺序） | `frontend/reports/gpt-5.5-evaluation-whitepaper.html` |

**使用方式**：

```bash
python3 scripts/build_report.py
```

**依赖**：Python `markdown` 库（`pip3 install markdown`）。

### 3.4 `skills/` - AI 技能集合

**职责**：封装可复用的 AI 工作流，每个 skill 是一个 `.md` 定义文件，由 AI agent 调用。

| Skill | 输入 | 输出 |
|-------|------|------|
| `report-generator` | 报告主题 | `reports-md/*.md` |
| `page-builder` | md 文件路径 | `frontend/reports/*.html` + 更新 `reports.json` |

详见 [`skills/README.md`](../skills/README.md)。

### 3.5 `wiki/` - 项目文档

**职责**：说明项目的架构与工作流，供人类开发者阅读。

### 3.6 `Progress/` - 进展记录

**职责**：按时间顺序记录项目的关键变更，作为「项目记忆」。

### 3.7 `.github/workflows/` - CI/CD

**职责**：`deploy-pages.yml` 在每次推送 `main` 分支时，将 `frontend/` 目录上传到 GitHub Pages。

## 4. 数据流向图

```
                ┌─────────────────────┐
                │  用户提需求          │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │  report-generator   │
                │  skill (AI)         │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │  reports-md/*.md    │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │  page-builder skill │
                │  (AI)               │
                └──────────┬──────────┘
                           ▼
              ┌────────────┴────────────┐
              ▼                          ▼
   ┌──────────────────┐      ┌─────────────────────┐
   │ frontend/reports/│      │ frontend/data/      │
   │ *.html           │      │ reports.json        │
   └────────┬─────────┘      └──────────┬──────────┘
            │                           │
            └───────────┬───────────────┘
                        ▼
            ┌─────────────────────┐
            │  git commit + push  │
            └──────────┬──────────┘
                       ▼
            ┌─────────────────────┐
            │  GitHub Actions     │
            │  deploy-pages.yml   │
            └──────────┬──────────┘
                       ▼
            ┌─────────────────────┐
            │  GitHub Pages 上线   │
            │  gl-universe.github  │
            │  .io/AnalystReport   │
            └─────────────────────┘
```

## 5. 关键设计决策

### 5.1 为什么前端在 `frontend/` 而非根目录？

- 隔离前端代码与文档/skill，避免目录混乱
- GitHub Actions 部署时只上传 `frontend/`，文档和 skill 不会暴露到 Pages
- 仓库根目录保持「项目元信息」角色（README、Progress、wiki）

### 5.2 为什么用 `reports.json` 注册表而非自动扫描？

- 控制首页展示顺序（按日期降序）
- 添加额外元数据（icon、description、tags）方便首页卡片渲染
- 解耦报告存在性与展示性

### 5.3 为什么用 front-matter 而非单独 metadata 文件？

- 元数据与正文同文件，便于维护
- 标准 YAML 格式，工具兼容性好
- `page-builder` 解析简单

## 6. 扩展性

未来可能扩展：

- 🌐 多语言支持（`reports-md/en/`、`reports-md/zh/`）
- 📊 数据可视化（在 HTML 报告中嵌入图表库）
- 🔄 md 自动监听（git hook 触发 page-builder）
- 📈 访问统计（接入 Plausible / Umami）
