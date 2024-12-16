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

def iter_round(t):
  out = t.copy()
  change = False
  for j, i in t.iter_all():
    if t[j][i] == "L":
      if all(t[jj][ii] != "#" for jj, ii in t.iter_neigh8(j, i)):
        out[j][i] = "#"
        change = True
    elif t[j][i] == "#":
      if sum(t[jj][ii] == "#" for jj, ii in t.iter_neigh8(j, i)) >= 4:
        out[j][i] = "L"
        change = True
  return out, change

def is_occupied(t, pos, cdir):
  while True:
    pos += cdir
    if not t.cvalid(pos):
      return False
    if t.get(pos) == "#":
      return True
    if t.get(pos) == "L":
      return False

def iter_round2(t):
  out = t.copy()
  change = False
  for j, i in t.iter_all():
    all_cdir = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
    count = 0
    if t[j][i] != ".":
      for cdir in all_cdir:
        count += is_occupied(t, j * 1j + i, cdir)
    if t[j][i] == "L" and count == 0:
      out[j][i] = "#"
      change = True
    elif t[j][i] == "#" and count >= 5:
      out[j][i] = "L"
      change = True
  return out, change


def solve(t):
  while (out := iter_round(t))[1]:
    t, change = out
  return sum(t[j][i] == "#" for j, i in t.iter_all())

def solve2(t):
  while (out := iter_round2(t))[1]:
    t, change = out
  return sum(t[j][i] == "#" for j, i in t.iter_all())

data = [list(line) for line in sys.stdin.read().splitlines()]
data = aoc.Table(data)
aoc.cprint(solve(data))
aoc.cprint(solve2(data))
