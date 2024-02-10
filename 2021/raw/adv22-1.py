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
import numpy as np

def solve(cubes):
  m = np.zeros((200, 200, 200))
  for cube in cubes:
    state = 1 if cube.state == "on" else 0
    ax = max(-50, cube.ax) + 50
    bx = min(50, cube.bx) + 50
    ay = max(-50, cube.ay) + 50
    by = min(50, cube.by) + 50
    az = max(-50, cube.az) + 50
    bz = min(50, cube.bz) + 50
    if cube.ax < -50 or cube.ay <-50 or cube.az <-50:
      continue
    if cube.bx > 50 or cube.by > 50 or cube.bz > 50:
      continue
    m[ax:bx+1,ay:by+1,az:bz+1]=state
  return np.count_nonzero(m)

data = [line.strip() for line in sys.stdin]
cubes = aoc.retuple_read("state ax_ bx_ ay_ by_ az_ bz_",
    r"^(on|off).*?x=([-+]?\d+)..([-+]?\d+),y=([-+]?\d+)..([-+]?\d+),z=([-+]?\d+)..([-+]?\d+)",
    data)
aoc.cprint(solve(cubes))
