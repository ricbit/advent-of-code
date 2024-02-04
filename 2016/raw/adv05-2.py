import sys
import re
import itertools
import math
import aoc
from collections import *
import hashlib
import _md5

def search(pwd):
  for i in itertools.count(0):
    md5 = _md5.md5((pwd + str(i)).encode("ascii")).hexdigest()
    if md5[:5] == "00000":
      if (pos := int(md5[5], 16)) < 8:
        yield pos, md5[6]

def build(pwd):
  new_pwd = ["_"] * 8
  for pos, char in search(pwd):
    if new_pwd[pos] == "_":
      new_pwd[pos] = char
      print("".join(new_pwd))
      if "_" not in new_pwd:
        return "".join(new_pwd)

pwd = sys.stdin.read().strip()
print(f"-{pwd}-")
aoc.cprint(build(pwd))
