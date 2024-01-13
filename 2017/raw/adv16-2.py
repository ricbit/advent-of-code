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

def execute(prog, cmd):
  for c in cmd:
    match (c.code, c.src, c.dst):
      case "s", src, _:
        s = int(src)
        prog = prog[-s:] + prog[:-s]
      case "x", src, dst:
        a, b = int(src), int(dst)
        prog[a], prog[b] = prog[b], prog[a]
      case "p", src, dst:
        a = prog.index(src)
        b = prog.index(dst)
        prog[a], prog[b] = prog[b], prog[a]
  return "".join(prog)

def find(prog, perm):
  original = prog[:]
  nprog = prog[:]
  perm = [ord(p) - ord("a") for p in perm]
  for i in itertools.count(1):
    for j in range(len(perm)):
      nprog[j] = prog[perm[j]]
    prog = nprog[:]
    print(prog)
    if prog == original:
      return i
      return "".join(prog)

line = sys.stdin.read().strip()
cmd = []
for p in line.split(","):
  q = aoc.retuple("code src dst", r"(.)(.*?)(?:/(.*))?$", p)
  cmd.append(q)
prog = list(chr(i) for i in range(ord("a"), ord("p") + 1))
#prog=list("abcde")
original = prog[:]
for i in range(40):
  prog = list(execute(prog[:], cmd))
  aoc.cprint("".join(prog))
  if prog == original:
    print(i)
    break

#aoc.cprint(find(prog,perm))
#aoc.cprint(ans)
