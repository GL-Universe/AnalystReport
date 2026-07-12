#!/usr/bin/env python3
"""
Remove example.com placeholder URL references from all chapter files.

For each .md file:
1. Remove URL: https://example.com/... suffixes from reference list entries
2. Remove entire reference list entries that point to example.com
3. Remove inline "(source, YYYY-MM-DD). URL: https://example.com/..." source attributions
4. Remove appendix rows pointing to example.com
5. Remove entire appendix subsections whose only source is an example.com URL
"""
import re
import os
import glob


def process(content: str) -> str:
    # 1. Remove "URL: https://example.com/..." trailing phrases (keep the citation title, drop URL)
    # e.g., "An independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15. URL: https://example.com/..."
    # ->   "An independent technical review. "Gemini 3.5 Flash vs GPT-5.5: a hands-on comparison." 2026-05-15."
    content = re.sub(r'\s*URL:\s*https?://example\.com[^\n]*', '', content)

    # 2. Remove inline source attribution lines like:
    #    **Source**: an independent technical review, 2026-05-15. URL: https://example.com/...
    #    -> remove whole line
    content = re.sub(
        r'^\*\*Source\*\*:[^\n]*example\.com[^\n]*\n?',
        '',
        content,
        flags=re.MULTILINE
    )
    # Also remove "**Source URL**: https://example.com/..." standalone
    content = re.sub(
        r'^Source URL:\s*https?://example\.com[^\n]*\n?',
        '',
        content,
        flags=re.MULTILINE
    )

    # 3. Remove reference list lines that now have no URL/title (i.e., start with number but end at date)
    #    Actually the pattern is "N. Author. "Title." Date." — keep these; they're valid references without URL.
    #    But if the whole entry was ONLY a URL line, drop it.
    #    A reference entry spanning multiple lines, where one line was "   URL: https://example.com/...",
    #    that line is already handled by rule 1.

    # 4. Remove appendix rows whose URL column is example.com
    #    Pattern: "| <text> | <source> | https://example.com/... |"
    content = re.sub(
        r'^\|[^\n]*\|[^|]*\|\s*https?://example\.com[^\n]*\|\s*$\n?',
        '',
        content,
        flags=re.MULTILINE
    )

    # 5. Remove appendix rows where URL is example.com but the row has only 2 cols (no separator)
    #    e.g., "| Independent technical review head-to-head tests | industry technical article | https://example.com/technical-review/... |"
    #    Already handled by rule 4.

    # 6. Remove entire reference list entries that contain "example.com" (now they're only the citation text without URL, but still mention example.com via the title's source)
    #    Actually since we removed URL, example.com shouldn't appear. But if a source is "independent technical review" with a fake URL, the citation text itself is still valid (just unverifiable).
    #    Decision per user: delete all example.com references. Since URL is gone, we should also delete the entire reference entry if it was one of the "TechnicalAnalysis-X" anonymous sources
    #    OR the "independent technical review" source. These sources are unverifiable.

    # 7. Delete reference list entries for TechnicalAnalysis-A/B/C/E and "independent technical review"
    #    Pattern: numbered list items with these source names
    delete_patterns = [
        r'^\d+\.\s+TechnicalAnalysis-[A-Z][^\n]*(?:\n\s+[^\n]*)*\n?',
        r'^\d+\.\s+an?\s+independent\s+technical\s+review[^\n]*(?:\n\s+[^\n]*)*\n?',
        r'^\d+\.\s+An\s+independent\s+technical\s+review[^\n]*(?:\n\s+[^\n]*)*\n?',
        r'^\d+\.\s+Industry\s+technical\s+analysis[^\n]*(?:\n\s+[^\n]*)*\n?',
    ]
    for pat in delete_patterns:
        content = re.sub(pat, '', content, flags=re.MULTILINE)

    # 8. Also delete the same sources when they appear as unnumbered appendix list items
    #    Pattern in 12-appendix.md Appendix H:
    #    "1. **TechnicalAnalysis-A (industry technical press)**. ..."  — already handled above
    #    "5. **an independent technical review**. ..." — handled above
    #    But these are bolded; update pattern:
    content = re.sub(
        r'^\d+\.\s+\*\*TechnicalAnalysis-[A-Z][^\n]*(?:\n[^\n]*)*\n?',
        '',
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r'^\d+\.\s+\*\*an\s+independent\s+technical\s+review\*\*[^\n]*(?:\n[^\n]*)*\n?',
        '',
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r'^\d+\.\s+\*\*An\s+independent\s+technical\s+review\*\*[^\n]*(?:\n[^\n]*)*\n?',
        '',
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r'^\d+\.\s+\*\*Industry\s+technical\s+analysis\*\*[^\n]*(?:\n[^\n]*)*\n?',
        '',
        content,
        flags=re.MULTILINE
    )

    # 9. Clean up double blank lines left by deletions
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    pattern = os.path.join(repo_root, 'reports-md', '[0-9][0-9]-*.md')
    md_files = sorted(glob.glob(pattern))

    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        cleaned = process(original)
        if cleaned != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f'✓  modified: {os.path.basename(filepath)}')
        else:
            print(f'   unchanged: {os.path.basename(filepath)}')


if __name__ == '__main__':
    main()
