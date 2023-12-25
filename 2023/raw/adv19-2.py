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
      return rule, [d]
    var, cmp, value, dest = re.match(r"(\w+)([<>])(\d+):(\w+)", rule).groups()
    value = int(value)
    if cmp == "<":
      if d[var][1] < value:
        return dest, [d]
      if d[var][0] < value:
        a = d.copy()
        a[var] = (a[var][0], value - 1)
        b = d.copy()
        b[var] = (value, b[var][1])
        return None, [a, b]
    elif cmp == ">":
      if d[var][0] > value:
        return dest, [d]
      if d[var][1] > value:
        a = d.copy()
        a[var] = (a[var][0], value)
        b = d.copy()
        b[var] = (value + 1, b[var][1])
        return None, [a,b]
  return "bug", ["nug"]

def parse_parts(parts):
  parts = parts.strip("{}").split(",")
  d= {}
  for part in parts:
    k, v = part.split("=")
    d[k] = int(v)
  return d

def split_traverse(flows, block, state):
  while state not in ["R", "A"]:
    state, new_blocks = parse_flow(flows[state], block)
    if len(new_blocks) > 1:
      return state, new_blocks
  return state, [block]

def count(flows):
  block = {"x":(1, 4000), "m":(1, 4000), "a": (1,4000), "s":(1, 4000)}
  blocks = [block]
  ans = 0
  while blocks:
    block = blocks.pop()
    state, new_blocks = split_traverse(flows, block, "in")
    if len(new_blocks) > 1:
      blocks.extend(new_blocks)
      continue
    if state == "A":
      p = 1
      for k, (a, b) in block.items():
        p *= (b - a + 1)
      ans += p
  return ans

flows, parts = aoc.line_blocks()
flows = {re.match(r"(\w+)\{", f).group(1):f for f in flows}
print(count(flows))
