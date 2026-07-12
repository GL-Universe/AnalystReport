#!/usr/bin/env python3
"""
cleanup_citations.py — Phase 1 white paper cleanup.

Transformations applied to all 13 chapter files:
1. Remove Tier suffix from inline citations: (Author, Year, T3) -> (Author, Year)
2. Remove standalone (T3)/(T5)/(T6) from section headings and source lines
3. Remove Tier labels from reference list entries: — **T3 independent evaluation**
4. Remove blockquote lines that expose internal writing meta-commentary
5. Remove body-text references to internal project files
"""

import re
import os
import glob

# ---------------------------------------------------------------------------
# Tier label → description mapping (for body text substitution)
# ---------------------------------------------------------------------------
TIER_DESCRIPTIONS = {
    'T3': 'independent measurement',
    'T5': 'practitioner testing',
    'T6': 'vendor-reported',
}


def process_content(content: str) -> str:

    # -----------------------------------------------------------------------
    # 1. Remove Tier suffix from inline parenthetical citations
    #    (Author, Year, T3) -> (Author, Year)
    #    (Author, Date, T5) -> (Author, Date)
    # -----------------------------------------------------------------------
    content = re.sub(r',\s*T[1-6]\)', ')', content)

    # -----------------------------------------------------------------------
    # 2. Remove standalone (T3)/(T5)/(T6) at end of section headings
    #    ### 7.3.1 Aggregate hallucination rate (T3) -> ### 7.3.1 ...
    # -----------------------------------------------------------------------
    content = re.sub(r'\s+\(T[1-6]\)\s*$', '', content, flags=re.MULTILINE)

    # -----------------------------------------------------------------------
    # 3. Remove Tier labels from reference list entries
    #    "— **T3 independent evaluation**"  -> ""
    #    "— **T5+T6 analysis**"             -> ""
    #    "— T5 user testing"                -> ""
    # -----------------------------------------------------------------------
    content = re.sub(r'\s*—\s*\*\*T[1-6][+/]?T?[1-6]?\s+[^*\n]+\*\*', '', content)
    content = re.sub(r'\s*—\s*T[1-6][+/]?T?[1-6]?\s+[a-zA-Z][^\n]*', '', content)

    # -----------------------------------------------------------------------
    # 4. Remove blockquote lines exposing internal meta-commentary
    # -----------------------------------------------------------------------
    meta_patterns = [
        # References to internal project files
        r'^>.*`summary-white-paper-focus\.md`[^\n]*\n?',
        r'^>.*`GPT5\.5outline\.md`[^\n]*\n?',
        r'^>.*`GPT5\.5outline`[^\n]*\n?',
        r'^>.*Per the chapter outline[^\n]*\n?',
        # CNN/BBC media targeting language
        r'^>.*[Cc][Nn][Nn]\s*/\s*[Bb][Bb][Cc][^\n]*\n?',
        r'^>.*[Bb][Bb][Cc]\s*/\s*[Cc][Nn][Nn][^\n]*\n?',
        r'^>.*citable by CNN[^\n]*\n?',
        r'^>.*citable by Journalists[^\n]*\n?',
        r'^>.*CNN and BBC[^\n]*\n?',
        r'^>.*BBC.*mandatory[^\n]*\n?',
        r'^>.*mandatory.*BBC[^\n]*\n?',
        r'^>.*BBC.*reporters[^\n]*\n?',
        r'^>.*policy.*journalists[^\n]*\n?',
        r'^>.*journalists.*cite[^\n]*\n?',
        r'^>.*Omission.*BBC[^\n]*\n?',
        r'^>.*BBC.*willing[^\n]*\n?',
        r'^>.*BBC.*credibility[^\n]*\n?',
        r'^>.*BBC.*downgrade[^\n]*\n?',
        r'^>.*downgrade.*BBC[^\n]*\n?',
        r'^>.*classified as a vendor[^\n]*\n?',
        r'^>.*determines whether the report is cited[^\n]*\n?',
        r'^>.*[Dd]ocument nature.*CNN[^\n]*\n?',
        r'^>.*[Rr]eference standard.*CNN[^\n]*\n?',
    ]
    for pattern in meta_patterns:
        content = re.sub(pattern, '', content, flags=re.MULTILINE)

    # -----------------------------------------------------------------------
    # 5. Remove body-text references to internal project files
    # -----------------------------------------------------------------------
    # "per `summary-white-paper-focus.md` Section VIII" → ""
    content = re.sub(
        r'\s*per\s+`summary-white-paper-focus\.md`[^.,;\n]*',
        '', content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'\s*in\s+`summary-white-paper-focus\.md`[^.,;\n]*',
        '', content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'`summary-white-paper-focus\.md`[^.,;\n ]*',
        '', content
    )
    # "per `GPT5.5outline.md` Chapter 7" → ""
    content = re.sub(
        r'\s*\(per\s+`GPT5\.5outline\.md`[^)]*\)',
        '', content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'\s*per\s+`GPT5\.5outline\.md`[^.,;\n]*',
        '', content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'`GPT5\.5outline\.md`[^.,;\n ]*',
        '', content
    )
    # "The chapter outline (`GPT5.5outline.md`) recommended..."
    content = re.sub(
        r'[Tt]he chapter outline \(`GPT5\.5outline\.md`\)',
        'The original research plan',
        content
    )

    # -----------------------------------------------------------------------
    # 6. Replace T3/T5/T6 shorthand in source attribution lines
    #    "**Source**: Artificial Analysis, 2026-04-23 (T3)"
    #    -> "**Source**: Artificial Analysis, 2026-04-23"
    #    Already handled above by rule 2, but catch remaining cases
    # -----------------------------------------------------------------------
    content = re.sub(r'\(T[1-6]\)(?=\s*$)', '', content, flags=re.MULTILINE)

    # -----------------------------------------------------------------------
    # 7. Replace "T3 source" / "T3 sources" in confidence statements
    #    "Confidence statement: T3 source. ..."
    #    -> "Confidence statement: Independent measurement. ..."
    # -----------------------------------------------------------------------
    content = content.replace('T3 source.', 'Independent measurement (Artificial Analysis).')
    content = content.replace('T3 source;', 'Independent measurement (Artificial Analysis);')

    # -----------------------------------------------------------------------
    # 8. Replace "T3-verified" / "T3 verified" / "T3 verification"
    # -----------------------------------------------------------------------
    content = re.sub(r'\bT3-verified\b', 'independently verified', content)
    content = re.sub(r'\bT3 verified\b', 'independently verified', content)
    content = re.sub(r'\bT3 verification\b', 'independent verification', content)
    content = re.sub(r'\bnot T3-verified\b', 'not independently verified', content)
    content = re.sub(r'\bnot T3 verified\b', 'not independently verified', content)

    # -----------------------------------------------------------------------
    # 9. Replace "(T3 absent)" / "(T3, contradiction...)"
    # -----------------------------------------------------------------------
    content = re.sub(r'\(T3 absent\)', '(no independent verification available)', content)
    content = re.sub(
        r'\(T3,\s*(contradiction[^)]*)\)',
        r'(independently measured; \1)',
        content
    )

    # -----------------------------------------------------------------------
    # 10. Clean up empty blockquote lines left over after removals
    #     (a > with nothing after it, or a > with only whitespace)
    # -----------------------------------------------------------------------
    content = re.sub(r'^>\s*$\n?', '', content, flags=re.MULTILINE)

    # -----------------------------------------------------------------------
    # 11. Collapse 3+ consecutive blank lines to 2
    # -----------------------------------------------------------------------
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    pattern = os.path.join(repo_root, 'reports-md', '[0-9][0-9]-*.md')

    md_files = sorted(glob.glob(pattern))
    if not md_files:
        print("No chapter files found. Run from repo root or adjust path.")
        return

    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()

        cleaned = process_content(original)

        if cleaned != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f"✓  modified: {os.path.basename(filepath)}")
        else:
            print(f"   unchanged: {os.path.basename(filepath)}")


if __name__ == '__main__':
    main()
