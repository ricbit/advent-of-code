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
from multiprocessing import Pool

def pattern(size):
  first = True
  for b in itertools.cycle([0, 1, 0, -1]):
    for r in range(size + 1):
      if not first:
        yield b
      first = False

def conv(x):
  return abs(x) % 10


def extrapolate(it, goal, calc):
  seen, inv = {}, {}
  last_key = []
  for time, key in enumerate(it, 1):
    #last_key.append(key)
    #last_key = last_key[-8:]
    last_key = key
    print(time)
    if last_key in seen:
      period = time - seen[last_key]
      print(f"period {period} seen {seen[last_key]}")
      return period
    else:
      seen[last_key] = time
      inv[time] = calc(last_key)

def solve(data):
  #offset = int("".join(str(i) for i in data[:7]))
  print("yes")
  data *= 1
  size = len(data)
  for t in range(100000):
    print(f"data {data}")
    yield tuple(data)
    ans = []
    for d in range(size):
      ans.append(conv(sum(a * b for a, b in zip(data, pattern(d)))))
    data = ans
  #return "".join(str(i) for i in data[offset:offset+8])

def solve2(data):
  return extrapolate(solve(data), 0, lambda x:x)

def near(x):
  return math.floor(x + 0.5)

def wavelet(stage):
  for i in itertools.count(1):
    yield near(math.sin(math.pi / 2 * math.floor(i / stage)))

ticks = 0
@functools.lru_cache(maxsize=None)
def search(digit, stage):
  if stage == 0:
    return data[digit]
  ans = 0
  global ticks
  ticks += 1
  for i, seq in zip(range(len(data)), wavelet(digit + 1)):
    if seq != 0:
      ans += search(i, stage - 1) * seq
  return abs(ans) % 10

def build(data, start, size, stage):
  ans = []
  for i in range(size):
    ans.append(str(search(start + i, stage)))
  return "".join(ans)

def step(data):
  newdata = [0] * len(data)
  newdata[0] = sum(data)
  for i in range(1, len(data)):
    newdata[i] = newdata[i - 1] - data[i - 1]
  for i in range(len(data)):
    newdata[i] = abs(newdata[i]) % 10
  return newdata

data = aoc.ints(sys.stdin.read().strip())
data *= 10000
start = int("".join(str(i) for i in data[:7]).lstrip("0"))
data = data[start:]
for i in range(100):
  data = step(data)
aoc.cprint("".join(str(i) for i in data[:8]))
#print(ticks)
