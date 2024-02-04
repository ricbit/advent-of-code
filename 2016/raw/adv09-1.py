import sys
import re
import itertools
import math
import aoc
from collections import *

for line in sys.stdin:
  ans = []
  while line:
    t = aoc.retuple("prelude size_ rep_ rest", r"(.*?)(?:\((\d+)x(\d+)\)(.*))?$", line)
    if t.prelude:
      ans.append(t.prelude)
    if t.size is not None:
      ans.append(t.rest[:t.size] * t.rep)
      line = t.rest[t.size:]
    else:
      line = ""
  aoc.cprint(len("".join(ans)))

  
