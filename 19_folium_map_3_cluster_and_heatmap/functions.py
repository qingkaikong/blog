import numpy as np


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
    
