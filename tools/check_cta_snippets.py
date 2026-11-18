with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Check where toggle-sidebar is
print("toggle-sidebar snippet:")
m = re.search(r'.{0,60}toggle-sidebar.{0,100}', html)
if m:
    print(m.group(0))

# Check where mob-enquire is
print("mob-enquire snippet:")
m = re.search(r'.{0,60}mob-enquire.{0,100}', html)
if m:
    print(m.group(0))

# Check where brochure_cta is
print("brochure_cta snippet:")
m = re.search(r'.{0,60}brochure_cta.{0,100}', html)
if m:
    print(m.group(0))

