import sys
import re
import itertools
import math
import aoc
from collections import *

def check(words):
  for w in words:
    for i in range(len(w) - 4):
      if w[i] != w[i + 1] and w[i] == w[i + 3] and w[i + 1] == w[i + 2]:
        return True
  return False

ans = 0
for line in sys.stdin:
  words = re.sub(r"\[.*?\]", "-", line).split("-")
  if check(words):
    ans += 1
aoc.cprint(ans)

  
