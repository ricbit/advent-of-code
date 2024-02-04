import sys
import re
import itertools
import math
import aoc
from collections import *

def decode(line):
  size = 0
  while line:
    t = aoc.retuple("prelude size_ rep_ rest", r"(.*?)(?:\((\d+)x(\d+)\)(.*))?$", line)
    if t.prelude:
      size += len(t.prelude)
    if t.size is not None:
      size += t.rep * decode(t.rest[:t.size])
      line = t.rest[t.size:]
    else:
      line = ""
  return size

for line in sys.stdin:
  aoc.cprint(decode(line))

  
