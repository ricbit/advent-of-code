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

def count(line):
  ans = []
  pos = 0
  while pos < len(line) - 1:
    if abs(ord(line[pos]) - ord(line[pos + 1])) == abs(ord('A') - ord('a')):
      pos += 2
    else:
      ans.append(line[pos])
      pos += 1
  if pos == len(line) - 1:
    ans.append(line[-1])
  return "".join(ans)

def long(line):
  while True:
    line2 = count(line)
    if line == line2:
      return line
    line = line2

def checkall(line):
  for c in string.ascii_lowercase:
    yield len(long(line.replace(c, "").replace(c.upper(), "")))

line = sys.stdin.read().strip()
aoc.cprint(len(long(line)))
aoc.cprint(min(checkall(line)))
