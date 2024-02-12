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
from aoc.refintcode import IntCode

main = "ABABACBCAC"
subroutines = [
  ['L', '10', 'L', '12', 'R', '6'], 
  ['R', '10', 'L', '4', 'L', '4', 'L', '12'], 
  ['L', '10', 'R', '10', 'R', '6', 'L', '4']
]

bigpath = """
A 'L', '10', 'L', '12', 'R', '6',
B 'R', '10', 'L', '4', 'L', '4', 'L', '12', 
A 'L', '10', 'L', '12', 'R', '6',
B 'R', '10', 'L', '4', 'L', '4', 'L', '12', 
A 'L', '10', 'L', '12', 'R', '6', 
C 'L', '10', 'R', '10', 'R', '6', 'L', '4',
B 'R', '10', 'L', '4', 'L', '4', 'L', '12', 
C 'L', '10', 'R', '10', 'R', '6', 'L', '4', 
A 'L', '10', 'L', '12', 'R', '6', 
C 'L', '10', 'R', '10', 'R', '6', 'L', '4'
"""

def alignment(t):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == "#":
      count = 0
      for jj, ii in t.iter_neigh4(j, i):
        if t[jj][ii] == "#":
          count += 1
      if count == 4:
        ans += (j - 1) * (i - 1)
  return ans

def read_table(data):
  cpu = IntCode(data[:])
  table = []
  line = []
  while cpu.run():
    match cpu.state:
      case cpu.OUTPUT:
        if cpu.output == 10:
          line = ["."] + line + ["."]
          table.append(line)
          line = []
        else:
          line.append(chr(cpu.output))
  empty = ["."] * len(table[0])
  table = [empty] + table[:-1] + [empty]
  return aoc.Table(table)

def get_pos(t):
  for j, i in t.iter_all():
    if t[j][i] == "^":
      return i + j * 1j

def get_full_path(t):
  pos = get_pos(t)
  vdir = -1
  cmd = ["L"]
  dirs = {"R": 1j, "L": -1j}
  while True:
    if t.get(pos + vdir) == "#":
      pos += vdir
      cmd.append("w")
    else:
      for c, d in dirs.items():
        if t.get(pos + vdir * d) == "#":
          vdir *= d
          pos += vdir
          cmd.append(c)
          cmd.append("w")
          break
      else:
        return cmd

def get_short_path(t):
  full_path = get_full_path(t)
  path = []
  for k, v in itertools.groupby(full_path):
    if k == "w":
      path.append(str(len(list(v))))
    else:
      path.append(k)
  return path

def solve2(data):
  data[0] = 2
  cpu = IntCode(data)
  cmd = ",".join(main) + chr(10)
  print(len(cmd))
  for sub in subroutines:
    cmd += ",".join(sub) + chr(10)
  cmd += "y" + chr(10) + chr(10)
  pos = 0
  output = 0
  print(cmd)
  line = []
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        cpu.input = ord(cmd[pos])
        pos += 1
      case cpu.OUTPUT:
        output = cpu.output
        if output == 10:
          print("".join(chr(i) for i in line))
          if not line:
            aoc.cls()
            aoc.goto0()
          line = []
        else:
          line.append(output)
  return output

data = aoc.ints(sys.stdin.read().split(","))
table = read_table(data)
aoc.cprint(alignment(table))
path = get_short_path(table)
print(path)
#aoc.cprint(solve2(data))
