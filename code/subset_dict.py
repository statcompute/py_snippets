from csv import DictReader
 
selected = ["origin", "dest", "distance", "carrier"]
 
with open("Downloads/nycflights.csv") as f:
  d = DictReader(f)
  l = map(lambda d: {k: d[k] for k in selected}, [next(d) for i in xrange(10)])
 
from pandas import DataFrame
 
from sys import getsizeof
 
### COMPARING OBJECT SIZES BETWEEN A DATAFRAME AND A LIST ###
float(getsizeof(DataFrame(l))) / getsizeof(l)
# 13.282894736842104
 
from tabulate import tabulate
 
print tabulate([l[i] for i in range(3)], headers = "keys")
# origin    dest    carrier      distance
# --------  ------  ---------  ----------
# EWR       IAH     UA               1400
# LGA       IAH     UA               1416
# JFK       MIA     AA               1089
 
### SOLUTION 1: LIST COMPREHENSION ###
list(x for x in l if x["origin"] == 'JFK' and x["carrier"] == 'B6')
 
### SOLUTION 2: FILTER() FUNCTION ###
filter(lambda x: x["origin"] == 'JFK' and x["carrier"] == 'B6', l)
 
### SOLUTION 3: MAP() AND LAMBDA() FUNCTIONS ###
list(v for v, i in map(lambda x: (x, x['origin'] == 'JFK' and x["carrier"] == 'B6'), l) if i)
 
### SOLUTION 4: CREATE A CLASS ###
class subset:
  def __init__(self, lst, expr):
    self.result = []
    for x in lst:
      if eval(expr):
        self.result.append(x)
 
subset(l, 'x["origin"] == "JFK" and x["carrier"] == "B6"').result
 
### SOLUTION 5: LIST_DICT_DB MODULE ###
from list_dict_DB import list_dict_DB as dict2db
db = dict2db(l)
db.query(origin = 'JFK', carrier = 'B6')
 
# EXPECTED OUTCOME:
# [{'carrier': 'B6', 'dest': 'BQN', 'distance': '1576', 'origin': 'JFK'},
#  {'carrier': 'B6', 'dest': 'MCO', 'distance': '944', 'origin': 'JFK'}]
