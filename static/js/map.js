/* Sets map */
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 51.5074, lng: -0.1278 },
        zoom: 3,
    });
     /* Array of contents */
    let UKParks = [
        {
            coordinates: { lat: 53.3342 , lng: -1.7837 },
            content: <h3>Peak District</h3>
        },
        {
            coordinates: { lat: 53.0932 , lng: -3.8017 },
            content: <h3>Snowdonia</h3>
        },
        {
            coordinates: { lat: 50.5719 , lng: -3.9207 },
            content: <h3>Dartmoor</h3>
        },
        {
            coordinates: { lat: 54.4609 , lng: -3.0886 },
            content: <h3>Lake District</h3>
        }
    ]
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
      animation: google.maps.Animation.DROP,
    });
    /* Add Click Listener */
    marker.addListener("click", function () {
      infoWindow.setContent(props.content);
      infoWindow.open(map, marker);
    });
  }
}
