import pandas as pd
import numpy as np

df = pd.DataFrame([['a',1,6],['b',3,4],['c',5,2]])
df.columns = ['z','t','w']


def rank_zips(alpha=1):
	t = df['t']
	w = df['w']
	r = alpha*t + (1-alpha)*w
	df['r'] = r
	print df.sort(['r'])['z']

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

