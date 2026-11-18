window.addEventListener("load", ((forms) => {
    // Get the host (e.g., www.example.com)
    const host = window.location.hostname;

    // Get the URI (e.g., /path/to/page)
    const requestUri = window.location.pathname;

    // Combine them to form the full URL without query parameters
    const urlWithoutQuery = requestUri.split('?')[0];
    const siteurl = `${host}${urlWithoutQuery}`;

    // Define other necessary variables
    const url = window.location.href;


    forms.forEach(formName => {
        const form = document.querySelector(`.${formName}`);

        if (!form) return;

        // Set hidden input field values dynamically
        form.querySelector("#utm_campid") && (form.querySelector("#utm_campid").value = new URLSearchParams(window.location.search).get("utm_campid") || "");

        form.querySelector("#referrer_client") && (form.querySelector("#referrer_client").value = new URLSearchParams(window.location.search).get("client_name") || ""); // Replace with dynamic value if available

        form.querySelector("#Campaign_ID") && (form.querySelector("#Campaign_ID").value = new URLSearchParams(window.location.search).get("campid") || form.querySelector("#Campaign_ID").value); 

        form.querySelector("#utm_term") && (form.querySelector("#utm_term").value = new URLSearchParams(window.location.search).get("utm_term") || ""); // Replace with dynamic value if available

        form.querySelector("#utm_content") && (form.querySelector("#utm_content").value = new URLSearchParams(window.location.search).get("utm_content") || ""); // Replace with dynamic value if available

        form.querySelector("#gclid") && (form.querySelector("#gclid").value = new URLSearchParams(window.location.search).get("gclid") || ""); // Replace with dynamic value if available

        form.querySelector("#Publisher_Id") && (form.querySelector("#Publisher_Id").value = new URLSearchParams(window.location.search).get("Publisher_Id") || ""); // Replace with dynamic value if available

        form.querySelector("#WEB_URL") && (form.querySelector("#WEB_URL").value = url);
    });

}).bind(null, forms))