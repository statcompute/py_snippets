def rollsum(l, w):
  return([sum(l[i:i + w]) for i in range(len(l) - w + 1)])
