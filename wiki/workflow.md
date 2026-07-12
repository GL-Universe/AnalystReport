# 🔄 工作流说明

本文档说明 AnalystReport 项目的三种核心工作流：报告生成、页面搭建、部署上线。

## 1. 完整工作流概览

```
[1] 报告生成      →  reports-md/*.md
[2] 页面搭建      →  frontend/reports/*.html + reports.json
[3] 部署上线      →  git push → GitHub Pages
[4] 进展记录      →  Progress/changelog.md
```

---

## 2. 工作流 1：报告生成

### 2.1 触发方式

作者撰写 Markdown 文件，保存到 `reports-md/` 目录。

### 2.2 产出

- 文件路径：`reports-md/{slug}.md`（单篇模式）或 `reports-md/NN-{name}.md`（多章节模式）
- 文件结构：YAML front-matter + Markdown 正文

### 2.3 校验

- [ ] front-matter 含 title、description、date、author、icon、tags、slug
- [ ] 正文含「核心摘要」+ 编号章节 + 「展望与建议」
- [ ] 数据有来源标注
- [ ] 字数符合深度要求（brief 800 / standard 1500 / deep 3000）

---

## 3. 工作流 2：页面搭建

### 3.1 触发方式

作者完成 Markdown 后，运行构建脚本或手动转换为 HTML。

### 3.2 产出

- 新文件：`frontend/reports/{slug}.html`
- 更新文件：`frontend/data/reports.json`（追加条目）

### 3.3 校验

- [ ] 本地用浏览器打开 `frontend/index.html` 能看到新卡片
- [ ] 点击卡片跳转到详情页正常
- [ ] 详情页样式渲染正常（表格、引用块、标签）
- [ ] 返回按钮可回到首页

### 3.4 子流程 A：单篇 md 转 HTML

适用：`reports-md/{slug}.md`（含 front-matter 的单文件报告）。

手动按 `sample-report.html` 风格编写 HTML，引用 `assets/css/style.css`。参考示例 [`frontend/reports/sample-report.html`](../frontend/reports/sample-report.html)。

### 3.5 子流程 B：多章节 md 批量合并

适用：`reports-md/` 下含多个 `NN-*.md` 章节文件（如 GPT-5.5 白皮书的 00 ~ 12 章）。

使用构建脚本一键生成：

```bash
python3 scripts/build_report.py
```

脚本逻辑：
1. 自动收集 `reports-md/` 下匹配 `^\d{2}-.+\.md$` 的章节文件，按文件名升序
2. 用 Python `markdown` 库渲染（启用 `tables` / `fenced_code` / `toc` / `sane_lists` / `nl2br`）
3. 自动生成章节目录（h1 锚点列表）注入页面顶部
4. 套用 HTML 模板（含返回链接、CSS 引用、footer）
5. 输出到 `frontend/reports/gpt-5.5-evaluation-whitepaper.html`，引用 `assets/css/github-markdown.css`

脚本完成后需手动更新 `frontend/data/reports.json` 追加条目。

详见 [`wiki/whitepaper-build-guide.md`](./whitepaper-build-guide.md)。

---

## 4. 工作流 3：部署上线

### 4.1 触发方式

```bash
git add -A
git commit -m "发布新报告：{标题}"
git push origin main
```

### 4.2 自动化流程

GitHub Actions 工作流 [`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml) 自动执行：

1. 检出代码
2. 配置 Pages
3. 上传 `frontend/` 目录作为 Pages artifact
4. 部署到 `https://gl-universe.github.io/AnalystReport/`

### 4.3 部署状态查询

- GitHub 仓库 → Actions 标签页查看构建日志
- Settings → Pages 查看部署 URL 和历史

### 4.4 验证

```bash
curl -s -o /dev/null -w "%{http_code}" https://gl-universe.github.io/AnalystReport/
# 期望: 200
```

---

## 5. 工作流 4：进展记录

### 5.1 触发方式

每次完成上述工作流后，在用户要求下追加记录。

### 5.2 记录位置

`Progress/changelog.md`，按时间倒序追加。

### 5.3 记录格式

```markdown
## YYYY-MM-DD - {简短标题}

**变更类型**: feat / refactor / fix / docs
**影响范围**: {模块}

- 具体变更点 1
- 具体变更点 2

**验证**: {如何验证通过}
```

详见 [`Progress/changelog.md`](../Progress/changelog.md)。

---

## 6. 常见场景

### 场景 A：新增一份完整报告（从零到上线）

1. 撰写 md → `reports-md/{slug}.md`
2. 转换为 HTML → `frontend/reports/{slug}.html`（手动或脚本）
3. 本地预览校验
4. `git push`
5. 自动部署 → Pages 上线
6. 追加 `Progress/changelog.md` 记录

### 场景 B：仅修改已有报告内容

1. 编辑 `reports-md/{slug}.md`
2. 重新生成 HTML（覆盖）
3. `git push`

### 场景 C：仅调整前端样式/首页布局

1. 编辑 `frontend/assets/css/style.css` 或 `frontend/index.html`
2. 本地预览
3. `git push`

### 场景 D：删除一份报告

1. 删除 `reports-md/{slug}.md` 与 `frontend/reports/{slug}.html`
2. 从 `frontend/data/reports.json` 移除条目
3. `git push`

---

## 7. 相关文档

- 📖 [项目架构](./architecture.md)
- 📝 [白皮书构建指南](./whitepaper-build-guide.md)
- 📈 [变更日志](../Progress/changelog.md)
- 📋 [任务追踪](../Progress/todo.md)
