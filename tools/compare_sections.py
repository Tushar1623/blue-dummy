with open('index.html', 'r', encoding='utf-8') as f:
    i_html = f.read()

with open('source.html', 'r', encoding='utf-8') as f:
    s_html = f.read()

import re
print("index.html sections:")
for m in re.finditer(r'<section[^>]*id=["\']([^"\']+)["\']', i_html):
    print(" ", m.group(1))

print("\nsource.html sections:")
for m in re.finditer(r'<section[^>]*id=["\']([^"\']+)["\']', s_html):
    print(" ", m.group(1))

