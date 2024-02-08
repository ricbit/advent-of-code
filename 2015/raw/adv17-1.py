import sys
import re
import itertools
import math
import aoc
import functools
from collections import *

@functools.lru_cache(maxsize=None)
def count(n, flask, used):
  if n == 0 and not flask and used == 0:
    return 1
  if not flask:
    return 0
  return count(n - flask[0], tuple(flask[1:]), used - 1) + count(n, tuple(flask[1:]), used)

def search(flask):
  for i in range(1, 10):
    if (m := count(150, tuple(flask), i)):
      return (i, m)

flask = [int(line.strip()) for line in sys.stdin]
flask.sort(reverse=True)
print(search(flask))
