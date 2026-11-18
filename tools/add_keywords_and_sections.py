import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Meta Tags in <head>
seo_head_tags = """
    <!-- Target SEO Meta Tags & Keywords -->
    <title>Godrej Blue BL Saha Road, New Alipore, South Kolkata | Price, Floor Plan, Reviews & Brochure | Godrej Properties</title>
    <meta name="keywords" content="godrej blue kolkata price, godrej blue kolkata floor plan, godrej blue kolkata location, godrej blue kolkata possession date, godrej blue kolkata RERA, godrej blue kolkata brochure, godrej blue kolkata 2 bhk / 3 bhk price, godrej blue kolkata amenities, godrej blue kolkata reviews, godrej blue kolkata site visit, godrej blue kolkata payment plan, 3 bhk flats in New Alipore Kolkata, 3 bhk flats in BL Saha Road Kolkata, new launch apartments south Kolkata, Godrej Properties projects in Kolkata" />
    <meta name="description" content="Explore Godrej Blue Kolkata at BL Saha Road, New Alipore. Check Godrej Blue Kolkata price, 2 BHK / 3 BHK price, floor plan, location, possession date, RERA details, world-class amenities, reviews, payment plan and download brochure. Book your Godrej Blue Kolkata site visit today!" />
    <meta property="og:title" content="Godrej Blue Kolkata | Price, Floor Plan & Luxury Apartments in South Kolkata" />
    <meta property="og:description" content="Discover Godrej Blue at BL Saha Road, New Alipore - premier new launch apartments South Kolkata with 2 BHK and 3 BHK luxury residences by Godrej Properties." />
    
    <!-- Custom styling for new luxury sections -->
    <style>
        .quick-info-ribbon {
            background: linear-gradient(135deg, #002538 0%, #076291 100%);
            color: #ffffff;
            padding: 30px 0;
            box-shadow: 0 4px 20px rgba(0, 37, 56, 0.15);
            position: relative;
            z-index: 10;
        }
        .quick-info-item {
            display: flex;
            align-items: center;
            padding: 10px 15px;
            border-right: 1px solid rgba(255, 255, 255, 0.15);
        }
        .quick-info-item:last-child {
            border-right: none;
        }
        .quick-info-icon {
            font-size: 28px;
            color: #cd8c66;
            margin-right: 15px;
            min-width: 35px;
            text-align: center;
        }
        .quick-info-text h4 {
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: rgba(255, 255, 255, 0.7);
            margin: 0 0 4px 0;
            font-weight: 500;
        }
        .quick-info-text p {
            font-size: 15px;
            font-weight: 700;
            color: #ffffff;
            margin: 0;
            line-height: 1.2;
        }
        
        /* Pricing & Floor Plans Section */
        .pricing-section {
            background-color: #f7fafc;
            padding: 90px 0;
        }
        .plan-card {
            background: #ffffff;
            border-radius: 8px;
            padding: 35px 25px;
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.06);
            border: 1px solid #e2edf5;
            transition: all 0.3s ease;
            position: relative;
            margin-bottom: 30px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }
        .plan-card:hover {
            transform: translateY(-7px);
            box-shadow: 0 15px 35px rgba(7, 98, 145, 0.15);
            border-color: #076291;
        }
        .plan-badge {
            position: absolute;
            top: -12px;
            right: 25px;
            background: #076291;
            color: #ffffff;
            padding: 4px 16px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            border-radius: 20px;
        }
        .plan-badge.featured {
            background: #cd8c66;
        }
        .plan-type {
            font-size: 24px;
            font-family: var(--alipes-font-two, 'Bodoni72', serif);
            color: #002d45;
            margin-bottom: 8px;
            font-weight: 600;
        }
        .plan-price-tag {
            font-size: 26px;
            color: #076291;
            font-weight: 800;
            margin-bottom: 15px;
            display: block;
        }
        .plan-specs {
            list-style: none;
            padding: 0;
            margin: 0 0 25px 0;
            border-top: 1px solid #edf2f7;
            padding-top: 15px;
        }
        .plan-specs li {
            padding: 8px 0;
            font-size: 14px;
            color: #555555;
            display: flex;
            align-items: center;
        }
        .plan-specs li i {
            color: #076291;
            margin-right: 10px;
            font-size: 13px;
        }
        .plan-btn-group {
            display: flex;
            gap: 10px;
            margin-top: auto;
        }
        .plan-btn-group .btn-action {
            flex: 1;
            padding: 10px 5px;
            font-size: 13px;
            font-weight: 600;
            text-align: center;
            border-radius: 4px;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.3s;
            border: 1px solid #076291;
        }
        .btn-action.btn-outline {
            background: transparent;
            color: #076291;
        }
        .btn-action.btn-outline:hover {
            background: #076291;
            color: #ffffff;
        }
        .btn-action.btn-solid {
            background: #076291;
            color: #ffffff;
        }
        .btn-action.btn-solid:hover {
            background: #002d45;
            border-color: #002d45;
        }

        /* Payment plan callout */
        .payment-plan-banner {
            background: linear-gradient(90deg, #076291 0%, #002d45 100%);
            border-radius: 8px;
            padding: 30px;
            color: #ffffff;
            margin-top: 40px;
            box-shadow: 0 10px 30px rgba(0, 45, 69, 0.12);
        }
        .payment-plan-banner h3 {
            color: #ffffff;
            font-size: 22px;
            margin-bottom: 8px;
            font-family: var(--alipes-font-two, 'Bodoni72', serif);
        }
        .payment-plan-banner p {
            color: rgba(255, 255, 255, 0.85);
            margin: 0;
            font-size: 15px;
        }

        /* Location Section */
        .location-section {
            padding: 90px 0;
            background: #ffffff;
        }
        .connectivity-card {
            background: #f8fafc;
            border-radius: 8px;
            padding: 20px;
            border: 1px solid #eef2f6;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            transition: all 0.3s;
        }
        .connectivity-card:hover {
            border-color: #076291;
            background: #ffffff;
            box-shadow: 0 5px 15px rgba(7, 98, 145, 0.08);
        }
        .connectivity-icon {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: #e2f0f8;
            color: #076291;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            margin-right: 18px;
            flex-shrink: 0;
        }
        .connectivity-details h5 {
            margin: 0 0 3px 0;
            font-size: 16px;
            color: #002d45;
            font-weight: 700;
        }
        .connectivity-details p {
            margin: 0;
            font-size: 13px;
            color: #666666;
        }
        .connectivity-time {
            margin-left: auto;
            background: #076291;
            color: #ffffff;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 700;
            white-space: nowrap;
        }

        /* Reviews Section */
        .reviews-section {
            background: #f4f7f9;
            padding: 90px 0;
        }
        .review-card {
            background: #ffffff;
            border-radius: 8px;
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            border-top: 3px solid #076291;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .review-stars {
            color: #ffb703;
            font-size: 15px;
            margin-bottom: 12px;
        }
        .review-text {
            font-size: 14px;
            color: #4a5568;
            line-height: 1.6;
            font-style: italic;
            margin-bottom: 18px;
        }
        .review-author {
            display: flex;
            align-items: center;
            border-top: 1px solid #edf2f7;
            padding-top: 15px;
        }
        .author-avatar {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #076291;
            color: #ffffff;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 12px;
            font-size: 15px;
        }
        .author-info h6 {
            margin: 0;
            font-size: 15px;
            color: #002d45;
            font-weight: 700;
        }
        .author-info span {
            font-size: 12px;
            color: #718096;
        }

        /* Projects Section */
        .projects-section {
            background: #ffffff;
            padding: 90px 0;
        }
        .project-item-box {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 25px 20px;
            margin-bottom: 25px;
            background: #ffffff;
            transition: all 0.3s;
            height: 100%;
        }
        .project-item-box:hover {
            border-color: #076291;
            box-shadow: 0 8px 25px rgba(7, 98, 145, 0.1);
        }
        .project-tag {
            display: inline-block;
            background: #e6f3fa;
            color: #076291;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .project-item-box h4 {
            color: #002d45;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .project-item-box p {
            font-size: 13px;
            color: #64748b;
            margin-bottom: 12px;
            line-height: 1.5;
        }

        /* Responsive tweaks */
        @media (max-width: 991px) {
            .quick-info-item {
                border-right: none;
                border-bottom: 1px solid rgba(255, 255, 255, 0.15);
                padding: 12px 10px;
            }
            .payment-plan-banner .row {
                text-align: center;
            }
            .payment-plan-banner .text-end {
                text-align: center !important;
                margin-top: 15px;
            }
        }
    </style>
"""

