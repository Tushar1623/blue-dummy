with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,50}\.brochure_cta.{0,100}', text)
for i, m in enumerate(matches):
    print(f"Match {i+1}: {repr(m)}")

