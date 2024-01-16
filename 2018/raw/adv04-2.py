import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def minutes(s):
  h, m = s.split(":")
  return int(h) * 60 + int(m)

lines = [line.strip() for line in sys.stdin]
lines.sort()
guards = []
for line in lines:
  q = aoc.retuple("date time action", r"\[(.*?) (.*?)\] (wakes up|falls|Guard #\d+)", line)
  guards.append(q)
mins = aoc.ddict(lambda: aoc.ddict(lambda: 0))
current = 0
total = aoc.ddict(lambda: 0)
for k, v in itertools.groupby(guards, key=lambda q:q.date):
  sleep = {}
  for q in v:
    match q.action:
      case "wakes up":
       d = minutes(q.time) - minutes(sleep[current])
       print(minutes(sleep[current]), minutes(q.time))
       for i in range(minutes(sleep[current]), minutes(q.time)):
          mins[current][i] += 1
       total[current] += d
      case "falls":
        sleep[current] = q.time
      case guard:
        current = int(re.search(r"#(\d+)", guard).group(1))
guilty = max(total.keys(), key=lambda g: total[g])        
aoc.cprint(guilty * max(mins[guilty].keys(), key=lambda x:mins[guilty][x]))
sleepy = max(mins.keys(), key=lambda x: max(mins[x].values()))
minmax = max(mins[sleepy].keys(), key=lambda x: mins[sleepy][x])
aoc.cprint(sleepy * minmax)
