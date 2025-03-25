// Function to dynamically load the Google Maps API
function loadMap(apiKey) {
    const script = document.createElement("script");
    script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=initMap`;
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
}

// Call the function to load the Google Maps API script
loadMap("AIzaSyC-AdsplgsFvIJEvEnhY_LIjFXvyaw2LU0");