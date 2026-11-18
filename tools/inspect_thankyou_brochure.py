import re

with open('thankyou.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'.{0,60}brochure.{0,60}', text, re.IGNORECASE):
    print(m.group(0))

print("\n--- Any download links or buttons in thankyou.html ---")
for m in re.finditer(r'.{0,60}download.{0,60}', text, re.IGNORECASE):
    print(m.group(0))

