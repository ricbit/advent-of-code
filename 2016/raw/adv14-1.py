import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def get(i, salt):
  value = salt + str(i)
  for i in range(2017):
    value = aoc.md5(value)
  return value

def search(salt):
  prev = [get(i, salt) for i in range(1000)]
  for i in itertools.count(): 
    char = re.match(r".*?(\w)\1\1", prev[i % 1000])
    if char is not None:
      char = char.group(1) * 5
      for j in range(1000):
        if i % 1000 != j and char in prev[j]:
          print(i)
          yield i
          break
    prev[i % 1000] = get(i + 1000, salt)

def count(salt):
  for i, value in enumerate(search(salt)):
    if i == 63:
      return value

salt = sys.stdin.read().strip()
#print(get(0, salt))
aoc.cprint(count(salt))
