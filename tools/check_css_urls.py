import os
import re

css_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.css'):
            css_files.append(os.path.join(root, file))

missing = set()
for css_path in css_files:
    with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for m in re.findall(r'url\(["\']?([^"\'\)\?\#]+(?:\?[^"\'\)]*)?)["\']?\)', content):
        if m.startswith('data:') or m.startswith('http://') or m.startswith('https://'):
            continue
        clean_m = m.split('?')[0].split('#')[0]
        css_dir = os.path.dirname(css_path)
        full_path = os.path.normpath(os.path.join(css_dir, clean_m))
        if not os.path.exists(full_path):
            missing.add((css_path, m, full_path))

print(f"Missing referenced assets from CSS: {len(missing)}")
for css_path, m, full_path in sorted(missing)[:20]:
    print(f"In {css_path}: {m} -> not found at {full_path}")
