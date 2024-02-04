import sys
import re
import itertools
import math
import aoc
from collections import *

ans = 0
for line in sys.stdin:
  a, b, c = map(int, line.split())
  if a < b + c and b < a + c and c < a + b:
    ans += 1
aoc.cprint(ans)
  
