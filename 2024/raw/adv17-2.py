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

def combo(regs, val):
  if val < 4:
    return val
  return regs[val - 4]

def dcombo(val):
  if val < 4:
    return str(val)
  return f"regs{val - 4}"

def printprog(program):
  print(program)
  for pc in range(0, len(program), 2):
    match program[pc]:
      case 0: # adv
        print(f"a = a // 2 ** {dcombo(program[pc + 1])}")
      case 1: # bxl
        print(f"b = b ^ {program[pc + 1]}")
      case 2: # bst
        print(f"b = {dcombo(program[pc + 1])} $ 8")
      case 3: # jnz
        print(f"jnz {program[pc + 1]}")
      case 4: # bxc
        print("b = b ^c")
      case 5: # out
        print(f"out {dcombo(program[pc + 1])} % 8")
      case 6: # bdv
        print(f"b = a // 2 ** {dcombo(program[pc + 1])}")
      case 7: # cdv
        print(f"c = a // 2 ** {dcombo(program[pc + 1])}")

def parse(data):
  register, program = data
  regs = {}
  for line in register:
    x = aoc.retuple("name val_", r"Register (\w): (\d+)", line)
    regs[ord(x.name) - ord("A")] = x.val
  #print(program[0].split(":"))
  program = aoc.ints(program[0].split(":")[1].strip().split(","))
  return regs, program

def solve(regs, program):
  register, program = data
  regs = {}
  for line in register:
    x = aoc.retuple("name val_", r"Register (\w): (\d+)", line)
    regs[ord(x.name) - ord("A")] = x.val
  #regs[0] = i
  #print(program[0].split(":"))
  program = aoc.ints(program[0].split(":")[1].strip().split(","))
  pc = 0
  ans = []
  while True:
    match program[pc]:
      case 0: # adv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[0] = d
      case 1: # bxl
        regs[1] ^= program[pc + 1]
      case 2: # bst
        regs[1] = combo(regs, program[pc + 1]) % 8
      case 3: # jnz
        if regs[0] != 0:
          #n-= 1
          pc = program[pc + 1] - 2
        pass
      case 4: # bxc
        regs[1] ^= regs[2]
      case 5: # out
        ans.append(combo(regs, program[pc + 1]) % 8)
      case 6: # bdv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[1] = d
      case 7: # cdv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[2] = d
    pc += 2
    if pc >= len(program):
      break
  return ",".join(str(i) for i in ans)
  #return ans

def simulate(a):
  b,c = 0,0
  ans=[]
  while a:
    b = a % 8
    b = b ^ 5
    c = a // (2 ** b)
    b = b ^ 6
    a = a // 8
    b = b ^ c
    ans.append(b % 8)
  return ans

class Sim:
  def __init__(self, prog):
    self.prog = prog
    self.minback = 1e20

  @functools.cache
  def rec(self, back, shift):
    if shift == 16:
      x = simulate(back)
      if x[:shift] == self.prog[:shift]:
        self.minback = min(self.minback, back)
        #print(self.minback, back, simulate(back))
      return
    for i in range(256 * 8):
      stable = 2 ** (3 * shift)
      n = back + i * stable
      x = simulate(n)
      if x[:shift + 1] == self.prog[:shift + 1]:
        self.rec(n % (2 ** (3 * shift + 3)), shift + 1)


  def search(self):
    self.rec(0, 0)
    return self.minback

data = aoc.line_blocks()
regs, program = parse(data)
aoc.cprint(solve(regs, program))
s = Sim(program)
print(s.search())
##for i in range(256):
#  x = solve(a, b, i, 2)
#  if x== "2":
#    aoc.cprint((i, x))
