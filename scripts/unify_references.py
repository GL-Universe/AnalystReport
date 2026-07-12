#!/usr/bin/env python3
"""
Extract all References entries from 12 chapter files (excluding 12-appendix.md),
deduplicate them by (author, title), filter out internal-file references,
and output a unified list sorted by author name.

Also removes the per-chapter "## References for This Chapter" section from each
chapter file (Step 2 of the plan).
"""
import re
import os
import glob


def extract_references(content: str):
    """Extract the References section content from a chapter file.
    
    Returns (content_without_references, references_text) where references_text
    is the raw text of the references items (one per line, possibly multi-line).
    """
    # Find "## References for This Chapter" and capture everything after it
    # (possibly with a --- separator before it)
    m = re.search(
        r'^(---\s*\n+)?## References for This Chapter\s*\n(.*)$',
        content,
        flags=re.MULTILINE | re.DOTALL
    )
    if not m:
        return content, None
    references_text = m.group(2)
    start = m.start()
    new_content = content[:start].rstrip() + '\n'
    return new_content, references_text


def parse_reference_items(references_text: str):
    """Parse a references section text into a list of full_text strings.
    
    Each item starts with a number followed by a period at the start of a line.
    Multi-line items are joined.
    """
    if not references_text:
        return []
    
    # Split into items: each item starts with "N. " at the beginning of a line
    items = re.split(r'\n(?=\d+\.\s)', references_text.strip())
    
    parsed = []
    for item in items:
        item = item.strip()
        if not item:
            continue
        # Remove leading "N. " (number prefix)
        item = re.sub(r'^\d+\.\s+', '', item)
        # Normalize whitespace within item
        item = re.sub(r'\s+', ' ', item).strip()
        parsed.append(item)
    
    return parsed


def get_author(item: str) -> str:
    """Extract author from a reference item.
    
    Patterns:
    - **Author**. "Title." ...
    - Author. "Title." ...
    - `internal-file.md` — ... (internal file)
    """
    # Bold author
    m = re.match(r'\*\*([^*]+)\*\*', item)
    if m:
        return m.group(1).strip()
    # Non-bold author: first segment before ". "
    m = re.match(r'^([^.`]+)\.', item)
    if m:
        return m.group(1).strip()
    return item[:50]


def get_title(item: str) -> str:
    """Extract title from a reference item (text within first quotes)."""
    m = re.search(r'"([^"]+)"', item)
    if m:
        return m.group(1).strip().lower()
    return ''


def is_internal_file(item: str) -> bool:
    """Check if the item is an internal project file reference."""
    return bool(re.match(r'^`[a-z/-]+\.md`', item))


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    pattern = os.path.join(repo_root, 'reports-md', '[0-9][0-9]-*.md')
    md_files = sorted(glob.glob(pattern))

    all_references = {}  # key: (author_lower, title_lower), value: full_text
    
    for filepath in md_files:
        basename = os.path.basename(filepath)
        if basename == '12-appendix.md':
            print(f'   skip (appendix): {basename}')
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, refs_text = extract_references(content)
        if refs_text is None:
            print(f'   no References: {basename}')
            continue
        
        items = parse_reference_items(refs_text)
        print(f'✓  {basename}: {len(items)} references extracted')
        
        for item in items:
            # Skip internal project file references
            if is_internal_file(item):
                print(f'      skip internal: {item[:80]}')
                continue
            
            author = get_author(item)
            title = get_title(item)
            key = (author.lower(), title)
            
            if key not in all_references:
                all_references[key] = item
        
        # Write the content without References section back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    # Sort by author name (case-insensitive)
    sorted_items = sorted(all_references.values(), key=lambda x: get_author(x).lower())
    
    print(f'\n=== Unified Reference List ({len(sorted_items)} entries) ===\n')
    for i, item in enumerate(sorted_items, 1):
        print(f'{i}. {item}')
    
    # Save the unified list to a temp file
    output_path = os.path.join(repo_root, 'scripts', '_unified_references.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Unified Reference List\n\n')
        for i, item in enumerate(sorted_items, 1):
            f.write(f'{i}. {item}\n\n')
    print(f'\nSaved to: {output_path}')


if __name__ == '__main__':
    main()
