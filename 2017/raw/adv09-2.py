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

def parser(chars):
  pos = 0
  copen = 0
  state = True
  score = 0
  garbage = 0
  while pos < len(chars):
    if chars[pos] == "{" and state:
      copen += 1
      score+= copen
    elif chars[pos] == "}" and state:
      copen -= 1
    elif chars[pos] == "<" and state:
      state = False
    elif chars[pos] == ">" and not state:
      state = True
    elif chars[pos] == "!" and not state:
      pos += 1
    elif not state:
      garbage += 1
    pos += 1
  return score, garbage

line = sys.stdin.read().strip()
aoc.cprint(parser(line)[1])
