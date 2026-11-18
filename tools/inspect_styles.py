import re

with open('landing_page/assets/css/alipes.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's search for primary colors and typography
colors = re.findall(r'(?:color|background|border-color):\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)|var\([^)]+\))', css)
print("Color count:", len(colors))

# Check font families
fonts = set(re.findall(r'font-family:\s*([^;]+);', css))
print("Fonts:", fonts)

# Check some common classes like .thm-btn, .section-title, .about-one
classes = ['.thm-btn', '.section-title', '.section-title__title', '.section-title__tagline']
for c in classes:
    m = re.search(r'(' + re.escape(c) + r'\s*\{[^}]+\})', css)
    if m:
        print(m.group(1))

