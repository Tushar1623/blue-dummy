const countryMap = {
  al: "Albania",
  dz: "Algeria",
  ao: "Angola",
  ar: "Argentina",
  am: "Armenia",
  au: "Australia",
  at: "Austria",
  az: "Azerbaijan",
  bs: "Bahamas",
  bh: "Bahrain",
  bd: "Bangladesh",
  by: "Belarus",
  be: "Belgium",
  bj: "Benin",
  bm: "Bermuda",
  bo: "Bolivia",
  ba: "Bosnia-Herz.",
  bw: "Botswana",
  br: "Brazil",
  bg: "Bulgaria",
  ca: "Canada",
  cb: "Caribbean Nations",
  cl: "Chile",
  cn: "China",
  co: "Colombia",
  ck: "Cook Islands",
  cr: "Costa Rica",
  hr: "Croatia",
  cy: "Cyprus",
  cz: "Czech Republic",
  dk: "Denmark",
  do: "Dominican Republic",
  ec: "Ecuador",
  eg: "Egypt",
  sv: "El Salvador",
  gq: "Equatorial Guinea",
  ee: "Estonia",
  et: "Ethiopia",
  fo: "Faroe Islands",
  fm: "Federated States of Micronesia",
  fi: "Finland",
  fr: "France",
  pf: "French Polynesia",
  ga: "Gabon",
  gm: "Gambia",
  ge: "Georgia",
  de: "Germany",
  gh: "Ghana",
  gi: "Gibraltar",
  gr: "Greece",
  gl: "Greenland",
  gt: "Guatemala",
  hn: "Honduras",
  hk: "Hong Kong",
  hu: "Hungary",
  is: "Iceland",
  in: "India",
  id: "Indonesia",
  ir: "Iran",
  iq: "Iraq",
  ie: "Ireland",
  il: "Israel",
  it: "Italy",
  jp: "Japan",
  jo: "Jordan",
  kz: "Kazakhstan",
  ke: "Kenya",
  kr: "Korea",
  kw: "Kuwait",
  kg: "Kyrgyzstan",
  lv: "Latvia",
  lb: "Lebanon",
  li: "Liechtenstein",
  lt: "Lithuania",
  lu: "Luxembourg",
  mk: "Macedonia",
  mg: "Madagascar",
  my: "Malaysia",
  mt: "Malta",
  mu: "Mauritius",
  mx: "Mexico",
  md: "Moldova",
  ma: "Morocco",
  na: "Namibia",
  np: "Nepal",
  nl: "Netherlands",
  an: "Netherlands Antilles",
  nz: "New Zealand",
  ni: "Nicaragua",
  ng: "Nigeria",
  no: "Norway",
  oo: "Other",
  pa: "Panama",
  pe: "Peru",
  ph: "Philippines",
  pl: "Poland",
  pt: "Portugal",
  qa: "Qatar",
  ro: "Romania",
  ru: "Russian Federation",
  sa: "Saudi Arabia",
  cs: "Serbia and Montenegro",
  sg: "Singapore",
  sk: "Slovak Republic",
  si: "Slovenia",
  za: "South Africa",
  es: "Spain",
  lk: "Sri Lanka",
  om: "Sultanate of Oman",
  se: "Sweden",
  ch: "Switzerland",
  sy: "Syria",
  tw: "Taiwan",
  tz: "Tanzania",
  th: "Thailand",
  tl: "Timor-Leste",
  tg: "Togo",
  tt: "Trinidad and Tobago",
  tn: "Tunisia",
  tr: "Turkey",
  ug: "Uganda",
  ua: "Ukraine",
  gb: "United Kingdom",
  uy: "Uruguay",
  us: "USA",
  ae: "Utd.Arab Emir.",
  uz: "Uzbekistan",
  ve: "Venezuela",
  vn: "Vietnam",
  ye: "Yemen",
  yu: "Yugoslavia",
  zw: "Zimbabwe",
};