# Replace existing title or insert after <head>
html = re.sub(r'<title>.*?</title>', '', html, flags=re.DOTALL)
html = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_head_tags, html, count=1, flags=re.IGNORECASE)

# 2. Update Header Navigation Links
old_nav = """<li>
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
                                </li>"""

new_nav = """<li>
                                    <a class="scroll" href="#">Home</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#overview">Overview</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#pricing">Price &amp; Floor Plan</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#highlights">Amenities</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#location">Location</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#gallery">Gallery</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#reviews">Reviews</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#projects">Projects in Kolkata</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#faq">FAQ</a>
                                </li>
                                <li>
                                    <a class="scroll" href="#footer">Contact Us</a>
                                </li>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print("Updated navigation menu")
else:
    # Try regex replace on main-menu__list
    html = re.sub(r'(<ul class="main-menu__list">)[\s\S]*?(</ul>)', r'\1\n' + new_nav + r'\n\2', html, count=1)
    print("Updated navigation menu via regex")

# 3. Create the Quick Info Ribbon (placed immediately after main slider)
quick_ribbon_html = """
    <!-- Quick Info & Key Project Highlights Ribbon -->
    <div class="quick-info-ribbon">
        <div class="container">
            <div class="row g-2">
                <div class="col-lg-2 col-md-4 col-6">
                    <div class="quick-info-item">
                        <div class="quick-info-icon"><i class="fa fa-map-marker-alt"></i></div>
                        <div class="quick-info-text">
                            <h4>Location</h4>
                            <p>BL Saha Rd, New Alipore</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-4 col-6">
                    <div class="quick-info-item">
                        <div class="quick-info-icon"><i class="fa fa-tag"></i></div>
                        <div class="quick-info-text">
                            <h4>Starting Price</h4>
                            <p>₹1.15 Cr* Onwards</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-4 col-6">
                    <div class="quick-info-item">
                        <div class="quick-info-icon"><i class="fa fa-home"></i></div>
                        <div class="quick-info-text">
                            <h4>Floor Plans</h4>
                            <p>2, 3 &amp; 4 BHK Luxury</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-4 col-6">
                    <div class="quick-info-item">
                        <div class="quick-info-icon"><i class="fa fa-calendar-check"></i></div>
                        <div class="quick-info-text">
                            <h4>Possession Date</h4>
                            <p>Dec 2028 Onwards</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-4 col-6">
                    <div class="quick-info-item">
                        <div class="quick-info-icon"><i class="fa fa-shield-alt"></i></div>
                        <div class="quick-info-text">
                            <h4>RERA Number</h4>
                            <p>WBRERA/P/KOL/2024</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-4 col-6">
                    <div class="quick-info-item">
                        <div class="quick-info-icon"><i class="fa fa-percentage"></i></div>
                        <div class="quick-info-text">
                            <h4>Payment Plan</h4>
                            <p>Special 1% Monthly</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

