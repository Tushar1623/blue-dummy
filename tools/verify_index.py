import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Collect all local file paths
patterns = [
    r'(?:href|src|data-src|data-background|poster)=["\']([^"\']+)["\']',
    r'url\(["\']?([^"\'\)]+)["\']?\)'
]

resources = set()
for p in patterns:
    for m in re.findall(p, html):
        if not m.startswith('http://') and not m.startswith('https://') and not m.startswith('#') and not m.startswith('tel:') and not m.startswith('mailto:') and not m.startswith('data:') and not m.startswith('javascript:'):
            clean = m.split('?')[0].split('#')[0]
            if clean:
                resources.add(clean)

missing = []
present = []
for r in sorted(resources):
    if os.path.exists(r):
        present.append((r, os.path.getsize(r)))
    else:
        missing.append(r)

print(f"Present local resources: {len(present)}")
print(f"Missing local resources: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")
