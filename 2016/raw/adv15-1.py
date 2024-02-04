import sys
import re
import itertools
import math
import aoc
import heapq
import functools
from collections import *

def simulate(discs, time):
  for t, disc in enumerate(discs):
    if (time + disc.pos + t + 1) % disc.mod != 0:
      return False
  return True
        
def search(discs):
  for i in itertools.count():
    if simulate(discs, i):
      return i

discs = []
lines = sys.stdin.readlines()
lines.append("1000 11 0 0")
for line in lines:
  discs.append(aoc.retuple(
      "disc mod_ time_ pos_", r".*?(\d+).*?(\d+).*?(\d+).*?(\d+)", line))
aoc.cprint(search(discs))
  
