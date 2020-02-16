from tabulate import tabulate
from astropy.io import ascii
from itertools import groupby
from collections import defaultdict, OrderedDict
from operator import itemgetter

sel = ["year", "origin", "dest", "carrier", "distance", "air_time"]
key = ["year", "origin"]
tbl = ascii.read("nycflights.csv", format = 'csv', data_end = 6)[sel]
lst = [dict(zip(r.colnames, r)) for r in tbl]

for i in lst:
  print(i)
'''
{'carrier': 'UA', 'air_time': 227, 'distance': 1400, 'dest': 'IAH', 'origin': 'EWR', 'year': 2013}
{'carrier': 'UA', 'air_time': 227, 'distance': 1416, 'dest': 'IAH', 'origin': 'LGA', 'year': 2013}
{'carrier': 'AA', 'air_time': 160, 'distance': 1089, 'dest': 'MIA', 'origin': 'JFK', 'year': 2013}
{'carrier': 'B6', 'air_time': 183, 'distance': 1576, 'dest': 'BQN', 'origin': 'JFK', 'year': 2013}
{'carrier': 'DL', 'air_time': 116, 'distance': 762, 'dest': 'ATL', 'origin': 'LGA', 'year': 2013}
'''

### USING ITERTOOLS.GROUPBY ###

class group1:
  def __init__(self, lst, key):
    sort = sorted(lst, key = itemgetter(*key))
    self.result = [(k, list(v)) for k, v in groupby(sort, itemgetter(*key))]

### USING DEFAULTDICT ###

class group2:
  def __init__(self, lst, key):
    data = [(tuple(r[k] for k in key), r) for r in lst]
    ddic = defaultdict(list)
    for k, v in data:
      ddic[k].append(v)
    self.result = sorted(ddic.items(), key = itemgetter(0))

### USING ORDEREDDICT ###

class group3:
  def __init__(self, lst, key):
    data = [(tuple(r[k] for k in key), r) for r in lst]
    odic = OrderedDict()
    for k, v in data:
      if k in odic: odic[k].append(v)
      else: odic[k] = [v]
    self.result = sorted(odic.items(), key = itemgetter(0))

### CHECKING EQUALITY ##
group1(lst, key).result == group2(lst, key).result == group3(lst, key).result

for i in group1(lst, key).result:
  print(tabulate(i[1], headers = "keys"), "\n")
'''
carrier      air_time    distance  dest    origin      year
---------  ----------  ----------  ------  --------  ------
UA                227        1400  IAH     EWR         2013

carrier      air_time    distance  dest    origin      year
---------  ----------  ----------  ------  --------  ------
AA                160        1089  MIA     JFK         2013
B6                183        1576  BQN     JFK         2013

carrier      air_time    distance  dest    origin      year
---------  ----------  ----------  ------  --------  ------
UA                227        1416  IAH     LGA         2013
DL                116         762  ATL     LGA         2013
'''
