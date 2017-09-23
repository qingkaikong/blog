'''
Author: Qingkai Kong, qingkai.kong@gmail.com
Date: 2014-10-21

Modified:
2017-09-22 by Qingkai, delete all the non-use information
'''

from obspy.geodetics import gps2dist_azimuth
from obspy import UTCDateTime
from obspy.taup.taup import getTravelTimes
from obspy.geodetics import locations2degrees
import numpy as np
import math
import pickle
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

    
def get_warning_time_common(stla, stlo, evla, evlo, evdp, evt0, alertT):
    '''
    function to get the warning time based on the common model
    '''
    P_WAVE_VELOCITY = 6.10
    S_WAVE_VELOCITY = 3.55
    
    epi_val = locations2degrees(evla, evlo, stla, stlo) * 111.12 
    
    hypo_dist = np.sqrt(epi_val**2 + evdp**2)
    
    timediff = alertT - evt0
    warningtime = hypo_dist/S_WAVE_VELOCITY - timediff
    return warningtime  
    

def find_time(d_target, p_time, s_time, distance, alert_since_o):
    '''
    Find the warning time for the cities that the user defined, 
    it is the time from S wave arrival to the time when the 
    alert sent out
    '''
    
    ix = (np.abs(d_target - np.array(distance))).argmin()
    poz = ix
    p0 = p_time[poz]
    s0 = s_time[poz]
    
    #time difference between S and alert time
    delta_t = s0 - alert_since_o
    return poz, delta_t, s0, p0
    
def P_S_arrival_T_common(epi_val, evdp):
    '''
    p and s travel time for common model
    '''
    P_WAVE_VELOCITY = 6.10
    S_WAVE_VELOCITY = 3.55
        
    hypo_dist = np.sqrt(epi_val**2 + evdp**2)
    
    P_arrival_T = hypo_dist/P_WAVE_VELOCITY
    S_arrival_T = hypo_dist/S_WAVE_VELOCITY
    
    return P_arrival_T, S_arrival_T  
    
    
def get_dist_p_s(dist, evdp, model):
    '''
    function to get the p and s travel time for 3 different models
    '''
    p_time = []
    s_time = []
    if model not in ['ak135', 'iasp91', 'common']:
        print 'model must be (1) iasp91, (2) ak135, (3) common'
        print 'use model common'
    

    for d in dist:
        epi_val = d
    
        if model == 'iasp91' or model =='ak135':
            delta = d / 111.1
            tt = getTravelTimes(delta=delta, depth=evdp, model=model)
            p_t = (item for item in tt if item["phase_name"] == "p").next()
            s_t = (item for item in tt if item["phase_name"] == "s").next()
            p_time.append(p_t['time'])
            s_time.append(s_t['time'])
            
        else:
            model = 'common'
            p_t, s_t = P_S_arrival_T_common(epi_val, evdp)
            p_time.append(p_t)
            s_time.append(s_t)
    dist_p = dist
    dist_s = dist
    return dist_p, p_time, dist_s, s_time, model

    
def plot_P_and_S(evla, evlo, evdp, evt0, alertT, cities = None, show_city = True, 
    max_dist = 120, max_T = 50, showP = True, showS = True, showAlertT=True, 
    model='ak135', show_title = True):
    '''
    Plot the P and S travel time curve and alert time. If you want to plot cities and the
    corresponding warning time, you need specify the cities dictionary which is a dictionary
    of the a tuple. For example {'Name':(lat,   lon,     dx,  dy)}. Also if you set the 
    flag of showAlertT to False or showS to False, then it won't plot the warning time and
    the cities. 
    
    model either by 'ak135', or 'iasp91', or 'common'
    '''
    
    #dist_ = range(1, max_dist, 1)
    num = max_dist 
    dist_ = np.linspace(0, max_dist, num)
    alert_since_o = (alertT - evt0)
    
    model = model.lower()
    
    dist_p, p_time, dist_s, s_time, model = get_dist_p_s(dist_, evdp, model)
    plt.figure(figsize = (12,8))
    if showP:
        plt.plot(dist_p, p_time, 'b', label = 'P wave')
    if showS:
        plt.plot(dist_s, s_time, 'r', label = 'S wave') 

        
    #print len(dist), len(p_time)
    if showAlertT:
        plt.axhline(alert_since_o, linewidth=1, color = 'k', linestyle="dashed", label = 'Alert time')
     
    if show_city:
        if cities is not None:
            for city in cities:
                lat = cities[city][0]
                lon = cities[city][1]
                dx = cities[city][2]
                dy = cities[city][3]
                
                d = gps2dist_azimuth(lat, lon, evla, evlo)[0] / 1000
                 
                poz, delta_t, maxV, minV = find_time(d, p_time, s_time, dist_s, alert_since_o)   
                
                if showS and showAlertT: 
                    plt.vlines(dist_s[poz], alert_since_o, maxV, 'k')
                    plt.annotate(city + ' %.1fs' % delta_t, xycoords='data',xy=(dist_s[poz], maxV), xytext=(dist_s[poz] + dx, dy + maxV),
                        arrowprops=dict(facecolor='black', shrink=0.1, width = 0.05,headwidth = 4),fontsize = 12) 
    
    if show_title:
        plt.title('Warning time based on ' + model + ' model')
     
    plt.xlabel('Distance from epicenter (km)')
    plt.ylabel('Time since the orgin of the earthquake (s)')
    plt.xlim((0,max_dist))
    plt.ylim((0,max_T))
    plt.legend(loc = 2, numpoints=1)
    plt.show()
    
    
