# 📚 AnalystReport Wiki

本目录存放项目的结构维度文档（架构、工作流、案例研究），均为静态说明，不记录时间线变更。

> 时间维度文档（变更日志、任务追踪）在 [`../Progress/`](../Progress/) 目录。

## 📖 文档索引

| 文档 | 内容 | 适用读者 |
|------|------|----------|
| [`architecture.md`](./architecture.md) | 项目目录结构、模块职责、数据流向 | 新加入的开发者、维护者 |
| [`workflow.md`](./workflow.md) | 报告生成 → 页面搭建 → 部署的完整工作流 | 内容作者、AI skill 调用者 |
| [`media-citation-patterns.md`](./media-citation-patterns.md) | 主流媒体 AI 评测引用模式研究 + 评测报告大纲模板 | `report-generator` skill 调用者、报告作者 |
| [`whitepaper-build-guide.md`](./whitepaper-build-guide.md) | GPT-5.5 评测白皮书构建案例研究（某次具体构建的结构化总结） | 撰写多章节合并型报告的作者 |

## 🔗 关联资源

- 🛠️ AI Skills: [`../skills/`](../skills/) 目录
- 📊 报告源文件: [`../reports-md/`](../reports-md/) 目录
- 🚀 前端代码: [`../frontend/`](../frontend/) 目录
- 📈 项目进展（时间维度）: [`../Progress/`](../Progress/) 目录
- 🧰 构建脚本: [`../scripts/`](../scripts/) 目录（多章节 md 批量合并工具）

## 📝 维护说明

- 本目录文档定位为"结构维度"（静态说明），不记录时间线变更
- 时间线变更请记录到 `Progress/changelog.md`
- 新增文档时在本索引添加条目
