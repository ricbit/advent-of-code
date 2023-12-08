import sys
import re
import itertools
import math

lines = [line.strip() for line in sys.stdin.readlines()]
commands = lines[0].strip()
graph = {}
for line in lines[2:]:
  src, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
  graph[src] = (left, right)

start = [node for node in graph if node.endswith("A")]

def simulate(cur):
  steps = 0
  zs = []
  cycle = itertools.cycle(commands)
  visited = set()
  #print("\n", cur)
  for command in cycle:
    if command == "R":
      cur = graph[cur][1]
    elif command == "L":
      cur = graph[cur][0]
    steps += 1
    #print(cur, graph[cur])
    if cur.endswith("Z"):
      zs.append(steps)
      return zs,steps
    #if (cur,command) in visited:
    # return zs, steps
    visited.add((cur,command))

numbs = []
for node in start:
  a = simulate(node)
  numbs.append(a[1])
  print(node, a)
print(math.lcm(*numbs))


  
