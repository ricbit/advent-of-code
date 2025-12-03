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

sys.setrecursionlimit(300000)

def iter_jolts(s):
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      yield int(s[i] + s[j])

@functools.lru_cache(maxsize=None)
def search(s, pos, left):
  if left == 0:
    return 0
  if pos == len(s):
    return None
  skip = search(s, pos + 1, left)
  use = search(s, pos + 1, left - 1)
  match skip, use:
    case (None, None):
      return None
    case (a, None):
      return a
    case (None, b):
      return int(s[pos]) * 10 ** (left-1) + b
    case (a, b):
      return max(a, int(s[pos]) * 10 ** (left-1) + b)

def search2(s):
  cur = 0
  left = 2
  build = []
  
  for i in s:
    if cur == 0:
      build.append(i)
      left -= 1
    elif len(s)- cur == left:
      #print("break on ", list(s)[-left:], " previous ", build)
      build.extend(list(s)[cur:])
      break
    elif i > build[-1]:
      print(f"swap {i} with {build[-1]}, current {build}")
      build = build[:-1] + [i]
      print(f"after {build}")
    elif left > 0:
      build.append(i)
      left -= 1
    cur += 1
  return int("".join(build))

def solve(data):
  ans = 0
  for line in data:
    print(line, search(line.strip(), 0, 12))
    ans += search(line.strip(), 0, 12)
  return ans

data = sys.stdin.readlines()
aoc.cprint(solve(data))
