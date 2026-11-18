import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all <a> and <button> tags with their text
interactive = re.findall(r'<(?:a|button)[^>]*>[\s\S]*?</(?:a|button)>', html)
print(f"Total interactive elements: {len(interactive)}")

actions = []
for el in interactive:
    clean_text = re.sub(r'<[^>]+>', '', el).strip()
    has_modal = 'popupModal' in el
    has_href = re.search(r'href=["\']([^"\']+)["\']', el)
    href = has_href.group(1) if has_href else None
    actions.append((clean_text, has_modal, href, el[:120]))

print("\n--- BUTTONS / LINKS WITH BROCHURE / ENQUIRE / FLOOR PLAN / SITE VISIT / PRICE ---")
for text, has_modal, href, snippet in actions:
    lower = text.lower()
    if any(k in lower for k in ['brochure', 'enquire', 'floor plan', 'price', 'site visit', 'cab', 'contact']):
        print(f"Text: '{text}' | HasModal: {has_modal} | Href: {href}")

