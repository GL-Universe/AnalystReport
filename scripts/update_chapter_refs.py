#!/usr/bin/env python3
"""
Update internal Chapter N references after reordering.

Old -> New mapping:
- Chapter 2 (Methodology) -> Chapter 3
- Chapter 3 (Dataset Description) -> Chapter 10
- Chapter 10 (Practical Recommendations) -> Chapter 2
- Chapter 0, 1, 4, 5, 6, 7, 8, 9, 11, 12 -> unchanged

To avoid double-substitution, use placeholders.
"""
import re
import os
import glob


# Mapping from OLD chapter number to NEW chapter number
OLD_TO_NEW = {
    2: 3,
    3: 10,
    10: 2,
}

# For section references like "Section 2.4" we need to update to "Section 3.4"
# But only within Methodology/Dataset/Practical context


def update_content(content: str) -> str:
    """Replace Chapter N references using placeholder to avoid double-substitution."""
    
    # Step 1: protect all "Chapter N" references with placeholders
    placeholders = {}
    counter = [0]
    
    def replace_chapter(m):
        key = f'__CH{counter[0]}__'
        counter[0] += 1
        placeholders[key] = m.group(0)
        return key
    
    # Match "Chapter N" or "Chapter N (Section X.Y)" patterns
    # Be careful: "Chapter 0" stays as 0
    content = re.sub(
        r'Chapter (\d+)(\s*\(Section \d+\.\d+(?:\.\d+)?\))?',
        replace_chapter,
        content
    )
    
    # Also protect "Section N.M" patterns (without Chapter prefix) - but be careful
    # because section numbers also shift within the renamed files
    # For cross-chapter references like "Section 2.4" appearing in other chapters,
    # they refer to Methodology's sections (which are now 3.x not 2.x)
    # However within 02-practical-recommendations.md, Section 10.x has already been
    # rewritten to Section 2.x by the per-file update above. So we don't need to
    # touch those here.
    
    # Now apply replacements to the placeholder content
    new_placeholders = {}
    for key, val in placeholders.items():
        m = re.match(r'Chapter (\d+)(\s*\(Section (\d+)\.(\d+)(?:\.(\d+))?\))?', val)
        if m:
            old_ch = int(m.group(1))
            if old_ch in OLD_TO_NEW:
                new_ch = OLD_TO_NEW[old_ch]
                # Also shift section number if it's a Methodology (old 2) or Dataset (old 3) or Practical (old 10) section
                sec_prefix = m.group(3)
                if sec_prefix is not None:
                    sec_num = int(sec_prefix)
                    # Old Chapter 2's sections are 2.x -> 3.x; we already updated within file
                    # but cross-refs from OTHER files still say "Section 2.x"
                    # Map section prefix only if it matches old chapter number
                    if sec_num == old_ch:
                        new_sec = new_ch
                    else:
                        new_sec = sec_num
                    sec_minor = m.group(4)
                    if m.group(5):
                        new_val = f'Chapter {new_ch} (Section {new_sec}.{sec_minor}.{m.group(5)})'
                    else:
                        new_val = f'Chapter {new_ch} (Section {new_sec}.{sec_minor})'
                else:
                    new_val = f'Chapter {new_ch}'
                new_placeholders[key] = new_val
            else:
                new_placeholders[key] = val
        else:
            new_placeholders[key] = val
    
    for key, val in new_placeholders.items():
        content = content.replace(key, val)
    
    return content


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    pattern = os.path.join(repo_root, 'reports-md', '[0-9][0-9]-*.md')
    md_files = sorted(glob.glob(pattern))

    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        cleaned = update_content(original)
        if cleaned != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f'✓  {os.path.basename(filepath)}')
        else:
            print(f'   {os.path.basename(filepath)} (no change)')


if __name__ == '__main__':
    main()
