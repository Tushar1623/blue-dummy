with open('landing_page/assets/css/alipes-responsive.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
# check mobile nav styles
for m in re.finditer(r'.{0,40}mobile-nav__wrapper.{0,100}', text):
    print(m.group(0))

# check main-menu__logo on mobile
for m in re.finditer(r'.{0,40}main-menu__logo.{0,100}', text):
    print(m.group(0))