def shoot(lon, lat, azimuth, maxdist=None):
    """Shooter Function
    Original javascript on http://williams.best.vwh.net/gccalc.htm
    Translated to python by Thomas Lecocq
    """
    glat1 = lat * np.pi / 180.
    glon1 = lon * np.pi / 180.
    s = maxdist / 1.852
    faz = azimuth * np.pi / 180.
 
    EPS= 0.00000000005
    if ((np.abs(np.cos(glat1))<EPS) and not (np.abs(np.sin(faz))<EPS)):
        alert("Only N-S courses are meaningful, starting at a pole!")
 
    a=6378.13/1.852
    f=1/298.257223563
    r = 1 - f
    tu = r * np.tan(glat1)
    sf = np.sin(faz)
    cf = np.cos(faz)
    if (cf==0):
        b=0.
    else:
        b=2. * np.arctan2 (tu, cf)
 
    cu = 1. / np.sqrt(1 + tu * tu)
    su = tu * cu
    sa = cu * sf
    c2a = 1 - sa * sa
    x = 1. + np.sqrt(1. + c2a * (1. / (r * r) - 1.))
    x = (x - 2.) / x
    c = 1. - x
    c = (x * x / 4. + 1.) / c
    d = (0.375 * x * x - 1.) * x
    tu = s / (r * a * c)
    y = tu
    c = y + 1
    while (np.abs (y - c) > EPS):
 
        sy = np.sin(y)
        cy = np.cos(y)
        cz = np.cos(b + y)
        e = 2. * cz * cz - 1.
        c = y
        x = e * cy
        y = e + e - 1.
        y = (((sy * sy * 4. - 3.) * y * cz * d / 6. + x) *
              d / 4. - cz) * sy * d + tu
 
    b = cu * cy * cf - su * sy
    c = r * np.sqrt(sa * sa + b * b)
    d = su * cy + cu * sy * cf
    glat2 = (np.arctan2(d, c) + np.pi) % (2*np.pi) - np.pi
    c = cu * cy - su * sy * cf
    x = np.arctan2(sy * sf, c)
    c = ((-3. * c2a + 4.) * f + 4.) * c2a * f / 16.
    d = ((e * cy * c + cz) * sy * c + y) * sa
    glon2 = ((glon1 + x - (1. - c) * d * f + np.pi) % (2*np.pi)) - np.pi    
 
    baz = (np.arctan2(sa, b) + np.pi) % (2 * np.pi)
 
    glon2 *= 180./np.pi
    glat2 *= 180./np.pi
    baz *= 180./np.pi
 
    return (glon2, glat2, baz)

def equi(m, centerlon, centerlat, radius, *args, **kwargs):
    '''
    plot circles on basemap
    '''
    glon1 = centerlon
    glat1 = centerlat
    X = []
    Y = []
    for azimuth in range(0, 360):
        glon2, glat2, baz = shoot(glon1, glat1, azimuth, radius)
        X.append(glon2)
        Y.append(glat2)
    X.append(X[0])
    Y.append(Y[0])
 
    #m.plot(X,Y,**kwargs) #Should work, but doesn't...
    X,Y = m(X,Y)
    plt.plot(X,Y,**kwargs)
    
def warningTime2distance_common(warningT, evdp, evt0, alertT):
    '''
    Given warning time, distance list, s_time list, earthquake origin time, 
    alert time, this function will return distance of this warning time, 
    blind zone radius. This is for models 'common'. 
    '''
    P_WAVE_VELOCITY = 6.10
    S_WAVE_VELOCITY = 3.55
    
    timediff = alertT - evt0
    
    hypo_dist = (warningT + timediff) * S_WAVE_VELOCITY
    epi_dist = np.sqrt(hypo_dist**2 - evdp**2)    

    blind_radius = timediff * S_WAVE_VELOCITY
    
    return epi_dist, blind_radius, timediff
    
