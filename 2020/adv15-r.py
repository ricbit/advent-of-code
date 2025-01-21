import sys
import aoc

def sequence(values, target):
  vlink = [(i, None) for i, v in enumerate(values)]
  vhash = [None] * 50000000
  for i, v in enumerate(values):
    vhash[v] = i
  vlast = vlink[-1]
  for _ in range(len(values), target):
    i, prev = vlast
    if prev is not None:
      new_value = i - prev
      vlast = (i + 1, vhash[new_value])
      vhash[new_value] = i + 1
    else:
      vlast = (i + 1, vhash[0])
      vhash[0] = i + 1
  return aoc.first(k for k, v in enumerate(vhash) if v == vlast[0])

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(sequence(data, 2020))
aoc.cprint(sequence(data, 30000000))
