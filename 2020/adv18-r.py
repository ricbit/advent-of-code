import sys
import aoc

def rewind1(stack):
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

def rewind2(stack):
  while True:
    if (len(stack) >= 3 and isinstance(stack[-1], int) and
        stack[-2] in "+" and isinstance(stack[-3], int)):
      a = int(stack.pop())
      stack.pop()
      b = int(stack.pop())
      stack.append(a + b)
    elif (len(stack) >= 4 and isinstance(stack[-1], str) and
          stack[-1] in ")=" and isinstance(stack[-2], int) and
          stack[-3] == "*" and isinstance(stack[-4], int)):
      close = stack.pop()
      a = stack.pop()
      stack.pop()
      b = stack.pop()
      stack.append(a * b)
      stack.append(close)
    elif (len(stack) >= 3 and stack[-1] == ")" and
          isinstance(stack[-2], int) and stack[-3] == "("):
      stack.pop()
      value = stack.pop()
      stack.pop()
      stack.append(value)
    else:
      break

def parse(line, rewind):
  line = line.replace(" ", "") + "="
  line = [int(c) if c.isdigit() else c for c in line]
  stack = []
  for op in line:
    stack.append(op)
    rewind(stack)
  return stack[0]

def solve(lines, rewind):
  ans = 0
  for line in lines:
    value = parse(line, rewind)
    ans += value
  return ans

data = sys.stdin.read().splitlines()
aoc.cprint(solve(data, rewind1))
aoc.cprint(solve(data, rewind2))
