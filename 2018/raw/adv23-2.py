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

def solve1(nano):
  j = max(nano, key=lambda q:q.r)
  ans = 0
  for i in nano:
    if abs(j.x - i.x) + abs(j.y - i.y) + abs(j.z - i.z) <= j.r:
      ans += 1
  return ans

def bounds(series, calc):
  return [min(calc(q) - q.r for q in series), max(calc(q) + q.r for q in series)]

def qinside(q, vert, box):
  return (
      box[0][0] <= q.x + vert[0] <= box[0][1] and
      box[1][0] <= q.y + vert[1] <= box[1][1] and
      box[1][0] <= q.z + vert[2] <= box[2][1]
  )

def vinside(q, corner):
  return abs(q.x - corner[0]) + abs(q.y - corner[1]) + abs(q.z - corner[2]) <= q.r

def check(q, box):
  vertexes = [
      [q.r, 0, 0], [-q.r, 0, 0],
      [0, q.r, 0], [0, -q.r, 0],
      [0, 0, q.r], [0, 0, -q.r]
  ]
  return (
      any(qinside(q, vert, box) for vert in vertexes) or
      any(vinside(q, corner) for corner in itertools.product(*box))
  )

def count(nano, box):
  return -sum(check(q, box) for q in nano)

def partition(nano, box):
  vnext = [(count(nano, box), box)]
  while vnext:
    score, box = heapq.heappop(vnext)
    sides = [
       (box[0][1] - box[0][0] + 1, 0),
       (box[1][1] - box[1][0] + 1, 1),
       (box[2][1] - box[2][0] + 1, 2)
    ]
    sides.sort(reverse=True)
    if sides[0][0] == 1:
      return sum(box[i][0] for i in range(3))
    middle = sides[0][0] // 2
    side = sides[0][1]
    newbox1 = copy.deepcopy(box)
    newbox1[side][1] = newbox1[side][0] + middle - 1
    heapq.heappush(vnext, (count(nano, newbox1), newbox1))
    newbox2 = copy.deepcopy(box)
    newbox2[side][0] += middle 
    heapq.heappush(vnext, (count(nano, newbox2), newbox2))

data = [line.strip() for line in sys.stdin]
nano = aoc.retuple_read("x_ y_ z_ r_", r"pos=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, r=(\d+)", data)
aoc.cprint(solve1(nano))
box = [
  bounds(nano, lambda q: q.x),
  bounds(nano, lambda q: q.y),
  bounds(nano, lambda q: q.z)
]
aoc.cprint(partition(nano, box))
