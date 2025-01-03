import aoc
import re
import sys
from collections import defaultdict
from operator import eq, lt, gt

target = {
  "children": (3, eq),
  "cats": (7, gt),
  "samoyeds": (2, eq),
  "pomeranians": (3, lt),
  "akitas": (0, eq),
  "vizslas": (0, eq),
  "goldfish": (5, lt),
  "trees": (3, gt),
  "cars": (2, eq),
  "perfumes": (1, eq)
}

def search(sues):
  for sue, items in sues.items():
    if all(items[k] == target[k][0] for k in items.keys()):
      return sue
  return None

def search2(sues):
  for sue, items in sues.items():
    if all(target[k][1](items[k], target[k][0]) for k in items.keys()):
      return sue
  return None

sues = defaultdict(lambda: {})
for line in sys.stdin:
  n, items = re.search(r"(\d+): (.*)$", line).groups()
  n = int(n)
  for item in items.split(","):
    name, value = item.split(":")
    sues[n][name.strip()] = int(value)

aoc.cprint(search(sues))
aoc.cprint(search2(sues))
