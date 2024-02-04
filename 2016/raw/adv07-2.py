import sys
import re
import itertools
import math
import aoc
from collections import *

def check(words, hyper):
  for w in words:
    for i in range(len(w) - 2):
      if w[i] != w[i + 1] and w[i] == w[i + 2]:
        bab = "".join([w[i + 1], w[i], w[i + 1]])
        if any(bab in h for h in hyper):
          return True
  return False

ans = 0
for line in sys.stdin:
  hyper = re.findall(r"\[(.*?)\]", line)
  words = re.sub(r"\[.*?\]", "-", line).split("-")
  if check(words, hyper):
    ans += 1
aoc.cprint(ans)

  
