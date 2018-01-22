I am currently learning [QGIS](https://www.qgis.org/en/site/) by attending the workshop at D-Lab, [Geospatial Data and Mapping Fundamentals](http://dlab.berkeley.edu/training/geospatial-data-and-mapping-fundamentals-part-1). Here I am using a small prject to show what I learned for the basics. 

The goal of this small project is to make a map with the population count and the earthquakes world wide, so that we can easily see where are the most dangerous places on earth. 

### Data download
First we need to download the population grid count data from [Socioeconomic Data and Applications Center](http://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev10/data-download), I downloaded the popultation count data for 2015 at the resolution about 110km for demonstration purposes (you can download more higher resolution ones), you can find the population count data in [GeoTiff here](https://github.com/qingkaikong/blog/tree/master/2018_01_QGIS_projection_systems/data/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev10_2015_1_deg_tif). And the earthquake data by query USGS catalogs, I've already downloaded the world wide earthquakes larger than M6 from 2006 to 2018, you can find it [here](https://github.com/qingkaikong/blog/blob/master/2018_01_QGIS_projection_systems/data/World_EQ_6%2B_2000_2018.csv). 

### Import data into QGIS
Let's load the data into the QGIS first. Since the population data is a GeoTiff, which is a raster file, we can add a raster layer as shown in the following figure:

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_1.png)

The earthquake data is a vector data, and it can be added as a vector layer as the following figure, the QGIS is smart enough to find out the latitude and longitude as the Y and X field. You don't need to change anything:

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_2.png)

After we add the earthquake data, it now looks like this:
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_3.png)

### Change the projection
Many times, you will find that different data will have different [projections](https://en.wikipedia.org/wiki/Map_projection). In a simple sense, the projection is the rule when you want to show things on the earth (3D sphere) onto a 2D Map. There are different projections, and if your data are in different projections, they will not line up in the map. Therefore, you need to make all the layers have the same projection. 

You can find the projection of the data by righ click the layer in the 'Layers Panel', and click the properties. The projection of this layer will be shown in the 'General' tab. As shown in the next two figures:
 
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_4.png)

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_5.png)

**Note that**, you can not change the projection here (even you change it here, the underlying projection is still the old one). If you want to change the projection, do the following steps:

**Step 1**:  
Right click the layer you want to change the projection, and choose 'Save as':
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_6.png)

**Step 2**:
A pop up window will ask you the new name you want to save, and in the 'CRS', you can choose your new projection system. 
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_7.png)

Click the small global near it, and in the pop up window, you can type '4326' in the 'Filter', which will list the name of the projection system below. (in our case, we don't need to change, but if you need change to another projection, just find it here)

![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_8.png)


**Step 3**:  
After you save it as a new layer, you will see that in the 'Layers Panel'. Remove the old layer:
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_9.png)

Then you will have all the new layer with the new projections. Do this for all the layers in different projections (usually you change the vector layers to the projection system which the raster layer use) 
![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_01_QGIS_projection_systems/figures/figure_10.png)

Dada, we can see the above figure, we have the data loaded into the QGIS, but the population is all black, we want to change the color of the population based on the count, and for the earthquakes, maybe use the size of the circle as the magnitude and color it by using the depth. How we can do this? We will talk this next week. 