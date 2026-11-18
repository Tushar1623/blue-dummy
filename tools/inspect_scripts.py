import re

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect all script tags
scripts = re.findall(r'<script[^>]*>.*?</script>', html, re.DOTALL | re.IGNORECASE)
print(f"Total script tags: {len(scripts)}")

for i, s in enumerate(scripts):
    src = re.search(r'src=["\']([^"\']+)["\']', s)
    if src:
        print(f"Script {i+1} src: {src.group(1)}")
    else:
        # inline script snippet
        content = re.sub(r'<script[^>]*>|</script>', '', s).strip()
        preview = content[:80].replace('\n', ' ')
        print(f"Script {i+1} inline ({len(content)} chars): {preview}...")
