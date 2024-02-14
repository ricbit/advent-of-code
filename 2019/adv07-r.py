import sys
import itertools
import aoc
from collections import deque
from aoc.refintcode import IntCode

def simulate(data, seq):
  inp = 0
  seq = list(seq)
  cpus = []
  for x in seq:
    cpus.append(IntCode(data))
    cpus[-1].input = x
  while True:
    halted = 0
    for i, cpu in enumerate(cpus):
      while cpu.run():
        match cpu.state:
          case cpu.INPUT:
            cpu.input = inp
          case cpu.OUTPUT:
            inp = cpu.output
            break
      if cpu.state == cpu.HALTED:
        halted += 1
    if halted == 5:
      return inp

def solve(data, phases):
  for seq in itertools.permutations(phases):
    yield simulate(data, seq)

data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(max(solve(data, range(5))))
aoc.cprint(max(solve(data, range(5, 10))))
