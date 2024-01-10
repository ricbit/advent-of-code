import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

def sumiter(m, j, i):
  return sum(m[(jj, ii)] for jj, ii in aoc.iter_neigh8(j, i))

def part1(goal):
  for j, i, value in aoc.spiral():
    if value == goal:
      return abs(j) + abs(i)

def part2(goal):
  for j, i, value in aoc.spiral(lambda m, j, i, cur: sumiter(m, j, i)):
    if value > goal:
      return value

goal = int(sys.stdin.read())
aoc.cprint(part1(goal))
aoc.cprint(part2(goal))
