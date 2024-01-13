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

def maybe(state, y):
  if y[0].isalpha():
    return state[y]
  else:
    return int(y)

class Computer:
  def __init__(self, prog, p):
    self.pc = 0
    self.state = aoc.ddict(lambda: 0, {"p": p})
    self.recv = []
    self.finished = False
    self.prog = prog
    self.p = p
    self.sent = 0
    self.waiting = False

  def check(self):
    return self.waiting and not self.recv

  def execute(self, send):
    #print(f"{self.p} {self.recv}")
    while True:
      if self.pc >= len(self.prog):
        self.finished = True
        return
      #print(len(self.recv), self.p, self.state, self.prog[self.pc])
      match self.prog[self.pc]:
        case "snd", x:
          send(maybe(self.state, x))
          #print(f"{self.p} sends {maybe(self.state,x)}")
          self.sent += 1
        case "set", x, y:
          self.state[x] = maybe(self.state, y)
        case "add", x, y:
          self.state[x] += maybe(self.state, y)
        case "mul", x, y:
          self.state[x] *= maybe(self.state, y)
        case "mod", x, y:
          self.state[x] %= maybe(self.state, y)
        case "rcv", x:
          if self.recv:
            #print(f"{self.p} recv {self.recv[0]}")
            self.state[x] = self.recv.pop(0)
            self.waiting = False
          else:
            self.waiting = True
            print(f"{self.p}  waiting")
            return
        case "jgz", x, y:
          if maybe(self.state, x) > 0:
            self.pc += maybe(self.state, y) - 1
      self.pc += 1

def multicore(prog):
  comps = [Computer(prog, 0), Computer(prog, 1)]
  while True:
    if all(comps[i].finished for i in range(2)):
      return comps[1].sent
    if all(comps[i].check() for i in range(2)):
      return comps[1].sent
    if comps[0].finished and comps[1].check():
      return comps[1].sent
    if comps[1].finished and comps[0].check():
      return comps[1].sent
    comps[0].execute(lambda x: comps[1].recv.append(x))
    comps[1].execute(lambda x: comps[0].recv.append(x))

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  prog.append(line.split())
aoc.cprint(multicore(prog))
