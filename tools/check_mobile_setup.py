with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Viewport tag
viewport = re.search(r'<meta[^>]*viewport[^>]*>', html, re.IGNORECASE)
print("Viewport:", viewport.group(0) if viewport else "NONE")

# Check mobile nav toggler and mobile menu
toggler = re.findall(r'.{0,50}mobile-nav.{0,50}', html)
print("\nMobile nav matches:")
for t in toggler[:10]:
    print(" ", t.strip())

# Check mobile styles in index.html
inline_styles = re.findall(r'<style[^>]*>[\s\S]*?</style>', html)
print(f"\nInline style blocks: {len(inline_styles)}")
for s in inline_styles:
    queries = re.findall(r'@media[^{]+', s)
    if queries:
        print("  Media queries found:", queries)

# Check fixed / floating elements for mobile
print("\nFloating elements:")
for m in re.finditer(r'.{0,50}(?:mob-enquire|brochure_cta|toggle-sidebar|enquire-btn-fixed).{0,50}', html):
    print(" ", m.group(0).strip())
