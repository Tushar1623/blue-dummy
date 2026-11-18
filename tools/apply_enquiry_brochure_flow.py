import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update toggle-sidebar to have modal attributes
html = html.replace(
    '<div class="toggle-sidebar">',
    '<div class="toggle-sidebar" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="enquire" role="button" tabindex="0" title="Click to Enquire">'
)

# 2. Add header Enquire Now button in main-menu__wrapper-inner
header_target = '<div class="main-menu__left">'
header_replacement = """<div class="d-none d-lg-flex align-items-center ms-auto me-3">
                            <a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="enquire" class="thm-btn header-enquire-btn" style="background:#076291; color:#fff; padding:9px 24px; font-size:13px; border-radius:4px; font-weight:600; text-transform:uppercase;">Enquire Now</a>
                        </div>
                        <div class="main-menu__left">"""

if 'header-enquire-btn' not in html:
    html = html.replace(header_target, header_replacement, 1)
    print("Added header Enquire Now button")

# 3. Add CTAs in Overview section
overview_cta_target = 'Timeless elegance, and landmark lifestyle.\n                                    </p>'
overview_cta_replacement = """Timeless elegance, and landmark lifestyle.
                                    </p>
                                    <div class="about-one__btn-box mt-4">
                                        <a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="brochure" class="thm-btn" style="background:#076291; color:#fff; margin-right:15px; margin-bottom:10px;"><i class="fa fa-download me-2"></i>Download Brochure</a>
                                        <a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="enquire" class="thm-btn" style="background:#002d45; color:#fff; margin-bottom:10px;"><i class="fa fa-envelope me-2"></i>Enquire Now</a>
                                    </div>"""

if 'about-one__btn-box' not in html:
    html = html.replace(overview_cta_target, overview_cta_replacement, 1)
    print("Added overview CTAs")

# 4. Add CTAs in Highlights section
highlights_cta_target = '</div>\n            <section class="gallery'
highlights_cta_replacement = """<div class="text-center mt-5 mb-3">
                <a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="enquire" class="thm-btn" style="background:#076291; color:#fff; margin-right:15px; margin-bottom:10px;"><i class="fa fa-phone-alt me-2"></i>Schedule Site Visit &amp; Enquiry</a>
                <a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#popupModal" data-id="brochure" class="thm-btn" style="background:#002d45; color:#fff; margin-bottom:10px;"><i class="fa fa-download me-2"></i>Download Project Brochure</a>
            </div>
        </div>
    </section>
    <section class="gallery"""

if 'Schedule Site Visit &amp; Enquiry' not in html:
    html = re.sub(r'</div>\s*</section>\s*<section class="gallery', highlights_cta_replacement, html, count=1)
    print("Added highlights CTAs")

# 5. Ensure modal controller handles all clicks cleanly
controller_script = """
    <!-- Modal Dynamic State Controller: Download Brochure vs Enquiry -->
    <script>
        $(document).ready(function() {
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
            $(document).on('click', '.brochure_cta, [data-id="brochure"], [data-action="brochure"], a:contains("Download Brochure"), button:contains("Download Brochure"), a:contains("Download Project Brochure")', function(e) {
                setupModal('brochure');
            });

            // Click listener for any enquiry button
            $(document).on('click', '.enquire-btn, .toggle-sidebar, .mob-enquire, .header-enquire-btn, [data-id="enquire"], [data-action="enquire"], a:contains("Enquire"), button:contains("ENQUIRE"), a:contains("Schedule Site Visit")', function(e) {
                setupModal('enquiry');
            });

            // Reset modal on close
            $(document).on('click', '.btn-close, [data-bs-dismiss="modal"]', function() {
                setupModal('enquiry');
            });
        });
    </script>
"""

# Replace existing controller script if present or append before </body>
if 'Modal Dynamic State Controller' in html:
    html = re.sub(r'<!-- Modal Dynamic State Controller[\s\S]*?</script>', controller_script.strip(), html, count=1)
    print("Updated modal controller script")
else:
    html = html.replace('</body>', controller_script + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully!")

