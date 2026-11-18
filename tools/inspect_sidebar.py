with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div class="sidebar-contact[\s\S]*?</div>\s*</div>\s*</div>', text)
if m:
    print(m.group(0)[:1200])

