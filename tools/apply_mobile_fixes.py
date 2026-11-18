import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add link to mobile-custom.css in <head>
css_link = '<link rel="stylesheet" href="landing_page/assets/css/mobile-custom.css" />'
if 'mobile-custom.css' not in html:
    html = html.replace('</head>', f'    {css_link}\n</head>')
    print("Linked mobile-custom.css in head")

# 2. Add Mobile Sticky Action Bar before </body>
sticky_bar_html = """
    <!-- Mobile Bottom Sticky Action Bar (Phones & Tablets) -->
    <div class="mobile-sticky-bar d-lg-none">
        <button type="button" class="mob-bar-btn mob-bar-brochure" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="brochure">
            <i class="fa fa-download"></i> Brochure
        </button>
        <button type="button" class="mob-bar-btn mob-bar-enquire" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="enquire">
            <i class="fa fa-paper-plane"></i> Enquire Now
        </button>
    </div>
"""

# Remove old single mob-enquire button
html = re.sub(
    r'<button type="button" class="btn btn-primary mob-enquire[^>]*>[\s\S]*?</button>',
    '',
    html
)

if 'mobile-sticky-bar' not in html:
    html = html.replace('</body>', f'{sticky_bar_html}\n</body>')
    print("Added mobile-sticky-bar")

# 3. Update Modal Controller script to listen to mob-bar-brochure and mob-bar-enquire
ctrl_old = '$(document).on(\'click\', \'.brochure_cta, [data-id="brochure"]'
ctrl_new = '$(document).on(\'click\', \'.brochure_cta, .mob-bar-brochure, [data-id="brochure"]'
html = html.replace(ctrl_old, ctrl_new)

ctrl_enq_old = '$(document).on(\'click\', \'.enquire-btn, .toggle-sidebar, .mob-enquire, .header-enquire-btn'
ctrl_enq_new = '$(document).on(\'click\', \'.enquire-btn, .toggle-sidebar, .mob-enquire, .mob-bar-enquire, .header-enquire-btn'
html = html.replace(ctrl_enq_old, ctrl_enq_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with mobile enhancements!")
