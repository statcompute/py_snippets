import timeit, more_itertools, pydash, underscore, cytoolz, functional

l = [{'year': 1, 'acct': 1, 'x': 'x1'}, {'year': 1, 'acct': 2, 'x': 'x2'}] * 10000

# Expected Output: 
# [{'year': 1, 'acct': 1, 'x': 'x1'}, {'year': 1, 'acct': 2, 'x': 'x2'}]

if __name__ == '__main__':
  n = 3
  r = 10
  t1 = timeit.repeat(stmt   = "[dict(t) for t in {tuple(d.items()) for d in l}]",
                     setup  = "from __main__ import l",
                     number = n, repeat = r)
  t2 = timeit.repeat(stmt   = "[i for n, i in enumerate(l) if i not in l[n + 1:]]",
                     setup  = "from __main__ import l",
                     number = n, repeat = r)
  t3 = timeit.repeat(stmt   = "list({frozenset(item.items()): item for item in l}.values())",
                     setup  = "from __main__ import l",
                     number = n, repeat = r)
  t4 = timeit.repeat(stmt   = "[dict(i) for i in cytoolz.unique([tuple(i.items()) for i in l])]",
                     setup  = "from __main__ import l, cytoolz",
                     number = n, repeat = r)
  t5 = timeit.repeat(stmt   = "[dict(i) for i in functional.seq([tuple(i.items()) for i in l]).distinct()]",
                     setup  = "from __main__ import l, functional",
                     number = n, repeat = r)
  t6 = timeit.repeat(stmt   = "list(more_itertools.unique_everseen(l))",
                     setup  = "from __main__ import l, more_itertools",
                     number = n, repeat = r)
  t7 = timeit.repeat(stmt   = "underscore._.uniq(l)",
                     setup  = "from __main__ import l, underscore",
                     number = n, repeat = r)
  t8 = timeit.repeat(stmt   = "pydash.uniq(l)",
                     setup  = "from __main__ import l, pydash",
                     number = n, repeat = r)

  print("Remove Duplicates Benchmarking:", 
    "\n set                            :", str("{:.8f}".format(min(t1))) + " - " + str("{:.8f}".format(max(t1))), 
    "\n list comprehension             :", str("{:.8f}".format(min(t2))) + " - " + str("{:.8f}".format(max(t2))), 
    "\n frozenset                      :", str("{:.8f}".format(min(t3))) + " - " + str("{:.8f}".format(max(t3))), 
    "\n cytoolz.unique                 :", str("{:.8f}".format(min(t4))) + " - " + str("{:.8f}".format(max(t4))), 
    "\n functional.seq                 :", str("{:.8f}".format(min(t5))) + " - " + str("{:.8f}".format(max(t5))), 
    "\n more_itertools.unique_everseen :", str("{:.8f}".format(min(t6))) + " - " + str("{:.8f}".format(max(t6))),
    "\n underscore._.uniq              :", str("{:.8f}".format(min(t7))) + " - " + str("{:.8f}".format(max(t7))), 
    "\n pydash.uniq                    :", str("{:.8f}".format(min(t8))) + " - " + str("{:.8f}".format(max(t8))))

# Remove Duplicates Benchmarking:
#  set                            : 0.01445410 - 0.02452520
#  list comprehension             : 0.92194630 - 0.99189070
#  frozenset                      : 0.01971170 - 0.02251440
#  cytoolz.unique                 : 0.03398420 - 0.03594400
#  functional.seq                 : 0.01791830 - 0.03209410
#  more_itertools.unique_everseen : 0.01833930 - 0.02351100
#  underscore._.uniq              : 0.83479710 - 0.95693390
#  pydash.uniq                    : 0.01862020 - 0.02926500
