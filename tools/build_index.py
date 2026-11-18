import re

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements
replacements = [
    # GLightbox
    ('https://dev.firsteconomy.com/godrej-mahalaxmi-lp/assets/component/glightbox/css/glightbox.min.css', 'landing_page/assets/vendors/glightbox/css/glightbox.min.css'),
    ('https://dev.firsteconomy.com/godrej-mahalaxmi-lp/assets/component/glightbox/js/glightbox.min.js', 'landing_page/assets/vendors/glightbox/js/glightbox.min.js'),
    
    # Slick
    ('https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.css', 'landing_page/assets/vendors/slick/slick.css'),
    ('https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js', 'landing_page/assets/vendors/slick/slick.min.js'),
    
    # Intl tel input
    ('https://cdn.jsdelivr.net/npm/intl-tel-input@18.1.1/build/css/intlTelInput.css', 'landing_page/assets/vendors/intl-tel-input/css/intlTelInput.css'),
    ('https://cdn.jsdelivr.net/npm/intl-tel-input@18.1.1/build/js/intlTelInput.min.js', 'landing_page/assets/vendors/intl-tel-input/js/intlTelInput.min.js'),
    
    # Form fields script
    ('../../../populateFormFields.js', 'populateFormFields.js'),
    
    # Footer logo
    ('https://www.godrejproperties.com/images/revamp/godrej_properties_logo.svg', 'external/images/revamp/godrej_properties_logo.svg'),
]

for old, new in replacements:
    html = html.replace(old, new)

# Let's add tracking stubs at the top of head so console doesn't spam errors if trackers are blocked/offline
tracker_stub = """
    <!-- Tracking Fallbacks & Console Cleaners -->
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){window.dataLayer.push(arguments);}
        window.fbq = window.fbq || function(){};
        window._tfa = window._tfa || [];
        window.twq = window.twq || function(){};
        window.clarity = window.clarity || function(){};
    </script>
"""

# Insert right after <head>
html = re.sub(r'(<head[^>]*>)', r'\1\n' + tracker_stub, html, count=1, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated index.html successfully, size:", len(html))
