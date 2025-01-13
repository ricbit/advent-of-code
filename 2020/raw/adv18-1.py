import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def rewind(stack):
  while True:
    if (len(stack) >= 3 and isinstance(stack[-1], int) and 
        stack[-2] in "+*" and isinstance(stack[-3], int)):
      a = int(stack.pop())
      op = stack.pop()
      b = int(stack.pop())
      if op == "+":
        stack.append(a + b)
      elif op == "*":
        stack.append(a * b)
    elif (len(stack) >= 3 and stack[-1] == ")" and 
          isinstance(stack[-2], int) and stack[-3] == "("):
      stack.pop()
      value = stack.pop()
      stack.pop()
      stack.append(value)
    else:
      break

def parse(line):
  line = line.replace(" ", "")
  line = [int(c) if c.isdigit() else c for c in line]
  stack = []
  for op in line:
    stack.append(op)
    rewind(stack)
  print(stack)
  return stack[0]

def solve(lines):
  ans = 0
  for line in lines:
    value = parse(line)
    ans += value
  return ans

data = sys.stdin.read().splitlines()
aoc.cprint(solve(data))
