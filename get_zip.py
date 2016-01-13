import math 
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

df = pd.read_csv('mta_geo_tags.csv',header = None)
mta = np.array(df)
geolocator = Nominatim()

mta = mta[-5:]
mta_zips = np.empty((0,8))
for station in mta:
	if math.isnan(station[5]):
		station = np.append(station,float('nan'))
	else:
		print 'in else'
		geo = station[5],station[6]
		location = geolocator.reverse(geo)
		zipcode = str(location.raw['address']['postcode'])
		station = np.append(station,zipcode)
	mta_zips = np.append(mta_zips,[station],axis = 0)


print mta_zips
