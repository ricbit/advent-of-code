import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def get(line, i):
  if 0 <= i < len(line):
    return line[i]
  return "."

def search(line):
  ans = line.count(".")
  for _ in range(400000 - 1):
    new = []
    for i in range(len(line)):
      match (get(line, i - 1), get(line, i), get(line, i + 1)):
        case ("^", "^", ".") | (".", "^", "^") | (".", ".", "^") | ("^", ".", "."):
          new.append("^")
        case _:
          new.append(".")
    line = new
    ans += line.count(".")
  return ans

def count(big):
  ans = 0
  for line in big:
    ans += line.count(".")
  return ans

cline = sys.stdin.read().strip()
#cline = ".^^.^.^^^^"
aoc.cprint(str(search(cline)))
