/* Sets map */
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 51.5074, lng: -0.1278 },
        zoom: 5,
    });
     /* Array of contents */
    let UKParks = [
        {
            coordinates: { lat: 53.3342 , lng: -1.7837 },
            content:'<p>Peak District<p>'
        },
        {
            coordinates: { lat: 53.0932 , lng: -3.8017 },
            content:'<p>Snowdonia</p>'
        },
        {
            coordinates: { lat: 50.5719 , lng: -3.9207 },
            content:'<p>Dartmoor<p>'
        },
        {
            coordinates: { lat: 54.4609 , lng: -3.0886 },
            content:'<p>Lake District<p>'
        }
    ];
    /* Info Window */
    let infoWindow = new google.maps.InfoWindow();
        for (let i = 0; i < UKParks.length; i++) {
        setParks(UKParks[i]);
        }
    /* Set Content to Markers */
  function setParks(props) {
    let marker = new google.maps.Marker({
      position: props.coordinates,
      map: map,
      animation: google.maps.Animation.DROP
    });
    /* Add Click Listener */
    marker.addListener("click", function () {
      infoWindow.setContent(props.content);
      infoWindow.open(map, marker);
    });
  }
}
