import re
import urllib.request
import os

with open('landing_page/assets/vendors/intl-tel-input/css/intlTelInput.css', 'r', encoding='utf-8') as f:
    text = f.read()

urls = re.findall(r'url\(([^)]+)\)', text)
print("intlTelInput urls:", urls)

base = "https://cdn.jsdelivr.net/npm/intl-tel-input@18.1.1/build/img/"
for u in urls:
    clean = u.strip('"\'')
    if 'img/' in clean:
        filename = clean.split('img/')[-1]
        target = os.path.join('landing_page/assets/vendors/intl-tel-input/img', filename)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        img_url = base + filename
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as res:
                with open(target, 'wb') as out:
                    out.write(res.read())
            print(f"Downloaded {target}")
        except Exception as e:
            print(f"Error {filename}: {e}")
