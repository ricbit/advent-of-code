import re
import sys
from dataclasses import dataclass
from functools import lru_cache

@dataclass(init=False, repr=True)
class Monkey:
  op: str
  first: int
  second: int

def parse():
  lines = sys.stdin.readlines()
  monkey_name = {}
  for i, line in enumerate(lines):
    name = line.split(":")[0]
    monkey_name[name] = i
  monkeys = []
  for i, line in enumerate(lines):
    g = re.search(r":\s+(?:(\d+)|(\w+)\s+(.)\s+(\w+))", line)
    value, first, op, second = g.groups()
    monkey = Monkey()
    if op is None:
      monkey.op = "n"
      monkey.first = int(value)
      monkey.second = 0
    else:
      monkey.op = op
      monkey.first = int(monkey_name[first])
      monkey.second = int(monkey_name[second])
    monkeys.append(monkey)
  return monkeys, monkey_name["root"], monkey_name["humn"]

@lru_cache()
def monkey_value(index):
  base = monkeys[index]
  if base.op == "n":
    return base.first
  else:
    first = monkey_value(base.first)
    second = monkey_value(base.second)
    op = "%d%s%d" % (first, base.op, second)
    value = eval(op)
    return value

@lru_cache()
def monkey_guess(index, root, human, guess):
  base = monkeys[index]
  if index == human:
    return guess
  elif base.op == "n":
    return base.first
  elif index == root:
    first = monkey_guess(base.first, root, human, guess)
    second = monkey_guess(base.second, root, human, guess)
    if first == second:
      return 0
    elif first < second:
      return -1
    else:
      return 1
  else:
    first = monkey_guess(base.first, root, human, guess)
    second = monkey_guess(base.second, root, human, guess)
    op = "%d%s%d" % (first, base.op, second)
    return eval(op)

def get_bounds(root, human):
  guess = 1
  first = monkey_guess(root, root, human, guess)
  while True:
    guess *= 2
    last = monkey_guess(root, root, human, guess)
    if first * last < 0:
      return (guess // 2, guess // 2)

def search(root, human):
  start, size = get_bounds(root, human)
  lower = monkey_guess(root, root, human, start)
  while size > 1:
    m = size // 2
    if (val := monkey_guess(root, root, human, start + m)) == 0:
      return start + m
    if val * lower < 0:
      size = m
    else:
      start += m
      size -= m
      lower = val
  return start + size - 1

monkeys, root, human = parse()
print(monkey_value(root))
print(search(root, human))

    
