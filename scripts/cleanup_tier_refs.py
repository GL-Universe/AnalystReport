#!/usr/bin/env python3
"""
Second-pass cleanup: replace remaining T3/T5/T6 inline references with
plain-English descriptions.
"""
import re
import os
import glob

REPLACEMENTS = [
    # "(T3)" standalone in parens → "" (already handled for inline citations)
    (r'\bT3\b', 'independently verified (Artificial Analysis)'),
    (r'\bT5\b', 'practitioner testing'),
    (r'\bT6\b', 'vendor-reported'),
    (r'\bT4\b', 'government/regulatory evaluation'),
    (r'\bT1\b', 'independent research institution'),
    (r'\bT2\b', 'peer-reviewed academic publication'),
]

# But we DON'T want to replace within TechnicalAnalysis-X or in URLs
# We'll use a post-filter approach: first protect special patterns, then substitute

def safe_replace(content):
    # Protect: TechnicalAnalysis-A/B/C/D/E, Tau2, T3-fold, T2-fold, table headers like | T3 |
    # Use placeholder scheme
    protected = {}
    counter = [0]

    def protect(m):
        key = f'__PROT{counter[0]}__'
        counter[0] += 1
        protected[key] = m.group(0)
        return key

    # Protect TechnicalAnalysis-X
    content = re.sub(r'TechnicalAnalysis-[A-Z]', protect, content)
    # Protect Tau2
    content = re.sub(r'Tau2', protect, content)
    # Protect T3-fold / T2-fold (unlikely but safe)
    content = re.sub(r'T[123]-fold', protect, content)
    # Protect references in table column headers like "| T3 |" which are the Tier table itself
    content = re.sub(r'\| \*\*T[1-6]\*\* \|', protect, content)
    # Protect "T3 datasets (AA-hosted)" style
    content = re.sub(r'T[1-6] datasets \([^)]+\)', protect, content)

    # Now do targeted substitutions that are contextually safe
    # "T3 source" → "independent measurement (Artificial Analysis)"
    content = re.sub(r'\bT3 source\b', 'independent measurement (Artificial Analysis)', content)
    content = re.sub(r'\bT3 sources\b', 'independent measurement sources', content)
    # "T5 source(s)" 
    content = re.sub(r'\bT5 sources\b', 'practitioner testing sources', content)
    content = re.sub(r'\bT5 source\b', 'practitioner testing source', content)
    # "T6 source(s)"
    content = re.sub(r'\bT6 sources\b', 'vendor-reported sources', content)
    content = re.sub(r'\bT6 source\b', 'vendor-reported source', content)
    # "T5 finding" / "T5 findings"
    content = re.sub(r'\bT5 finding\b', 'practitioner testing finding', content)
    content = re.sub(r'\bT5 findings\b', 'practitioner testing findings', content)
    # "T5 only" / "T3 only"  
    content = re.sub(r'\bT5 only\b', 'practitioner testing only', content)
    content = re.sub(r'\bT3 only\b', 'independent measurement only', content)
    # "T5 user testing"
    content = re.sub(r'\bT5 user testing\b', 'practitioner user testing', content)
    # "T6 and not independently verified"
    content = re.sub(r'\bT6 and not independently verified\b', 'vendor-reported and not independently verified', content)
    # "T3 benchmark" / "T3 benchmarks"
    content = re.sub(r'\bT3 benchmark\b', 'independent benchmark', content)
    content = re.sub(r'\bT3 benchmarks\b', 'independent benchmarks', content)
    # "T3 (Artificial Analysis)" in Appendix F
    content = re.sub(r'\bT3 \(Artificial Analysis\)', 'Artificial Analysis (independent measurement institution)', content)
    # "T5 (user testing reports)" in Appendix F
    content = re.sub(r'\bT5 \(user testing reports\)', 'Practitioner testing sources', content)
    # "T6 (vendor)" in Appendix F
    content = re.sub(r'\bT6 \(vendor\)', 'Vendor-published data', content)
    # "T3 independent" 
    content = re.sub(r'\bT3 independent\b', 'independently measured', content)
    # "T3 medical-domain evaluation"
    content = re.sub(r'\bT3 ([a-z-]+-domain) evaluation\b', r'independent \1 evaluation', content)
    # "(T3)" alone as a tag at end of table cell
    content = re.sub(r' \(T3\)', '', content)
    content = re.sub(r' \(T5\)', '', content)
    content = re.sub(r' \(T6\)', '', content)
    content = re.sub(r' \(T4\)', '', content)
    # "No T3 Intelligence Index measurement"
    content = re.sub(r'\bNo T3 Intelligence Index measurement\b', 'No independent Intelligence Index measurement', content)
    # "No T3 safety benchmark"
    content = re.sub(r'\bNo T3 ([a-z-]+ )?benchmark\b', r'No independent \1benchmark', content)
    # "T5 report" 
    content = re.sub(r'\bT5 report\b', 'practitioner report', content)
    # "T5 single cases"
    content = re.sub(r'\bT5 single cases\b', 'single practitioner cases', content)
    # "T6;" at table end
    content = re.sub(r'\(T6;', '(vendor-reported;', content)
    # "per T5" 
    content = re.sub(r'\bper T5;?\b', 'per practitioner testing;', content)
    content = re.sub(r'\bper T5\b', 'per practitioner testing', content)
    # "T5 practitioner findings"
    content = re.sub(r'\bT5 practitioner findings\b', 'practitioner findings', content)
    # "T5 single"
    content = re.sub(r'\bT5 single\b', 'single practitioner', content)
    # For "T3 aggregate" in table cells
    content = re.sub(r'\bT3 aggregate\b', 'independent measurement aggregate', content)
    # "(T5 aggregate)" / "(T5 specific)"
    content = re.sub(r'\bT5 specific\b', 'practitioner testing, specific case', content)
    # "T5)" in table cells like "S11 (T5 specific)"
    # These are in 03-dataset-description.md source labels like "S11 (T3 aggregate)"
    content = re.sub(r'S\d+ \(T[1-6][^\)]*\)', lambda m: re.sub(r'T[1-6]\w*', '', m.group(0)), content)
    # "all T5" 
    content = re.sub(r'\ball T5\b', 'all practitioner sources', content)
    # "T4 regulatory evaluation" in body text
    content = re.sub(r'\bT4 regulatory evaluation\b', 'regulatory body evaluation', content)
    # "No T4 regulatory evaluation" 
    content = re.sub(r'\bNo T4 regulatory evaluation\b', 'No regulatory body evaluation', content)

    # Restore protected strings
    for key, val in protected.items():
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

        cleaned = safe_replace(original)

        if cleaned != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f'✓  modified: {os.path.basename(filepath)}')
        else:
            print(f'   unchanged: {os.path.basename(filepath)}')


if __name__ == '__main__':
    main()
