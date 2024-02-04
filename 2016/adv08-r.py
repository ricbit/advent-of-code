import sys
import aoc
import numpy as np

m = np.zeros((6, 50))
for line in sys.stdin:
  t = aoc.retuple("name p1_ p2_", r"(rect|.*?column|.*?row).*?(\d+).*?(\d+)", line)
  match t.name:
    case "rect":
      m[0:t.p2, 0:t.p1] = 1
    case "rotate column": 
      m[:,t.p1] = np.roll(m[:,t.p1], t.p2)
    case "rotate row": 
      m[t.p1,:] = np.roll(m[t.p1,:], t.p2)
aoc.cprint(np.count_nonzero(m))
for line in m:
  print("".join(("*" if c == 1 else " ") for c in line))
