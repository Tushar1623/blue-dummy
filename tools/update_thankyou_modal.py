with open('thankyou.html', 'r', encoding='utf-8') as f:
    t_html = f.read()

# Update download_file call in thankyou.html to use local PDF
old_js_download = """function download_pdf_new(downloadtype) {
      if (downloadtype == 'brochure') {
        download_file('https://www.godrejproperties.com/digitalcollateral/kolkata/godrej-blue/pdf/godrej-blue-project-brochure.pdf');
      }
    }"""

new_js_download = """function download_pdf_new(downloadtype) {
      if (downloadtype == 'brochure') {
        download_file('landing_page/assets/godrej_blue_brochure.pdf', 'Godrej_Blue_Kolkata_Brochure.pdf');
      }
    }"""

t_html = t_html.replace(old_js_download, new_js_download)

# Now update the modal body in thankyou.html to dynamically reflect brochure vs enquiry
old_modal_content = """<p style="color: #fff;" class="success">
                        Your enquiry has been successfully submitted. Thank you for showing interest in us. One of our
                        executives will get in touch with you.<br><br>

                        We’ll use your information to contact you about our services and products.</p>"""

new_modal_content = """<div id="thankYouEnquiryMsg">
                        <p style="color: #fff; font-size:16px; line-height:1.6;" class="success">
                            Your enquiry has been successfully submitted. Thank you for showing interest in Godrej Blue. One of our executives will get in touch with you shortly.<br><br>
                            We’ll use your information to contact you about our services and products.
                        </p>
                    </div>
                    <div id="thankYouBrochureMsg" style="display:none; text-align:center;">
                        <h4 style="color:#ffffff; margin-bottom:12px;">Thank you for your interest!</h4>
                        <p style="color: #e2e8f0; font-size:15px; line-height:1.6;">
                            Your official <strong>Godrej Blue Kolkata Brochure</strong> download will begin automatically.<br>
                            If the download doesn't start, please click the button below:
                        </p>
                        <div style="margin:25px 0 10px;">
                            <a href="landing_page/assets/godrej_blue_brochure.pdf" download="Godrej_Blue_Kolkata_Brochure.pdf" class="thm-btn" style="background:#076291; color:#fff; padding:12px 28px; border-radius:4px; font-weight:700; text-decoration:none; display:inline-block;">
                                <i class="fa fa-download me-2"></i> DOWNLOAD BROCHURE PDF
                            </a>
                        </div>
                    </div>"""

t_html = t_html.replace(old_modal_content, new_modal_content)

# Add script to toggle display based on downloadBrochure
dynamic_toggle_script = """
    <script>
        $(document).ready(function() {
            const bParam = (new URLSearchParams(window.location.search).get("brochure") || "").toLowerCase();
            const isBrochure = ["1", "true", "yes", "brochure"].includes(bParam);
            if (isBrochure) {
                $('#thankYouEnquiryMsg').hide();
                $('#thankYouBrochureMsg').show();
            } else {
                $('#thankYouEnquiryMsg').show();
                $('#thankYouBrochureMsg').hide();
            }
        });
    </script>
"""

t_html = t_html.replace('</body>', dynamic_toggle_script + '\n</body>')

with open('thankyou.html', 'w', encoding='utf-8') as f:
    f.write(t_html)

print("Updated thankyou.html successfully!")