async function getUserIp() {
  try {
    const response = await fetch("https://api.ipify.org?format=json");
    const data = await response.json();
    return data.ip;
  } catch (error) {
    console.error("Unable to fetch IP:", error);
    return "";
  }
}

/* ================================
   GLOBAL STATE
================================ */
let selectedAction = {
  type: "",
  file: ""
};



/* ================================
   CTA CLICK TRACK
================================ */
document.addEventListener("click", function (e) {
  const btn = e.target.closest(".enquirelink, .brochure_cta");

  if (btn) {
    selectedAction.type = btn.dataset.type || btn.dataset.id || "";
    selectedAction.file = btn.dataset.file || selectedAction.type;


    document.getElementById("fixedEnqFrm")?.classList.add("active");
  }
});

/* ================================
   POPUP CLOSE RESET
================================ */
const popup = document.getElementById("fixedEnqFrm");
const closeBtn = document.querySelector(".enquiryFormClose");

closeBtn?.addEventListener("click", () => {
  popup?.classList.remove("active");
  selectedAction = { type: "", file: "" };
  
});

/* ================================
   FORM INIT
================================ */
document.querySelectorAll('form[class*="frmContactus"]').forEach((form) => {

  form.setAttribute("novalidate", "novalidate");
  
  const nameInput = form.querySelector(`[name="txt_firstname"]`);
  const phoneInput = form.querySelector(`[name="txt_mobile"]`);
  const emailInput = form.querySelector(`[name="txt_email"]`);
  const countryInput = form.querySelector(`[name="txt_country"]`);
  const passwordInput = form.querySelector('[name="password"], [name="txt_password"], #password');
  const confirmPasswordInput = form.querySelector('[name="confirm_password"], [name="txt_confirm_password"], #confirm_password');

  const nameError = form.querySelector(".name-error");
  const phoneError = form.querySelector(".phone-error");
  const emailError = form.querySelector(".email-error");
  const countryError = form.querySelector(".country-error");
  const passwordError = form.querySelector(".password-error");
  const confirmPasswordError = form.querySelector(".confirm-password-error");

  nameInput?.setAttribute("autocomplete", "name");
  phoneInput?.setAttribute("inputmode", "numeric");

  const getSelectedCountry = () => iti?.getSelectedCountryData()?.iso2 || countryInput?.value || "";

  const getSelectedDialCode = () => iti?.getSelectedCountryData()?.dialCode || "";

  const getLocalPhone = (value = phoneInput?.value || "") => {
    let digits = value.replace(/\D/g, "");
    const countryCode = getSelectedCountry();
    const dialCode = getSelectedDialCode();

    if (countryCode === "in" && digits.length === 12 && digits.startsWith("91")) {
      digits = digits.slice(2);
    } else if (dialCode && digits.length > 10 && digits.startsWith(dialCode)) {
      digits = digits.slice(dialCode.length);
    }

    return digits;
  };

  const syncPhoneInput = (value = phoneInput?.value || "") => {
    const localPhone = getLocalPhone(value);

    if (phoneInput && phoneInput.value !== localPhone) {
      phoneInput.value = localPhone;
    }

    return localPhone;
  };

  /* ================================
     PHONE INIT
  ================================= */
  let iti = null;

  if (window.intlTelInput && phoneInput) {
    iti = window.intlTelInputGlobals?.getInstance(phoneInput);

    if (!iti) {
      iti = window.intlTelInput(phoneInput, {
      initialCountry: "in",
      separateDialCode: true,
      preferredCountries: ["in", "us", "gb"],
      useFullscreenPopup: false,
      utilsScript:
        "https://cdn.jsdelivr.net/npm/intl-tel-input@18.1.1/build/js/utils.js",
      });
    }

    
  } else {
    
  }

  function showError(el, msg) {
    if (el) el.innerText = msg;
  }

  function clearErrors() {
    [nameError, phoneError, emailError, countryError, passwordError, confirmPasswordError].forEach((el) => {
      if (el) {
        el.innerText = "";
        el.classList.add("hide");
      }
    });

    [nameInput, phoneInput, emailInput, countryInput, passwordInput, confirmPasswordInput].forEach((input) => {
      if (input) {
        input.classList.remove("is-invalid", "is-valid");
      }
    });
  }

  function validate() {
  let valid = true;

  const rawPhone = phoneInput?.value.replace(/\D/g, "");
  const countryCode = iti?.getSelectedCountryData()?.iso2;

  if (!nameInput?.value.trim()) {
    showError(nameError, "Enter your name");
    valid = false;
  }

  if (!rawPhone) {
    showError(phoneError, "Enter phone number");
    valid = false;
  } 
  else {
    // ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« block fake numbers

    // same digits (111111, 999999)
    if (/^(\d)\1+$/.test(rawPhone)) {
      showError(phoneError, "Invalid phone number");
      valid = false;
    }

    // sequential numbers
    if (
      "0123456789".includes(rawPhone) ||
      "9876543210".includes(rawPhone)
    ) {
      showError(phoneError, "Invalid phone number");
      valid = false;
    }

    // length safety
    if (rawPhone.length < 6 || rawPhone.length > 15) {
      showError(phoneError, "Invalid phone number");
      valid = false;
    }

    // ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡Ãƒâ€šÃ‚Â®ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡Ãƒâ€šÃ‚Â³ India strict
    if (countryCode === "in" && !/^[6-9]\d{9}$/.test(rawPhone)) {
      showError(phoneError, "Enter valid Indian mobile number");
      valid = false;
    }
  }

  if (
    !emailInput?.value.trim() ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)
  ) {
    showError(emailError, "Enter valid email");
    valid = false;
  }

  
  return valid;
}

  const setFieldState = (input, errorEl, message) => {
    if (!input) return true;

    const hasValue = input.type === "checkbox" ? input.checked : input.value.trim() !== "";
    const isValid = !message;

    input.classList.toggle("is-invalid", !isValid);
    input.classList.toggle("is-valid", isValid && hasValue);

    if (errorEl) {
      errorEl.textContent = message;
      errorEl.classList.toggle("hide", !message);
    }

    return isValid;
  };

  const getRequiredError = (input) => {
    if (!input || input.disabled || input.type === "hidden") return "";
    if (input.type === "checkbox") return input.checked || !input.required ? "" : "Required";
    return input.value.trim() ? "" : "Required";
  };

  const validateName = () => {
    const value = nameInput?.value.trim() || "";
    let message = getRequiredError(nameInput);

    if (!message && !/^[A-Za-z]+(?: [A-Za-z]+)*$/.test(value)) {
      message = "Only alphabets and spaces allowed";
    }

    return setFieldState(nameInput, nameError, message);
  };

  const validateEmail = () => {
    const value = emailInput?.value.trim() || "";
    let message = getRequiredError(emailInput);

    if (!message && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value)) {
      message = "Enter valid email";
    }

    return setFieldState(emailInput, emailError, message);
  };

  const validateCountry = () =>
    setFieldState(countryInput, countryError, getRequiredError(countryInput));

  const validatePhone = () => {
    const rawPhone = syncPhoneInput();
    const countryCode = getSelectedCountry();
    let message = "";

    if (!rawPhone) {
      message = "Required";
    } else if (rawPhone.length < 6 || rawPhone.length > 15) {
      message = "Invalid phone number";
    } else if (/^(\d)\1+$/.test(rawPhone)) {
      message = "Invalid phone number";
    } else if ("0123456789".includes(rawPhone) || "9876543210".includes(rawPhone)) {
      message = "Invalid phone number";
    } else if (countryCode === "in" && !/^[6-9]\d{9}$/.test(rawPhone)) {
      message = "Enter valid Indian mobile number";
    }

    return setFieldState(phoneInput, phoneError, message);
  };

  const validatePassword = () => {
    if (!passwordInput) return true;

    const value = passwordInput.value;
    let message = getRequiredError(passwordInput);

    if (!message && value.length < 8) {
      message = "Password must be at least 8 characters";
    } else if (!message && !/(?=.*[A-Za-z])(?=.*\d)/.test(value)) {
      message = "Password must include letters and numbers";
    }

    return setFieldState(passwordInput, passwordError, message);
  };

  const validateConfirmPassword = () => {
    if (!confirmPasswordInput) return true;

    const value = confirmPasswordInput.value;
    let message = getRequiredError(confirmPasswordInput);

    if (!message && passwordInput && value !== passwordInput.value) {
      message = "Passwords do not match";
    }

    return setFieldState(confirmPasswordInput, confirmPasswordError, message);
  };

  function validate() {
    return [
      validateName(),
      validateEmail(),
      validateCountry(),
      validatePhone(),
      validatePassword(),
      validateConfirmPassword(),
    ].every(Boolean);
  }

  nameInput?.addEventListener("beforeinput", (e) => {
    if (e.data && !/^[A-Za-z ]+$/.test(e.data)) {
      e.preventDefault();
    }
  });

  nameInput?.addEventListener("input", () => {
    nameInput.value = nameInput.value.replace(/[^A-Za-z ]+/g, "").replace(/\s{2,}/g, " ");
    validateName();
  });

  emailInput?.addEventListener("input", validateEmail);
  countryInput?.addEventListener("change", () => {
    if (iti && countryInput.value) {
      iti.setCountry(countryInput.value);
    }

    validateCountry();
    validatePhone();
  });

  phoneInput?.addEventListener("input", () => {
    syncPhoneInput();
    validatePhone();
  });

  phoneInput?.addEventListener("countrychange", () => {
    const countryData = iti?.getSelectedCountryData();
    const countryCodeField = form.querySelector(`[name="txt_countrycode"]`);

    if (countryData) {
      if (countryInput) countryInput.value = countryData.iso2;
      if (countryCodeField) countryCodeField.value = `+${countryData.dialCode}`;
    }

    validateCountry();
    validatePhone();
  });

  passwordInput?.addEventListener("input", () => {
    validatePassword();
    validateConfirmPassword();
  });

  confirmPasswordInput?.addEventListener("input", validateConfirmPassword);

  /* ================================
     FORM SUBMIT
  ================================= */
  form.addEventListener("submit", function (e) {
    e.preventDefault();

   

    clearErrors();

    if (!validate()) {
      
      return;
    }

    
    // BROCHURE INJECTION
    const downloadField = form.querySelector('[name="download_file_type"]');

    if (downloadField) {
      if (selectedAction.type === "brochure") {
        downloadField.value = selectedAction.file || "brochure";
      }
    }

    // COUNTRY CODE
    const countryCodeField = form.querySelector(`[name="txt_countrycode"]`);
    if (countryCodeField && iti) {
      countryCodeField.value =
        "+" + iti.getSelectedCountryData().dialCode;
    }

    syncPhoneInput();

    submit(form, iti);
  });
});

