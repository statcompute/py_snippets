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

