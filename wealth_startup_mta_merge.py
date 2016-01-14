import pandas as pd
import numpy as np

#Read in files for wealth/startups by zip code and file for mta entrances by zip code
wlth_strt = pd.read_csv("wealth_and_startups.csv")
mta_zips = pd.read_csv("mta_with_zips.csv")

#Drop mta file columns we don't need
mta_zips = mta_zips[[1, 2, 3, 4, 8]]

#Rename mta file columns to allow merging with mta volume data and wealth/startup file
mta_zips.columns = ['ca', 'unit', 'station', 'line', 'zip']

#Merge mta and startup/wealth by zip
merge = wlth_strt.merge(mta_zips, on = 'zip')

#Create subset of data that has either income or startups populated
merge_filled = merge[(merge['income'] > 0) | (merge['startups'] > 0)]

#Calculate indices at unique zip level
score = merge_filled[['zip', 'income', 'startups']]

#drop duplicates by zip
score_dedup = score.drop_duplicates(subset = 'zip')

#calculate index scores
score_dedup['income_index'] = np.round(score_dedup['income']/score_dedup.income.mean(), decimals = 2)
score_dedup['startups_index'] = np.round(score_dedup['startups']/score_dedup.startups.mean(), decimals = 2)

#calculate proportion scores
score_dedup['income_prop'] = np.round(score_dedup['income']/score_dedup.income.sum(), decimals = 2)
score_dedup['startups_prop'] = np.round(score_dedup['startups']/score_dedup.startups.sum(), decimals = 2)
score_dedup = score_dedup[['zip', 'income_index', 'startups_index', 'income_prop', 'startups_prop']]
#append indices to mta and startup/wealth file
score_final = merge_filled.merge(score_dedup, on = 'zip')

#Export file
score_final.to_csv("wealth_startups_mta_entrances.csv", index = False)

#test

######################
#QA CHECKS
######################
#Check unique counts by station and zip
#103 unique stations
merge.duplicated('STATION').value_counts()
#40 unique zips
merge.duplicated('zip').value_counts()

#Check merged file against individual source files to QA
wlth_strt[wlth_strt['zip'] == 10007]
mta_zips[mta_zips['zip'] == 10007]
merge[merge['zip'] == 10007]

#293 entrances with either non-zero income or non-zero startups
len(merge[(merge['income'] > 0) | (merge['startups'] > 0)])

#99 unique stations
merge_filled.duplicated('STATION').value_counts()
#38 unique zips
merge_filled.duplicated('zip').value_counts()