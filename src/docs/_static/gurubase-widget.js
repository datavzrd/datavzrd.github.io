document.addEventListener('DOMContentLoaded', function() {
    // Load the GuruBase widget
    const guruScript = document.createElement("script");
    guruScript.src = "https://widget.gurubase.io/widget.latest.min.js";
    guruScript.defer = true;
    guruScript.id = "guru-widget-id";

    // Add widget settings as data attributes
    Object.entries({
        "data-widget-id": "ao3Yf4RcOguLV7ecYB9L4_9eLe-eOk8LYUkx3xa9lIQ",
        "data-text": "Ask AI",
        "data-overlap-content": "false"
    }).forEach(([key, value]) => {
        guruScript.setAttribute(key, value);
    });

    // Append the script to the document
    document.body.appendChild(guruScript);
});
