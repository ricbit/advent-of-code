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

def apply(line):
  pos = 0
  skip = 0
  q = list(range(256))
  #print(line)
  for _ in range(64):
    #print(line,pos,skip)
    for n in line:
      qq = q[:]
      for i in range(0, n):
        qq[(pos + i) % len(q)] = q[(pos + n - 1 - i + len(q)) % len(q)]
      q = qq
      pos += n + skip
      skip += 1
  sparse = [0] * 16
  for i in range(16):
    #print(q[i*16:i*16+16])
    for j in range(16):
      sparse[i] ^= q[j + i * 16]
  return "".join("%02x" % i for i in sparse)


line = [ord(i) for i in sys.stdin.read().strip()] + [17,31,73,47,23]
q = apply(line)
aoc.cprint(q)
