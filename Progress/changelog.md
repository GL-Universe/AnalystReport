# 📝 Changelog

本文件按时间倒序记录 AnalystReport 项目的关键变更。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/)。

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
