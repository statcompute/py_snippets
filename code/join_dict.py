### IMPORT AND PREPARE THE DATA ###
from astropy.io.ascii import read
 
selected = ["origin", "dep_delay", "distance"]
 
tbl = read("Downloads/nycflights.csv", format = 'csv', data_end = 11)[selected]
 
lst = map(lambda x: dict(zip(x.colnames, x)), tbl)
 
key = set(map(lambda x: x["origin"], lst))
 
grp = dict(map(lambda x: (x, [i for i in lst if i["origin"] == x]), key))
 
#   ALTERNATIVELY, USE CLJ.SEQS.GROUP_BY()
# from clj.seqs import group_by
# group_by(lambda x: x["origin"], lst)
#   OR TOOLZ.ITERTOOLZ.GROUPBY()
# from toolz import itertoolz
# itertoolz.groupby("origin", lst)
#   OR ITERTOOLS.GROUPBY()
# key_fn = lambda x: x["origin"]
# dict((k, list(g)) for k, g in groupby(sorted(lst, key = key_fn), key_fn))
 
### CREATE 2 DICTIONARY LISTS TO BE MERGED ###
from numpy import nanmean, nanmedian
 
l1 = list({"origin"   : k,
           "med_dist" : nanmedian([v["distance"] for v in grp[k]])
          } for k in grp.keys())
#[{'med_dist': 1089.0, 'origin': 'JFK'},
# {'med_dist': 1065.0, 'origin': 'EWR'},
# {'med_dist': 747.5, 'origin': 'LGA'}]
 
l2 = list({"origin"   : k,
           "avg_delay": round(nanmean(map(lambda v: v["dep_delay"], grp[k])), 2)
          } for k in grp.keys())
#[{'avg_delay': -0.67, 'origin': 'JFK'},
# {'avg_delay': -2.33, 'origin': 'EWR'},
# {'avg_delay': -1.75, 'origin': 'LGA'}]
 
### METHOD 1: LIST COMPREHENSION ###
join1 = list(dict(v1, **v2) for v2 in l2 for v1 in l1 if v1["origin"] == v2["origin"])
 
### METHOD 2: CARTESIAN PRODUCT WITH ITERTOOLS.PRODUCT() ###
from itertools import product
 
join2 = list(dict(d1, **d2) for d1, d2 in product(l1, l2) if d1["origin"] == d2["origin"])
 
### METHOD 3: AD-HOC FUNCTION WITH DICT COPY() AND UPDATE() METHODS ###
def join_fn(x, y, key):
  result = list()
  for i, j in group_by(lambda x: x[key], x + y).values():
    xy = i.copy()
    xy.update(j)
    result.append(xy)
  return result
 
join3 = join_fn(l1, l2, "origin")
 
### METHOD 4: DEFAULTDICT() ###
from collections import defaultdict
 
dd = defaultdict(dict)
 
for x in l1 + l2:
  dd[x["origin"]].update(x)
 
join4 = dd.values()
 
### METHOD 5: ORDEREDDICT() ###
from collections import OrderedDict
 
od = OrderedDict()
 
for x in l1 + l2:
  if x["origin"] in od:
    od[x["origin"]].update(x)
  else:
    od[x["origin"]] = x
 
join5 = od.values()
 
### METHOD 6:  ###
from toolz import itertoolz, dicttoolz
 
join6 = list(dicttoolz.merge(i, j) for i, j in  itertoolz.join("origin", l1, "origin", l2))
 
# EXPECTED OUTPUT:
# [{'avg_delay': -0.67, 'med_dist': 1089.0, 'origin': 'JFK'},
#  {'avg_delay': -2.33, 'med_dist': 1065.0, 'origin': 'EWR'},
#  {'avg_delay': -1.75, 'med_dist': 747.5, 'origin': 'LGA'}]