/* ================================
   SUBMIT FUNCTION
================================ */
const submit = async (form, iti) => {
  const subBtn = form.querySelector(".btnSubmitContactForm, button[type='submit'], input[type='submit'], button");
  let shouldRestoreSubmit = true;

  const setSubmitLocked = (isLocked) => {
    if (!subBtn) return;

    if (isLocked) {
      form.dataset.submitting = "true";
      subBtn.dataset.submitting = "true";
      subBtn.dataset.originalText = subBtn.innerText || subBtn.value || "SUBMIT";

      if ("disabled" in subBtn) {
        subBtn.disabled = true;
      }

      subBtn.setAttribute("aria-disabled", "true");
      subBtn.classList.add("disabled", "loading");

      if ("value" in subBtn) {
        subBtn.value = "Submitting...";
      } else {
        subBtn.innerText = "Submitting...";
      }
    } else {
      form.dataset.submitting = "false";
      subBtn.dataset.submitting = "false";

      if ("disabled" in subBtn) {
        subBtn.disabled = false;
      }

      subBtn.setAttribute("aria-disabled", "false");
      subBtn.classList.remove("disabled", "loading");

      if ("value" in subBtn) {
        subBtn.value = subBtn.dataset.originalText || "SUBMIT";
      } else {
        subBtn.innerText = subBtn.dataset.originalText || "SUBMIT";
      }
    }
  };

  if (form.dataset.submitting === "true" || subBtn?.dataset.submitting === "true") {
    return;
  }

  try {
    setSubmitLocked(true);

    const name = form.querySelector(`[name="txt_firstname"]`).value.trim();
  const nameArr = name.split(" ");
  const lastName = nameArr.pop();
  const firstName = nameArr.join(" ");
  const email = form.querySelector(`[name="txt_email"]`).value;
  let phone = form.querySelector(`[name="txt_mobile"]`).value.replace(/\D/g, "");
  const countryCode = form.querySelector(`[name="txt_countrycode"]`).value;
  const dialCodeDigits = countryCode.replace(/\D/g, "");

  if (dialCodeDigits && phone.startsWith(dialCodeDigits) && phone.length > 10) {
    phone = phone.slice(dialCodeDigits.length);
  }
  const country =
    countryMap?.[form.querySelector(`[name="txt_country"]`)?.value] || "India";
  const prjcode = form.querySelector(`[name="projid"]`).value;
  //   const addCode = form.querySelector(`[name="Campaign_ID"]`).value;
  const urlParams = new URLSearchParams(window.location.search);
  const url = new URL(window.location.href);
url.searchParams.delete("busted");
url.hash = "";
const originalUrl =
  url.origin + url.pathname + (url.search ? url.search : "");
  const ipAddress = await getUserIp();
  const addCode =
    urlParams.get("campid") || form.querySelector(`[name="Campaign_ID"]`).value;
  const websiteName =
  form.querySelector(`[name="WEB_URL"]`).value || window.location.href;
  const optIn = form.querySelector(`[name="whatsapp_check"]`)?.checked
    ? "Yes"
    : "No";
  const download =
    form.querySelector('[name="download_file_type"]')?.value || "";

    if (!prjcode || !addCode) {
      setSubmitLocked(false);
      return;
    }

    const payload = {
      download_file_type: download,
      formData: {
        firstName,
        lastName,
        email,
        propertyType: "",
        dateTime: new Date().toISOString(),
        property: {
          projCode: prjcode,
          addCode,
          url: websiteName,
        },
        phone,
        countryCode,
        country,
        optIn,
        OrganicCampagnID: "",
        websiteName: originalUrl,
      googleGCLID: originalUrl,
      landingPageURL: originalUrl,
      userIPAddress: ipAddress,
      },
    };

    fetch("/api/enquiry", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then((res) => {
       
        return res.json();
      })
      .then((result) => {
        

        const leadId = result?.Id || result?.leadId || result?.[0]?.Id || "LEAD_" + Date.now();

        const baseUrl =
          window.location.origin +
          window.location.pathname.replace(/[^/]*$/, "");


        let redirect =
          baseUrl +
          "thankyou.html?sub_id=" +
          leadId;

        if (download) {
          redirect += "&brochure=" + download;
        }

        if (selectedAction.type === "direction") {
          redirect += "&direction=1";
        }

        

        

        shouldRestoreSubmit = false;
        window.location.href = redirect;

        selectedAction = { type: "", file: "" };
      })
      .catch((err) => {
        console.warn("API request fallback:", err);
        const baseUrl =
          window.location.origin +
          window.location.pathname.replace(/[^/]*$/, "");

        let redirect =
          baseUrl +
          "thankyou.html?sub_id=DEMO" +
          Math.floor(100000 + Math.random() * 900000);

        if (download) {
          redirect += "&brochure=" + download;
        }

        if (selectedAction.type === "direction") {
          redirect += "&direction=1";
        }

        shouldRestoreSubmit = false;
        window.location.href = redirect;

        selectedAction = { type: "", file: "" };
      })
      .finally(() => {
        if (shouldRestoreSubmit) {
          setSubmitLocked(false);
        }
      });

  } catch (err) {
    setSubmitLocked(false);
  }
};
