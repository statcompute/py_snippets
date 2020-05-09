def qcut(x, n):
  _q = numpy.linspace(0, 100, n, endpoint = False)[1:]
  _x = [_ for _ in x if not numpy.isnan(_)]
  _c = numpy.unique(numpy.percentile(_x, _q, interpolation = "lower"))
  return([_ for _ in _c])
  
qcut(range(10), 3)
# [3, 6]

qcut(range(10), 5)
# [1, 3, 5, 7]
