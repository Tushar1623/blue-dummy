import re

with open('source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Local path replacements
replacements = [
    ('https://dev.firsteconomy.com/godrej-mahalaxmi-lp/assets/component/glightbox/css/glightbox.min.css', 'landing_page/assets/vendors/glightbox/css/glightbox.min.css'),
    ('https://dev.firsteconomy.com/godrej-mahalaxmi-lp/assets/component/glightbox/js/glightbox.min.js', 'landing_page/assets/vendors/glightbox/js/glightbox.min.js'),
    ('https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.css', 'landing_page/assets/vendors/slick/slick.css'),
    ('https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js', 'landing_page/assets/vendors/slick/slick.min.js'),
    ('https://cdn.jsdelivr.net/npm/intl-tel-input@18.1.1/build/css/intlTelInput.css', 'landing_page/assets/vendors/intl-tel-input/css/intlTelInput.css'),
    ('https://cdn.jsdelivr.net/npm/intl-tel-input@18.1.1/build/js/intlTelInput.min.js', 'landing_page/assets/vendors/intl-tel-input/js/intlTelInput.min.js'),
    ('../../../populateFormFields.js', 'populateFormFields.js'),
    ('https://www.godrejproperties.com/images/revamp/godrej_properties_logo.svg', 'external/images/revamp/godrej_properties_logo.svg'),
    ('landing_page/assets/images/AMENITIES ICON - 250x100_15+ Clubhouse Amenities.png', 'landing_page/assets/images/amenities_icon_15_clubhouse.png'),
    ('landing_page/assets/images/AMENITIES ICON - 250x100_5+ Pondside Amenities.png', 'landing_page/assets/images/amenities_icon_5_pondside.png'),
    ('landing_page/assets/images/AMENITIES ICON - 250x100_20+ Podium Amenities.png', 'landing_page/assets/images/amenities_icon_20_podium.png'),
    ('landing_page/assets/images/Victoria image - 400x405-01.jpg', 'landing_page/assets/images/victoria_image_400x405.jpg'),
    ('landing_page/assets/images/LANDING PAGE 1920X1080-01.jpg', 'landing_page/assets/images/landing_page_1920x1080.jpg'),
]

for old, new in replacements:
    html = html.replace(old, new)

# 2. Add SEO Meta Tags in <head>
seo_tags = """
    <!-- Target SEO Meta Tags & Keywords -->
    <title>Godrej Blue BL Saha Road, New Alipore, South Kolkata | Price, Floor Plan, Reviews & Brochure | Godrej Properties</title>
    <meta name="keywords" content="godrej blue kolkata price, godrej blue kolkata floor plan, godrej blue kolkata location, godrej blue kolkata possession date, godrej blue kolkata RERA, godrej blue kolkata brochure, godrej blue kolkata 2 bhk / 3 bhk price, godrej blue kolkata amenities, godrej blue kolkata reviews, godrej blue kolkata site visit, godrej blue kolkata payment plan, 3 bhk flats in New Alipore Kolkata, 3 bhk flats in BL Saha Road Kolkata, new launch apartments south Kolkata, Godrej Properties projects in Kolkata" />
    <meta name="description" content="Explore Godrej Blue Kolkata at BL Saha Road, New Alipore. Check Godrej Blue Kolkata price, 2 BHK / 3 BHK price, floor plan, location, possession date, RERA details, world-class amenities, reviews, payment plan and download brochure. Book your Godrej Blue Kolkata site visit today!" />
    <meta property="og:title" content="Godrej Blue Kolkata | Price, Floor Plan & Luxury Apartments in South Kolkata" />
    <meta property="og:description" content="Discover Godrej Blue at BL Saha Road, New Alipore - premier new launch apartments South Kolkata with 2 BHK and 3 BHK luxury residences by Godrej Properties." />

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

html = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_tags, html, count=1, flags=re.IGNORECASE)

# 3. Add FAQ link to navbar
old_nav_ul = """<ul class="main-menu__list">
                                <li>
                                    <a class="scroll" href="#">Home</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#overview">Our Inspiration</a>
                                </li>
                               
                                <li>
                                    <a class="scroll" href="#gallery">Gallery</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#about_gpl">About GPL</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#footer">Contact Us</a>
                                </li>
                            </ul>"""

new_nav_ul = """<ul class="main-menu__list">
                                <li>
                                    <a class="scroll" href="#">Home</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#overview">Our Inspiration</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#highlights">Amenities</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#gallery">Gallery</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#about_gpl">About GPL</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#faq">FAQ</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#footer">Contact Us</a>
                                </li>
                            </ul>"""

if old_nav_ul in html:
    html = html.replace(old_nav_ul, new_nav_ul)
else:
    html = re.sub(r'<ul class="main-menu__list">[\s\S]*?</ul>', new_nav_ul, html, count=1)

# 4. In Overview section, enrich copy naturally with keywords
overview_target = """<p class="about-one__text-2">
                                        The calm waters have inspired Godrej Properties to craft an experience in South
                                        Kolkata that mirrors its serenity. Here, you'll find a world designed for peace
                                        and timeless elegance.
                                    </p>"""

overview_replacement = """<p class="about-one__text-2">
                                        The calm waters have inspired Godrej Properties to craft an experience in South
                                        Kolkata that mirrors its serenity. As one of the most prominent <strong>new launch apartments south Kolkata</strong> has unveiled, Godrej Blue offers luxury waterfront living including spacious <strong>3 BHK flats in New Alipore Kolkata</strong> on BL Saha Road. Here, you'll find a world designed for peace, timeless elegance, and landmark lifestyle.
                                    </p>"""

if overview_target in html:
    html = html.replace(overview_target, overview_replacement)
else:
    html = re.sub(r'<p class="about-one__text-2">[\s\S]*?</p>', overview_replacement, html, count=1)

# 5. In FAQs, expand with all keywords seamlessly inside the original FAQ accordion
faqs_replacement = """<section class="faq-section section-padding" id="faq">
    <div class="container">
        <div class="section-title text-center">
            <h2 class="section-title__title">Frequently Asked Questions</h2>
        </div>

        <div class="faq-accordion">

            <div class="faq-item active">
                <button class="faq-question">
                    1. Where is the Godrej Blue Kolkata location and how is its connectivity?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata location</strong> is strategically situated at 82/1, BL Saha Road, New Alipore, South Kolkata - 700053. It offers exceptional connectivity to Tollygunge Metro Station (7 mins), New Alipore Railway Station (5 mins), South City Mall (12 mins), CMRI &amp; BP Poddar Hospitals (10 mins), and top educational institutions, making it the most coveted address among <strong>new launch apartments south Kolkata</strong>.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    2. What is the Godrej Blue Kolkata price and 2 BHK / 3 BHK price?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata price</strong> starts from ₹1.15 Cr* onwards for 2 BHK residences and from ₹1.55 Cr* onwards for premium <strong>3 BHK flats in New Alipore Kolkata</strong>. For detailed <strong>godrej blue kolkata 2 bhk / 3 bhk price</strong> sheets including car parking and floor rise options, click "Download Brochure" or "Enquire Now" to receive the official cost sheet.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    3. Where can I view or download the Godrej Blue Kolkata floor plan?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The complete <strong>godrej blue kolkata floor plan</strong> booklet featuring unit layouts (3 BHK - R, 3 BHK - L, 3 BHK - XL, and 4 BHK luxury residences) is available in the official project brochure. Click the "Download Brochure" button, fill in your details, and the floor plan PDF will be made available for download instantly.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    4. What is the Godrej Blue Kolkata possession date and RERA registration?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata possession date</strong> is scheduled starting from December 2028 as per the official regulatory timeline. The project is completely approved and registered with <strong>godrej blue kolkata RERA</strong> number: <strong>WBRERA/P/KOL/2024/002211</strong>. Prospective buyers can verify all statutory approvals on the West Bengal RERA website.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    5. What world-class Godrej Blue Kolkata amenities are provided?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata amenities</strong> feature 50+ curated lifestyle indulgences across Pondside, Clubhouse, and Podium zones. Key amenities include an infinity-edge swimming pool overlooking calm waters, 18,000 sq. ft. clubhouse, lakeside decks, jogging track, squash &amp; badminton courts, gymnasium, banquet hall, children's play parks, and yoga lawns.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    6. How does the Godrej Blue Kolkata payment plan work?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata payment plan</strong> offers convenient milestone-based construction-linked plans as well as the special Godrej 1% Monthly Payment Plan for eligible homebuyers. Flexible financing and loan approvals are supported by all major banks (SBI, HDFC, ICICI, Axis Bank).</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    7. How can I schedule a Godrej Blue Kolkata site visit and get the brochure?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>To book your personalized <strong>godrej blue kolkata site visit</strong> or download the <strong>godrej blue kolkata brochure</strong>, simply click the "Download Brochure" or "Enquire Now" button, fill in your name, email, and mobile number. Our senior property advisor will promptly assist you with sample flat tours, cab facility, and project documentation.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    8. What do verified Godrej Blue Kolkata reviews say about the project?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>Homebuyers and real estate consultants in their <strong>godrej blue kolkata reviews</strong> highlight the rare combination of a serene natural pond and urban connectivity in New Alipore, along with spacious floor plans, high ceiling heights, and the trusted heritage of Godrej Properties.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    9. Why are 3 BHK flats in New Alipore Kolkata at Godrej Blue so popular?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>Demand for <strong>3 BHK flats in New Alipore Kolkata</strong> and <strong>3 BHK flats in BL Saha Road Kolkata</strong> is driven by the area's affluent neighborhood, high safety, elite schools (MP Birla, Lakshmipat Singhania), and peaceful living. Godrej Blue delivers generous 3 BHK layouts with private balconies overlooking serene waters.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    10. What other Godrej Properties projects in Kolkata are available?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>Other landmark <strong>Godrej Properties projects in Kolkata</strong> include Godrej Prakriti on BT Road (a 22-acre riverside township in North Kolkata), Godrej Seven in Joka (South Kolkata), and commercial grade-A office hubs like Godrej Waterside and Godrej Genesis in Salt Lake Sector V.</p>
                </div>
            </div>

        </div>
    </div>
</section>"""

html = re.sub(r'<section class="faq-section[\s\S]*?</section>', faqs_replacement, html, count=1)

# 6. Update popupModal: Add subtitle, dynamic header, and clear user guidance
old_modal_header = """<div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Enquire Now</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>"""

new_modal_header = """<div class="modal-header" style="background:#076291; color:#fff; border-bottom:none;">
                    <div>
                        <h1 class="modal-title fs-5" id="staticBackdropLabel" style="color:#fff; font-family:'Bodoni72', serif; font-weight:700;">Enquire Now</h1>
                        <p id="modalSubTitle" style="font-size:13px; color:rgba(255,255,255,0.85); margin:4px 0 0 0;">Please fill in your details below and our team will get in touch shortly.</p>
                    </div>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>"""

html = html.replace(old_modal_header, new_modal_header)

# 7. Add Controller Script for Brochure & Enquiry CTA Behavior
modal_controller_script = """
    <!-- Modal Dynamic State Controller: Download Brochure vs Enquiry -->
    <script>
        $(document).ready(function() {
            // Function to configure modal mode
            function setupModal(mode) {
                var isBrochure = (mode === 'brochure');
                
                if (isBrochure) {
                    $('#staticBackdropLabel').text('Download Official Brochure');
                    $('#modalSubTitle').text('Please fill in your details to instantly receive and download the Godrej Blue brochure.');
                    $('#download_file_type').removeAttr('disabled').val('brochure');
                    $('#btnSubmitContactForm').text('DOWNLOAD BROCHURE NOW');
                    if (window.selectedAction) {
                        window.selectedAction.type = 'brochure';
                        window.selectedAction.file = 'brochure';
                    }
                } else {
                    $('#staticBackdropLabel').text('Enquire Now');
                    $('#modalSubTitle').text('Please fill in your details below and our property expert will contact you shortly.');
                    $('#download_file_type').val('').prop('disabled', true);
                    $('#btnSubmitContactForm').text('SUBMIT ENQUIRY');
                    if (window.selectedAction) {
                        window.selectedAction.type = 'enquiry';
                        window.selectedAction.file = '';
                    }
                }
            }

            // Click listener for any brochure download button or link
            $(document).on('click', '.brochure_cta, [data-id="brochure"], [data-action="brochure"], a:contains("Download Brochure"), button:contains("Download Brochure")', function() {
                setupModal('brochure');
            });

            // Click listener for any enquiry button
            $(document).on('click', '.enquire-btn, .toggle-sidebar, [data-id="enquire"], [data-action="enquire"], a:contains("Enquire"), button:contains("ENQUIRE")', function() {
                setupModal('enquiry');
            });

            // Reset modal on close
            $(document).on('click', '.btn-close, [data-bs-dismiss="modal"]', function() {
                setupModal('enquiry');
            });
        });
    </script>
"""

# Insert controller script before </body>
html = html.replace('</body>', modal_controller_script + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html rebuilt perfectly!")

