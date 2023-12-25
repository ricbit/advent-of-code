import sys
import re
import itertools
import math

lines = [line.strip() for line in sys.stdin.readlines()]
commands = lines[0]
graph = {}
for line in lines[2:]:
  src, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
  graph[src] = (left, right)

cycle = itertools.cycle(commands)
cur = "AAA"
steps = 0
for command in cycle:
  if command == "R":
    cur = graph[cur][1]
  elif command == "L":
    cur = graph[cur][0]
  steps += 1
  if cur == "ZZZ":
    break

print(steps)


  
