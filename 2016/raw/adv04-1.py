import sys
import re
import itertools
import math
import aoc
from collections import *

ans = 0
for line in sys.stdin:
  t = aoc.retuple("x", "name number_ check", r"(.*)-(\d+)\[(.*)\]", line)
  h = Counter()
  for c in t.name:
    if c.islower():
      h[c] += 1
  chars = list(h.keys())
  chars.sort(key=lambda c: (-h[c], c))
  print("".join(chars[:5]), t.check)
  if "".join(chars[:5]) == t.check:
    ans += t.number
aoc.cprint(ans)
  
