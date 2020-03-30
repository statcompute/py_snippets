import timeit, cytoolz, collections, operator

lx = [{'year': 1, 'acct': 1, 'x': 'x1'}, {'year': 1, 'acct': 2, 'x': 'x2'},
      {'year': 1, 'acct': 3, 'x': 'x3'}, {'year': 1, 'acct': 4, 'x': 'x4'},
      {'year': 1, 'acct': 5, 'x': 'x5'}]

ly = [{'year': 1, 'acct': 3, 'y': 'y3'}, {'year': 1, 'acct': 4, 'y': 'y4'},
      {'year': 1, 'acct': 5, 'y': 'y5'}, {'year': 1, 'acct': 6, 'y': 'y6'},
      {'year': 1, 'acct': 7, 'y': 'y7'}]

key = ('year', 'acct')

def left_join1(lseq, rseq, key):
  key_fn = operator.itemgetter(*key)
  lr = [cytoolz.merge(_) for _ in cytoolz.groupby(key_fn, lseq + rseq).values()]
  return(sorted(list(filter(lambda d: key_fn(d) in [key_fn(l) for l in lseq], lr)), key = key_fn))

def left_join2(lseq, rseq, key):
  key_fn = operator.itemgetter(*key)
  return(sorted(list(dict(l, **r) for l, r in cytoolz.join(key_fn, lseq, key_fn, rseq, right_default = {})), key = key_fn))

def left_join3(lseq, rseq, key):
  key_fn = operator.itemgetter(*key)
  ddic = collections.defaultdict(dict)
  for k, v in [(key_fn(d), d) for d in lseq + rseq]:
    if k in [key_fn(l) for l in lseq]:
      ddic[k].update(v)
  return(sorted(list(ddic.values()), key = key_fn))

# OUTPUT:
# [{'acct': 1, 'x': 'x1', 'year': 1},
#  {'acct': 2, 'x': 'x2', 'year': 1},
#  {'acct': 3, 'x': 'x3', 'y': 'y3', 'year': 1},
#  {'acct': 4, 'x': 'x4', 'y': 'y4', 'year': 1},
#  {'acct': 5, 'x': 'x5', 'y': 'y5', 'year': 1}]

if __name__ == '__main__':
  n = 1000
  r = 1000
  t1 = timeit.repeat(stmt   = "left_join1(lx, ly, key)",
                     setup  = "from __main__ import key, lx, ly, left_join1, operator, cytoolz",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "left_join2(lx, ly, key)",
                     setup  = "from __main__ import key, lx, ly, left_join2, operator, cytoolz",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt   = "left_join3(lx, ly, key)",
                     setup  = "from __main__ import key, lx, ly, left_join3, operator, collections",
                     number = n, repeat = r)
  print("left Join Benchmarking:", 
    "\n cytoolz.groupby         :", str("{:.8f}".format(min(t1))) + " - " + str("{:.8f}".format(max(t1))), 
    "\n cytoolz.join            :", str("{:.8f}".format(min(t2))) + " - " + str("{:.8f}".format(max(t2))), 
    "\n collections.defaultdict :", str("{:.8f}".format(min(t3))) + " - " + str("{:.8f}".format(max(t3))))

# Left Join Benchmarking:
#  cytoolz.groupby         : 0.01200810 - 0.14574020
#  cytoolz.join            : 0.00553730 - 0.05955770
#  collections.defaultdict : 0.01256320 - 0.07409620
