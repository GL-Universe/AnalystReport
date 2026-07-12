# 📝 Changelog

本文件按时间倒序记录 AnalystReport 项目的关键变更。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/)。

---

## [v0.3.0] - 2026-07-12 - GPT-5.5 评测白皮书上线

**变更类型**: feat
**影响范围**: frontend/、scripts/、reports-md/

### 变更内容

- 📄 **新增完整白皮书 HTML 报告**：`frontend/reports/gpt-5.5-evaluation-whitepaper.html`（约 235 KB）
  - 将 `reports-md/` 下 13 个章节 Markdown（`00-executive-summary.md` ~ `12-appendix.md`）按文件名顺序合并为一份完整白皮书
  - 自动生成章节目录（13 个锚点链接）
  - 章节之间用虚线分隔，保留原文档标题层级（h1/h2/h3）
- 🎨 **新增 GitHub 风格精简样式**：`frontend/assets/css/github-markdown.css`（约 180 行）
  - 模仿 GitHub README 渲染风格（字体、颜色、表格、代码块、引用块）
  - 仅用于多章节合并型报告详情页，与首页 `style.css` 解耦
- 🛠️ **新增构建脚本**：`scripts/build_report.py`
  - 用 Python `markdown` 库（启用 `tables` / `fenced_code` / `toc` / `sane_lists` / `nl2br` 扩展）批量渲染章节
  - 自动收集 `NN-*.md` 文件，跳过 outline / sample 等辅助文件
  - 输出含章节目录、来源注释、章节分隔线
- 📋 **更新报告注册表**：`frontend/data/reports.json`
  - 追加 GPT-5.5 白皮书条目（title / description / date / author / icon / tags / file）
  - 排序：白皮书（2026-07-12）在前，示例报告（2026-07-01）在后

### 设计动机

- 用户要求将 `reports-md/` 下分散的多章节 Markdown 合并为一份完整报告并通过 GitHub Pages 展示
- 用户明确要求"GitHub 简易风格，尽可能减少样式的代码量" → 新建精简 CSS 而非复用现有 366 行的 `style.css`
- 项目零依赖原则 → 不引入前端 Markdown 渲染库，改用构建期 Python 转换

### 验证

- ✅ 本地 `python3 -m http.server 8765` 启动后所有资源 HTTP 200
- ✅ 首页显示 "2 份报告"，含 GPT-5.5 白皮书 + 示例报告 两张卡片
- ✅ 详情页含 13 个章节链接（Executive Summary + Chapter 1-12），锚点可点击
- ✅ 表格、引用块、代码块、章节分隔线渲染正常（通过浏览器自动化验证）
- ✅ `reports.json` 通过 `python3 -m json.tool` 格式校验
- ⏳ 待推送后验证 GitHub Actions 自动部署到 Pages

---

## [v0.2.1] - 2026-07-06 - 主流媒体引用模式研究

**变更类型**: docs
**影响范围**: wiki/

### 变更内容

- 📚 **新增研究文档**：`wiki/media-citation-patterns.md`
  - 调研 The Verge / BBC / MIT Technology Review / NYT / CNN 五家主流媒体的 AI 评测引用模式
  - 提炼出 10 类引用材料（A 作者亲测、B 命名专家访谈、C 学术研究、D 竞品对比、E 公司声明 vs 现实、F 数据统计、G 真实案例、H 先前报道、I 官方/监管文件、J 专家社交反应）
  - 按"对评测报告的支撑力"分三梯队排序，明确哪些来源是更好的引用示例
  - 产出**通用 AI 评测报告大纲（去 Benchmark 化）**，每章节标注引用类型（A-J）
  - 为 `report-generator` skill 提供 7 条关键洞察输入

### 设计动机

- `report-generator` skill 需要产出"看起来像主流媒体写的"AI 评测报告
- 反向工程真实媒体文章的引用结构，比凭空设计章节模板更可信
- 用户明确要求忽略 Benchmark 类引用，故大纲不含跑分章节

### 验证

- ✅ 4 篇样本文章通过 browser_agent 深度分析引用模式
- ⏳ 后续将此大纲同步到 `skills/report-generator/SKILL.md` 与 `reports-md/sample-report.md`

---

## [v0.2.0] - 2026-07-05 - 项目结构重构

**变更类型**: refactor
**影响范围**: 全项目结构

### 变更内容

- 🔄 **重构项目结构**：将扁平结构拆分为 5 个职责独立的模块
  - `frontend/` - 前端代码（首页 + 报告详情页）
  - `skills/` - AI 技能集合（report-generator、page-builder）
  - `reports-md/` - Markdown 报告源文件
  - `wiki/` - 项目文档（架构、工作流）
  - `Progress/` - 项目进展记录
- 📁 **文件迁移**：
  - `index.html` → `frontend/index.html`
  - `assets/` → `frontend/assets/`
  - `data/reports.json` → `frontend/data/reports.json`
  - `reports/sample-report.html` → `frontend/reports/sample-report.html`
- 📝 **新增示例**：`reports-md/sample-report.md`（带 front-matter 的 Markdown 源）
- 🛠️ **新增 skill 框架**：
  - `skills/report-generator/SKILL.md` - 报告生成 skill 定义
  - `skills/page-builder/SKILL.md` - 页面搭建 skill 定义
  - `skills/README.md` - skill 总览
- 📚 **新增 wiki 文档**：
  - `wiki/architecture.md` - 项目架构说明
  - `wiki/workflow.md` - 工作流说明
- 📈 **新增 Progress 记录**：
  - `Progress/README.md` - 进展索引
  - `Progress/changelog.md` - 本文件
- ⚙️ **修改 GitHub Actions**：`deploy-pages.yml` 的 `path` 改为 `frontend`，仅部署前端目录
- 📖 **更新根 README**：反映新的项目结构与工作流

### 设计动机

- 为后续 AI skill 工作流做准备（生成报告 → 转页面 → 上线）
- 分离前端代码与文档/skill，避免目录混乱
- GitHub Pages 仅暴露 `frontend/`，其他文档不公开到网站

### 验证

- ✅ 内部相对路径无需修改（frontend/ 内部结构未变）
- ✅ Git 历史保留（使用 `git mv` 迁移）
- ⏳ 待推送后验证 GitHub Actions 部署成功

---

## [v0.1.0] - 2026-07-05 - 项目初始化

**变更类型**: feat
**影响范围**: 全新项目

### 变更内容

- 🎉 **初始化项目**：AnalystReport
- 🏠 **创建首页**：`index.html`，报告卡片列表（动态加载）
- 🎨 **样式系统**：`assets/css/style.css`，全局变量 + 响应式
- ⚡ **交互脚本**：`assets/js/main.js`，异步加载 reports.json
- 📋 **报告注册表**：`data/reports.json`
- 📄 **示例报告**：`reports/sample-report.html`，2026 科技行业趋势分析
- ⚙️ **CI/CD**：`.github/workflows/deploy-pages.yml`，GitHub Pages 自动部署
- 📖 **README**：项目说明与使用指南

### 验证

- ✅ GitHub 仓库创建（`GL-Universe/AnalystReport`）
- ✅ 代码推送成功
- ✅ GitHub Actions 部署成功
- ✅ 网站上线：`https://gl-universe.github.io/AnalystReport/`

---

## 变更类型说明

| 类型 | 说明 |
|------|------|
| `feat` | 新功能 |
| `refactor` | 重构（不改变外部行为） |
| `fix` | 修复 bug |
| `docs` | 文档变更 |
| `chore` | 构建/工具/配置变更 |
