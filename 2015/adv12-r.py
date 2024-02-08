import json
import sys
import re
import aoc

def jsum(j, forbidden):
  if isinstance(j, list):
    return sum(jsum(x, forbidden) for x in j)
  if isinstance(j, dict):
    if all(x not in forbidden for x in j.values()):
      return sum(jsum(x, forbidden) for x in j.values())
  if isinstance(j, int):
    return j
  return 0

doc = sys.stdin.read()
j = json.loads(doc)
aoc.cprint(jsum(j, []))
aoc.cprint(jsum(j, ["red"]))
