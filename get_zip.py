import pandas as pd
import numpy as np
import geopy

df = pd.read_csv('mta_geo_tags.csv',header = None)
mta = np.array(df)


geolocator = Nominatim()

geo = mta[0][5:]

location = geolocator.reverse("52.509669, 13.376294")



print geo