import re
import urllib.parse

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

base_url = 'https://www.godrejproperties.com/landing-page/kolkata/residential/godrej-blue/'

# Find all links, scripts, img src, source srcset, background-image urls
urls = set()

# Attributes: src, href, data-src, data-background, poster, etc.
patterns = [
    r'(?:href|src|data-src|data-background|poster)=["\']([^"\']+)["\']',
    r'url\(["\']?([^"\'\)]+)["\']?\)',
    r'srcset=["\']([^"\']+)["\']'
]

for p in patterns:
    for match in re.findall(p, html, re.IGNORECASE):
        # Handle srcset which might have multiple urls with descriptors
        if ',' in match and (' ' in match or '.webp' in match or '.jpg' in match or '.png' in match):
            parts = match.split(',')
            for part in parts:
                clean = part.strip().split(' ')[0]
                if clean:
                    urls.add(clean)
        else:
            urls.add(match.strip())

# Filter and resolve
filtered = []
for u in sorted(urls):
    if u.startswith('data:') or u.startswith('javascript:') or u.startswith('#') or u.startswith('tel:') or u.startswith('mailto:'):
        continue
    # Exclude external tracking pixels or social shares unless useful
    full = urllib.parse.urljoin(base_url, u)
    filtered.append((u, full))

print(f"Total discovered assets/links: {len(filtered)}")
with open('discovered_assets.txt', 'w', encoding='utf-8') as f:
    for orig, full in filtered:
        f.write(f"{orig} -> {full}\n")

for orig, full in filtered[:40]:
    print(f"{orig} -> {full}")
