# 🛠️ Skills - AI 技能集合

本目录存放 AnalystReport 项目使用的 AI 技能（Skill）。每个 skill 是一个独立的可复用工作流，由 AI 调用以完成特定任务。

## 📋 Skill 列表

| Skill | 用途 | 输入 | 输出 |
|-------|------|------|------|
| [`report-generator`](./report-generator/) | 生成分析报告 | 主题、数据来源 | `reports-md/*.md` |
| [`page-builder`](./page-builder/) | 将 md 转为 HTML 页面 | md 文件路径 | `frontend/reports/*.html` + 更新 `reports.json` |

## 🔄 协作流程

```
   用户提需求
       │
       ▼
┌──────────────────┐
│ report-generator │  →  reports-md/*.md
└──────────────────┘
       │
       ▼
┌──────────────────┐
│   page-builder   │  →  frontend/reports/*.html
└──────────────────┘       + frontend/data/reports.json
       │
       ▼
   git push → GitHub Pages 自动部署
       │
       ▼
┌──────────────────┐
│  Progress 记录    │  →  Progress/changelog.md
└──────────────────┘
```

## 📁 目录结构

```
skills/
├── README.md                       # 本文件
├── report-generator/               # 报告生成 skill
│   └── SKILL.md
└── page-builder/                   # 页面搭建 skill
    └── SKILL.md
```

## 📖 如何调用

每个 skill 通过 `use_skill(skill_name="...")` 调用，详见各 skill 内的 `SKILL.md` 说明。
