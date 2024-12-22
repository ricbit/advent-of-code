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

def secret(n):
  while True:
    mult = n * 64
    f = mult ^ n
    n = f % 16777216
    mult = n // 32
    f = n ^ mult
    n = f % 16777216
    mult = n * 2048
    f = mult ^ n
    n = f % 16777216
    yield n

def banana(n):
  for x in secret(n):
    yield x % 10

def change(n):
  prev = n % 10
  for x in banana(n):
    yield x - prev
    prev = x

def get_prefix(n, size):
  prefix = deque([])
  ans = aoc.ddict(lambda: set())
  for i, (value, vchange) in enumerate(zip(banana(n), change(n))):
    prefix.append(vchange)
    if i >= 3:
      #print(value, prefix)
      if tuple(prefix) not in ans:
          ans[tuple(prefix)].add(value)
      prefix.popleft()
    if i == size - 2:
      break
  return {p: max(values) for p, values in ans.items()}

def solve(data):
  prefix = []
  allseqs = set()
  for line in data:
    #print(line)
    x = get_prefix(line, 2001)
    prefix.append(x)
    allseqs.update(x.keys())
  maxvalue = 0
  for i, seq in enumerate(allseqs):
    if i % 10 == 0:
      print(i)
    x = sum(p.get(seq, 0) for p in prefix)
    if x > maxvalue:
      maxvalue = x
      bestseq = seq
  return maxvalue, bestseq

# not 2095
data = list(aoc.flatten(aoc.ints_read()))
print(data)
aoc.cprint(solve(data))
