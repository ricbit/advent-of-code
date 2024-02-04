import sys
import re
import itertools
import math
import aoc
from collections import *

lines = [line.strip() for line in sys.stdin]
tlines = [list(sorted(x)) for x in zip(*lines)]
message = []
for line in tlines:
  ans = []
  for k, v in itertools.groupby(line):
    ans.append((len(list(v)), k))
  message.append(max(ans)[1])
aoc.cprint("".join(message))

