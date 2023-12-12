import sys
import re
import itertools
import math
import functools

@functools.lru_cache(maxsize=None)
def count(springs, opensize, groups):
  if not springs:
    if opensize > 0:
      if groups == (opensize, ):
        return 1
      else:
        return 0
    if not groups:
      return 1
    else:
      return 0
  if springs[0] == ".":
    if opensize > 0:
      if groups and groups[0] == opensize:
        return count(springs[1:], 0, tuple(groups[1:]))
      return 0
    else:
      return count(springs[1:], 0, groups)
  if springs[0] == "#":
    return count(springs[1:], opensize + 1, groups)
  if springs[0] == "?":
    return (count("#" + springs[1:], opensize, groups) + 
      count("." + springs[1:], opensize, groups))

ans = 0
for line in sys.stdin:
  springs, groups = line.strip().split()
  groups = [int(i) for i in groups.split(",")]
  ans += count(springs, 0, tuple(groups))
print(ans)
  
