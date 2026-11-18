import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

faq_sec = re.search(r'<section[^>]*id=["\']faq["\'][\s\S]*?</section>', html)
if faq_sec:
    print(faq_sec.group(0)[:2500])

