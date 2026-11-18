with open('landing_page/assets/css/alipes.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'body\.locked\s*\{[^}]+\}', text)
print("body.locked:", m)
