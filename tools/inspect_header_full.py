with open('source.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
header = re.search(r'<header[\s\S]*?</header>', text)
if header:
    print(header.group(0))

