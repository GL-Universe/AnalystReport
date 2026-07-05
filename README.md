# 📊 AnalystReport

> 多维度数据分析报告中心 · 通过 GitHub Pages 静态呈现

## 🚀 快速开始

### 在线查看

访问 **[https://gl-universe.github.io/AnalystReport](https://gl-universe.github.io/AnalystReport)** 即可浏览所有报告。

### 本地预览

```bash
# 克隆仓库
git clone git@github.com:GL-Universe/AnalystReport.git
cd AnalystReport

# 使用任意静态服务器启动
python3 -m http.server 8080
# 然后访问 http://localhost:8080
```

## 📁 项目结构

```
AnalystReport/
├── index.html              # 🏠 首页 — 报告列表
├── assets/
│   ├── css/style.css       # 🎨 全局样式
│   └── js/main.js          # ⚡ 动态加载报告列表
├── data/
│   └── reports.json        # 📋 报告元数据（标题、日期、路径等）
├── reports/                # 📄 报告文件夹
│   └── sample-report.html  # 示例报告
└── README.md
```

## ✍️ 如何添加新报告

### 第 1 步：创建报告 HTML 文件

在 `reports/` 目录下创建新的 `.html` 文件。推荐复制 `reports/sample-report.html` 作为模板，修改内容即可。

> 💡 **模板已内置：**
> - 返回首页链接
> - 统一的报告头部样式
> - 表格、引用块、高亮框等组件
> - 标签系统

### 第 2 步：注册报告元数据

编辑 `data/reports.json`，在 `reports` 数组中添加条目：

```json
{
  "title": "你的报告标题",
  "description": "简短描述，会显示在首页卡片上",
  "date": "2026-07-05",
  "author": "你的名字",
  "icon": "📊",
  "tags": ["tech", "market"],
  "file": "reports/your-report.html"
}
```

### 第 3 步：提交并推送

```bash
git add .
git commit -m "添加新报告：你的报告标题"
git push origin main
```

推送后，GitHub Pages 会自动更新（通常 1-2 分钟内生效）。

## 🏷️ 可用标签

在 `reports.json` 中的 `tags` 字段支持以下预设标签：

| 标签 | CSS 类 | 用途 |
|------|--------|------|
| `tech` | `tag-tech` | 技术分析 |
| `market` | `tag-market` | 市场研究 |
| `data` | `tag-data` | 数据分析 |
| `strategy` | `tag-strategy` | 战略规划 |

可在 `assets/css/style.css` 的 `.tag-*` 中自定义更多标签样式。

## 🛠️ 技术栈

- 纯静态 HTML/CSS/JavaScript（零依赖）
- 通过 `reports.json` 动态加载报告列表
- 托管于 **GitHub Pages**，免费、自动部署

## 📄 License

MIT