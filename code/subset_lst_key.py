### READ A DATA SAMPLE WITH THREE RECORDS FROM THE CSV FILE
from csv import DictReader
 
with open("Downloads/nycflights.csv") as f:
  d = DictReader(f)
  l = [next(d) for i in xrange(3)]
 
### GET A DICT FROM THE LIST
d = l[0]
 
### SHOW KEYS OF THE DICT
print d.keys()
#['origin', 'dep_time', 'flight', 'hour', 'dep_delay', 'distance', 'dest', 'month', 'air_time', 'carrier', 'year', 'arr_delay', 'tailnum', 'arr_time', 'day', 'minute']
 
### SELECTED KEYS
selected = ["origin", "dest", "distance", "carrier"]
 
# EXPECTED OUTPUT 
# {'carrier': 'UA', 'dest': 'IAH', 'distance': '1400', 'origin': 'EWR'}
 
### METHOD 1: DEFINE BY THE DICT COMPREHENSION
 
{k: d[k] for k in selected}
 
{k: d.get(k) for k in selected}
 
{k: v for k, v in d.items() if k in selected}
 
### METHOD 2: DEFINE BY THE DICT CONSTRUCTOR
 
dict((k, d[k]) for k in selected)
 
dict(map(lambda k: (k, d[k]), selected))
 
dict(filter(lambda i: i[0] in selected, d.items()))
 
### METHOD 3: DEFINE WITH THE ZIP() FUNCTION
 
dict(zip(selected, [d[k] for k in selected]))
 
# ITEMGETTER() FUNCTION WITH THE UNPACK OPERATOR (*)
from operator import itemgetter
dict(zip(selected, itemgetter(*selected)(d)))
 
# AT() FUNCTION WITH THE UNPACK OPERATOR (*)
from pydash import at
dict(zip(selected, at(d, *selected)))
 
### APPLY ABOVE LOGIC TO THE WHOLE LIST OF DICTIONARIES
### WITH THE MAP FUNCTION
map(lambda d: {k: d[k] for k in selected}, l)
 
### ALTERNATIVELY, WITH THE LIST COMPREHENSION
[(lambda x: {k: x[k] for k in selected})(d) for d in l]
 
### OR THE PARALLEL POOL.MAP() FUNCTION
# ALWAYS DEFINE THE FUNCTION FIRST
def sel(d):
  return({k: d[k] for k in selected})
 
# THE MULTIPROCESSING MODULE NEXT
from multiprocessing import Pool, cpu_count
from contextlib import closing

with closing(Pool(processes = cpu_count())) as pool:
  pool.map(sel, l)
  pool.terminate()
 
# OUTPUT:
# [{'carrier': 'UA', 'dest': 'IAH', 'distance': '1400', 'origin': 'EWR'},
#  {'carrier': 'UA', 'dest': 'IAH', 'distance': '1416', 'origin': 'LGA'},
#  {'carrier': 'AA', 'dest': 'MIA', 'distance': '1089', 'origin': 'JFK'}]
