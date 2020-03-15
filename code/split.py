import cytoolz, timeit, numpy

def split(seq, chunks):
  v1, v2 = divmod(len(seq), chunks)
  n = [v1 + 1 if i < v2 else v1 for i in range(chunks)]
  g = zip(sum([[v1] * v2 for  v1, v2 in zip(range(len(n)), n)], []), seq)
  return([[i for _, i in v] for v in cytoolz.groupby(lambda x: x[0], g).values()])

split(range(10), 3)
# [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]

[list(i) for i in numpy.array_split(range(10), 3)]
# [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]

if __name__ == '__main__':
  n = 100
  r = 1000
  t1 = timeit.repeat(stmt = "split(range(100), 10)",
                     setup = "from __main__ import split, cytoolz",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt = "[list(i) for i in numpy.array_split(range(100), 10)]",
                     setup = "from __main__ import numpy",
                     number = n, repeat = r)
  print("Benchmarking:", 
    "\n split       :", str("{:.8f}".format(min(t1))) + " - " + str("{:.8f}".format(max(t1))), 
    "\n array_split :", str("{:.8f}".format(min(t2))) + " - " + str("{:.8f}".format(max(t2))))

# Benchmarking:
#  split       : 0.00222610 - 0.00392640
#  array_split : 0.00460760 - 0.00761110