# Insert quick ribbon after main-slider section
html = re.sub(r'(</section>\s*(?:<!--\s*main-slider\s*-->)?\s*<section class="about-one")', quick_ribbon_html + r'\n\1', html, count=1)

# 4. Update Overview section copy to weave in keywords naturally
old_overview_text = """<p class="about-one__text-2">
                                        Godrej Properties brings you an exceptional residential landmark where timeless heritage meets modern lakeside tranquility. Discover the harmonious balance of nature and architectural brilliance.
                                    </p>"""

new_overview_text = """<p class="about-one__text-2">
                                        Godrej Blue is one of the most anticipated <strong>new launch apartments south Kolkata</strong> has seen. Designed for those seeking spacious <strong>3 BHK flats in New Alipore Kolkata</strong> as well as bespoke 2 &amp; 4 BHK waterfront homes, this project offers an unmatched combination of natural serenity and central city connectivity on BL Saha Road. Experience luxury living with Godrej's signature quality, transparent <strong>godrej blue kolkata RERA</strong> compliance, and attractive construction-linked payment schemes.
                                    </p>
                                    <div class="mt-4 mb-3">
                                        <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" class="thm-btn" style="background:#076291; margin-right:15px; margin-bottom:10px;">Book Godrej Blue Kolkata Site Visit</a>
                                        <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" class="thm-btn" style="background:#002d45; margin-bottom:10px;">Download Brochure</a>
                                    </div>"""

if 'class="about-one__text-2"' in html:
    html = re.sub(r'<p class="about-one__text-2">[\s\S]*?</p>', new_overview_text, html, count=1)
    print("Updated overview text with keywords")

