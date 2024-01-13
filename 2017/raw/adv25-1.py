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

def turing():
  tape = set()
  state = "A"
  pos = 0
  for i in range(12261543):
    if state == "A":
      if pos not in tape:
        tape.add(pos)
        pos += 1
        state = "B"
      else:
        tape.remove(pos)
        pos -= 1
        state = "C"
    elif state == "B":
      if pos not in tape:
        tape.add(pos)
        pos -= 1
        state = "A"
      else:
        tape.add(pos)
        pos += 1
        state = "C"
    elif state == "C":
      if pos not in tape:
        tape.add(pos)
        pos += 1
        state = "A"
      else:
        tape.remove(pos)
        pos -= 1
        state = "D"
    elif state == "D":
      if pos not in tape:
        tape.add(pos)
        pos -= 1
        state = "E"
      else:
        tape.add(pos)
        pos -= 1
        state = "C"
    elif state == "E":
      if pos not in tape:
        tape.add(pos)
        pos += 1
        state = "F"
      else:
        tape.add(pos)
        pos += 1
        state = "A"
    elif state == "F":
      if pos not in tape:
        tape.add(pos)
        pos += 1
        state = "A"
      else:
        tape.add(pos)
        pos += 1
        state = "E"
  return len(tape)

lines = [line.strip() for line in sys.stdin]
aoc.cprint(turing())

