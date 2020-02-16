from astropy.io.ascii import read
 
selected = ["origin", "dest", "distance", "carrier"]
 
### IMPORT CSV FILE INTO ASTROPY TABLE ###
tbl = read("Downloads/nycflights.csv", format = 'csv', data_end = 11)[selected]
 
### CONVERT ASTROPY TABLE TO DICTIONARY LIST ###
lst = map(lambda x: dict(zip(x.colnames, x)), tbl)
 
### DISPLAY DATA CONTENTS ###
from tabulate import tabulate
 
print tabulate([lst[i] for i in range(3)], headers = "keys", tablefmt = "fancy_grid")
 
╒══════════╤════════╤═══════════╤════════════╕
│ origin   │ dest   │ carrier   │   distance │
╞══════════╪════════╪═══════════╪════════════╡
│ EWR      │ IAH    │ UA        │       1400 │
├──────────┼────────┼───────────┼────────────┤
│ EWR      │ ORD    │ UA        │        719 │
├──────────┼────────┼───────────┼────────────┤
│ EWR      │ FLL    │ B6        │       1065 │
╘══════════╧════════╧═══════════╧════════════╛

### APPROACH 1: HOMEBREW GROUPING ###
 
from operator import itemgetter
 
### GET UNIQUE VALUES OF GROUP KEY ###
g_key = set([x["origin"] for x in lst])
 
### GROUPING LIST BY GROUP KEY ###
g_lst1 = sorted(map(lambda x: (x, [i for i in lst if i["origin"] == x]), g_key), key = itemgetter(0))
 
for i in g_lst1:
  print tabulate(i[1], headers = "keys", tablefmt = "fancy_grid")
  
  
### APPROACH 2: ITERTOOLS.GROUPBY  ###
 
### SORTING DICTIONARY BEFORE GROUPING ###
s_lst = sorted(lst, key = itemgetter('origin'))
 
### GROUPING DICTIONARY BY "ORIGIN" ###
from itertools import groupby
 
g_lst2 = [(k, list(g)) for k, g in groupby(s_lst, itemgetter("origin"))]
 
for i in g_lst2:
  print tabulate(i[1], headers = "keys", tablefmt = "fancy_grid")
  
  
### APPROACH 3: DEFAULTDICT ###
 
from collections import defaultdict
 
### CREATE KEY-VALUE PAIRS FROM LIST ###
ddata = [(x["origin"], x) for x in lst]
 
### CREATE DEFAULTDICT ###
ddict = defaultdict(list)
 
for key, value in ddata:
  ddict[key].append(value)
 
g_lst3 = sorted(ddict.items(), key = itemgetter(0))
 
for i in g_lst3:
  print tabulate(i[1], headers = "keys", tablefmt = "fancy_grid")
  
  
### APPROACH 4: ORDEREDDICT ###
from collections import OrderedDict
 
odict = OrderedDict()
 
for key, value in ddata:
  if key in odict: odict[key].append(value)
  else: odict[key] = [value]
 
g_lst4 = sorted(odict.items(), key = itemgetter(0))
 
for i in g_lst4:
  print tabulate(i[1], headers = "keys", tablefmt = "fancy_grid")
  
  
