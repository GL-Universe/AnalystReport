# 📝 AnalystReport 待办事项

> 项目任务追踪文件 · 按状态分类记录已完成与待办事项
> 最近更新：2026-07-12

---

## ✅ 已完成事项

### 阶段一：项目初始化（v0.1.0 - 2026-07-05）

- [x] 初始化 GitHub 仓库 `GL-Universe/AnalystReport`
- [x] 创建首页 `frontend/index.html`（报告卡片列表，动态加载）
- [x] 搭建样式系统 `frontend/assets/css/style.css`（全局变量 + 响应式）
- [x] 实现交互脚本 `frontend/assets/js/main.js`（异步加载 reports.json）
- [x] 创建报告注册表 `frontend/data/reports.json`
- [x] 编写示例报告 `frontend/reports/sample-report.html`
- [x] 配置 GitHub Actions 自动部署 `.github/workflows/deploy-pages.yml`
- [x] 验证网站上线 `https://gl-universe.github.io/AnalystReport/`

### 阶段二：项目结构重构（v0.2.0 - 2026-07-05）

- [x] 将扁平结构拆分为 5 个职责独立模块（`frontend/`、`skills/`、`reports-md/`、`wiki/`、`Progress/`）
- [x] 迁移文件至新结构（`index.html` → `frontend/index.html` 等）
- [x] 新增示例 `reports-md/sample-report.md`（带 front-matter 的 Markdown 源）
- [x] 创建 skill 框架（`skills/report-generator/SKILL.md`、`skills/page-builder/SKILL.md`、`skills/README.md`）
- [x] 新增 wiki 文档（`wiki/architecture.md`、`wiki/workflow.md`）
- [x] 新增 Progress 记录（`Progress/README.md`、`Progress/changelog.md`）
- [x] 修改 GitHub Actions 部署路径为 `frontend`
- [x] 更新根 README 反映新结构

### 阶段三：主流媒体引用模式研究（v0.2.1 - 2026-07-06）

- [x] 调研 The Verge / BBC / MIT Technology Review / The New York Times / CNN 五家媒体的 AI 评测引用模式
- [x] 深度分析 4 篇样本文章（Verge Rabbit R1 / BBC chatbots / MIT health tools / NYT chatbot manipulation）
- [x] 提炼出 10 类引用材料分类（A-J），按支撑力分三梯队
- [x] 识别哪些来源是更好的引用示例（第一/二/三梯队 + 推荐组合策略）
- [x] 产出基于主流媒体引用模式的评测报告大纲（去 Benchmark 化，11 章节）
- [x] 写入研究文档 `wiki/media-citation-patterns.md`（276 行）
- [x] 在 `Progress/changelog.md` 追加 v0.2.1 变更记录
- [x] 更新 `wiki/README.md` 索引

### 阶段四：大纲文件输出（2026-07-11）

- [x] 将评测报告大纲作为独立文件输出到项目根目录 `report-outline-v1.md`
- [x] 文件自包含：引用类型图例（A-J）+ 推荐组合策略 + 11 章节大纲 + 7 条关键洞察

### 阶段五：GPT-5.5 白皮书撰写与四轮修订（v0.3.0 ~ v0.3.4 - 2026-07-12）

#### v0.3.0 - 白皮书首次构建
- [x] 编写 `scripts/build_report.py` 构建脚本
- [x] 编写 `frontend/assets/css/github-markdown.css` GitHub 风格精简样式
- [x] 运行脚本生成 `frontend/reports/gpt-5.5-evaluation-whitepaper.html`
- [x] 更新 `frontend/data/reports.json` 注册表追加白皮书条目
- [x] 本地验证渲染一致性
- [x] git commit + push，GitHub Pages 部署成功

#### v0.3.1 - 引用格式行业惯例化
- [x] 删除 Tier 标签（T3/T5/T6）从内联引用
- [x] 正文 Tier 缩写替换为描述性语言
- [x] 删除 CNN/BBC media-targeting meta-commentary（14+ 处）
- [x] 删除内部项目文件引用（`summary-white-paper-focus.md`、`GPT5.5outline.md`）
- [x] COI 声明从 code block 改为普通段落
- [x] "Core Findings (Citable by Journalists)" 改为 "Key Findings"
- [x] Source Tier 分类表改为标准 Source Classification 格式
- [x] Appendix H/I/J 去除 Tier 编码

