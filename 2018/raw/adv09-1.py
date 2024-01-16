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

def solve(players, goal):
  m = aoc.bidi([0])
  m.values[0][0] = 0
  m.values[0][1] = 0
  pos = m.start
  score = [0] * players
  for i in range(1, 1 + goal): #itertools.count(1)
    if i % 23 != 0:
      pos = m.insert(m.next(pos), i)
    else:
      for j in range(7):
        pos = m.prev(pos)
      npos = m.prev(pos)
      score[i % players] += i + m.value(pos)
      print(score)
      m.remove(pos)
      pos = m.next(npos)
  return max(score)


data = sys.stdin.read().strip()
q = aoc.retuple("players_ goal_", r"(\d+).*?(\d+)", data)
aoc.cprint(solve(q.players, q.goal))
