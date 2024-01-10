import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

lines = [line.strip() for line in sys.stdin]
ans = 0
for line in lines:
  print(line)
  for a in itertools.combinations([int(i) for i in line.strip().split()], 2):
    if max(a) % min(a) == 0:
      print(a)
      ans += max(a) / min(a)
      break
aoc.cprint(ans)
