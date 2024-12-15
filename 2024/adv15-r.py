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


class Maze:
  def __init__(self, data):
    wide = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    maze, moves = data
    maze = ["".join(wide[k] for k in s.strip()) for s in maze]
    self.moves = "".join(s.strip() for s in moves)
    self.t = aoc.Table([list(p) for p in maze])

  def canon(self, pos):
    if self.get(pos) == "]":
      pos -= 1
    return pos

  def put(self, pos, value):
    self.t.put(pos, value)

  def get(self, pos):
    return self.t.get(pos)

  def move(self, pos, pdir):
    pos = self.canon(pos)
    if self.get(pos) == ".":
      return
    if pdir == 1:
      self.move(self.canon(pos+2), pdir)
      self.put(pos + 2, self.get(pos + 1))
      self.put(pos + 1, self.get(pos))
      self.put(pos, ".")
    elif pdir == -1:
      self.move(self.canon(pos-1),pdir)
      self.put(pos - 1, self.get(pos - 0))
      self.put(pos, self.get(pos+1))
      self.put(pos+1, ".")
    elif pdir == -1j:
      a = self.canon(pos + pdir)
      b = self.canon(pos + pdir + 1)
      self.move( a, pdir)
      self.move( b, pdir)
      self.put(pos-1j, self.get(pos))
      self.put(pos+1-1j, self.get(pos+1))
      self.put(pos, ".")
      self.put(pos+1, ".")
    elif pdir == 1j:
      a = self.canon(pos + pdir)
      b = self.canon(pos + pdir + 1)
      self.move( a, pdir)
      self.move( b, pdir)
      self.put(pos+1j, self.get(pos))
      self.put(pos+1+1j, self.get(pos+1))
      self.put(pos, ".")
      self.put(pos+1, ".")

  def check(self, pos, pdir):
    pos = self.canon(pos)
    if self.get(pos) == "#":
      return False
    if self.get(pos) == ".":
      return True
    if pdir == 1:
      return self.check( self.canon(pos + 2), pdir)
    elif pdir == -1:
      return self.check( self.canon(pos - 1), pdir)
    elif pdir == -1j:
      a = self.check( self.canon(pos-1j), pdir)
      b = self.check( self.canon(pos-1j+1), pdir)
      return a and b
    elif pdir == 1j:
      a = self.check( self.canon(pos+1j), pdir)
      b = self.check( self.canon(pos+1j+1), pdir)
      return a and b


  def solve(self, data):
    cdir = aoc.get_cdir(">")
    for j, i in self.t.iter_all():
      if self.t[j][i] == "@":
        self.t[j][i] = "."
        pos = j * 1j + i
    for move in self.moves:
      pdir = cdir[move]
      if self.get(pos + pdir) == ".":
        pos += pdir
      elif self.get(pos + pdir) in "[]":
        if self.check(pos + pdir, pdir):
          self.move(pos + pdir, pdir)
          pos += pdir
    ans = 0
    for j, i in self.t.iter_all():
      if self.t[j][i] == "[":
        ans += j * 100 + i
    return ans

data = aoc.line_blocks()
maze = Maze(data)
aoc.cprint(maze.solve(data))
