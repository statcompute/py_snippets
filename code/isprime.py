def isprime(x):
  if x < 2:
    return(False)
  elif len([i for i in range(2, x) if x%i == 0]) == 0:
    return(True)
  else:
    return(False)
