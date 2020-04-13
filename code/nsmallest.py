import heapq, timeit

portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}] * 1000

def nsmallest(n, seq, key):
  return(sorted(seq, key = key)[0:n])

# Expected Output:
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}]

if __name__ == '__main__':
  n = 10
  r = 100
  t1 = timeit.repeat(stmt   = "nsmallest(1, portfolio, key = lambda x: x['price'])",
                     setup  = "from __main__ import portfolio, nsmallest",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "heapq.nsmallest(1, portfolio, key = lambda x: x['price'])",
                     setup  = "from __main__ import portfolio, heapq",
                     number = n, repeat = r)

  print("Benchmarks: Find The Smallest Value", 
    "\n sort: ", str("{:.8f}".format(min(t1))) + " - " + str("{:.8f}".format(max(t1))), 
    "\n heap: ", str("{:.8f}".format(min(t2))) + " - " + str("{:.8f}".format(max(t2))))

# Benchmarks: Find The Smallest Value
#  sort:  0.00534900 - 0.00943570
#  heap:  0.00405760 - 0.00715450
