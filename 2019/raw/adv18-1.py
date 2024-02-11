import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass
from aoc.refintcode import IntCode

def encode(pos, keys):
  return (pos, "".join(sorted(keys)))

def heuristic(t, pos_keys, pos, col_keys, score):
  ans = score
  y, x = pos
  for j, i in pos_keys.values():
    if t[j][i] not in col_keys:
      ans = max(ans, score + abs(y - j) + abs(x - i))
  return ans

def solve(t):
  pos_keys = {}
  doors = {}
  for j, i in t.iter_all():
    if t[j][i] == "@":
      start = (j, i)
    elif t[j][i].isupper():
      doors[t[j][i]] = (j, i)
    elif t[j][i].islower():
      pos_keys[t[j][i]] = (j, i)
  print(pos_keys, doors, start)
  vnext = aoc.bq([(heuristic(t, pos_keys, start, set(), 0), 0, start, set())], size=6000)
  visited = set()
  tick = 0
  while vnext:
    old_h, score, pos, col_keys = vnext.pop()
    tick += 1
    if tick % 1000 == 0:
      print(tick, score, old_h, len(vnext))
    visited.add(encode(pos, col_keys))
    y, x = pos
    if len(col_keys) == len(pos_keys):
      return score
    for j, i in t.iter_neigh4(y, x):
      if t[j][i].islower():
        new_keys = col_keys.union(t[j][i])
        if encode((j, i), new_keys) not in visited:
          h = heuristic(t, pos_keys, (j, i), new_keys, score + 1) 
          vnext.push((h, score + 1, (j, i), new_keys))
      elif t[j][i].isupper():
        if t[j][i].lower() in col_keys:
          if encode((j, i), col_keys) not in visited:
            h = heuristic(t, pos_keys, (j, i), col_keys, score + 1) 
            vnext.push((h, score + 1, (j, i), col_keys))
      elif t[j][i] in "@." and encode((j, i), col_keys) not in visited:
        h = heuristic(t, pos_keys, (j, i), col_keys, score + 1) 
        vnext.push((h, score + 1, (j, i), col_keys))
  return None

t = aoc.Table.read()
aoc.cprint(solve(t))
