with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's ensure both micro-locations (New Alipore & BL Saha Road) are covered
html = html.replace('3 bhk flats in BL Saha Road Kolkata', '3 BHK flats in BL Saha Road Kolkata')
if '3 BHK flats in BL Saha Road Kolkata' not in html:
    html = html.replace(
        'For detailed <strong>godrej blue kolkata 2 bhk / 3 bhk price</strong> sheets',
        'Whether you are looking for luxury <strong>3 BHK flats in New Alipore Kolkata</strong> or <strong>3 BHK flats in BL Saha Road Kolkata</strong>, for detailed <strong>godrej blue kolkata 2 bhk / 3 bhk price</strong> sheets'
    )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added BL Saha Road micro-location variant!")
else:
    print("Already present!")

