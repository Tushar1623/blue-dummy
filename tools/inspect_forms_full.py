with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sb = re.search(r'<div class="sidebar-contact[\s\S]*?</div>\s*</div>\s*</div>', text)
if sb:
    print("--- SIDEBAR CONTACT HTML ---")
    print(sb.group(0))

hero_form = re.search(r'<div class="home-enquire[\s\S]*?</form>', text)
if hero_form:
    print("\n--- HERO FORM HTML ---")
    print(hero_form.group(0))