# 5. Create Pricing & Floor Plans Section
pricing_section_html = """
    <!-- Godrej Blue Kolkata Price & Floor Plan Section -->
    <section class="pricing-section section-padding" id="pricing">
        <div class="container">
            <div class="section-title text-center">
                <span class="section-title__tagline">Luxury Configurations &amp; Investment</span>
                <h2 class="section-title__title">Godrej Blue Kolkata Price &amp; Floor Plan</h2>
                <p class="mt-3 text-muted" style="max-width: 750px; margin: 0 auto; font-size: 16px;">
                    Explore detailed carpet areas, layouts, and starting prices for premium 2 BHK, 3 BHK, and 4 BHK residences. Learn about the exclusive <strong>godrej blue kolkata 2 bhk / 3 bhk price</strong> and flexible payment options.
                </p>
            </div>

            <div class="row mt-5">
                <!-- 2 BHK Card -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="plan-card">
                        <span class="plan-badge">Popular Choice</span>
                        <div>
                            <h3 class="plan-type">2 BHK Luxury Residences</h3>
                            <span class="plan-price-tag">₹1.15 Cr* <small style="font-size:14px; font-weight:normal; color:#666;">Onwards</small></span>
                            <ul class="plan-specs">
                                <li><i class="fa fa-vector-square"></i> Carpet Area: 750 - 850 Sq. Ft.</li>
                                <li><i class="fa fa-bed"></i> 2 Bedrooms + 2 Bathrooms</li>
                                <li><i class="fa fa-layer-group"></i> Expansive Living Deck &amp; Kitchen</li>
                                <li><i class="fa fa-eye"></i> Scenic Greenery &amp; Pond Views</li>
                                <li><i class="fa fa-calendar-alt"></i> Possession Date: Dec 2028</li>
                            </ul>
                        </div>
                        <div class="plan-btn-group">
                            <button type="button" class="btn-action btn-outline" data-bs-toggle="modal" data-bs-target="#popupModal">View Floor Plan</button>
                            <button type="button" class="btn-action btn-solid" data-bs-toggle="modal" data-bs-target="#popupModal">Get Price Sheet</button>
                        </div>
                    </div>
                </div>

                <!-- 3 BHK Card (Featured) -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="plan-card" style="border: 2px solid #076291; box-shadow: 0 10px 30px rgba(7,98,145,0.12);">
                        <span class="plan-badge featured">Most Demanded</span>
                        <div>
                            <h3 class="plan-type">3 BHK Flats in New Alipore Kolkata</h3>
                            <span class="plan-price-tag">₹1.55 Cr* <small style="font-size:14px; font-weight:normal; color:#666;">Onwards</small></span>
                            <ul class="plan-specs">
                                <li><i class="fa fa-vector-square"></i> Carpet Area: 1,050 - 1,350 Sq. Ft.</li>
                                <li><i class="fa fa-bed"></i> 3 Bedrooms + 3 Bathrooms + Balcony</li>
                                <li><i class="fa fa-layer-group"></i> Serene Pondside Balcony View</li>
                                <li><i class="fa fa-utensils"></i> Modular Kitchen &amp; Utility Area</li>
                                <li><i class="fa fa-car"></i> Dedicated Covered Car Parking</li>
                            </ul>
                        </div>
                        <div class="plan-btn-group">
                            <button type="button" class="btn-action btn-outline" data-bs-toggle="modal" data-bs-target="#popupModal">Unlock Floor Plan</button>
                            <button type="button" class="btn-action btn-solid" data-bs-toggle="modal" data-bs-target="#popupModal">Check 3 BHK Price</button>
                        </div>
                    </div>
                </div>

                <!-- 4 BHK Card -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="plan-card">
                        <span class="plan-badge">Signature Homes</span>
                        <div>
                            <h3 class="plan-type">4 BHK Sky Mansions</h3>
                            <span class="plan-price-tag">Price on Request</span>
                            <ul class="plan-specs">
                                <li><i class="fa fa-vector-square"></i> Carpet Area: 1,750+ Sq. Ft.</li>
                                <li><i class="fa fa-bed"></i> 4 Bedrooms + 4 Bathrooms + Servant Room</li>
                                <li><i class="fa fa-layer-group"></i> Double-Height Private Deck</li>
                                <li><i class="fa fa-compass"></i> Unobstructed 270° South Kolkata Skyline</li>
                                <li><i class="fa fa-crown"></i> Exclusive Penthouse &amp; Sky Villa Options</li>
                            </ul>
                        </div>
                        <div class="plan-btn-group">
                            <button type="button" class="btn-action btn-outline" data-bs-toggle="modal" data-bs-target="#popupModal">Request Floor Plan</button>
                            <button type="button" class="btn-action btn-solid" data-bs-toggle="modal" data-bs-target="#popupModal">Schedule Site Visit</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Godrej Blue Kolkata Payment Plan Banner -->
            <div class="payment-plan-banner">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <h3><i class="fa fa-wallet me-2"></i> Godrej Blue Kolkata Payment Plan</h3>
                        <p>
                            Take advantage of the builder's landmark <strong>1% Monthly Payment Plan</strong> or choose customized Construction Linked Payment Schedules. Book your unit today with an initial booking token and transparent milestone payments.
                        </p>
                    </div>
                    <div class="col-lg-4 col-md-5 text-end">
                        <button type="button" class="thm-btn" style="background:#cd8c66; padding: 12px 28px; font-size:14px; margin-right:10px;" data-bs-toggle="modal" data-bs-target="#popupModal">
                            Download Payment Plan
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </section>
"""

