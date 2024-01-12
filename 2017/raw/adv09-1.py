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
  while pos < len(chars):
    if chars[pos] == "{" and state:
      copen += 1
      score+= copen
    if chars[pos] == "}" and state:
      copen -= 1
    if chars[pos] == "<" and state:
      state = False
    if chars[pos] == ">" and not state:
      state = True
    if chars[pos] == "!" and not state:
      pos += 1
    pos += 1
  return score

line = sys.stdin.read().strip()
aoc.cprint(parser(line))
