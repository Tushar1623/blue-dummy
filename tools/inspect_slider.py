with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
slider = re.search(r'<section class="main-slider[\s\S]*?</section>', text)
if slider:
    print(slider.group(0)[:2500])

