import sys
import re
import math
import aoc

def split(d, var, lower, upper):
  a = d.copy()
  a[var] = (a[var][0], lower)
  b = d.copy()
  b[var] = (upper, b[var][1])
  return None, [a, b]

def parse_flow(flow, d):
  name, rules = re.match(r"(\w+)\{(.*)\}", flow).groups()
  for rule in rules.split(","):
    if ":" not in rule:
      return rule, [d]
    var, cmp, value, dest = re.match(r"(\w+)([<>])(\d+):(\w+)", rule).groups()
    value = int(value)
    if cmp == "<":
      if d[var][1] < value:
        return dest, [d]
      if d[var][0] < value:
        return split(d, var, value - 1, value)
    elif cmp == ">":
      if d[var][0] > value:
        return dest, [d]
      if d[var][1] > value:
        return split(d, var, value, value + 1)

def parse_parts(parts):
  parts = [part.split("=") for part in parts.strip("{}").split(",")]
  return {k:int(v) for k, v in parts}

def split_traverse(flows, block, state):
  while state not in ["R", "A"]:
    state, new_blocks = parse_flow(flows[state], block)
    if len(new_blocks) > 1:
      return state, new_blocks
  return state, [block]

def count(flows):
  block = {"x":(1, 4000), "m":(1, 4000), "a":(1, 4000), "s":(1, 4000)}
  blocks, ans = [block], 0
  while blocks:
    block = blocks.pop()
    state, new_blocks = split_traverse(flows, block, "in")
    if len(new_blocks) > 1:
      blocks.extend(new_blocks)
      continue
    if state == "A":
      ans += math.prod(b - a + 1 for k, (a, b) in block.items())
  return ans

def validate(flows, part):
  d = {k:(v, v) for k, v in parse_parts(part).items()}
  state, _ = split_traverse(flows, d, "in")
  return sum(a for a, b in d.values()) if state == "A" else 0

flows, parts = aoc.line_blocks()
flows = {re.match(r"(\w+)\{", f).group(1):f for f in flows}
print(sum(validate(flows, part) for part in parts))
print(count(flows))
