import sys
import itertools
import math
import aoc
import numpy as np

def from_digits(seq, n):
  return "".join(str(int(i)) for i in seq[:n])

def solve1(data):
  data = np.array(data)
  x = np.arange(1, len(data) + 1)
  y = np.arange(1, len(data) + 1)
  xx, yy = np.meshgrid(x, y)
  mat = np.round(np.sin(np.floor(xx / yy) * math.pi / 2))
  for _ in range(100):
    data = np.abs(mat @ data) % 10
  return from_digits(data, 8)

def solve2(data):
  newdata = np.zeros(len(data), dtype=np.uint32)
  data = np.flip(np.array(data, dtype=np.uint32))
  for _ in range(100):
    data.cumsum(out=newdata)
    newdata = np.abs(newdata) % 10
    data, newdata = newdata, data
  return np.flip(data)

data = aoc.ints(sys.stdin.read().strip())
aoc.cprint(solve1(data))
data *= 10000
start = int(from_digits(data, 7))
data = data[start:]
aoc.cprint(from_digits(solve2(data), 8))
