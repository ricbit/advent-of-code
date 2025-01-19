import sys
import aoc

def sequence(values, target):
  vlink = [(v, i, None) for i, v in enumerate(values)]
  vhash = aoc.ddict(lambda: None)
  vhash.update({v: i for i, v in enumerate(values)})
  for _ in range(len(values), target):
    _, i, prev = vlink[-1]
    if prev is not None:
      new_value = i - prev
      vlink.append((new_value, i + 1, vhash[new_value]))
      vhash[new_value] = i + 1
    else:
      vlink.append((0, i + 1, vhash[0]))
      vhash[0] = i + 1
  return vlink[-1][0]

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(sequence(data, 2020))
aoc.cprint(sequence(data, 30000000))