def warningTime2distance_othermodel(warningT, dist, s_time, evt0, alertT):
    '''
    Given warning time, distance list, s_time list, earthquake origin time, 
    alert time, this function will return distance of this warning time, 
    blind zone radius. This is for models 'iasp91', and 'ak135', 
    because there's no equation to calculate warning time. 
    '''
    
    timediff_ = alertT - evt0
    timediff = warningT + timediff_
    ix = (np.abs(timediff - np.array(s_time))).argmin()
    poz = ix
    d = dist[poz]
    s0 = s_time[poz]
    
    
    ix = (np.abs(timediff_ - np.array(s_time))).argmin()
    blind_radius = dist[ix]
    
    return d, blind_radius, timediff

def plot_warningTime_on_map(evla, evlo, evdp, evt0, alertT, map_range = 1.5, cities = None, show_cities = False, 
                            figsize = (10,10), resolution = 'h', pretty = False, show_distance_label = False, max_dist = 120,
                            show_counties = False, show_blind_zone = True, show_legend= False, model = 'common', 
                            show_title = True):
    '''
    Function to plot warning time on map
    
    This function will plot the event at the center of the map, and then draw the warning time 5s, 
    10s, 15s, and 20s circle on map. Also, you can choose if you want to plot the cities you defined, 
    show the distance label, show counties, and blind zone. 
    
    Here, you can specify model, either 'ak135', 'iasp91', or 'common'. The first 
    two models are accurate to 0.1 km. 
    
    '''
    
    num = max_dist
    dist_ = np.linspace(0, max_dist, num)
    
    if evla and evlo is not None:
        llat = evla - map_range
        ulat = evla + map_range
        llon = evlo - map_range
        ulon = evlo + map_range
    
    
    plt.figure(figsize=figsize)
    m = Basemap(projection='merc', lon_0=-125.36929, lat_0=38.3215, 
            llcrnrlon=llon,llcrnrlat=llat- 0.01,urcrnrlon=ulon,urcrnrlat=ulat + 0.01,resolution=resolution)
    m.drawcoastlines()
    m.drawmapboundary()
    
    m.drawparallels(np.arange(llat, ulat + 0.01, (ulat - llat)/2.), labels=[1,0,0,0], linewidth=0.1, fmt='%.1f')
    m.drawmeridians(np.arange(llon, ulon + 0.01, (ulon - llon)/2.), labels=[0,0,0,1], linewidth=0.1, fmt='%.1f') 
    
    x_0, y_0 = m(evlo, evla)
    m.plot(x_0, y_0, 'r*', markersize=25, label = 'Event') 
    model = model.lower()
    
    dist_p, p_time, dist_s, s_time, model = get_dist_p_s(dist_, evdp, model)
    
    ##plot the warning time contours and label them
    for i in range(5,25,5):
        
        if model == 'iasp91' or model == 'ak135':
            d, blind, timediff = warningTime2distance_othermodel(i, dist_s, s_time, evt0, alertT)
        else:
            
            d, blind, timediff = warningTime2distance_common(i, evdp, evt0, alertT) 
        
        
        
        equi(m, evlo, evla, d, color = 'g', label = 'Warning time' if i == 5 else "")
        
        if show_distance_label:
            x,y = m(evlo - 0.2, evla + d/105.1)
            plt.annotate('%ds, %.1fkm'%(i, d), xy=(x, y), xycoords='data', color = 'g')
        else:
            x,y = m(evlo - 0.1, evla + d/105.1)
            plt.annotate('%ds'%(i), xy=(x, y), xycoords='data', color = 'g')
     
    if show_counties:
        m.drawcounties(zorder = 10)
        
    plt.annotate('Alert sent out %.1fs after earthquake origin'%timediff, xy=(0.01, 0.95), xycoords='axes fraction', fontsize = 14)
    
    if show_title:
        plt.title('Warning time based on ' + model + ' model')
    
    if show_blind_zone:
        equi(m, evlo, evla, blind, color = 'r', label = 'Blind zone')
        
        x,y = m(evlo - 0.15, evla + blind/105.1)
        plt.annotate('%.1fkm'%(blind), xy=(x, y), xycoords='data', color = 'r')
        
    if show_cities:
        for city in cities.keys():
            city_lat = cities[city][0]
            city_lon = cities[city][1]
            dx = cities[city][2]
            dy = cities[city][3]  
            
            x,y = m(city_lon, city_lat)
            m.plot(x, y, 'o', markersize=8, color = 'b') 
            x,y = m(city_lon + dx, city_lat + dy)
            plt.annotate(city, xy=(x, y),fontsize = 10,zorder=10)
                
    #if draw_scale_bar:
    #    m.drawmapscale(-122.4, 36.32, -122, 37, 30, barstyle='fancy')
        
    if pretty:    
        m.etopo()
    else:
        m.fillcontinents()
    if show_legend:
        plt.legend(loc = 3, numpoints = 1)
    plt.show()
