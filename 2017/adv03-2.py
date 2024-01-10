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

def sumiter(m, j, i, goal):
  ans = 0
  for jj, ii in aoc.iter_neigh8(j, i):
    if 0 <= jj < len(m) and 0 <= ii < len(m[0]):
      #print(j,i,jj,ii,m[jj][ii])      
      ans += m[jj][ii]
  #print(ans)
  return ans

def grow(goal):
  m = [[1]]
  stride = 1
  pos = (0, 0)
  cur = 1
  for i in itertools.count(2):
    m = [[0] * (2 * stride + 1)] + [[0] + rest + [0] for rest in m] + [[0] * (2 * stride + 1)]
    #print(m)
    pos = (stride, 2 * stride + 1 - 1)
    for j in range(2*stride-1, pos[0] - stride -1, -1):
      ans = sumiter(m, j, pos[1], goal)
      if ans > goal:
        return ans
      m[j][pos[1]] = sumiter(m, j, pos[1], goal)
      cur += 1
    for j in range(2 * stride - 1, -1, -1):
      ans = sumiter(m, 0, j, goal)
      if ans > goal:
        return ans
      m[0][j] = sumiter(m, 0, j,goal)
      cur += 1
    for j in range(1, 2 * stride + 1):
      ans = sumiter(m, j,0, goal)
      if ans > goal:
        return ans
      m[j][0] = sumiter(m, j, 0,goal)
      cur += 1
    for j in range(1, 2 * stride + 1):
      ans = sumiter(m, len(m)-1,j, goal)
      if ans > goal:
        return ans
      m[-1][j] = sumiter(m, len(m)-1, j,goal)
      cur += 1
    stride += 1
    #print(m)
    if any(goal in line for line in m):
      for i, line in enumerate(m):
        if goal in line:
          print(line.index(goal), i)
          return abs(line.index(goal) - stride +1) + abs(i - stride +1) 
      break

line = sys.stdin.read().strip()
ans = grow(int(line))
aoc.cprint(ans)
