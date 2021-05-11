
# coding: utf-8

# ## readtle
# import pyorbital
# from pyorbital import Orbital
# from pyorbital import tlefile
# tle = tlefile.read('ISS (ZARYA)', '/home/u16/atshaver/Norad DeMi TLE.txt')
# #from datetime import datetime
# import datetime
# now = datetime.datetime.utcnow()
# 
# 
# 
# #use matplotlib to plot coordinates on a map 
# 
# import numpy as np
# 
# import matplotlib.pyplot as plt
# %matplotlib inline
# 
# import mpl_toolkits
# #from mpl_toolkits.basemap import Basemap
# #print(tle)
# 



# zarya = pyorbital.Orbital('ISS (ZARYA)', tle_file= '/home/u16/atshaver/Norad DeMi TLE.txt', line1=None, line2=None)
# 
# #paloalto(1)
# PAtime=datetime.datetime(2021, 1, 12, 3, 0) 
# lat1 = 37.4419
# lon1 = 122.1430
# alt1 = 30
# 
# #biosphere(2)
# B2time=datetime.datetime(2021, 1, 12, 3, 0)
# lat2 = 32.5784
# lon2 = 110.8514
# alt2 = 3820
# 
# 
# # plugging each minute in a month into get_observer_look function for both 
# #locations and recording how many times each location’s function returns a positive elevation value at the same time. 
# 
# count = 0
# starttime = datetime.datetime(2021, 1, 12, 3, 0)
# overlap_times=[]
# 
# def find_elevation(i):
#     
#     PAfunctiontime = starttime + datetime.timedelta(minutes=i)
#     PA = zarya.get_observer_look(PAfunctiontime, lon1, lat1, alt1)
#     #plot locations
#     
#     B2functiontime= starttime + datetime.timedelta(minutes=i)
#     B2 = zarya.get_observer_look(B2functiontime, lon2, lat2, alt2)
#     #plot locations
# 
#      
#     
#     if B2[1]>0 and PA[1]>0:
#         count += 1
#         overlap_times.append(starttime + i)
# 
#     
# for i in range (1000):
#     find_elevation(i)
# 
# print(count)
# print(overlap_times)    


