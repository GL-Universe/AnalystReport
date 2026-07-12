#!/usr/bin/env python3
"""
build_report.py

将 reports-md/ 目录下的章节 Markdown 文件按文件名顺序合并为一份完整的 HTML 白皮书，
输出到 frontend/reports/gpt-5.5-evaluation-whitepaper.html，供 GitHub Pages 部署。

执行方式：
    python3 scripts/build_report.py

约束：
- 仅读取文件名形如 `NN-*.md` 的章节文件（NN 为 00~12），跳过 outline / sample 等辅助文件
- 使用 Python `markdown` 库（已启用 tables / fenced_code / toc / sane_lists 扩展）
- 输出 HTML 自引用精简 GitHub 风格 CSS（frontend/assets/css/github-markdown.css）
- 不修改任何源 Markdown 文件
"""

import os
import re
import sys
from pathlib import Path
import markdown


# --- 路径定义 ---
ROOT = Path(__file__).resolve().parent.parent
REPORTS_MD_DIR = ROOT / "reports-md"
OUTPUT_HTML = ROOT / "frontend" / "reports" / "gpt-5.5-evaluation-whitepaper.html"

# 仅匹配形如 00-xxx.md ~ 12-xxx.md 的章节文件
CHAPTER_FILE_PATTERN = re.compile(r"^\d{2}-.+\.md$")


def collect_chapter_files():
    """收集 reports-md/ 下所有章节 Markdown 文件，按文件名升序返回。"""
    if not REPORTS_MD_DIR.is_dir():
        raise FileNotFoundError(f"reports-md 目录不存在：{REPORTS_MD_DIR}")
    files = [
        p for p in sorted(REPORTS_MD_DIR.iterdir())
        if p.is_file() and CHAPTER_FILE_PATTERN.match(p.name)
    ]
    if not files:
        raise RuntimeError("未找到任何章节 Markdown 文件（期望 00-*.md ~ 12-*.md）")
    return files


def render_chapter(path: Path) -> str:
    """读取单个章节 Markdown 并渲染为 HTML 片段。"""
    text = path.read_text(encoding="utf-8")
    html = markdown.markdown(
        text,
        extensions=[
            "tables",        # GitHub 风格表格
            "fenced_code",   # ``` 围栏代码块
            "toc",           # 自动生成锚点 id
            "sane_lists",    # 修正嵌套列表解析
            "nl2br",         # 段落内换行转 <br/>（保持原文断句）
        ],
        output_format="html5",
    )
    return html


def build_full_html(chapters: list[tuple[str, str]]) -> str:
    """组装完整 HTML 文档。chapters = [(filename, html), ...]"""
    parts = []
    for filename, html in chapters:
        parts.append(f'<!-- 章节来源: reports-md/{filename} -->')
        parts.append(html)
        parts.append('<hr class="chapter-divider" />')
    body = "\n".join(parts)

    # 提取章节大标题作为目录条目（仅 h1）
    toc_items = []
    for filename, html in chapters:
        m = re.search(r"<h1[^>]*id=\"([^\"]+)\"[^>]*>(.*?)</h1>", html, re.S)
        if m:
            anchor = m.group(1)
            # 去掉内部 HTML 标签只留文本
            title_text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            toc_items.append(f'<li><a href="#{anchor}">{title_text}</a></li>')
    toc_html = (
        '<nav class="toc"><h2>Chapters</h2><ol>'
        + "\n".join(toc_items)
        + '</ol></nav>'
        if toc_items
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>GPT-5.5 Model Service Evaluation White Paper - AnalystReport</title>
    <link rel="stylesheet" href="../assets/css/github-markdown.css" />
</head>
<body>
    <header class="page-header">
        <a href="../index.html" class="back-link">&larr; Back to report list</a>
        <h1 class="report-title">GPT-5.5 Model Service Evaluation White Paper</h1>
        <p class="report-meta">
            Independent evaluation &middot; Draft date: 2026-07-12 &middot; Citable by CNN / BBC body text
        </p>
    </header>

    <main class="markdown-body">
        {toc_html}
        {body}
    </main>

    <footer class="page-footer">
        <p>&copy; 2026 AnalystReport &middot;
            <a href="https://github.com/GL-Universe/AnalystReport" target="_blank">GitHub</a>
        </p>
    </footer>
</body>
</html>
"""


def main():
    files = collect_chapter_files()
    print(f"[1/3] 收集到 {len(files)} 个章节文件：")
    for f in files:
        print(f"      - {f.name}")

    chapters = []
    for f in files:
        html = render_chapter(f)
        chapters.append((f.name, html))
        print(f"[2/3] 渲染完成: {f.name} ({len(html):,} chars)")

    full_html = build_full_html(chapters)
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(full_html, encoding="utf-8")
    print(f"[3/3] 输出: {OUTPUT_HTML.relative_to(ROOT)} ({len(full_html):,} chars)")

    # 简单一致性自检
    h1_count = len(re.findall(r"<h1", full_html))
    h2_count = len(re.findall(r"<h2", full_html))
    table_count = len(re.findall(r"<table", full_html))
    pre_count = len(re.findall(r"<pre", full_html))
    print(f"\n[stats] h1={h1_count}, h2={h2_count}, tables={table_count}, code-blocks={pre_count}")
    if h1_count != len(files):
        print(f"[warn] h1 数量 ({h1_count}) 与章节文件数 ({len(files)}) 不一致", file=sys.stderr)


if __name__ == "__main__":
    main()
