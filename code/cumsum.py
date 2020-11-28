cumsum = lambda x: [sum(x[0:(i + 1)]) for i in range(len(x))]

cumsum(range(10))
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
