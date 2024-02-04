import sys
import re
import itertools
import math
import aoc
from collections import *
import hashlib

def search(pwd):
  for i in itertools.count(0):
    md5 = hashlib.md5((pwd + str(i)).encode("ascii")).hexdigest()
    if md5[:5] == "00000":
      yield md5[5]

pwd = sys.stdin.read().strip()
print(f"-{pwd}-")
aoc.cprint("".join(itertools.islice(search(pwd), 8)))
