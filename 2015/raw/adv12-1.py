import json
import sys
import re

def jsum(j):
  ans = 0
  if type(j) is list:
    return sum(jsum(x) for x in j)
  if type(j) is dict:
    if "red" not in j.values():
      return sum(jsum(x) for x in j.values())
  if type(j) is int:
    return j
  return 0

doc = sys.stdin.read()
j = json.loads(doc)
print(jsum(j))
