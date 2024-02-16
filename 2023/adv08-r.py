import sys
import re
import itertools
import math
import aoc

lines = [line.strip() for line in sys.stdin.readlines()]
commands = lines[0].strip()
graph = {}
for line in lines[2:]:
  src, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
  graph[src] = {"L": left, "R": right}
start = [node for node in graph if node.endswith("A")]

def simulate(cur):
  for steps, command in enumerate(itertools.cycle(commands)):
    if (cur := graph[cur][command]).endswith("Z"):
      return steps + 1

aoc.cprint(simulate("AAA"))
aoc.cprint(math.lcm(*(simulate(node) for node in start)))