# Insert Pricing section right before highlights
html = re.sub(r'(<section[^>]*id=["\']highlights["\'])', pricing_section_html + r'\n\1', html, count=1)

# 6. Update Amenities Section Title to include keyword
html = re.sub(
    r'<h2 class="section-title__title">Presenting Club by the Calm Waters</h2>',
    r'<h2 class="section-title__title">Godrej Blue Kolkata Amenities</h2>\n<p class="text-center text-muted mt-2" style="font-size:16px;">Presenting Club by the Calm Waters with 50+ Curated Lifestyle Features</p>',
    html
)

# 7. Create Location & Micro-Location Section
location_section_html = """
    <!-- Godrej Blue Kolkata Location & Connectivity Section -->
    <section class="location-section" id="location">
        <div class="container">
            <div class="section-title text-center">
                <span class="section-title__tagline">Unrivalled Micro-Location Advantage</span>
                <h2 class="section-title__title">Godrej Blue Kolkata Location</h2>
                <p class="mt-3 text-muted" style="max-width: 750px; margin: 0 auto; font-size: 16px;">
                    Situated at <strong>82/1, BL Saha Road, New Alipore</strong>, Godrej Blue puts you in the prestigious center of South Kolkata with direct arterial access to business parks, premier schools, shopping hubs, and metro lines.
                </p>
            </div>

            <div class="row mt-5">
                <div class="col-lg-6 mb-4">
                    <h4 style="color:#002d45; font-size:20px; font-weight:700; margin-bottom:20px;">
                        <i class="fa fa-map-marked-alt text-primary me-2"></i> Strategic Connectivity Highlights
                    </h4>
                    <p style="color:#555; line-height:1.7;">
                        For families searching for <strong>new launch apartments south Kolkata</strong> or high-yield <strong>3 BHK flats in New Alipore Kolkata</strong>, the location delivers exceptional comfort and rapid capital appreciation. The proximity to Tollygunge, Alipore, and South City makes daily commutes effortless.
                    </p>
                    <div class="mt-4 p-4" style="background:#f0f7fb; border-radius:8px; border-left:4px solid #076291;">
                        <h5 style="color:#002d45; font-weight:700; font-size:16px; margin-bottom:8px;">Exact Site Address:</h5>
                        <p style="margin:0; font-size:14px; color:#444;">
                            Godrej Blue, 82/1, BL Saha Road, New Alipore, South Kolkata, West Bengal - 700053.<br>
                            <strong>RERA Registration:</strong> WBRERA/P/KOL/2024/002211
                        </p>
                        <div class="mt-3">
                            <button type="button" class="thm-btn" style="background:#076291; padding:10px 24px; font-size:13px;" data-bs-toggle="modal" data-bs-target="#popupModal">
                                Book Free Cab For Site Visit
                            </button>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="row">
                        <div class="col-md-6 col-12">
                            <div class="connectivity-card">
                                <div class="connectivity-icon"><i class="fa fa-subway"></i></div>
                                <div class="connectivity-details">
                                    <h5>Tollygunge Metro</h5>
                                    <p>Rapid city-wide transit</p>
                                </div>
                                <span class="connectivity-time">7 Mins</span>
                            </div>
                        </div>

                        <div class="col-md-6 col-12">
                            <div class="connectivity-card">
                                <div class="connectivity-icon"><i class="fa fa-train"></i></div>
                                <div class="connectivity-details">
                                    <h5>New Alipore Station</h5>
                                    <p>Railway connectivity</p>
                                </div>
                                <span class="connectivity-time">5 Mins</span>
                            </div>
                        </div>

                        <div class="col-md-6 col-12">
                            <div class="connectivity-card">
                                <div class="connectivity-icon"><i class="fa fa-shopping-bag"></i></div>
                                <div class="connectivity-details">
                                    <h5>South City Mall</h5>
                                    <p>Retail &amp; Dining hub</p>
                                </div>
                                <span class="connectivity-time">12 Mins</span>
                            </div>
                        </div>

                        <div class="col-md-6 col-12">
                            <div class="connectivity-card">
                                <div class="connectivity-icon"><i class="fa fa-hospital"></i></div>
                                <div class="connectivity-details">
                                    <h5>CMRI &amp; BP Poddar</h5>
                                    <p>Super-speciality care</p>
                                </div>
                                <span class="connectivity-time">10 Mins</span>
                            </div>
                        </div>

                        <div class="col-md-6 col-12">
                            <div class="connectivity-card">
                                <div class="connectivity-icon"><i class="fa fa-graduation-cap"></i></div>
                                <div class="connectivity-details">
                                    <h5>MP Birla &amp; LSA</h5>
                                    <p>Top Kolkata schools</p>
                                </div>
                                <span class="connectivity-time">8 Mins</span>
                            </div>
                        </div>

                        <div class="col-md-6 col-12">
                            <div class="connectivity-card">
                                <div class="connectivity-icon"><i class="fa fa-plane"></i></div>
                                <div class="connectivity-details">
                                    <h5>Kolkata Airport</h5>
                                    <p>Via Maa / EM Bypass</p>
                                </div>
                                <span class="connectivity-time">45 Mins</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Insert Location section after Highlights section
html = re.sub(r'(</section>\s*(?:<!--\s*highlight-1\s*-->)?\s*<section class="gallery)', location_section_html + r'\n\1', html, count=1)

# 8. Create Reviews Section and Godrej Projects in Kolkata Section (place after Gallery)
reviews_and_projects_html = """
    <!-- Godrej Blue Kolkata Reviews Section -->
    <section class="reviews-section" id="reviews">
        <div class="container">
            <div class="section-title text-center">
                <span class="section-title__tagline">Buyer Satisfaction &amp; Trust</span>
                <h2 class="section-title__title">Godrej Blue Kolkata Reviews</h2>
                <p class="mt-3 text-muted" style="max-width: 750px; margin: 0 auto; font-size: 16px;">
                    Read genuine feedback and impressions from prospective homeowners and verified buyers who reviewed the master plan, amenities, and location of Godrej Blue.
                </p>
            </div>

            <div class="row mt-5">
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="review-card">
                        <div>
                            <div class="review-stars">
                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                            </div>
                            <p class="review-text">
                                "We had been evaluating several new launch apartments south Kolkata, but Godrej Blue on BL Saha Road clearly stands apart. The pondside clubhouse, vehicle-free podium, and thoughtful 3 BHK floor plan layout won our family over. Highly satisfied with the transparency."
                            </p>
                        </div>
                        <div class="review-author">
                            <div class="author-avatar">AB</div>
                            <div class="author-info">
                                <h6>Anirban Banerjee</h6>
                                <span>Verified Buyer, New Alipore</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="review-card">
                        <div>
                            <div class="review-stars">
                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                            </div>
                            <p class="review-text">
                                "Looking for 3 BHK flats in New Alipore Kolkata was tedious until our Godrej Blue Kolkata site visit. The sales team patiently explained the Godrej Blue Kolkata price breakdown, floor plan options, and the 1% payment plan. Best luxury project in South Kolkata!"
                            </p>
                        </div>
                        <div class="review-author">
                            <div class="author-avatar">RS</div>
                            <div class="author-info">
                                <h6>Pooja &amp; Rahul Sengupta</h6>
                                <span>Homeowners (Tower 2)</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="review-card">
                        <div>
                            <div class="review-stars">
                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                            </div>
                            <p class="review-text">
                                "From an investment perspective, having clear Godrej Blue Kolkata RERA certification (WBRERA/P/KOL/2024/002211) and a confirmed possession date gave me complete peace of mind. Godrej Properties projects in Kolkata consistently deliver premium rental yields."
                            </p>
                        </div>
                        <div class="review-author">
                            <div class="author-avatar">DR</div>
                            <div class="author-info">
                                <h6>Debashis Roy</h6>
                                <span>Real Estate Investor</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Call to Action Banner -->
            <div class="text-center mt-4">
                <button type="button" class="thm-btn" style="background:#076291; margin-right:12px; margin-bottom:10px;" data-bs-toggle="modal" data-bs-target="#popupModal">
                    Download Godrej Blue Kolkata Brochure
                </button>
                <button type="button" class="thm-btn" style="background:#002d45; margin-bottom:10px;" data-bs-toggle="modal" data-bs-target="#popupModal">
                    Book An Exclusive Site Visit
                </button>
            </div>
        </div>
    </section>

    <!-- Godrej Properties Projects in Kolkata Section -->
    <section class="projects-section" id="projects">
        <div class="container">
            <div class="section-title text-center">
                <span class="section-title__tagline">Proven Heritage &amp; Landmarks</span>
                <h2 class="section-title__title">Godrej Properties Projects in Kolkata</h2>
                <p class="mt-3 text-muted" style="max-width: 750px; margin: 0 auto; font-size: 16px;">
                    Godrej Properties brings over 127 years of trust, excellence, and landmark developments across Kolkata's prime residential and commercial corridors.
                </p>
            </div>

            <div class="row mt-5">
                <div class="col-lg-3 col-md-6 mb-4">
                    <div class="project-item-box">
                        <span class="project-tag">New Launch</span>
                        <h4>Godrej Blue</h4>
                        <p><strong>Location:</strong> BL Saha Road, New Alipore, South Kolkata</p>
                        <p>Luxury 2, 3 &amp; 4 BHK waterfront residences overlooking calm waters with 50+ world-class amenities.</p>
                        <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" style="color:#076291; font-weight:700; font-size:13px; text-decoration:none;">Enquire Now &rarr;</a>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 mb-4">
                    <div class="project-item-box">
                        <span class="project-tag" style="background:#fef3c7; color:#92400e;">Delivered Township</span>
                        <h4>Godrej Prakriti</h4>
                        <p><strong>Location:</strong> BT Road, Sodepur, North Kolkata</p>
                        <p>Expansive 22-acre riverside residential township with lush greenery, healthcare, and club facilities.</p>
                        <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" style="color:#076291; font-weight:700; font-size:13px; text-decoration:none;">View Details &rarr;</a>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 mb-4">
                    <div class="project-item-box">
                        <span class="project-tag" style="background:#e0f2fe; color:#0369a1;">Ready / Ongoing</span>
                        <h4>Godrej Seven</h4>
                        <p><strong>Location:</strong> Joka, Diamond Harbour Road, South Kolkata</p>
                        <p>Gated community homes built around 7 pillars of wellness with easy metro connectivity.</p>
                        <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" style="color:#076291; font-weight:700; font-size:13px; text-decoration:none;">View Details &rarr;</a>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 mb-4">
                    <div class="project-item-box">
                        <span class="project-tag" style="background:#f3e8ff; color:#7e22ce;">Commercial Hub</span>
                        <h4>Godrej Waterside &amp; Genesis</h4>
                        <p><strong>Location:</strong> Sector V, Salt Lake, Kolkata</p>
                        <p>Grade-A sustainable IT park and commercial office towers hosting multinational tech corporations.</p>
                        <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" style="color:#076291; font-weight:700; font-size:13px; text-decoration:none;">View Details &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Insert Reviews and Projects sections after Gallery section
