import sys
import re
import itertools
import math
import aoc
from collections import *

ans = 0
numbers = [map(int, line.split()) for line in sys.stdin]
tnumbers = zip(*numbers)
for a, b, c in itertools.batched(aoc.flatten(tnumbers), 3):
  if a < b + c and b < a + c and c < a + b:
    ans += 1
aoc.cprint(ans)
  
