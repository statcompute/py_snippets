import heapq, cytoolz, timeit

prices = [{'name': 'IBM', 'shares': 100, 'price': 92},
          {'name': 'IBM', 'shares': 100, 'price': 91},
          {'name': 'HPQ', 'shares': 200, 'price': 32},
          {'name': 'HPQ', 'shares': 200, 'price': 31}] * 1000

def dedup_by1(seq, by_key, sort_key):
  grp = cytoolz.groupby(by_key, seq)
  return([a for a, *_ in [heapq.nsmallest(1, i, key = lambda x: x[sort_key]) for i in grp.values()]])

def dedup_by2(seq, by_key, sort_key):
  grp = cytoolz.groupby(by_key, seq)
  return([sorted(i, key = lambda x: x[sort_key])[0] for i in grp.values()])

def dedup_by3(seq, by_key, sort_key):
  grp = cytoolz.groupby(by_key, seq)
  return([min(i, key = lambda x: x[sort_key]) for i in grp.values()])

if __name__ == '__main__':
  n = 10
  r = 100
  t1 = timeit.repeat(stmt   = "dedup_by1(prices, ['name', 'shares'], 'price')",
                     setup  = "from __main__ import prices, heapq, cytoolz, dedup_by1",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "dedup_by2(prices, ['name', 'shares'], 'price')",
                     setup  = "from __main__ import prices, cytoolz, dedup_by2",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt   = "dedup_by3(prices, ['name', 'shares'], 'price')",
                     setup  = "from __main__ import prices, cytoolz, dedup_by3",
                     number = n, repeat = r)

  print("Benchmarks: Dedup by Key", 
    "\n heap: ", str("{:.8f}".format(min(t1))) + " - " + str("{:.8f}".format(max(t1))), 
    "\n sort: ", str("{:.8f}".format(min(t2))) + " - " + str("{:.8f}".format(max(t2))),
    "\n min : ", str("{:.8f}".format(min(t3))) + " - " + str("{:.8f}".format(max(t3))))

# Benchmarks: Dedup by Key
#  heap:  0.00518740 - 0.01293920
#  sort:  0.00546160 - 0.01049960
#  min :  0.00480080 - 0.00863380