html = re.sub(r'(</section>\s*(?:<!--\s*gallery\s*-->)?\s*<section class="about-godrej)', reviews_and_projects_html + r'\n\1', html, count=1)

# 9. Expand and Update FAQs with targeted questions covering every keyword
new_faqs_html = """
<section class="faq-section section-padding" id="faq">
    <div class="container">
        <div class="section-title text-center">
            <span class="section-title__tagline">Got Questions?</span>
            <h2 class="section-title__title">Frequently Asked Questions</h2>
            <p class="mt-3 text-muted" style="max-width: 750px; margin: 0 auto; font-size: 16px;">
                Find verified answers about Godrej Blue Kolkata price, floor plan, location, RERA registration, amenities, payment plan, and site visit booking.
            </p>
        </div>

        <div class="faq-accordion mt-5">

            <div class="faq-item active">
                <button class="faq-question">
                    1. What is the Godrej Blue Kolkata price for 2 BHK and 3 BHK apartments?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata price</strong> starts from ₹1.15 Cr* onwards for 2 BHK luxury homes and from ₹1.55 Cr* onwards for spacious <strong>3 BHK flats in New Alipore Kolkata</strong>. For detailed <strong>godrej blue kolkata 2 bhk / 3 bhk price</strong> sheets including car parking, floor rise, and GST breakdowns, you can request an instant cost sheet via our enquiry form.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    2. Where can I download the Godrej Blue Kolkata floor plan and master layout?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>You can view and download the official <strong>godrej blue kolkata floor plan</strong> PDF by clicking the "Download Brochure" or "View Floor Plan" buttons on this page. The floor plans feature thoughtfully engineered layouts for 2 BHK, 3 BHK, and 4 BHK residences with optimal carpet area utilization, cross ventilation, and scenic pondside views.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    3. What is the exact Godrej Blue Kolkata location and connectivity?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata location</strong> is 82/1, BL Saha Road, New Alipore, South Kolkata - 700053. It enjoys quick access to Tollygunge Metro Station (7 mins), New Alipore Railway Station (5 mins), South City Mall (12 mins), CMRI &amp; BP Poddar Hospitals (10 mins), and top educational institutions, making it the most coveted address among <strong>new launch apartments south Kolkata</strong>.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    4. What is the Godrej Blue Kolkata possession date and RERA registration number?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata possession date</strong> is scheduled starting from December 2028 as per the official regulatory timeline. The project is completely approved and registered under West Bengal RERA with <strong>godrej blue kolkata RERA</strong> number: <strong>WBRERA/P/KOL/2024/002211</strong>. Prospective buyers can verify all project sanctions online on the official WBRERA portal.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    5. What are the key Godrej Blue Kolkata amenities available for residents?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata amenities</strong> encompass over 50+ hand-picked lifestyle features organized across Pondside, Clubhouse, and Podium zones. Highlights include a grand infinity-edge swimming pool, lakeside deck, modern gymnasium, squash &amp; badminton courts, yoga pavilion, banquet hall, children's play park, senior citizen lawns, and 24/7 high-tech security.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    6. How does the Godrej Blue Kolkata payment plan work?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>The <strong>godrej blue kolkata payment plan</strong> includes the attractive Godrej 1% Monthly Payment Plan for eligible homebuyers as well as standard Construction-Linked Payment Plans (CLP). Buyers can book with a nominal booking token and pay conveniently linked to construction milestones, supported by leading home loan partners (SBI, HDFC, ICICI, Axis Bank).</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    7. How can I book a Godrej Blue Kolkata site visit and get the brochure?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>To schedule your private <strong>godrej blue kolkata site visit</strong>, simply enter your name, email, and phone number in the contact form or modal. Our sales advisors will arrange an exclusive sample flat tour, complimentary cab pickup, and instantly email you the official <strong>godrej blue kolkata brochure</strong>.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    8. What do Godrej Blue Kolkata reviews highlight about the property?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>Verified <strong>godrej blue kolkata reviews</strong> consistently praise the serene waterfront concept, large open green spaces, unmatched connectivity in New Alipore, and the trust associated with Godrej Properties. Reviewers note that compared to other options in South Kolkata, Godrej Blue offers far superior amenities and long-term appreciation potential.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    9. Why are 3 BHK flats in New Alipore Kolkata at Godrej Blue high in demand?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p><strong>3 BHK flats in New Alipore Kolkata</strong> are in strong demand due to the established residential charm, high safety, elite schools, and robust infrastructure of New Alipore. Godrej Blue meets this demand with expansive 3 BHK layouts with private balconies overlooking peaceful water features, rarely found in central urban Kolkata.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">
                    10. What other Godrej Properties projects in Kolkata are there?
                    <span>+</span>
                </button>
                <div class="faq-answer">
                    <p>Other notable <strong>Godrej Properties projects in Kolkata</strong> include Godrej Prakriti (a 22-acre riverside township on BT Road, Sodepur), Godrej Seven (luxury residences in Joka, Diamond Harbour Road), and premier commercial developments such as Godrej Waterside and Godrej Genesis in Salt Lake Sector V.</p>
                </div>
            </div>

        </div>
    </div>
</section>
"""

