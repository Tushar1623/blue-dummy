import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all buttons/links that say Download Brochure or Enquire
buttons = re.findall(r'<[^>]+(?:modal|brochure|enquire|btn)[^>]*>[\s\S]*?</[^>]+>', html, re.IGNORECASE)
print(f"Total candidate elements: {len(buttons)}")

# Find all occurrences of "Download Brochure" or "Brochure"
brochure_elements = re.findall(r'<[^>]+>[^<]*brochure[^<]*</[^>]+>', html, re.IGNORECASE)
print("\nBrochure elements:")
for b in brochure_elements:
    print(" ", b.strip())

# Check popupModal structure
m = re.search(r'<div[^>]*id=["\']popupModal["\'][\s\S]*?</div>\s*</div>\s*</div>', html)
if m:
    print("\npopupModal structure:")
    print(m.group(0)[:1200])

