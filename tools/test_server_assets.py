import urllib.request
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

errors = []
success = 0

for r in resources:
    url = f"http://127.0.0.1:8080/{r}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=5) as res:
            if res.status == 200:
                success += 1
            else:
                errors.append((r, res.status))
    except Exception as e:
        errors.append((r, str(e)))

print(f"Tested {len(resources)} local resources: {success} succeeded, {len(errors)} failed.")
if errors:
    print("Errors:")
    for err in errors:
        print(" ", err)
