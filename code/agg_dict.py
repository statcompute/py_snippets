from astropy.io.ascii import read
 
from numpy import nanmean, nanmedian, vectorize
 
selected = ["origin", "dep_delay", "distance"]
 
tbl = read("Downloads/nycflights.csv", format = 'csv', data_end = 11)[selected]
 
lst = map(lambda x: dict(zip(x.colnames, x)), tbl)
 
key = set([x["origin"] for x in lst])
 
grp = map(lambda x: {x: list(i for i in lst if i["origin"] == x)}, key)
 
### USING LIST COMPREHENSION ###
list({"origin"    : x.keys()[0],
      "flight_nbr": len(x.values()[0]),
      "med_dist"  : nanmedian([i["distance"] for i in x.values()[0]]),
      "avg_delay" : round(nanmean([i["dep_delay"] for i in x.values()[0]]), 2)
      } for x in grp)
 
### USING MAP() ALTERNATIVELY ###
map(lambda x: {"origin"    : x.keys()[0],
               "flight_nbr": len(x.values()[0]),
               "med_dist"  : nanmedian([i["distance"] for i in x.values()[0]]),
               "avg_delay" : round(nanmean([i["dep_delay"] for i in x.values()[0]]), 2)}, grp)
 
### USING VECTORIZE() ###
def agg(x):
  return({"origin"    : x.keys()[0],
          "flight_nbr": len(x.values()[0]),
          "med_dist"  : nanmedian([i["distance"] for i in x.values()[0]]),
          "avg_delay" : round(nanmean([i["dep_delay"] for i in x.values()[0]]), 2)})
 
list(vectorize(agg)(grp))
 
# RESULT:
# [{'avg_delay': -0.67, 'flight_nbr': 3, 'med_dist': 1089.0, 'origin': 'JFK'},
#  {'avg_delay': -2.33, 'flight_nbr': 3, 'med_dist': 1065.0, 'origin': 'EWR'},
#  {'avg_delay': -1.75, 'flight_nbr': 4, 'med_dist': 747.5, 'origin': 'LGA'}]
