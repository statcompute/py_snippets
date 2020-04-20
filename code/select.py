import itertools, timeit, pydash, fnc
 
portfolio = [{'name':  'IBM', 'shares': 100, 'price':  91.11}] + \
            [{'name': 'AAPL', 'shares':  50, 'price': 543.22},
             {'name':   'FB', 'shares': 200, 'price':  21.09},
             {'name':  'HPQ', 'shares':  35, 'price':  31.75},
             {'name': 'YHOO', 'shares':  45, 'price':  16.35},
             {'name': 'ACME', 'shares':  75, 'price': 115.65}] * 20000

fn = lambda x: x["shares"] == 100 and x["price"] > 90

### List Comprehension ###
[d for d in portfolio if fn(d)]

### Filter ###
list(filter(fn, portfolio))

### Map & Zip ###
[d for d, _ in zip(portfolio, map(fn, portfolio)) if _]

### Compress ###
list(itertools.compress(portfolio, map(fn, portfolio)))

### Expected Output ###
# [{'name': 'IBM', 'shares': 100, 'price': 91.11}]

if __name__ == '__main__':
  n = 10
  r = 100
  t1 = timeit.repeat(stmt   = "[d for d in portfolio if fn(d)]",
                     setup  = "from __main__ import portfolio, fn",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "list(filter(fn, portfolio))",
                     setup  = "from __main__ import portfolio, fn",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt   = "[d for d, _ in zip(portfolio, map(fn, portfolio)) if _]",
                     setup  = "from __main__ import portfolio, fn",
                     number = n, repeat = r)
  t4 = timeit.repeat(stmt   = "list(itertools.compress(portfolio, map(fn, portfolio)))",
                     setup  = "from __main__ import portfolio, fn, itertools",
                     number = n, repeat = r)
  t5 = timeit.repeat(stmt   = "pydash.filter_(portfolio, fn)",
                     setup  = "from __main__ import portfolio, fn, pydash",
                     number = n, repeat = r)
  t6 = timeit.repeat(stmt   = "list(fnc.filter(fn, portfolio))",
                     setup  = "from __main__ import portfolio, fn, fnc",
                     number = n, repeat = r)

  print("Benchmarks: Select", 
    "\n List Comprehension : ", str("{:.4f}".format(min(t1))) + " - " + str("{:.4f}".format(max(t1))), 
    "\n Filter             : ", str("{:.4f}".format(min(t2))) + " - " + str("{:.4f}".format(max(t2))),
    "\n Map & Zip          : ", str("{:.4f}".format(min(t3))) + " - " + str("{:.4f}".format(max(t3))), 
    "\n Itertools.Compress : ", str("{:.4f}".format(min(t4))) + " - " + str("{:.4f}".format(max(t4))),
    "\n Pydash.Filter_     : ", str("{:.4f}".format(min(t5))) + " - " + str("{:.4f}".format(max(t5))),
    "\n Fnc.Filter         : ", str("{:.4f}".format(min(t6))) + " - " + str("{:.4f}".format(max(t6))))

# Benchmarks: Select
# List Comprehension :  0.0827 - 0.1070
# Filter             :  0.0769 - 0.1439
# Map & Zip          :  0.0927 - 0.1659
# Itertools.Compress :  0.0758 - 0.1059
# Pydash.Filter_     :  0.6105 - 0.7596
# Fnc.Filter         :  0.0781 - 0.0961
