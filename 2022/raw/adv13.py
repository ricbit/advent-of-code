import functools
import sys

lines = sys.stdin.readlines()

def tribool(a, b):
  if a == b:
    return None
  return a < b

def compare(a, b):
  match a, b:
    case int(x), int(y):
      return tribool(x, y)
    case [], []:
      return None
    case [], [*y]:
      return True
    case [*x], []:
      return False
    case [x0, *x], [y0, *y] if compare(x0, y0) is not None:
      return compare(x0, y0)
    case [x0, *x], [y0, *y]:
      return compare([*x], [*y])
    case int(x), [*y]:
      return compare([x], [*y])
    case [*x], int(y):
      return compare([*x], [y])

def func_compare(a, b):
  return -1 if compare(a, b) else 1

def first():
  ans = 0
  for i, pos in enumerate(range(len(lines) // 3 + 1)):
    a, b = eval(lines[pos * 3]), eval(lines[pos * 3 + 1])
    if compare(a, b):
      ans += i + 1
  return ans

def second():
  ans = 1
  packets = [eval(line) for line in lines if line.strip()]
  packets.append([[2]])
  packets.append([[6]])
  packets.sort(key=functools.cmp_to_key(func_compare))
  for i, packet in enumerate(packets):
    if str(packet) in ["[[2]]", "[[6]]"]:
      ans *= i + 1
  return ans

print(first())
print(second())
