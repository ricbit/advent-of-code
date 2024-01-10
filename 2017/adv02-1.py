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
  a = [int(i) for i in line.strip().split()]
  ans += max(a) - min(a)
aoc.cprint(ans)
