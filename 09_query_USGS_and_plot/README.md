
The following shows you how to query the USGS earthquake catlog online and plot the earthquakes on a map. 
Dependences you need:
(1) Matplotlib
(2) Numpy
(3) BeautifulSoup
(4) urllib
(5) Basemap

The idea is: Query the data from USGS directly, get the location and magnitude of the earthquake, and plot them on the map. You can find the script on Qingkai's github. 


```
from bs4 import BeautifulSoup
import urllib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
%pylab inline
```

    Populating the interactive namespace from numpy and matplotlib



```
def build_query(outFormat = 'text', starttime = '2016-02-01', endtime = '2016-03-01', minmagnitude = 5.0):
    '''
    Funciton to build the url for query the data. Details can be found at USGS api documentation:
    http://earthquake.usgs.gov/fdsnws/event/1/
    
    Note: you can add more parameters, but I just need time range and minmum magnitude to start with. 
    '''
    base = 'http://earthquake.usgs.gov/fdsnws/event/1/query?'
    url = base + 'format=' + outFormat + '&starttime=' + starttime + '&endtime=' + endtime + '&minmagnitude=' + str(minmagnitude)
    return url

def parse_result(inputText):
    '''
    Function to parse the requested earthquake events data from USGS, and save it into numpy array
    '''
    event_id = []
    origin_time = []
    evla = []
    evlo = []
    evdp = []
    mag = []
    mag_type = []
    EventLocationName  = []
    for i, item in enumerate(inputText.split('\n')[0:-1]):
        if i < 1:
            # skip the header
            continue
            
        try:
            splited = item.split('|')
            event_id.append(splited[0])  
            origin_time.append(splited[1])
            evla.append(splited[2])
            evlo.append(splited[3])
            evdp.append(splited[4])
            mag.append(splited[10])
            mag_type.append(splited[9])
            EventLocationName.append(splited[-1])
        except:
            # just in case there are some wrong data in the catlog
            print item
            print 'Skip wrong data or there is something wrong' 
        
    return np.c_[event_id, origin_time, evla, evlo, mag, mag_type, EventLocationName]
```


```
# let's get the earthquake larger than M5 globally from 2010-01-01 to 2016-01-01. 
url = build_query(outFormat = 'text', starttime = '2010-01-01', endtime = '2016-01-01', minmagnitude = 5.0)
print url
```

    http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2010-01-01&endtime=2016-01-01&minmagnitude=5.0



```
# get the earthquake data from USGS and parse them into a numpy array
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "lxml")
events_mat = parse_result(soup.text)
```


```
fig = plt.figure(figsize = (12,9))
map_ax = fig.add_axes([0.03, 0.13, 0.94, 0.82])

map = Basemap(projection='hammer',lon_0=180, resolution = 'l')

map.drawmapboundary(fill_color='#99ffff')
map.fillcontinents(color='#cc9966',lake_color='#99ffff')
    
###################################plot earthquakes###################################
# get the latitude, longitude, and magnitude for plotting
lats = [float(item[2]) for item in events_mat]
lons = [float(item[3]) for item in events_mat]
mags = [float(item[4]) for item in events_mat]
x, y = map(lons, lats)

#scale the size of the earthquake on the map
min_size = 50
max_size = 90
min_mag = min(mags)
max_mag = max(mags)

frac = [(_i - min_mag) / (max_mag - min_mag) for _i in mags]
magnitude_size = [(_i * (max_size - min_size)) **2 for _i in frac]
map.scatter(x, y, marker='o', s=magnitude_size, c='r',zorder=10)


###################################plot scale, annotation, and legend###################################
plt.annotate('Berkeley Seismological Lab', xy=(0.01, 0.01), xycoords='axes fraction', fontsize = 16)
legends = []
for mag_ in [5., 6., 7., 8., 9.]:
    frac = (mag_ - min_mag + 0.1) / (max_mag - min_mag)
    magnitude_size = (frac * (max_size - min_size)) **2
    l1 = plt.scatter([], [], marker='o', s=magnitude_size, c='red', zorder=10)
    legends.append(l1)
    
ll = ['M5\n', 'M6\n', 'M7\n', 'M8\n', 'M9\n']

leg = plt.legend(legends, ll, scatterpoints = 1, ncol=6, frameon=False, fontsize=12, handlelength=7, \
    columnspacing = 0.01, bbox_to_anchor=(0.8, -0.06))   

plt.show()

```


![png](Query_events_from_USGS_files/Query_events_from_USGS_5_0.png)



```

```
