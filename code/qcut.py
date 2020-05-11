def qcut(x, n):
  """
  The function to discretize a numeric vector into n pieces based on quantiles

  Parameters:
    x: A numeric vector.
    n: An integer indicating the number of categories to discretize.

  Returns:
    A list of numeric values to divide the vector x into n categories.

  Example:
    qcut(range(10), 3)
    # [3, 6]
  """

  _q = numpy.linspace(0, 100, n, endpoint = False)[1:]
  _x = [_ for _ in x if not numpy.isnan(_)]
  _c = numpy.unique(numpy.percentile(_x, _q, interpolation = "lower"))
  return([_ for _ in _c])

  
qcut(range(10), 3)
# [3, 6]

qcut(range(10), 5)
# [1, 3, 5, 7]

for i in numpy.unique([qcut(range(100), _) for _ in numpy.arange(2, 10)]):
  print(i)
# [11, 22, 32, 44, 55, 65, 76, 88]
# [12, 24, 37, 49, 61, 74, 86]
# [14, 28, 42, 56, 70, 84]
# [16, 33, 49, 66, 82]
# [19, 39, 59, 79]
# [24, 49, 74]
# [33, 66]
# [49]
