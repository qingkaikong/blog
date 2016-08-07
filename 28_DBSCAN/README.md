
I am currently checking out a clustering algorithm: [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) (Density-Based Spatial Clustering of Application with Noise). As the name suggested, it is a density based clustering algorithm: given a set of points in some space, it groups together points that are closely packed together (points with many nearby neighbors), and marks points as outliers if they lie alone in low-density regions. It has many advantages, including no need specify the number of clusters, can find arbitrary shaped clusters, relatively fast, etc. Of course, there's no single algorithm can do everything, DBSCAN has disadvantage as well.   

The algorithm has two parameters: **epsilon** and **min_samples**, the advantage of the algorithm is that you don’t have to specify how many clusters you need, it can find all the clusters that satisfy the requirement. For the disadvantage, it is very sensitive to the parameter you choose. 

The summary of this algorithm is:  
**Step 1:** For each point in the dataset, we draw a n-dimensional sphere of radius epsilon around the point (if you have n-dimensional data).  
**Step 2:** If the number of points inside the sphere is larger than min_samples, we set the center of the sphere as a cluster, and all the points within the sphere are belong to this cluster.  
**Step 3:** Loop through all the points within the sphere with the above 2 steps, and expand the cluster whenever it satisfy the 2 rules.   
**Step 4:** For the points not belong to any cluster, you can ignore them, or treat them as outliers.  

The original paper about DBSCAN was published 10 years ago in 1996, and can be found [here](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf). It is currently ranked the [41st place](http://academic.research.microsoft.com/RankList?entitytype=1&topDomainID=2&subDomainID=7&last=0&start=1&end=100) in the most cited publication in data mining. If you find the paper is too heavy on defining different points, you can check this very nice video on youtube shows how this works: [Here](
https://www.youtube.com/watch?v=5E097ZLE9Sg). Scikit learn already has a very nice example to show the effectiveness of the algorithm. You can find the example [here](http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html). 
![sklearn example](http://scikit-learn.org/stable/_images/plot_cluster_comparison_001.png) 
In the following, we will cluster the Loma Prieta earthquake aftershocks using DBSCAN. 

## Grab the earthquake data


```python
%pylab inline  
import pandas as pd
import numpy as np
import folium
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
```

    Populating the interactive namespace from numpy and matplotlib


Earthquake data can be get from the [ANSS catalog](http://www.ncedc.org/anss/catalog-search.html). For simplicity, I just download aftershock data above Magnitude 2.0 for one week after the [Loma Prieta earthquake](https://en.wikipedia.org/wiki/1989_Loma_Prieta_earthquake). All together, there are 1009 earthquakes in this region. 


```python
# Read in earthquake data
df = pd.read_csv('./LomaPrieta_aftershocks_1week_above_2.csv', skiprows = 7)

# Get the latitude and logitude of the earthquakes
coords = df.as_matrix(columns=['Latitude', 'Longitude'])
```


```python
# Plot the location of the earthquakes

plt.figure(figsize = (12, 12))

m = Basemap(projection='merc', resolution='l', epsg = 4269, 
            llcrnrlon=-122.7,llcrnrlat=36.2, urcrnrlon=-120.8,urcrnrlat=37.5)

# plot the aftershock
x, y = m(coords[:, 1], coords[:, 0])
m.scatter(x,y,5,marker='o',color='b')
m.arcgisimage(service='World_Shaded_Relief', xpixels = 5000, verbose= False)
    
plt.show()
```


![png](DBSCAN_files/DBSCAN_5_0.png)


## Cluster and see the results

We are now using the DBSCAN from the sklearn. I followed [Geoff Boeing's blog](http://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/) to cluster the geo-spatial data using the metrics [haversine](https://en.wikipedia.org/wiki/Haversine_formula). I choose the epsilon roughly 1.5 km, and the min_samples = 5. We can see that DBSCAN detected 9 clusters. 


```python
from sklearn.cluster import DBSCAN
from sklearn import metrics

kms_per_radian = 6371.0088
epsilon = 1.5 / kms_per_radian

# Run the DBSCAN from sklearn
db = DBSCAN(eps=epsilon, min_samples=5, algorithm='ball_tree', \
            metric='haversine').fit(np.radians(coords))

cluster_labels = db.labels_
n_clusters = len(set(cluster_labels))

# get the cluster
# cluster_labels = -1 means outliers
clusters = \
    pd.Series([coords[cluster_labels == n] for n in range(-1, n_clusters)])
```


```python
import matplotlib.cm as cmx
import matplotlib.colors as colors

# define a helper function to get the colors for different clusters

def get_cmap(N):
    '''
    Returns a function that maps each index in 0, 1, ... N-1 to a distinct 
    RGB color.
    '''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='nipy_spectral') 
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color
```


```python
plt.figure(figsize = (12, 12))
m = Basemap(projection='merc', resolution='l', epsg = 4269, 
        llcrnrlon=-122.7,llcrnrlat=36.2, urcrnrlon=-120.8,urcrnrlat=37.5)

unique_label = np.unique(cluster_labels)

# get different color for different cluster
cmaps = get_cmap(n_clusters)

# plot different clusters on map, note that the black dots are 
# outliers that not belone to any cluster. 
for i, cluster in enumerate(clusters):
    lons_select = cluster[:, 1]
    lats_select = cluster[:, 0]
    x, y = m(lons_select, lats_select)
    m.scatter(x,y,5,marker='o',color=cmaps(i), zorder = 10)

m.arcgisimage(service='World_Shaded_Relief', xpixels = 5000, verbose= False)

plt.show()
```


![png](DBSCAN_files/DBSCAN_9_0.png)

