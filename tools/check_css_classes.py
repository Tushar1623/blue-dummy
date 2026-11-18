with open('landing_page/assets/css/alipes.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
# check section-padding
for m in re.finditer(r'\.section-padding\s*\{[^}]+\}', css):
    print(m.group(0))

# check card or box styles
print("\n--- Card or box matches ---")
for m in re.finditer(r'\.(?:pricing|amenities|about|faq|feature|single)[-_a-z0-9]*\s*\{[^}]+\}', css):
    print(m.group(0)[:150])

