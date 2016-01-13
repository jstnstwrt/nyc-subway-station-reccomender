import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

df = pd.read_csv('mta_geo_tags.csv',header = None)
mta = np.array(df)
geolocator = Nominatim()

mta = mta[:2]
for station in mta:
	geo = station[5],station[6]
	location = geolocator.reverse(geo)
	zipcode = str(location.raw['address']['postcode'])
	print geo , zipcode

