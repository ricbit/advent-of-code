import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def action(lines, pwd):
  for line in lines:
    match line.strip().split():
      case "move", _, p0, _, _, p1:
        a = pwd.pop(int(p0))
        pwd.insert(int(p1), a)
      case "swap", "position", p0, _, _, p1:
        pwd[int(p0)], pwd[int(p1)] = pwd[int(p1)], pwd[int(p0)]
      case "swap", "letter", a, _, _, b:
        for i in range(len(pwd)):
          if pwd[i] == a:
            pwd[i] = b
          elif pwd[i] == b:
            pwd[i] = a
      case "reverse", _, p0, _, p1:
        pwd[int(p0):int(p1) + 1] = pwd[int(p0):int(p1) + 1][::-1]
      case "rotate", "left", a, _:
        for i in range(int(a)):
          pwd = pwd[1:] + [pwd[0]]
      case "rotate", "right", a, _:
        for i in range(int(a)):
          pwd = [pwd[-1]] + pwd[:-1]
      case "rotate", "based", _, _, _, _, x:
        i = pwd.index(x)
        size = i + 1 + (1 if i >= 4 else 0)
        for j in range(int(size)):
          pwd = [pwd[-1]] + pwd[:-1]
  return "".join(pwd)

lines = [line.strip() for line in sys.stdin]
aoc.cprint(action(lines, list("abcdefgh"))) 
