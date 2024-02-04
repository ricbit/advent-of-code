import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def black(blist, source):
  valid = [source]
  for res in blist:
    new = []
    for v in valid:
      for i in v.sub(res):
        new.append(i)
    valid = new
  #return valid[0].begin
  return sum(len(i) for i in valid)


intervals = []
for line in sys.stdin:
  a, b = map(int, line.split("-"))
  intervals.append(aoc.Interval(a, b))
aoc.cprint(black(intervals, aoc.Interval(0, 0xFFFFFFFF)))
  
