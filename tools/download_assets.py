import os
import re
import urllib.parse
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_url = 'https://www.godrejproperties.com/landing-page/kolkata/residential/godrej-blue/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.godrejproperties.com/'
}

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

raw_urls = set()
patterns = [
    r'(?:href|src|data-src|data-background|poster)=["\']([^"\']+)["\']',
    r'url\(["\']?([^"\'\)]+)["\']?\)',
    r'srcset=["\']([^"\']+)["\']'
]

for p in patterns:
    for m in re.findall(p, html, re.IGNORECASE):
        if ',' in m and ('.webp' in m or '.jpg' in m or '.png' in m):
            for part in m.split(','):
                c = part.strip().split(' ')[0]
                if c: raw_urls.add(c)
        else:
            raw_urls.add(m.strip())

downloaded = set()
failed = set()

def encode_url(url):
    parts = urllib.parse.urlsplit(url)
    encoded_path = urllib.parse.quote(parts.path)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, encoded_path, parts.query, parts.fragment))

def download_file(url, local_path):
    clean_local = local_path.split('?')[0].split('#')[0]
    if clean_local in downloaded:
        return
    d = os.path.dirname(clean_local)
    if d:
        os.makedirs(d, exist_ok=True)
    if os.path.exists(clean_local) and os.path.getsize(clean_local) > 0:
        downloaded.add(clean_local)
        return

    safe_url = encode_url(url)
    req = urllib.request.Request(safe_url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            data = res.read()
            with open(clean_local, 'wb') as out:
                out.write(data)
            downloaded.add(clean_local)
            print(f"Downloaded: {clean_local} ({len(data)} bytes)")
    except Exception as e:
        failed.add((safe_url, str(e)))
        print(f"Failed {safe_url}: {e}")

# Process initial urls
for u in raw_urls:
    if u.startswith('data:') or u.startswith('javascript:') or u.startswith('#') or u.startswith('tel:') or u.startswith('mailto:'):
        continue
    if any(k in u for k in ['facebook.com', 'taboola.com', 'google-analytics.com', 'googletagmanager.com', 'clarity.ms', 'salesforce.com']):
        continue
    
    full_url = urllib.parse.urljoin(base_url, u)
    
    if not u.startswith('http://') and not u.startswith('https://'):
        download_file(full_url, u)
    elif 'godrejproperties.com/landing-page/kolkata/residential/godrej-blue/' in full_url:
        rel = full_url.split('/godrej-blue/')[-1]
        download_file(full_url, rel)
    elif 'godrejproperties.com' in full_url and any(full_url.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.svg', '.webp', '.ico', '.css', '.js']):
        parsed = urllib.parse.urlparse(full_url)
        rel = 'external' + parsed.path
        download_file(full_url, rel)

print(f"\nInitial assets downloaded: {len(downloaded)}, failed: {len(failed)}")

# Now find secondary assets inside CSS files (fonts, images, etc.)
css_files = []
for root, dirs, files in os.walk('landing_page'):
    for file in files:
        if file.endswith('.css'):
            css_files.append(os.path.join(root, file))

print(f"\nScanning {len(css_files)} CSS files for fonts and images...")
for css_path in css_files:
    try:
        with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
            css_text = f.read()
        for m in re.findall(r'url\(["\']?([^"\'\)\?\#]+(?:\?[^"\'\)]*)?)["\']?\)', css_text):
            if m.startswith('data:'):
                continue
            clean_m = m.strip()
            css_dir = os.path.dirname(css_path).replace('\\', '/')
            target_path = os.path.normpath(os.path.join(css_dir, clean_m.split('?')[0])).replace('\\', '/')
            rel_css_dir = os.path.relpath(css_dir, '.').replace('\\', '/')
            if rel_css_dir == '.':
                rel_css_dir = ''
            remote_css_url = urllib.parse.urljoin(base_url, rel_css_dir + ('/' if rel_css_dir else '') + os.path.basename(css_path))
            remote_asset_url = urllib.parse.urljoin(remote_css_url, clean_m)
            download_file(remote_asset_url, target_path)
    except Exception as e:
        print(f"Error reading CSS {css_path}: {e}")

print(f"\nTotal downloaded assets: {len(downloaded)}")
if failed:
    print(f"Failed assets ({len(failed)}):")
    for u, err in list(failed)[:10]:
        print(f"  {u} -> {err}")
