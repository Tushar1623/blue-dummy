with open('landing_page/assets/js/alipes.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('mobile-nav__toggler')
if idx != -1:
    print(text[idx-50:idx+400])
