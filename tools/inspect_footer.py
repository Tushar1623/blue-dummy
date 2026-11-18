import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

foot = re.search(r'<footer[\s\S]*?</footer>', html)
if foot:
    print(foot.group(0)[1500:])

