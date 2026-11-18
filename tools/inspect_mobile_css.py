with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('.mob-enquire')
if idx != -1:
    print("Around .mob-enquire in index.html:")
    print(text[idx-100:idx+600])

# Check where mob-enquire is in CSS
with open('landing_page/assets/css/alipes-responsive.css', 'r', encoding='utf-8', errors='ignore') as f:
    resp_css = f.read()

print(f"\nalipes-responsive.css length: {len(resp_css)}")
print("Media queries in alipes-responsive.css:")
for mq in set(re.findall(r'@media[^{]+', resp_css)):
    print(" ", mq.strip())
