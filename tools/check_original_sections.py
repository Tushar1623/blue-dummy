import re

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
print("Original section IDs:", sections)

nav = re.findall(r'<a[^>]*href=["\'](#[^"\']*)["\'][^>]*>(.*?)</a>', html)
print("Original nav links:", nav)

