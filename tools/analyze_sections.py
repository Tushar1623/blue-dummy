import re

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect sections and headings
sections = re.findall(r'<section[^>]*>.*?</section>', html, re.DOTALL | re.IGNORECASE)
print(f"Total sections: {len(sections)}")

for i, s in enumerate(sections):
    sec_id = re.search(r'id=["\']([^"\']+)["\']', s)
    sec_class = re.search(r'class=["\']([^"\']+)["\']', s)
    h_tags = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', s, re.DOTALL | re.IGNORECASE)
    clean_h = [re.sub(r'<[^>]+>', '', h).strip() for h in h_tags]
    print(f"Section {i+1}: ID={sec_id.group(1) if sec_id else 'None'}, Class={sec_class.group(1) if sec_class else 'None'}")
    if clean_h:
        print(f"   Headings: {clean_h}")

# Also check header and footer
headers = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL | re.IGNORECASE)
print(f"\nHeaders: {len(headers)}")
footers = re.findall(r'<footer[^>]*>.*?</footer>', html, re.DOTALL | re.IGNORECASE)
print(f"Footers: {len(footers)}")

# Modals
modals = re.findall(r'<div[^>]*class=["\'][^"\']*modal[^"\']*["\'][^>]*>.*?</div>\s*</div>\s*</div>', html, re.DOTALL | re.IGNORECASE)
print(f"Modals count approx: {len(modals)}")
