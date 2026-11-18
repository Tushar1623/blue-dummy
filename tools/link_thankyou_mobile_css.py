with open('thankyou.html', 'r', encoding='utf-8') as f:
    t_html = f.read()

css_link = '<link rel="stylesheet" href="landing_page/assets/css/mobile-custom.css" />'
if 'mobile-custom.css' not in t_html:
    t_html = t_html.replace('</head>', f'    {css_link}\n</head>')
    with open('thankyou.html', 'w', encoding='utf-8') as f:
        f.write(t_html)
    print("Linked mobile-custom.css in thankyou.html")
else:
    print("Already linked in thankyou.html")
