import aoc
import re
import sys
from collections import defaultdict

equal = lambda a, b: a == b
lt = lambda a, b: a < b
gt = lambda a, b: a > b

target = {
  "children": (3, equal),
  "cats": (7, gt),
  "samoyeds": (2, equal),
  "pomeranians": (3, lt),
  "akitas": (0, equal),
  "vizslas": (0, equal),
  "goldfish": (5, lt),
  "trees": (3, gt),
  "cars": (2, equal),
  "perfumes": (1, equal)
}

def search(sues):
  for sue, items in sues.items():
    if all(items[k] == target[k][0] for k in items.keys()):
      return sue

def search2(sues):
  for sue, items in sues.items():
    if all(target[k][1](items[k], target[k][0]) for k in items.keys()):
      return sue

sues = defaultdict(lambda: {})
for line in sys.stdin:
  n, items = re.search(r"(\d+): (.*)$", line).groups()
  n = int(n)
  for item in items.split(","):
    name, value = item.split(":")
    sues[n][name.strip()] = int(value)

aoc.cprint(search(sues))
aoc.cprint(search2(sues))


