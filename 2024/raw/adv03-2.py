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

def solve(data):
  return data

data = sys.stdin.read()
x = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data)
ans = 0
on = True
for a,b,c in x:
  if a.startswith("mul") and on:
    ans += int(b)*int(c)
  elif a == "don't()":
    on = False
  elif a == "do()":
    on = True
aoc.cprint(ans)
#aoc.cprint(sum(int(a)*int(b) for a,b in x))
