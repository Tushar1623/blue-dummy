import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect all <a> and <button> tags
links = re.findall(r'<a[^>]*>[\s\S]*?</a>', html)
buttons = re.findall(r'<button[^>]*>[\s\S]*?</button>', html)

print(f"Total links: {len(links)}")
print(f"Total buttons: {len(buttons)}")

print("\n--- ALL BUTTONS & LINKS WITH 'ENQUIRE' OR 'BROCHURE' OR MODAL ---")
for tag in links + buttons:
    text = re.sub(r'<[^>]+>', '', tag).strip()
    if any(k in tag.lower() for k in ['enquir', 'brochure', 'popupmodal', 'modal']):
        print(f"Tag: {tag[:100]} | Text: '{text}'")

