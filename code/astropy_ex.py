from astropy.io import ascii
 
from astropy.table import Table, join
 
from numpy import nanmean, nanmedian, array, sort
 
tbl1 = ascii.read("Downloads/nycflights.csv", format = "csv")
 
### SUBSETTING
sel_cols = ["origin", "dest", "distance", "dep_delay", "carrier"]
 
tbl2 = tbl1[sel_cols][range(10)]
 
tbl2.info
#   name   dtype
#--------- -----
#   origin  str3
#     dest  str3
# distance int64
#dep_delay int64
#  carrier  str2
 
### FILTERING ###
tbl2[list(i["carrier"] == "UA" and i["origin"] == 'EWR' for i in tbl2)]
#origin dest distance dep_delay carrier
#------ ---- -------- --------- -------
#   EWR  IAH     1400         2      UA
#   EWR  ORD      719        -4      UA
 
tbl2[(tbl2["carrier"] == "UA") & (tbl2["origin"] == "EWR")]
#origin dest distance dep_delay carrier
#------ ---- -------- --------- -------
#   EWR  IAH     1400         2      UA
#   EWR  ORD      719        -4      UA
 
### FILTER BY GROUPS ###
vstack(map(lambda x: x[(x["carrier"] == "UA") & (x["origin"] == "EWR")],
           tbl2.group_by(sort(array(range(len(tbl2))) % 2)).groups))
#origin dest distance dep_delay carrier
#------ ---- -------- --------- -------
#   EWR  IAH     1400         2      UA
#   EWR  ORD      719        -4      UA
 
### GROUPING ###
grp = tbl2.group_by("origin")
 
### AGGREGATING ###
agg1 = Table(grp['origin', 'distance'].groups.aggregate(nanmedian), names = ["origin", "med_dist"])
#origin med_dist
#------ --------
#   EWR   1065.0
#   JFK   1089.0
#   LGA    747.5
 
agg2 = Table(grp['origin', 'dep_delay'].groups.aggregate(nanmean), names = ["origin", "avg_delay"])
#origin      avg_delay
#------ -------------------
#   EWR -2.3333333333333335
#   JFK -0.6666666666666666
#   LGA               -1.75
 
### JOINING ###
join(agg1, agg2, join_type = "inner", keys = "origin")
#origin med_dist      avg_delay
#------ -------- -------------------
#   EWR   1065.0 -2.3333333333333335
#   JFK   1089.0 -0.6666666666666666
#   LGA    747.5               -1.75
