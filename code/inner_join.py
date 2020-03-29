import timeit, cytoolz, itertools, operator

lx = [{'year': 1, 'acct': 1, 'x': 'x1'}, {'year': 1, 'acct': 2, 'x': 'x2'},
      {'year': 1, 'acct': 3, 'x': 'x3'}, {'year': 1, 'acct': 4, 'x': 'x4'},
      {'year': 1, 'acct': 5, 'x': 'x5'}]

ly = [{'year': 1, 'acct': 3, 'y': 'y3'}, {'year': 1, 'acct': 4, 'y': 'y4'},
      {'year': 1, 'acct': 5, 'y': 'y5'}, {'year': 1, 'acct': 6, 'y': 'y6'},
      {'year': 1, 'acct': 7, 'y': 'y7'}]

key = ('year', 'acct')

key_fn = operator.itemgetter(*key)

list(dict(x, **y) for y in ly for x in lx if key_fn(x) == key_fn(y))

list(dict(x, **y) for x, y in cytoolz.join(key_fn, lx, key_fn, ly))

list(dict(x, **y) for x, y in itertools.product(lx, ly) if key_fn(x) == key_fn(y))

list(dict(_[0], **_[1]) for _ in cytoolz.groupby(key_fn, lx + ly).values() if len(_) > 1)

[cytoolz.merge(x, y) for x in lx for y in ly if key_fn(x) == key_fn(y)]

# OUTPUT:
# [{'acct': 3, 'x': 'x3', 'y': 'y3', 'year': 1},
#  {'acct': 4, 'x': 'x4', 'y': 'y4', 'year': 1},
#  {'acct': 5, 'x': 'x5', 'y': 'y5', 'year': 1}]

if __name__ == '__main__':
  n = 1000
  r = 1000
  t1 = timeit.repeat(stmt   = "list(dict(x, **y) for y in ly for x in lx if key_fn(x) == key_fn(y))",
                     setup  = "from __main__ import key_fn, lx, ly",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "list(dict(x, **y) for x, y in cytoolz.join(key_fn, lx, key_fn, ly))",
                     setup  = "from __main__ import cytoolz, key_fn, lx, ly",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt   = "list(dict(x, **y) for x, y in itertools.product(lx, ly) if key_fn(x) == key_fn(y))",
                     setup  = "from __main__ import itertools, key_fn, lx, ly",
                     number = n, repeat = r)
  t4 = timeit.repeat(stmt   = "list(dict(_[0], **_[1]) for _ in cytoolz.groupby(key_fn, lx + ly).values() if len(_) > 1)",
                     setup  = "from __main__ import cytoolz, key_fn, lx, ly",
                     number = n, repeat = r)
  t5 = timeit.repeat(stmt   = "[cytoolz.merge(x, y) for x in lx for y in ly if key_fn(x) == key_fn(y)]",
                     setup  = "from __main__ import cytoolz, key_fn, lx, ly",
                     number = n, repeat = r)
  print("Inner Join Benchmarking:", 
    "\n list comprehension :", str("{:.8f}".format(min(t1))) + " - " + str("{:.8f}".format(max(t1))), 
    "\n cytoolz.join       :", str("{:.8f}".format(min(t2))) + " - " + str("{:.8f}".format(max(t2))), 
    "\n itertools.product  :", str("{:.8f}".format(min(t3))) + " - " + str("{:.8f}".format(max(t3))), 
    "\n cytoolz.groupby    :", str("{:.8f}".format(min(t4))) + " - " + str("{:.8f}".format(max(t4))),
    "\n cytoolz.merge      :", str("{:.8f}".format(min(t5))) + " - " + str("{:.8f}".format(max(t5))))

#Inner Join Benchmarking:
# list comprehension : 0.00556100 - 0.00800710
# cytoolz.join       : 0.00271350 - 0.00450620
# itertools.product  : 0.00585470 - 0.00811770
# cytoolz.groupby    : 0.00297810 - 0.00462820
# cytoolz.merge      : 0.00570810 - 0.00783010

