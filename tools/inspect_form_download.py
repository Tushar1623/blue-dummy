import re

with open('formSubmit.js', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'.{0,50}download.{0,50}', text, re.IGNORECASE):
    print(m.group(0))

