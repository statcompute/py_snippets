from astropy.io import ascii

import operator

col = ["year", "origin", "dest", "carrier", "air_time"]

tbl = ascii.read("nycflights.csv", format = 'csv', data_end = 11)[col]

lst = [dict(zip(r.colnames, r)) for r in tbl]

# {'year': 2013, 'dest': 'IAH', 'carrier': 'UA', 'origin': 'EWR', 'air_time': 227}
# {'year': 2013, 'dest': 'IAH', 'carrier': 'UA', 'origin': 'LGA', 'air_time': 227}
# {'year': 2013, 'dest': 'MIA', 'carrier': 'AA', 'origin': 'JFK', 'air_time': 160}

### SELECT ###

sel = ["origin", "dest", "carrier"]

[dict(zip(sel, operator.itemgetter(*sel)(d))) for d in lst]

[*map(lambda x: dict(zip(sel, [x[k] for k in sel])), lst)]

# {'carrier': 'UA', 'dest': 'IAH', 'origin': 'EWR'}
# {'carrier': 'UA', 'dest': 'IAH', 'origin': 'LGA'}
# {'carrier': 'AA', 'dest': 'MIA', 'origin': 'JFK'}

### SORT ###

key = ["origin", "air_time"]

sorted(lst, key = operator.itemgetter(*key))

sorted(lst, key = lambda x: [x[k] for k in key])

# {'year': 2013, 'dest': 'ORD', 'carrier': 'UA', 'origin': 'EWR', 'air_time': 150}
# {'year': 2013, 'dest': 'FLL', 'carrier': 'B6', 'origin': 'EWR', 'air_time': 158}
# {'year': 2013, 'dest': 'IAH', 'carrier': 'UA', 'origin': 'EWR', 'air_time': 227}
