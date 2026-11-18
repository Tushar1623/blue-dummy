with open('source.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in source.html: {len(lines)}")

# Let's inspect nav items
import re
html = "".join(lines)

nav = re.search(r'<div class="main-menu__top">.*?</div>\s*</div>\s*</div>\s*</div>', html, re.DOTALL)
if not nav:
    nav = re.search(r'<header.*?</header>', html, re.DOTALL)
if nav:
    print("--- HEADER SNIPPET ---")
    print(nav.group(0)[:1500])

forms = re.findall(r'<form[^>]*>.*?</form>', html, re.DOTALL)
print(f"\n--- FORMS ({len(forms)}) ---")
for i, f_text in enumerate(forms):
    f_id = re.search(r'id=["\']([^"\']+)["\']', f_text)
    action = re.search(r'action=["\']([^"\']+)["\']', f_text)
    inputs = re.findall(r'<input[^>]+name=["\']([^"\']+)["\']', f_text)
    print(f"Form {i+1}: ID={f_id.group(1) if f_id else 'None'}, Action={action.group(1) if action else 'None'}, Inputs={inputs}")

foot = re.search(r'<footer.*?</footer>', html, re.DOTALL)
if foot:
    print("\n--- FOOTER SNIPPET ---")
    print(foot.group(0)[:1500])
