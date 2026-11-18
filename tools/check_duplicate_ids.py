with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
forms = re.findall(r'<form[^>]*>', text)
for f in forms:
    print(f)

btns = re.findall(r'<[^>]+id=["\']btnSubmitContactForm["\'][^>]*>', text)
print(f"\nbtnSubmitContactForm count: {len(btns)}")
for b in btns:
    print(b)

