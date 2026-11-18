import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modals = re.findall(r'<div[^>]*class=["\'][^"\']*modal[^"\']*["\'][^>]*>[\s\S]*?</div>\s*</div>\s*</div>', html)
print(f"Modals found: {len(modals)}")
for i, m in enumerate(modals):
    m_id = re.search(r'id=["\']([^"\']+)["\']', m)
    print(f"Modal {i+1}: ID={m_id.group(1) if m_id else 'None'}")
