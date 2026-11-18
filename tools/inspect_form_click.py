with open('formSubmit.js', 'r', encoding='utf-8') as f:
    text = f.read()

for i, line in enumerate(text.splitlines()):
    if 'click' in line.lower() or 'submit' in line.lower():
        if any(w in line for w in ['btn', 'Btn', 'form', 'Form', 'addEventListener', 'onclick']):
            print(f"{i+1}: {line}")

