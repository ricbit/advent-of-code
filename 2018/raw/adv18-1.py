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

def solve(t):
  for i in range(10):
    t2 = copy.deepcopy(t)
    for j, i in t.iter_all():
      ground, tree, lumber = 0, 0, 0
      for jj, ii in t.iter_neigh8(j, i):
        match t[jj][ii]:
          case ".":
            ground += 1
          case "|":
            tree += 1
          case "#":
            lumber += 1
      if t[j][i] == "." and tree >= 3:
        t2[j][i] = "|"
      elif t[j][i] == "|" and lumber >= 3:
        t2[j][i] = "#"
      elif t[j][i] == "#":
        if not (lumber >= 1 and tree >= 1):
          t2[j][i] = "."
    t = t2
    for line in t.table:
      print("".join(line))
    print()
  tree, lumber = 0, 0
  for j, i in t.iter_all():
    if t[j][i] == "#":
      lumber += 1
    elif t[j][i] == "|":
      tree += 1
  return tree * lumber

t = aoc.Table.read()
aoc.cprint(solve(t))
