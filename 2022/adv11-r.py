import math
import heapq
from dataclasses import dataclass
import re
import sys
import aoc
from collections import deque

@dataclass(repr=True, init=False)
class Monkey:
  number: int
  items: list[int]
  operation: str
  divisible: int
  if_true: int
  if_false: int
  activity: int

regexps = [
  r"Monkey (\d+)",
  r"items: ((?:\d+,?\s*)+)",
  r"new = (.*)$",
  r"by (\d+)",
  r"monkey (\d+)",
  r"monkey (\d+)"
]

lines = [line.strip() for line in sys.stdin]

def parse(lines):
  monkeys = []
  for i in range(len(lines) // 7 + 1):
    line = lambda index: lines[i * 7 + index]
    search = lambda index: re.search(regexps[index], line(index)).group(1)
    m = Monkey()
    m.number = int(search(0))
    m.items = deque(aoc.ints(search(1).split(",")))
    m.operation = search(2)
    m.divisible = int(search(3))
    m.if_true = int(search(4))
    m.if_false = int(search(5))
    m.activity = 0
    monkeys.append(m)
  return monkeys

def work_monkey(monkeys, current, worry, lcm):
  while current.items:
    current.activity += 1
    old = current.items.popleft()
    new = eval(current.operation)
    item = new // worry
    item %= lcm
    if item % current.divisible == 0:
      monkeys[current.if_true].items.append(item)
    else:
      monkeys[current.if_false].items.append(item)

def work_round(monkeys, worry, lcm):
  for i, current in enumerate(monkeys):
    work_monkey(monkeys, current, worry, lcm)

def work_problem(rounds, worry):
  monkeys = parse(lines)
  lcm = math.lcm(*[m.divisible for m in monkeys])
  for i in range(rounds):
    work_round(monkeys, worry, lcm)
  business = [m.activity for m in monkeys]
  return math.prod(heapq.nlargest(2, business))

aoc.cprint(work_problem(20, 3))
aoc.cprint(work_problem(10000, 1))
