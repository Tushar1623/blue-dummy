import os
import re

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all local references
refs = re.findall(r'(?:src|href|poster)=["\']([^"\']+)["\']', html)
missing = []
found = []

for r in set(refs):
    if r.startswith('http://') or r.startswith('https://') or r.startswith('#') or r.startswith('tel:') or r.startswith('mailto:') or r.startswith('data:'):
        continue
    clean_r = r.split('?')[0].split('#')[0]
    # Check if exists
    if os.path.exists(clean_r):
        found.append((clean_r, os.path.getsize(clean_r)))
    else:
        missing.append(r)

print(f"Found local assets: {len(found)}")
print(f"Missing local assets: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")
