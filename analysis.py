import pandas as pd
import numpy as np

df = pd.DataFrame([['a',1,6],['b',3,4],['c',5,2]])
df.columns = ['z','t','w']


da = pd.read_csv('wealth_startups_mta_entrances.csv')
da = da.drop_duplicates(subset = 'zip')

def rank_zips(alpha=1):
	t = da['startups_index']
	w = da['income_index']
	r = alpha*t + (1-alpha)*w
	da['r'] = r
	print da.sort(['r'],ascending = 0)[['zip','r']][:10]

rank_zips(1)

def zip_to_station(zipcode):
	# query data set for all staions in zipcode
	# return list of stations
	pass



def best_stations(ranked_zips):

	pass


# constraints on team
team_size = 10
max_team_in_zip = 5

