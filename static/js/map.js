/* Sets map */
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 53.3342 , lng: -1.7837 },
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
        },
        {
            coordinates: { lat: 51.1346 , lng: -3.6462 },
            content:'<p>Exmoor<p>'
        },
        {
            coordinates: { lat: 51.8815 , lng: -3.4435 },
            content:'<p>Breacon Beacons<p>'
        },
        {
            coordinates: { lat: 57.0492 , lng: -3.5616 },
            content:'<p>Cairngorms<p>'
        },
        {
            coordinates: { lat: 54.3872 , lng: -0.8927 },
            content:'<p>North Yorkshire Moors<p>'
        },
        {
            coordinates: { lat: 50.8759 , lng: -1.6328 },
            content:'<p>New Forest<p>'
        },  
        {
            coordinates: { lat: 50.9279 , lng: -0.6625 },
            content:'<p>South Downs<p>'
        },
        {
            coordinates: { lat: 56.1114 , lng: -4.6289 },
            content:'<p>Loch Lomond<p>'
        }, 
        {
            coordinates: { lat: 55.3378 , lng: -2.2567 },
            content:'<p>Northumberland<p>'
        }, 
        {
            coordinates: { lat: 51.8121 , lng: -5.1011 },
            content:'<p>Pembrokeshire Coast<p>'
        },
        {
            coordinates: { lat: 54.1963 , lng: -2.1632 },
            content:'<p>Yorkshire Dales<p>'
        },
        {
            coordinates: { lat: 52.6049 , lng: -1.6089 },
            content:'<p>Broads<p>'
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
