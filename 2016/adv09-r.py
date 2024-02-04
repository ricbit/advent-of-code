import sys
import re
import itertools
import math
import aoc
from collections import *

def decode(line, again):
  size = 0
  while line:
    t = aoc.retuple("prelude size_ rep_ rest", r"(.*?)(?:\((\d+)x(\d+)\)(.*))?$", line)
    if t.prelude:
      size += len(t.prelude)
    if t.size is not None:
      size += t.rep * again(t.rest[:t.size], again)
      line = t.rest[t.size:]
    else:
      line = ""
  return size

line = sys.stdin.read().strip()
aoc.cprint(decode(line, lambda x, y: len(x)))
aoc.cprint(decode(line, decode))

  
