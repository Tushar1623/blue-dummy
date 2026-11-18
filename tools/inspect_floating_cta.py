with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div[^>]*class=["\'][^"\']*(?:enquire-btn|brochure_cta|fixed)[^"\']*["\'][\s\S]*?</div>', text)
for m in matches:
    print(m)

# Also check around brochure_cta
idx = text.find('brochure_cta')
if idx != -1:
    print("\nAround brochure_cta:")
    print(text[idx-200:idx+500])

