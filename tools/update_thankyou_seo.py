with open('thankyou.html', 'r', encoding='utf-8') as f:
    t_html = f.read()

import re
if 'name="keywords"' not in t_html:
    seo_meta = """<meta name="keywords" content="godrej blue kolkata price, godrej blue kolkata floor plan, godrej blue kolkata location, godrej blue kolkata possession date, godrej blue kolkata RERA, godrej blue kolkata brochure, godrej blue kolkata 2 bhk / 3 bhk price, godrej blue kolkata amenities, godrej blue kolkata reviews, godrej blue kolkata site visit, godrej blue kolkata payment plan, 3 bhk flats in New Alipore Kolkata, new launch apartments south Kolkata, Godrej Properties projects in Kolkata" />"""
    t_html = re.sub(r'(<head[^>]*>)', r'\1\n    ' + seo_meta, t_html, count=1, flags=re.IGNORECASE)
    with open('thankyou.html', 'w', encoding='utf-8') as f:
        f.write(t_html)
    print("Added keywords to thankyou.html")
else:
    print("Keywords already in thankyou.html")

