with open('landing_page/assets/js/alipes.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = """  if ($(".mobile-nav__toggler").length) {
    $(".mobile-nav__toggler, li a").on("click", function (e) {
      // e.preventDefault();
      $(".mobile-nav__wrapper").toggleClass("expanded");
      $("body").toggleClass("locked");
    });
  }"""

replacement = """  if ($(".mobile-nav__toggler").length) {
    $(".mobile-nav__toggler, .mobile-nav__content li a").on("click", function (e) {
      $(".mobile-nav__wrapper").toggleClass("expanded");
      $("body").toggleClass("locked");
    });
  }"""

if target in text:
    text = text.replace(target, replacement)
    with open('landing_page/assets/js/alipes.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed mobile-nav toggler selector in alipes.js!")
else:
    print("Target not found in alipes.js, searching for partial...")
    idx = text.find('$(".mobile-nav__toggler')
    if idx != -1:
        print(text[idx:idx+200])
