import sys
import re
import itertools
import math
import aoc

def parse_flow(flow, d):
  name, rules = re.match(r"(\w+)\{(.*)\}", flow).groups()
  rules = rules.split(",")
  for rule in rules:
    if ":" not in rule:
      return rule
    var, cmp, value, dest = re.match(r"(\w+)([<>])(\d+):(\w+)", rule).groups()
    if cmp == "<":
      if d[var] < int(value):
        return dest
    elif cmp == ">":
      if d[var] > int(value):
        return dest
  return "bug"

def parse_parts(parts):
  parts = parts.strip("{}").split(",")
  d= {}
  for part in parts:
    k, v = part.split("=")
    d[k] = int(v)
  return d

def traverse(part, flows, state):
  while state not in ["R", "A"]:
    state = parse_flow(flows[state], part)
  return state

flows, parts = aoc.line_blocks()
flows = {re.match(r"(\w+)\{", f).group(1):f for f in flows}
ans = 0
for raw_part in parts:
  part = parse_parts(raw_part)
  if traverse(part, flows, "in") == "A":
    print(sum(part.values()))
    ans += sum(part.values())
print(ans)

  
