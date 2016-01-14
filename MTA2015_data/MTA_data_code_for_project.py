import csv
import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import os.path
import pandas as pd

def read_file(filename):
    d = []
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            d.append(row)
    
    for item in d:
        item[-1] = item[-1].rstrip()
        
    d = d[1:]
    return d

def get_turnstiles(filename):
    data = read_file(filename)
    #print(data[1])
    newDict = defaultdict(list)
    for item in data:
        newDict[tuple(item[:4])].append(item[4:])
        
    return newDict

def print_x_dict_kv(dictionary, numKeys):
    for key in sorted(dictionary)[:numKeys]:
        print("{}: {}".format(key,dictionary[key]))
        
def get_ts_timeseries(filename):
    data = get_turnstiles(filename)
    newDict = defaultdict(list)
    for k,v in data.items():
        for item in v:
            dt = item[2] + ' ' + item[3]
            dt = datetime.datetime.strptime(dt, "%m/%d/%Y %H:%M:%S")
            entries = int(item[5])
            ts = [dt, entries]
            newDict[k].append(ts)
            
    for k,v in newDict.items():
        newDict[k] = sorted(v)
    
    for item in newDict.values():
        assert item == sorted(item)        

    return newDict  

def get_ts_timeblock_entries(filename):
    data = get_ts_timeseries(filename)
    
    newDict = {turnstile: [[v[i][0],
                            v[i+1][1]-v[i][1],
                            v[i+1][0]-v[i][0]] for i in range(len(v)-1) 
                            if 0 <= v[i+1][1]-v[i][1] <= 5000] 
                            for turnstile,v in data.items()}
    
    return newDict

def dframes_of_weeks_and_hours(*args): 
    
    '''{(c/a, unit, station):
                            {day:
                                {time: count}
                            }
        }'''
    
    full_dict = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
    cols = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    
    for file in args:
        data = get_ts_timeblock_entries(file)    
        
        
        for k,v in data.items():
            newKey = k[:2] + (k[3],)
            #by_day = defaultdict(lambda : defaultdict(int))
            
            for item in v:
                day_string = item[0].strftime("%A")
                time = item[0].time()
                round_time = datetime.datetime.strptime(
                            str(int(time.hour / 4) * 4).zfill(2), "%H")
                round_time = round_time.time()
                #print(type(round_time))
                #break
                full_dict[newKey][day_string][round_time] += item[1] 
    
    
    df_dict = {turnstile: pd.DataFrame.from_dict(value) 
               for turnstile, value in full_dict.items()}
    for k,v in df_dict.items():
        df_dict[k] = v[cols]
        
    return df_dict


summer_data = dframes_of_weeks_and_hours('turnstile_150530.csv',  'turnstile_150606.csv', 'turnstile_150613.csv', 'turnstile_150620.csv', 'turnstile_150627.csv', 'turnstile_150704.csv', 'turnstile_150711.csv', 'turnstile_150718.csv', 'turnstile_150725.csv', 'turnstile_150801.csv', 'turnstile_150801.csv', 'turnstile_150808.csv', 'turnstile_150815.csv', 'turnstile_150822.csv', 'turnstile_150829.csv', 'turnstile_150905.csv', 'turnstile_150912.csv')

print_x_dict_kv(summer_data, 10)
   