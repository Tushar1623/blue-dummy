with open('thankyou.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'Thank\s*You[\s\S]{0,1000}', text, re.IGNORECASE)
if m:
    print("Found Thank You context:")
    print(m.group(0))

