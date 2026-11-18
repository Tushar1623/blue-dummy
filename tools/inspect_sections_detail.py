import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*>[\s\S]*?</section>', html)
for i, s in enumerate(sections):
    sec_id = re.search(r'id=["\']([^"\']+)["\']', s)
    sec_class = re.search(r'class=["\']([^"\']+)["\']', s)
    h_tags = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', s, re.DOTALL)
    clean_h = [re.sub(r'<[^>]+>', '', h).strip().replace('\n', ' ') for h in h_tags]
    print(f"Sec {i+1}: ID={sec_id.group(1) if sec_id else None}, Class={sec_class.group(1) if sec_class else None}")
    print("   Headings:", clean_h[:5])

# Also check existing FAQs
faqs = re.findall(r'<div class="faq-item">[\s\S]*?</div>\s*</div>', html)
print(f"\nExisting FAQs count: {len(faqs)}")

# Check header nav links
nav_links = re.findall(r'<li[^>]*>\s*<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html)
print("\nNav links:", [(href, re.sub(r'<[^>]+>', '', text).strip()) for href, text in nav_links])

