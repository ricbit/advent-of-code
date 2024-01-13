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

def conv(s):
  return [int(i) for i in s.split(",")]

def simulate(p):
  avail = set(range(len(p)))
  for i in range(5000):
    col = aoc.ddict(lambda: [])
    for j in range(len(p)):
      if j in avail:
        col[tuple(p[j][0])].append(j)
    for k, v in col.items():
      if len(v) > 1:
        for vv in v:
          avail.remove(vv)
        print(i, v)
    for j in range(len(p)):
      for k in range(3):
        p[j][1][k] += p[j][2][k]
    for j in range(len(p)):
      for k in range(3):
        p[j][0][k] += p[j][1][k]
  return len(avail)

lines = [line.strip() for line in sys.stdin]
particles = []
for line in lines:
  q=aoc.retuple("p v a", r"p=<(.*?)>, v=<(.*?)>, a=<(.*?)>", line)
  particles.append([conv(q.p), conv(q.v), conv(q.a)])
print(simulate(particles))
#aoc.cprint(ans)
