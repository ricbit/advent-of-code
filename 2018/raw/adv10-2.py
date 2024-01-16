import sys
import string
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(data):
  tps = [[q.px, q.py] for q in data]
  for i in range(100000):
    ps = set(tuple(x) for x in tps)
    b = aoc.bounds(ps)
    if b.maxy - b.miny < 100 and b.maxx - b.minx < 100:
      print(f"\n{i}\n")
      for y in range(b.miny, b.maxy + 1):
        line = []
        for x in range(b.minx, b.maxx + 1):
          line.append("#" if (y, x) in ps else ".")
        print("".join(line))
    for i in range(len(data)):
      tps[i][0] += data[i].vx
      tps[i][1] += data[i].vy

points = aoc.retuple_read("py_ px_ vy_ vx_",
    r".*?<(.*?), (.*)?>.*?<(.*?), (.*?)>")
aoc.cprint(solve(points))
