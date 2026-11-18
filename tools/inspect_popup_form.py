import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the popupModal in index.html
m = re.search(r'<div class="modal fade" id="popupModal"[\s\S]*?</form>\s*</div>\s*</div>\s*</div>\s*</div>', html)
if m:
    print(m.group(0))

