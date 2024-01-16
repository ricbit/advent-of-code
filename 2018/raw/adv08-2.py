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

def parse(data, pos):
  children = data[pos]
  meta = data[pos + 1]
  print(children, meta, pos)
  ans = 0
  pos += 2
  if children == 0:
    for i in range(meta):
      ans += data[pos + i]
    pos += meta
  else:
    ch = []
    for i in range(children):
      cmeta, pos = parse(data, pos)
      ch.append(cmeta)
    print(ch)
    for i in range(meta):
      if data[pos + i] - 1 < len(ch):
        ans += ch[data[pos + i] - 1]
    pos += meta
  return ans, pos

data = aoc.ints(sys.stdin.read().strip().split())
aoc.cprint(parse(data, 0)[0])
