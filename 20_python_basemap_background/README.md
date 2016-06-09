When using python [Basemap](http://matplotlib.org/basemap/users/examples.html) to plot maps, a nice background would be a big plus. But when using map.bluemarble(), map.etopo(), or  map.shadedrelief(), we can not zoom in to a smaller region, since it will generate a blur image. The best way to create a high resolution background image (either topography, street map, etc.) is using **arcgisimage** method. See the documentation [here](https://basemaptutorial.readthedocs.io/en/latest/backgrounds.html). I will show the following examples to plot the nice map.

For using arcgisimage method, you need specify the epsg for different region, and choose the services from the following list (see different services [here](http://server.arcgisonline.com/ArcGIS/rest/services), also [here](http://resources.arcgis.com/en/help/arcgis-rest-api/#/Basemaps/02r3000001mt000000/)):
1. World_Physical_Map
2. World_Shaded_Relief
3. World_Topo_Map
4. NatGeo_World_Map
5. ESRI_Imagery_World_2D
6. World_Street_Map
7. World_Imagery
8. ESRI_StreetMap_World_2D
9. Ocean_Basemap

Which map background do you like?