with open('formSubmit.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(670, min(len(lines), 720)):
    print(f"{i+1}: {lines[i]}", end='')
