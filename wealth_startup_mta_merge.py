#Read in files for wealth/startups by zip code and file for mta entrances by zip code
wlth_strt = pd.read_csv("wealth_and_startups.csv")
mta_zips = pd.read_csv("mta_with_zips_2.csv")

#Drop mta file columns we don't need
mta_zips = mta_zips[[1, 2, 3, 4, 8]]

#Rename mta file columns to allow merging with mta volume data and wealth/startup file
mta_zips.columns = ['C/A', 'UNIT', 'STATION', 'LINE', 'zip']

#Merge mta and startup/wealth by zip
merge = wlth_strt.merge(mta_zips, on = 'zip')

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

#Create subset of data that has either income or startups populated
merge_filled = merge[(merge['income'] > 0) | (merge['startups'] > 0)]

#99 unique entrances
merge_filled.duplicated('STATION').value_counts()
#38 unique stations
merge_filled.duplicated('zip').value_counts()

#Export to repo
merge_filled.to_csv("wealth_startups_mta_entrances.csv", index = False)