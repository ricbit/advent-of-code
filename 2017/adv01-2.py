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

line = sys.stdin.read().strip()
ans = 0
for i, a in enumerate(line):
  if a == line[(i + len(line) // 2) % len(line)]:
    ans += int(a)
aoc.cprint(ans)
  