#### v0.3.2 - 读者视角七项修订
- [x] 删除 "each citable by journalists" 表述
- [x] 删除 41 处 `https://example.com/...` 占位 URL + 对应参考文献条目
- [x] 删除 "Notably absent from this report's source set" meta-commentary 段落
- [x] 验证 References 节位于章节末尾
- [x] Test Dataset Description 从 Ch 3 移到 Ch 10（Safety 之后）
- [x] 删除无数据维度段落（P50/P95、consistency/stability、medical/legal evaluations）
- [x] 章节重排：原 Ch 10 → 新 Ch 2，原 Ch 2 → 新 Ch 3，原 Ch 3 → 新 Ch 10
- [x] 更新所有内部 "Chapter N" 引用
- [x] 更新 Appendix I 与 Appendix J 反映新顺序

#### v0.3.3 - References 全局合并
- [x] 删除 12 个章节末尾的 `## References for This Chapter` 节
- [x] 在 `12-appendix.md` 重写 Appendix H 为单一连续编号列表（1-12）
- [x] 按作者字母序排列，合并同一来源的多个标题变体
- [x] 添加 "Independent technical review" 条目
- [x] 清理 `04-evaluation-metrics.md` 中 `summary-white-paper-focus.md` 引用残留
- [x] 清理 `10-dataset-description.md` 中 `outline-reference.md` 引用残留

#### v0.3.4 - 项目文档结构整理
- [x] 新建 `wiki/whitepaper-build-guide.md`（白皮书构建案例研究）
- [x] 移动 `todo.md` 到 `Progress/todo.md`（时间维度归集）
- [x] 补齐 `Progress/changelog.md` v0.3.1~v0.3.4 四轮修订记录
- [x] 更新 `Progress/README.md` 版本概览表到 v0.3.4
- [x] 简化 `README.md` 重复内容为概览+链接，添加文档定位说明
- [x] 更新 `wiki/README.md` 索引添加 whitepaper-build-guide

---

## 📌 待办事项

### 🔥 高优先级 - 即将推进

- [ ] **按大纲重写 `reports-md/sample-report.md` 示例**：用真实主题演示 11 章节结构 + A-J 引用类型的落地形态
- [ ] **在报告 front-matter 增加 `evidence_types` 字段**：标注该报告用了哪些引用类型（A-J），便于首页展示评测严谨度

### 🟡 中优先级 - 待确认后推进

- [ ] **确认报告文件夹命名方案**：上一轮对话讨论的「顺序控制文件 + 章节文件」模式（一份报告对应一个文件夹，内含 `index.md` 顺序控制文件 + 多个按章节语义命名的 `.md` 文件），等待用户最终确认
- [ ] **更新 `frontend/data/reports.json` 结构**：如确认上述命名方案，需相应调整注册表字段以支持多章节报告

### 🟢 低优先级 - 未来扩展（来自 `wiki/architecture.md` 第 6 节）

- [ ] 🌐 多语言支持（`reports-md/en/`、`reports-md/zh/`）
- [ ] 📊 数据可视化（在 HTML 报告中嵌入图表库）
- [ ] 📈 访问统计（接入 Plausible / Umami）

---

## 📊 进度概览

| 阶段 | 状态 | 完成度 |
|------|------|--------|
| 阶段一：项目初始化 | ✅ 完成 | 8/8 |
| 阶段二：项目结构重构 | ✅ 完成 | 8/8 |
| 阶段三：媒体引用模式研究 | ✅ 完成 | 8/8 |
| 阶段四：大纲文件输出 | ✅ 完成 | 2/2 |
| 阶段五：GPT-5.5 白皮书撰写与四轮修订 | ✅ 完成 | 35/35 |
| 阶段六：示例报告与 front-matter 增强 | 🔥 进行中 | 0/2 |
| 阶段七：报告文件夹结构升级 | 🟡 待确认 | 0/2 |
| 阶段八：未来扩展 | 🟢 待启动 | 0/3 |

---

## 🔗 相关文件索引

- 📋 本文件：`Progress/todo.md`
- 📈 变更日志：`Progress/changelog.md`
- 🏗️ 项目架构：`wiki/architecture.md`
- 🔄 工作流：`wiki/workflow.md`
- 📰 媒体引用模式研究：`wiki/media-citation-patterns.md`
- 📝 白皮书构建指南：`wiki/whitepaper-build-guide.md`
- 📋 评测报告大纲 v1：`report-outline-v1.md`

---

## 📝 维护说明

- 完成一项后，将 `[ ]` 改为 `[x]`，并移至「已完成事项」对应阶段
- 新增事项时，按优先级归类到「待办事项」对应分区
- 每个阶段完成后，在 `Progress/changelog.md` 追加版本记录
- 本文件位于 `Progress/todo.md`（v0.3.4 起从项目根目录移到 Progress/）
- v0.3.5 起 `skills/` 目录已删除，所有文档不再引用 skills