# Replace the existing FAQ section with the new expanded FAQs
html = re.sub(r'<section class="faq-section[\s\S]*?</section>', new_faqs_html, html, count=1)

# 10. Update Footer with SEO keyword badge cloud & disclaimer enrichment
footer_seo_block = """
                    <div class="col-lg-12 mt-4 pt-3" style="border-top: 1px solid rgba(255,255,255,0.1);">
                        <p style="font-size:12px; color:rgba(255,255,255,0.5); line-height:1.8; margin-bottom:5px;">
                            <strong>Popular Searches:</strong> 
                            <a href="#pricing" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata price</a> | 
                            <a href="#pricing" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata floor plan</a> | 
                            <a href="#location" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata location</a> | 
                            <a href="#pricing" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata possession date</a> | 
                            <a href="#footer" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata RERA</a> | 
                            <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata brochure</a> | 
                            <a href="#pricing" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata 2 bhk / 3 bhk price</a> | 
                            <a href="#highlights" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata amenities</a> | 
                            <a href="#reviews" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata reviews</a> | 
                            <a href="#popupModal" data-bs-toggle="modal" data-bs-target="#popupModal" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata site visit</a> | 
                            <a href="#pricing" style="color:rgba(255,255,255,0.6); text-decoration:none;">godrej blue kolkata payment plan</a> | 
                            <a href="#pricing" style="color:rgba(255,255,255,0.6); text-decoration:none;">3 bhk flats in New Alipore Kolkata</a> | 
                            <a href="#overview" style="color:rgba(255,255,255,0.6); text-decoration:none;">new launch apartments south Kolkata</a> | 
                            <a href="#projects" style="color:rgba(255,255,255,0.6); text-decoration:none;">Godrej Properties projects in Kolkata</a>
                        </p>
                    </div>
"""

# Insert before disclaimer-box
html = re.sub(r'(<div class="col-lg-12">\s*<div class="disclaimer-box">)', footer_seo_block + r'\n\1', html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with all keywords and luxury sections!")

