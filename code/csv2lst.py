from csv import DictReader
from pprint import pprint
 
### EXAMINE 3 ROWS OF DATA
with open("Downloads/nycflights.csv") as f:
  d = DictReader(f)
  l = [next(d) for i in xrange(3)]
 
### NUMBERS SHOWN AS STRINGS 
pprint(l[0])
'''
{'air_time': '227',
 'arr_delay': '11',
 'arr_time': '830',
 'carrier': 'UA',
 ... ...
 'origin': 'EWR',
 'tailnum': 'N14228',
 'year': '2013'}
'''

### USING PANDAS ###
from pandas import read_csv
from numpy import array_split
from multiprocessing import Pool, cpu_count
 
n = 1000
d = read_csv("Downloads/nycflights.csv", nrows = n)

%time l1 = [dict(zip(d.iloc[i].index.values, d.iloc[i].values)) for i in range(len(d))]
#CPU times: user 396 ms, sys: 39.9 ms, total: 436 ms
#Wall time: 387 ms
 
pprint(l1[0])
#{'air_time': 227.0,
# 'arr_delay': 11.0,
# 'arr_time': 830.0,
# 'carrier': 'UA',
# 'day': 1,
# 'dep_delay': 2.0,
# 'dep_time': 517.0,
# 'dest': 'IAH',
# 'distance': 1400,
# 'flight': 1545,
# 'hour': 5.0,
# 'minute': 17.0,
# 'month': 1,
# 'origin': 'EWR',
# 'tailnum': 'N14228',
# 'year': 2013}

d2 = array_split(d, 4, axis = 0)
 
%%time
l2 = reduce(lambda a, b: a + b,
       map(lambda df: [dict(zip(df.iloc[i].index.values, df.iloc[i].values)) for i in range(len(df))], d2))
#CPU times: user 513 ms, sys: 83.3 ms, total: 596 ms
#Wall time: 487 ms

def p2dict(df):
  return([dict(zip(df.iloc[i].index.values, df.iloc[i].values)) for i in range(len(df))])
 
pool = Pool(processes = cpu_count())
 
%time l3 = reduce(lambda a, b: a + b, pool.map(p2dict, d2))
#CPU times: user 12.5 ms, sys: 23 µs, total: 12.5 ms
#Wall time: 204 ms
 
pool.close()

from astropy.io.ascii import read
 
a = read("Downloads/nycflights.csv", format = 'csv', data_end = n + 1)
 
def a2dict(row):
  return(dict(zip(row.colnames, row)))
 
pool = Pool(processes = cpu_count())
 
%time l4 = pool.map(a2dict, a)
#CPU times: user 90.6 ms, sys: 4.47 ms, total: 95.1 ms
#Wall time: 590 ms
 
pool.close()
