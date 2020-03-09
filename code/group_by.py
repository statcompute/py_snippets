import pandas, clj, cytoolz, itertools, operator, collections, timeit

file = "nycflights.csv"

n = 10000

col = ["year", "month", "origin", "dest", "carrier", "air_time"] 

pdf = pandas.read_csv(file, nrows = n)[col] 

### lst = [d.to_dict() for _, d in pdf.iterrows()]
lst = pdf.to_dict(orient = 'records')

grp = ["year", "origin"]

grp_fn = operator.itemgetter(*grp)

lst1 = clj.group_by(grp_fn, lst)

lst2 = cytoolz.groupby(grp, lst)

lst3 = dict((k, list(g)) for k, g in itertools.groupby(sorted(lst, key = grp_fn), key = grp_fn))

def lst2dd(lst, key):
  fn = operator.itemgetter(*key)	
  dt = [(fn(d), d) for d in lst]
  dd = collections.defaultdict(list)
  for k, v in dt:
    dd[k].append(v)
  return(dd)

lst4 = dict(lst2dd(lst, grp))

lst1 == lst2 == lst3 == lst4
# True

if __name__ == '__main__':
  n = 10
  r = 100
  t1 = timeit.repeat(stmt = "clj.group_by(grp_fn, lst)",
                     setup = "from __main__ import clj, grp_fn, lst",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt = "cytoolz.groupby(grp, lst)",
                     setup = "from __main__ import cytoolz, grp, lst",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt = "dict((k, list(g)) for k, g in itertools.groupby(sorted(lst, key = grp_fn), key = grp_fn))",
                     setup = "from __main__ import itertools, grp_fn, lst",
                     number = n, repeat = r)
  t4 = timeit.repeat(stmt = "dict(lst2dd(lst, grp))",
                     setup = "from __main__ import lst2dd, grp, lst",
                     number = n, repeat = r)
  print("Benchmarking:", 
    "\n clj.group_by            :", str("{:.8f}".format(min(t1), 4)) + " - " + str("{:.8f}".format(max(t1), 4)), 
    "\n cytoolz.groupby         :", str("{:.8f}".format(min(t2), 4)) + " - " + str("{:.8f}".format(max(t2), 4)), 
    "\n itertools.groupby       :", str("{:.8f}".format(min(t3), 4)) + " - " + str("{:.8f}".format(max(t3), 4)), 
    "\n collections.defaultdict :", str("{:.8f}".format(min(t4), 4)) + " - " + str("{:.8f}".format(max(t4), 4)))

# Benchmarking:
#  clj.group_by            : 0.02260390 - 0.03245390
#  cytoolz.groupby         : 0.01360830 - 0.01963830
#  itertools.groupby       : 0.05548110 - 0.06711240
#  collections.defaultdict : 0.03634000 - 0.05207950
