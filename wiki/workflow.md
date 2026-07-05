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

用户对 AI 说：
- 「帮我生成一份关于 XX 的分析报告」
- 「调研一下 XX 行业，整理成报告」

### 2.2 调用 skill

```python
use_skill(skill_name="report-generator", reason="生成 XX 主题分析报告")
```

详见 [`skills/report-generator/SKILL.md`](../skills/report-generator/SKILL.md)。

### 2.3 产出

- 文件路径：`reports-md/{slug}.md`
- 文件结构：YAML front-matter + Markdown 正文

### 2.4 校验

- [ ] front-matter 含 title、description、date、author、icon、tags、slug
- [ ] 正文含「核心摘要」+ 编号章节 + 「展望与建议」
- [ ] 数据有来源标注
- [ ] 字数符合深度要求（brief 800 / standard 1500 / deep 3000）

---

## 3. 工作流 2：页面搭建

### 3.1 触发方式

用户对 AI 说：
- 「把刚才的报告发布上线」
- 「md 转 HTML 整合到前端」

### 3.2 调用 skill

```python
use_skill(skill_name="page-builder", reason="将 reports-md/*.md 转为 HTML")
```

详见 [`skills/page-builder/SKILL.md`](../skills/page-builder/SKILL.md)。

### 3.3 产出

- 新文件：`frontend/reports/{slug}.html`
- 更新文件：`frontend/data/reports.json`（追加条目）

### 3.4 校验

- [ ] 本地用浏览器打开 `frontend/index.html` 能看到新卡片
- [ ] 点击卡片跳转到详情页正常
- [ ] 详情页样式渲染正常（表格、引用块、标签）
- [ ] 返回按钮可回到首页

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

每次完成上述工作流后，由 AI 自动或在用户要求下追加记录。

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

1. 调用 `report-generator` 生成 md → `reports-md/{slug}.md`
2. 调用 `page-builder` 转 HTML → `frontend/reports/{slug}.html`
3. 本地预览校验
4. `git push`
5. 自动部署 → Pages 上线
6. 追加 `Progress/changelog.md` 记录

### 场景 B：仅修改已有报告内容

1. 编辑 `reports-md/{slug}.md`
2. 调用 `page-builder` 重新生成 HTML（覆盖）
3. `git push`

### 场景 C：仅调整前端样式/首页布局

1. 编辑 `frontend/assets/css/style.css` 或 `frontend/index.html`
2. 本地预览
3. `git push`

### 场景 D：删除一份报告

1. 删除 `reports-md/{slug}.md`
2. 删除 `frontend/reports/{slug}.html`
3. 从 `frontend/data/reports.json` 移除对应条目
4. `git push`

---

## 7. 故障排查

| 现象 | 可能原因 | 解决方案 |
|------|----------|----------|
| 首页无新报告卡片 | `reports.json` 未更新 | 检查 JSON 格式，确认新条目已追加 |
| 卡片点击 404 | HTML 文件路径错误 | 检查 `file` 字段是否为 `reports/{slug}.html` |
| 部署失败 | Actions 工作流错误 | 查看 Actions 日志，确认 `path: 'frontend'` |
| Pages 未更新 | 缓存或部署延迟 | 等 1-2 分钟，或强制刷新浏览器 |
| 样式丢失 | CSS 路径错误 | 检查 HTML 中的 `../assets/css/style.css` 路径 |
