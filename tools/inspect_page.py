import re
from html.parser import HTMLParser

with open('source.html', 'r', encoding='utf-8') as f:
    content = f.read()

title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
print('Title:', title_m.group(1).strip() if title_m else 'No title')

css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content, re.IGNORECASE)
print('\nCSS links:')
for l in css_links:
    print(l)

images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
data_images = re.findall(r'data-src=["\']([^"\']+)["\']', content, re.IGNORECASE)
print(f'\nImages: {len(images)}, data-src: {len(data_images)}')
for img in images[:15]:
    print(img)

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
print(f'\nScripts count: {len(scripts)}')
for s in scripts:
    print(s)
