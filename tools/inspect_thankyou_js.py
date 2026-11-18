with open('thankyou.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'download_pdf_new' in l or 'downloadBrochure' in l:
        for j in range(max(0, i-5), min(len(lines), i+45)):
            print(f"{j+1}: {lines[j]}", end='')
        break

