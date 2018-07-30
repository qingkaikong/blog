This week I was making a map with many points on the map - plot all the GPS stations from [UNR's Nevada Geodetic Laboratory](http://geodesy.unr.edu/), they have a [google map](http://geodesy.unr.edu/NGLStationPages/gpsnetmap/GPSNetMap.html) that can show all the GPS stations. See the following figure:

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_34_google_map_cluster/figures/gps_locations_unr.png) 

But I want to plot a nice map that has the clustered markers that I can easily see the number of stations in a region. [Folium](https://github.com/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb), the package I usually use could do it, but not so beautiful. Therefore, I changed to use google map to generate the nice clustered markers. Here is the code that I modified slightly from [Google developers](https://developers.google.com/maps/documentation/javascript/marker-clustering). You can see the following figure as the final results I have (you can find all the locations of the GPS stations [here](ftp://gneiss.nbmg.unr.edu/rapids/llh)):


![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_34_google_map_cluster/figures/gps_locations.png)

The code is in javascript, but it should be simple to use it, note that, you need to get your own API key from google, but it should be easy to get it and replace the 'YOUR_API_KEY'

```javascript
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Marker Clustering</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 1,
          center: {lat: 37.5, lng: -123.5}
        });


        // Note: The code uses the JavaScript Array.prototype.map() method to
        // create an array of markers based on a given "locations" array.
        /* The map() method here has nothing to do with the Google Maps API,  
        it creates a new array with the results of calling a provided function  
        on every element in the calling array*/
        var markers = locations.map(function(location) {
          return new google.maps.Marker({
            position: location,
          });
        });

        // Add a marker clusterer to manage the markers.  
        // The imagePath gives the icon of the clusters
        var markerCluster = new MarkerClusterer(map, markers,
            {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
      }
      var locations = [
        {lat: -12.466640, lng: -229.156013},
        {lat: -12.478224, lng: -229.017953},
        {lat: -12.355923, lng: -229.118271},
        {lat: 30.407425, lng: -91.180262},
        {lat: 31.750800, lng: -93.097604},
        {lat: 32.529034, lng: -92.075906},
        {lat: -23.698194, lng: -226.117249},
        {lat: -23.766992, lng: -226.120783},
        {lat: -37.771915, lng: -67.715566},
        {lat: 64.028926, lng: -142.075778},
        {lat: -33.768794, lng: -208.883665},
        {lat: -23.698190, lng: -226.117246},
        {lat: -23.766988, lng: -226.120781},
        {lat: 41.838658, lng: -119.653981},
        {lat: 41.853118, lng: -119.607364},
        {lat: 41.850735, lng: -119.577144},
      ]
    </script>
    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
    </script>
  </body>
</html>

```