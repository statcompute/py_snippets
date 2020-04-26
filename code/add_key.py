import cytoolz, fnc, timeit

prices = [{'name':  'IBM', 'shares': 100, 'price':  91.11},
          {'name': 'AAPL', 'shares':  50, 'price': 543.22},
          {'name':   'FB', 'shares': 200, 'price':  21.09},
          {'name':  'HPQ', 'shares':  35, 'price':  31.75},
          {'name': 'YHOO', 'shares':  45, 'price':  16.35},
          {'name': 'ACME', 'shares':  75, 'price': 115.65}] 


fn = lambda d: {"ticker": "TICKER: " + d["name"], "amount": round(d["shares"] * d["price"])}

[cytoolz.merge(p, fn(p)) for p in prices]

[dict(p, **fn(p)) for p in prices]

[{**p, **fn(p)} for p in prices]

[fnc.merge(p, fn(p)) for p in prices]

[(lambda d: [d2 := d.copy(), d2.update(fn(d2))])(p)[0] for p in prices]

# Expected Output:
# {'name': 'IBM', 'shares': 100, 'price': 91.11, 'ticker': 'TICKER: IBM', 'amount': 9111}
# {'name': 'AAPL', 'shares': 50, 'price': 543.22, 'ticker': 'TICKER: AAPL', 'amount': 27161}
# {'name': 'FB', 'shares': 200, 'price': 21.09, 'ticker': 'TICKER: FB', 'amount': 4218}
# {'name': 'HPQ', 'shares': 35, 'price': 31.75, 'ticker': 'TICKER: HPQ', 'amount': 1111}
# {'name': 'YHOO', 'shares': 45, 'price': 16.35, 'ticker': 'TICKER: YHOO', 'amount': 736}
# {'name': 'ACME', 'shares': 75, 'price': 115.65, 'ticker': 'TICKER: ACME', 'amount': 8674}

if __name__ == '__main__':
  n = 10
  r = 100
  l = 1000
  t1 = timeit.repeat(stmt   = "[cytoolz.merge(p, fn(p)) for p in prices" + " * " + str(l) + "]",
                     setup  = "from __main__ import prices, fn, cytoolz",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "[dict(p, **fn(p)) for p in prices" + " * " + str(l) + "]",
                     setup  = "from __main__ import prices, fn",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt   = "[{**p, **fn(p)} for p in prices" + " * " + str(l) + "]",
                     setup  = "from __main__ import prices, fn",
                     number = n, repeat = r)
  t4 = timeit.repeat(stmt   = "[fnc.merge(p, fn(p)) for p in prices" + " * " + str(l) + "]",
                     setup  = "from __main__ import prices, fn, fnc",
                     number = n, repeat = r)
  t5 = timeit.repeat(stmt   = "[(lambda d: [d2 := d.copy(), d2.update(fn(d2))])(p)[0] for p in prices" + " * " + str(l) + "]",
                     setup  = "from __main__ import prices, fn",
                     number = n, repeat = r)

  print("Benchmarks: Add Keys to Dict", 
    "\n Cytoolz.Merge : ", str("{:.4f}".format(min(t1))) + " - " + str("{:.4f}".format(max(t1))), 
    "\n Dict          : ", str("{:.4f}".format(min(t2))) + " - " + str("{:.4f}".format(max(t2))),
    "\n Unpacking     : ", str("{:.4f}".format(min(t3))) + " - " + str("{:.4f}".format(max(t3))), 
    "\n Fnc.Merge     : ", str("{:.4f}".format(min(t4))) + " - " + str("{:.4f}".format(max(t4))),
    "\n Dict.Update   : ", str("{:.4f}".format(min(t5))) + " - " + str("{:.4f}".format(max(t5))))

#Benchmarks: Add Keys to Dict
# Cytoolz.Merge :  0.0354 - 0.0481
# Dict          :  0.0296 - 0.0477
# Unpacking     :  0.0287 - 0.0368
# Fnc.Merge     :  0.0446 - 0.0598
# Dict.Update   :  0.0424 - 0.0557
