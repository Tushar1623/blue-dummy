const getOriginUrl = () => {
    // Get the current URL
    const currentUrl = window.location.href;

    // Create a URL object
    const url = new URL(currentUrl);

    // Extract the pathname (excluding query params)
    const pathSegments = url.pathname.split('/');

    // Remove the last segment (e.g., "thankyou.html")
    pathSegments.pop();

    // Construct the new URL
    const newUrl = `${url.origin}${pathSegments.join('/')}/`;

    // Redirect to the new URL
    window.location.href = newUrl;

    return newUrl;
}