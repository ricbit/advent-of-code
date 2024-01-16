import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

line = sys.stdin.read().strip()
while True:
  for i in range(len(line) - 1):
    if abs(ord(line[i]) - ord(line[i + 1])) == abs(ord('A') - ord('a')):
      line = line[:i] + line[i + 2:]
      break
  else:
    aoc.cprint(len(line))
    break
