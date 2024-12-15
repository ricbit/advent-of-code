import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def canon(t, pos):
  if t.get(pos) == "]":
    pos -= 1
  return pos

def printt(t):
  print("".join(str(d % 10) for d in range(len(t[0]))))
  for line in t:
    print("".join(line))
  print("$$")

def recmove(t, pos, pdir):
  if t.get(pos) == ".":
    return
  pos = canon(t, pos)
  if pdir == 1:
    recmove(t,canon(t,pos+2), pdir)
    t.put(pos + 2, t.get(pos + 1))
    t.put(pos + 1, t.get(pos))
    t.put(pos, ".")
  elif pdir == -1:
    recmove(t,canon(t,pos-1),pdir)
    t.put(pos - 1, t.get(pos - 0))
    t.put(pos, t.get(pos+1))
    t.put(pos+1, ".")
  elif pdir == -1j:
    a = canon(t,pos + pdir)
    b = canon(t,pos + pdir + 1)
    recmove(t, a, pdir)
    recmove(t, b, pdir)
    t.put(pos-1j, t.get(pos))
    t.put(pos+1-1j, t.get(pos+1))
    t.put(pos, ".")
    t.put(pos+1, ".")
  elif pdir == 1j:
    a = canon(t,pos + pdir)
    b = canon(t,pos + pdir + 1)
    recmove(t, a, pdir)
    recmove(t, b, pdir)
    t.put(pos+1j, t.get(pos))
    t.put(pos+1+1j, t.get(pos+1))
    t.put(pos, ".")
    t.put(pos+1, ".")

def canmove(t, pos, pdir):
  pos = canon(t, pos)
  if t.get(pos) == "#":
    return False
  if t.get(pos) == ".":
    return True
  if pdir == 1:
    return canmove(t, canon(t,pos + 2), pdir)
  elif pdir == -1:
    return canmove(t, canon(t,pos - 1), pdir)
  elif pdir == -1j:
    a = canmove(t, canon(t,pos-1j), pdir)
    b = canmove(t, canon(t,pos-1j+1), pdir)
    return a and b
  elif pdir == 1j:
    a = canmove(t, canon(t,pos+1j), pdir)
    b = canmove(t, canon(t,pos+1j+1), pdir)
    return a and b


def qmove(t, pos, pdir):
  pos = canon(t, pos)
  a = canmove(t, pos, pdir)
  if a:
    recmove(t, pos, pdir)
  return a

def solve(data):
  wide = {"#": "##", "O": "[]", ".": "..", "@": "@."}
  maze, moves = data
  maze = ["".join(wide[k] for k in s.strip()) for s in maze]
  moves = "".join(s.strip() for s in moves)
  print(moves)
  #for line in maze:
  #  print(line)
  t = aoc.Table([list(p.strip()) for p in maze])
  cdir = aoc.get_cdir(">")
  for j, i in t.iter_all():
    if t[j][i] == "@":
      t[j][i] = "."
      pos = j * 1j + i
  for move in moves:
    pdir = cdir[move]
    rock = False
    if t.get(pos + pdir) == ".":
      pos += pdir
    elif t.get(pos + pdir) in "[]":
      if qmove(t, pos + pdir, pdir):
        pos += pdir
        rock = True
    t.put(pos, "@")
    rock=True
    if False:
      print(move, pdir)
      for line in t:
        print("".join(line))
      print()
    t.put(pos, ".")
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == "[":
      ans += j * 100 + i
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data))
