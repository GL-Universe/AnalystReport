# 📝 AnalystReport 待办事项

> 项目任务追踪文件 · 按状态分类记录已完成与待办事项
> 最近更新：2026-07-11

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

---

## 📌 待办事项

### 🔥 高优先级 - 即将推进

- [ ] **将大纲同步到 `skills/report-generator/SKILL.md`**：作为报告生成的章节模板，让 AI skill 调用时直接产出符合主流媒体引用模式的报告
- [ ] **按大纲重写 `reports-md/sample-report.md` 示例**：用真实主题演示 11 章节结构 + A-J 引用类型的落地形态
- [ ] **在报告 front-matter 增加 `evidence_types` 字段**：标注该报告用了哪些引用类型（A-J），便于首页展示评测严谨度

### 🟡 中优先级 - 待确认后推进

- [ ] **确认报告文件夹命名方案**：上一轮对话讨论的「顺序控制文件 + 章节文件」模式（一份报告对应一个文件夹，内含 `index.md` 顺序控制文件 + 多个按章节语义命名的 `.md` 文件），等待用户最终确认
- [ ] **更新 `frontend/data/reports.json` 结构**：如确认上述命名方案，需相应调整注册表字段以支持多章节报告
- [ ] **更新 `skills/page-builder/SKILL.md`**：让 page-builder 能识别新的「文件夹 + index.md + 章节文件」结构并正确转换为 HTML

### 🟢 低优先级 - 未来扩展（来自 `wiki/architecture.md` 第 6 节）

- [ ] 🌐 多语言支持（`reports-md/en/`、`reports-md/zh/`）
- [ ] 📊 数据可视化（在 HTML 报告中嵌入图表库）
- [ ] 🔄 md 自动监听（git hook 触发 page-builder）
- [ ] 📈 访问统计（接入 Plausible / Umami）

---

## 📊 进度概览

| 阶段 | 状态 | 完成度 |
|------|------|--------|
| 阶段一：项目初始化 | ✅ 完成 | 8/8 |
| 阶段二：项目结构重构 | ✅ 完成 | 8/8 |
| 阶段三：媒体引用模式研究 | ✅ 完成 | 8/8 |
| 阶段四：大纲文件输出 | ✅ 完成 | 2/2 |
| 阶段五：大纲落地到 skill & 示例 | 🔥 进行中 | 0/3 |
| 阶段六：报告文件夹结构升级 | 🟡 待确认 | 0/3 |
| 阶段七：未来扩展 | 🟢 待启动 | 0/4 |

---

## 🔗 相关文件索引

- 📋 本文件：`todo.md`
- 📈 变更日志：`Progress/changelog.md`
- 🏗️ 项目架构：`wiki/architecture.md`
- 🔄 工作流：`wiki/workflow.md`
- 📰 媒体引用模式研究：`wiki/media-citation-patterns.md`
- 📋 评测报告大纲 v1：`report-outline-v1.md`
- 🛠️ Skills 总览：`skills/README.md`

---

## 📝 维护说明

- 完成一项后，将 `[ ]` 改为 `[x]`，并移至「已完成事项」对应阶段
- 新增事项时，按优先级归类到「待办事项」对应分区
- 每个阶段完成后，在 `Progress/changelog.md` 追加版本记录
