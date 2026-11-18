with open('formSubmit.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function validate\(\)[\s\S]*?return[\s\S]*?\}', text)
if not m:
    m = re.search(r'const validate\s*=\s*\(\)[\s\S]*?return[\s\S]*?\}', text)

if m:
    print("Found validate function in formSubmit.js:")
    print(m.group(0)[:1200])
else:
    print("No validate function found directly, looking for validate occurrences:")
    for line in text.splitlines():
        if 'validate' in line:
            print(" ", line[:100])

