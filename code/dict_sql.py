from astropy.io.ascii import read
 
selected = ["origin", "dep_delay", "distance"]
 
csv = read("Downloads/nycflights.csv", format = 'csv', data_end = 11)[selected]
 
lst = map(lambda x: dict(zip(x.colnames, x)), csv)
 
from dataset import connect
 
### CREATE IN-MEMORY SQLITE DB ###
db = connect('sqlite:///:memory:', row_type = dict)
 
tbl = db.create_table("tbl", primary_id = False)
 
tbl.insert_many(lst)
 
list(db.query("select * from tbl limit 3"))
# [{u'dep_delay': 2, u'distance': 1400, u'origin': u'EWR'},
#  {u'dep_delay': 4, u'distance': 1416, u'origin': u'LGA'},
#  {u'dep_delay': 2, u'distance': 1089, u'origin': u'JFK'}]
 
sum1 = db.create_table("sum1", primary_id = False)
 
from numpy import nanmedian
 
sum1.insert_many(
  map(lambda x: dict(origin = x,
                     med_dist = nanmedian([i["distance"] for i in
                       db.query("select distance from tbl where origin = :origin", {"origin": x})])),
      [i["origin"] for i in db.query("select distinct origin from tbl")]))
 
sum2 = db.create_table("sum2", primary_id = False)
 
sum2.insert_many(list(db.query("select origin, ROUND(AVG(dep_delay), 2) as avg_delay from tbl group by origin")))
 
list(db.query("select a.*, b.avg_delay from sum1 as a, sum2 as b where a.origin = b.origin"))
#[{u'avg_delay': -2.33, u'med_dist': 1065.0, u'origin': u'EWR'},
# {u'avg_delay': -1.75, u'med_dist': 747.5, u'origin': u'LGA'},
# {u'avg_delay': -0.67, u'med_dist': 1089.0, u'origin': u'JFK'}]
