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
import z3

def read(reg, addr, zvar):
  match re.match(r"([-+]?\d+)|(\w)", reg).groups():
    case a, None:
      return int(a)
    case None, b:
      return zvar[addr - 1][b]

def simulate(lines, values):
  s = z3.Optimize()
  s.set(timeout=5 * 60 * 1000)
  zvar = [{c:z3.BitVec(f"{c}_{i}", 64) for c in 'xyzw'} for i in range(1 + len(lines))]
  values = [z3.BitVec(f'value_{i}', 64) for i in range(14)]
  s.add(zvar[0]['x'] == 0)
  s.add(zvar[0]['y'] == 0)
  s.add(zvar[0]['z'] == 0)
  s.add(zvar[0]['w'] == 0)
  for i in range(14):
    s.add(values[i] > 0)
    s.add(values[i] <= 9)
  cur = 0
  for i, line in enumerate(lines):
    addr = i + 1
    match line.split():
      case "inp", reg:
        s.add(zvar[addr][reg] == values[cur])
        cur += 1
        for c in 'xyzw':
          if c != reg:
            s.add(zvar[addr][c] == zvar[addr - 1][c])
      case "add", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] + read(b, addr, zvar))
        for c in 'xyzw':
          if c != a:
            s.add(zvar[addr][c] == zvar[addr - 1][c])
      case "mul", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] * read(b, addr, zvar))
        for c in 'xyzw':
          if c != a:
            s.add(zvar[addr][c] == zvar[addr - 1][c])
      case "div", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] / read(b, addr, zvar))
        for c in 'xyzw':
          if c != a:
            s.add(zvar[addr][c] == zvar[addr - 1][c])
      case "mod", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] % read(b, addr, zvar))
        for c in 'xyzw':
          if c != a:
            s.add(zvar[addr][c] == zvar[addr - 1][c])
      case "eql", a, b:
        s.add(zvar[addr][a] == z3.If(zvar[addr - 1][a] == read(b, addr, zvar), 
                                     z3.BitVecVal(1, 64), z3.BitVecVal(0, 64)))
        for c in 'xyzw':
          if c != a:
            s.add(zvar[addr][c] == zvar[addr - 1][c])
  s.add(zvar[-1]['z'] == 0)
  print(s.minimize(sum(values[13 - cur] * 10 ** cur for cur in range(14))))
  print(s.check())
  m = s.model()
  return "".join(str(m.evaluate(v)) for v in values)

lines = [line.strip() for line in sys.stdin]
print(simulate(lines, [0] * 14))
