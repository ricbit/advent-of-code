import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def jose(n):
  a = bin(n)[3:]
  return int(a, 2) * 2 + 1

def manual(n):
  elf = {(1 + i): 1 + (i + 1) % n for i in range(n)}
  pos = 1
  while len(elf) > 1:
    d = elf[pos]
    elf[pos] = elf[d]
    del elf[d]
    pos = elf[pos]

def manual2(n):
  elf = {(1 + i): [1 + (i + n - 1) % n, 1 + (i + 1) % n] for i in range(n)}
  pos = 1
  half = int(math.ceil(n / 2))
  a = half - pos - 1
  b = n - half
  while len(elf) > 1:
    #print(pos, half, a, b, elf)
    nhalf = elf[half][1]
    elf[elf[half][0]][1] = elf[half][1]
    elf[elf[half][1]][0] = elf[half][0]
    del elf[half]
    pos = elf[pos][1]
    a -= 1
    half = nhalf
    #print(half, a, b)
    while b - a > 1:
      half = elf[half][1]
      b -= 1
      a += 1
    #print(half, a, b)
  return list(elf.keys())[0]

n = int(sys.stdin.read())
aoc.cprint(manual2(n))
