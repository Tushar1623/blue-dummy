with open('formSubmit.js', 'r', encoding='utf-8') as f:
    text = f.read()

print('formSubmit len:', len(text))
for line in text.splitlines():
    if 'ajax' in line.lower() or 'submit' in line.lower() or 'url' in line.lower() or 'api' in line.lower():
        print(line[:120])

print("\n--- populateFormFields.js ---")
with open('populateFormFields.js', 'r', encoding='utf-8') as f:
    print(f.read()[:600])
