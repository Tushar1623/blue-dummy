import re, os, urllib.parse, urllib.request

with open('thankyou.html', 'r', encoding='utf-8') as f:
    text = f.read()

refs = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', text)
missing = []
for r in set(refs):
    if r.startswith('http') or r.startswith('#') or r.startswith('tel') or r.startswith('mailto') or r.startswith('data:') or r == 'contact.html':
        continue
    clean = r.split('?')[0].split('#')[0]
    if clean.startswith('../../../'):
        clean = os.path.basename(clean)
    if not os.path.exists(clean):
        missing.append((r, clean))

print('thankyou.html missing:', len(missing))
base_url = 'https://www.godrejproperties.com/landing-page/kolkata/residential/godrej-blue/'

for orig, clean in missing:
    d = os.path.dirname(clean)
    if d:
        os.makedirs(d, exist_ok=True)
    full = urllib.parse.urljoin(base_url, orig)
    parts = urllib.parse.urlsplit(full)
    encoded_path = urllib.parse.quote(parts.path)
    safe_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc, encoded_path, parts.query, parts.fragment))
    try:
        req = urllib.request.Request(safe_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            with open(clean, 'wb') as out:
                out.write(res.read())
        print(f"Downloaded: {clean}")
    except Exception as e:
        print(f"Error {safe_url}: {e}")
