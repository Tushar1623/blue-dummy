with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read().lower()

keywords = [
    "godrej blue kolkata price",
    "godrej blue kolkata floor plan",
    "godrej blue kolkata location",
    "godrej blue kolkata possession date",
    "godrej blue kolkata rera",
    "godrej blue kolkata brochure",
    "godrej blue kolkata 2 bhk / 3 bhk price",
    "godrej blue kolkata amenities",
    "godrej blue kolkata reviews",
    "godrej blue kolkata site visit",
    "godrej blue kolkata payment plan",
    "3 bhk flats in new alipore kolkata",
    "new launch apartments south kolkata",
    "godrej properties projects in kolkata"
]

print("=== KEYWORD CHECK IN INDEX.HTML ===")
all_present = True
for kw in keywords:
    count = html.count(kw.lower())
    print(f"Keyword: '{kw}' -> Found {count} times")
    if count == 0:
        all_present = False

print("\nAll keywords present:", all_present)

