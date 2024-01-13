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
  for i in range(5000):
    order = []
    for j in range(len(particles)):
      for k in range(3):
        p[j][1][k] += p[j][2][k]
    for j in range(len(particles)):
      for k in range(3):
        p[j][0][k] += p[j][1][k]
      d = sum(abs(p[j][0][k]) for k in range(3))
      order.append((d, j))
    order.sort()
    print([b for a,b in order[:5]])



lines = [line.strip() for line in sys.stdin]
particles = []
for line in lines:
  q=aoc.retuple("p v a", r"p=<(.*?)>, v=<(.*?)>, a=<(.*?)>", line)
  particles.append([conv(q.p), conv(q.v), conv(q.a)])
print(simulate(particles))
#aoc.cprint(ans)
