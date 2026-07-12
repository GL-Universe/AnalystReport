# 📝 GPT-5.5 评测白皮书构建指南

> 本文档记录 GPT-5.5 评测白皮书的撰写过程，作为案例研究便于以后查阅。
> 与 `Progress/changelog.md` 的区别：changelog 是项目所有变更的倒序时间线，本文档是某次具体白皮书构建的结构化总结。

---

## 1. 项目概览

| 项 | 内容 |
|----|------|
| 白皮书主题 | GPT-5.5 Model Service Evaluation White Paper |
| 最终输出 | `frontend/reports/gpt-5.5-evaluation-whitepaper.html` |
| 部署 URL | https://gl-universe.github.io/AnalystReport/reports/gpt-5.5-evaluation-whitepaper.html |
| 报告日期 | 2026-07-12 |
| 章节数 | 13（Ch 0 执行摘要 + Ch 1-12 主体） |
| HTML 大小 | 约 204 KB |

---

## 2. 关键依赖文件（输入）

### 2.1 白皮书章节源文件

`reports-md/` 下 13 个 Markdown 文件，按新章节顺序：

| 文件 | 章节 |
|------|------|
| `00-executive-summary.md` | Ch 0 Executive Summary |
| `01-research-background.md` | Ch 1 Research Background & Problem Setting |
| `02-practical-recommendations.md` | Ch 2 Practical Recommendations |
| `03-methodology.md` | Ch 3 Evaluation Methodology |
| `04-evaluation-metrics.md` | Ch 4 Evaluation Metrics System |
| `05-core-capability-results.md` | Ch 5 Core Capability Evaluation Results |
| `06-competitor-comparison.md` | Ch 6 Competitor Comparative Analysis |
| `07-failure-cases.md` | Ch 7 Failure Cases & Boundary Analysis |
| `08-cost-effectiveness.md` | Ch 8 Cost-Effectiveness Analysis |
| `09-safety-alignment.md` | Ch 9 Safety & Alignment Assessment |
| `10-dataset-description.md` | Ch 10 Test Dataset Description |
| `11-limitations.md` | Ch 11 Research Limitations |
| `12-appendix.md` | Ch 12 Appendix（含全局 References） |

### 2.2 研究依据文件

| 路径 | 用途 |
|------|------|
| `white-paper-research/summary-white-paper-focus.md` | 媒体引用标准研究（撰写时的内部参考） |
| `white-paper-research/white-paper-focus*.md` | 同上，多个版本 |
| `reference/` 目录 | 原始来源 outline 与转录稿（12 份） |
| `reports-md/GPT5.5outline.md` | 白皮书结构大纲（撰写时的内部参考） |
| `reports-md/outline-reference.md` | 来源到章节的映射（撰写时的内部参考） |

注：`white-paper-research/` 与 `reports-md/GPT5.5outline.md`、`reports-md/outline-reference.md` 是撰写期的内部参考文件，不发布到 GitHub Pages，但其内容已融入最终白皮书。

### 2.3 构建脚本

| 脚本 | 作用 |
|------|------|
| `scripts/build_report.py` | 收集 `NN-*.md` → Python `markdown` 库渲染 → 合并为单一 HTML |
| `scripts/cleanup_citations.py` | 第一轮引用格式清理（Tier 标签去除） |
| `scripts/cleanup_tier_refs.py` | 第二轮 Tier 标签残留清理 |
| `scripts/remove_example_urls.py` | 删除 example.com 占位 URL |
| `scripts/update_chapter_refs.py` | 章节重排后的内部 Chapter N 引用更新 |
| `scripts/unify_references.py` | 合并 12 章 References 为全局列表 |

### 2.4 样式与注册表

| 文件 | 作用 |
|------|------|
| `frontend/assets/css/github-markdown.css` | GitHub README 风格精简 CSS（约 180 行） |
| `frontend/data/reports.json` | 报告元数据注册表，首页渲染卡片来源 |

### 2.5 部署配置

| 文件 | 作用 |
|------|------|
| `.github/workflows/deploy-pages.yml` | 推送 `main` 分支时自动部署 `frontend/` 到 GitHub Pages |

---

## 3. 关键输出文件

| 文件 | 大小 | 说明 |
|------|------|------|
| `frontend/reports/gpt-5.5-evaluation-whitepaper.html` | 约 204 KB | 最终白皮书 HTML（13 章合并） |
| `https://gl-universe.github.io/AnalystReport/reports/gpt-5.5-evaluation-whitepaper.html` | — | 在线访问地址 |

---

## 4. 撰写过程关键决策

### 4.1 第 1 轮：白皮书首次构建 + 引用格式清理

