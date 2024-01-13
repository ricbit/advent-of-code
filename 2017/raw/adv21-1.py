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

#1:06
#20:49
#21:18

def fractal(rules, n):
  pattern = [".#.", "..#", "###"]
  for _ in range(n):
    size = len(pattern)
    if len(pattern) % 2 == 0:
      final = []
      for j in range(size // 2):
        line = []
        for i in range(size // 2):
          k = []
          for jj in range(2):
            kk = []
            for ii in range(2):
              kk.append(pattern[j * 2 + jj][i * 2 + ii])
            k.append("".join(kk))
          dst = rules["/".join(k)].split("/")
          line.append(dst)
        final.append(line)
      newp = [[0] * (size // 2 * 3) for _ in range(size // 2 * 3)]
      for j in range(size // 2):
        for i in range(size // 2):
          for jj in range(3):
            for ii in range(3):
              newp[j * 3 + jj][i * 3 + ii] = final[j][i][jj][ii]
    else:
      final = []
      for j in range(size // 3):
        line = []
        for i in range(size // 3):
          k = []
          for jj in range(3):
            kk = []
            for ii in range(3):
              kk.append(pattern[j * 3 + jj][i * 3 + ii])
            k.append("".join(kk))
          dst = rules["/".join(k)].split("/")
          line.append(dst)
        final.append(line)
      newp = [[0] * (size // 3 * 4) for _ in range(size // 3 * 4)]
      for j in range(size // 3):
        for i in range(size // 3):
          for jj in range(4):
            for ii in range(4):
              newp[j * 4 + jj][i * 4 + ii] = final[j][i][jj][ii]
    pattern = newp
  return sum(sum(i == "#" for i in line) for line in pattern)


  
lines = [line.strip() for line in sys.stdin]
rules = {}
for line in lines:
  src, dst = line.strip().split(" => ")
  tsrc = aoc.Table([list(c) for c in src.split("/")])
  for i in range(4):
    nsrc = "/".join("".join(line) for line in tsrc)
    rules[nsrc] = dst
    ksrc = tsrc.flipx()
    nsrc = "/".join("".join(line) for line in ksrc)
    rules[nsrc] = dst
    tsrc = tsrc.clock90()
aoc.cprint(fractal(rules, 18))
