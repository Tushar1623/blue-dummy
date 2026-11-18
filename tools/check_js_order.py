with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find script errors or conflicts
# Check if jQuery is loaded before custom scripts
jquery_pos = text.find('jquery-3.6.0.min.js')
modal_ctrl_pos = text.find('Modal Dynamic State Controller')

print(f"jQuery position: {jquery_pos}")
print(f"Modal controller position: {modal_ctrl_pos}")

# Check brochure_cta click handlers
for m in re.finditer(r'.{0,60}brochure_cta.{0,60}', text):
    print(m.group(0))