- 13 个 Markdown 章节合并为单一 HTML，通过 `scripts/build_report.py` 实现
- 删除 Tier 标签（T3/T5/T6）从内联引用，改为行业惯例的 `(Author, Year)` 形式
- 删除 CNN/BBC media-targeting meta-commentary（"citable by CNN/BBC"等）
- 删除内部项目文件引用（`summary-white-paper-focus.md`、`GPT5.5outline.md`）
- COI 声明从 code block 改为普通段落

### 4.2 第 2 轮：读者视角七项修订

1. 删除 "each citable by journalists" 表述
2. 删除 41 处 `https://example.com/...` 占位 URL + 对应参考文献条目
3. 删除 "Notably absent from this report's source set" meta-commentary 段落
4. 验证 References 节位于章节末尾（已满足）
5. Test Dataset Description 从 Ch 3 移到 Ch 10（Safety 之后）
6. 删除无数据维度段落（P50/P95 latency、generation consistency/stability、medical/legal domain evaluations）
7. 章节重排：原 Ch 10 → 新 Ch 2，原 Ch 2 → 新 Ch 3，原 Ch 3 → 新 Ch 10

### 4.3 第 3 轮：References 全局合并

- 删除 12 个章节末尾的 `## References for This Chapter` 节
- 在 `12-appendix.md` 重写 Appendix H 为单一连续编号列表（1-12）
- 按作者字母序排列，合并同一来源的多个标题变体（OpenAI 5 条→1 条，Anthropic 2 条→1 条等）
- 删除内部文件引用（`summary-white-paper-focus.md`、`outline-reference.md`）

### 4.4 第 4 轮：文档结构整理（本次）

- 新建 `wiki/whitepaper-build-guide.md`（本文档）
- 整理 `Progress/` 与 `wiki/` 职责分工
- 移动 `todo.md` 到 `Progress/todo.md`
- 在 `README.md` 添加文档定位说明
- 补齐 `Progress/changelog.md` 四轮修订记录

---

## 5. 最终章节顺序

| 新 Ch | 文件 | 章节标题 | 原章节号 |
|------|------|---------|---------|
| 0 | `00-executive-summary.md` | Executive Summary | 0 |
| 1 | `01-research-background.md` | Research Background & Problem Setting | 1 |
| 2 | `02-practical-recommendations.md` | Practical Recommendations | 10 |
| 3 | `03-methodology.md` | Evaluation Methodology | 2 |
| 4 | `04-evaluation-metrics.md` | Evaluation Metrics System | 4 |
| 5 | `05-core-capability-results.md` | Core Capability Evaluation Results | 5 |
| 6 | `06-competitor-comparison.md` | Competitor Comparative Analysis | 6 |
| 7 | `07-failure-cases.md` | Failure Cases & Boundary Analysis | 7 |
| 8 | `08-cost-effectiveness.md` | Cost-Effectiveness Analysis | 8 |
| 9 | `09-safety-alignment.md` | Safety & Alignment Assessment | 9 |
| 10 | `10-dataset-description.md` | Test Dataset Description | 3 |
| 11 | `11-limitations.md` | Research Limitations | 11 |
| 12 | `12-appendix.md` | Appendix（含全局 References） | 12 |

**全局 References** 位于 `12-appendix.md` Appendix H，共 12 条按字母序排列的引用条目。

---

## 6. 快速查阅

### 6.1 重新构建 HTML

```bash
cd /Users/haor/workspace/CodeFilcker/AnalystReport
python3 scripts/build_report.py
```

输出：`frontend/reports/gpt-5.5-evaluation-whitepaper.html`

### 6.2 本地预览

```bash
cd frontend && python3 -m http.server 8080
# 访问 http://localhost:8080/reports/gpt-5.5-evaluation-whitepaper.html
```

### 6.3 部署上线

```bash
git add -A && git commit -m "update whitepaper" && git push
# GitHub Actions 自动部署 frontend/ 到 GitHub Pages
```

### 6.4 添加新章节

1. 在 `reports-md/` 创建 `NN-{name}.md`（NN 为两位数字编号）
2. 文件首行为 `# Chapter N — Title`
3. 正文使用 `(Author, Year)` 形式引用，不依赖编号
4. 若引入新来源，在 `12-appendix.md` Appendix H 添加条目并保持字母序
5. 运行 `python3 scripts/build_report.py` 重建 HTML
6. `git push` 部署

### 6.5 依赖安装

```bash
pip3 install markdown  # Python Markdown 渲染库
```

---

## 7. 相关文档

- 📖 项目架构：[`wiki/architecture.md`](./architecture.md)
- 🔄 通用工作流：[`wiki/workflow.md`](./workflow.md)
- 📰 媒体引用研究：[`wiki/media-citation-patterns.md`](./media-citation-patterns.md)
- 📈 变更日志：[`../Progress/changelog.md`](../Progress/changelog.md)
- 📋 任务追踪：[`../Progress/todo.md`](../Progress/todo.md)
