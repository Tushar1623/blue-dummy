import os, re

files = ['index.html', 'formSubmit.js', 'landing_page/assets/js/alipes.js']
for fn in files:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
    matches = re.findall(r'.{0,40}btnSubmitContactForm.{0,40}', t)
    if matches:
        print(f"In {fn}:")
        for m in matches:
            print("  ", m.strip())

