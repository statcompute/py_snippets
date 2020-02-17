from tabulate import tabulate

from astropy.io import ascii

from itertools import groupby

from collections import defaultdict

from numpy import nanmedian, nanmean

sel = ["year", "month", "origin", "dest", "carrier", "distance", "air_time"]

tbl = ascii.read("nycflights.csv", format = 'csv', data_end = 51)[sel]

lst = [dict(zip(r.colnames, r)) for r in tbl]

class group:
  def __init__(self, lst, key):
    sort = sorted(lst, key = itemgetter(*key))
    self.result = [(k, list(v)) for k, v in groupby(sort, itemgetter(*key))]

key = ["origin"]

grp = group(lst, key).result

out = [dict(zip([*key, "cnt", "med_dist", "avg_time"], 
                [x[0], 
                 len(x[1]), 
                 nanmedian([i["distance"] for i in x[1]]), 
                 round(nanmean([i["air_time"] for i in x[1]]), 2)])) for x in grp]

print(tabulate(out, headers = "keys"))
#  avg_time    cnt  origin      med_dist
#----------  -----  --------  ----------
#    187.61     18  EWR             1044
#    177.07     15  JFK             1074
#    159.71     17  LGA             1020

key = ["year", "month", "origin"]

grp = group(lst, key).result

out = [dict(zip([*key, "cnt", "med_dist", "avg_time"], 
                [*x[0], 
                 len(x[1]), 
                 nanmedian([i["distance"] for i in x[1]]), 
                 round(nanmean([i["air_time"] for i in x[1]]), 2)])) for x in grp]

print(tabulate(out, headers = "keys"))
#  avg_time  origin      cnt    month    med_dist    year
#----------  --------  -----  -------  ----------  ------
#    187.61  EWR          18        1        1044    2013
#    177.07  JFK          15        1        1074    2013
#    159.71  LGA          17        1        1020    2013
