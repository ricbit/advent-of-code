import math
import functools
import heapq
from dataclasses import dataclass
import re
import sys
import aoc
from collections import deque
from typing import Callable

@dataclass(repr=True, init=False)
class Monkey:
  number: int
  items: list[int]
  operation: Callable[[int], int]
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
    operation = aoc.retuple("a op b", r"(\w+) (.) (\w+)", search(2))
    if operation.op == "+":
      if operation.a == "old" and operation.b.isdigit():
        m.operation = functools.partial(lambda b, x: x + b, int(operation.b))
    elif operation.op == "*":
      if operation.a == "old" and operation.b.isdigit():
        m.operation = functools.partial(lambda b, x: x * b, int(operation.b))
      elif operation.a == "old" and operation.b == "old":
        m.operation = lambda x: x * x
    m.divisible = int(search(3))
    m.if_true = int(search(4))
    m.if_false = int(search(5))
    m.activity = 0
    monkeys.append(m)
  return monkeys

def work_monkey(monkeys, current, low_worry, lcm):
  while current.items:
    current.activity += 1
    old = current.items.popleft()
    new = current.operation(old)
    if low_worry:
      item = new // 3
    else:
      item = new % lcm
    if item % current.divisible == 0:
      monkeys[current.if_true].items.append(item)
    else:
      monkeys[current.if_false].items.append(item)

def work_round(monkeys, worry, lcm):
  for i, current in enumerate(monkeys):
    work_monkey(monkeys, current, worry, lcm)

def work_problem(rounds, low_worry):
  monkeys = parse(lines)
  lcm = math.lcm(*[m.divisible for m in monkeys])
  for i in range(rounds):
    work_round(monkeys, low_worry, lcm)
  business = [m.activity for m in monkeys]
  return math.prod(heapq.nlargest(2, business))

aoc.cprint(work_problem(20, True))
aoc.cprint(work_problem(10000, False))
