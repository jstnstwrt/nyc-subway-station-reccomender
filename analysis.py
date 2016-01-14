import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2],[3,4],[5,6]])
df.columns = ['t','w']

def rank_zips(alpha=1):
	# for each zipcode
	# compute mixture of tech and wealth
	# ie, at + (1-a)w
	# return ranked list of zips
	pass

def zip_to_station(zipcode):
	# query data set for all staions in zipcode
	# return list of stations
	pass



def best_stations(ranked_zips):

	pass


# constraints on team
team_size = 10
max_team_in_zip = 5

