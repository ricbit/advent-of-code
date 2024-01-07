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
for a, b in zip(line, line[1:] + line[0]):
  if a == b:
    ans += int(a)
aoc.cprint(ans)
  
