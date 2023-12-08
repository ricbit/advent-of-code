import sys
import re
import itertools
import math

lines = [line.strip() for line in sys.stdin.readlines()]
commands = lines[0].strip()
graph = {}
for line in lines[2:]:
  src, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
  graph[src] = {"L": left, "R": right}
start = [node for node in graph if node.endswith("A")]

def simulate(cur):
  for steps, command in enumerate(itertools.cycle(commands)):
    cur = graph[cur][command]
    if cur.endswith("Z"):
      return steps + 1

print(simulate("AAA"))
print(math.lcm(*(simulate(node) for node in start)))
