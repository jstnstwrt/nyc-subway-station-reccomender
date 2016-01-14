import pandas as pd
import numpy as np

df = pd.read_csv('wealth_startups_mta_entrances.csv')
df.columns = ['rank', 'zip', 'population', 'income', 
			  'startups', 'national_rank', 'ca', 'unit', 
			  'station', 'line']

