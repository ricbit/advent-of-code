import sys
import aoc

def parse(data, size):
  a, b = 1, 0
  for line in data:
    q = aoc.retuple("words value_", r"(.+?)( [-+]?\d+)?$", line)
    match q.words, q.value:
      case "cut", value:
        b -= value
      case "deal into new stack", _:
        a = -a
        b = -1 - b
      case "deal with increment", value:
        a = (a * value) % size
        b = (b * value) % size
  return a % size, b % size

def apply(data, size, value):
  a, b = parse(data, size)
  return (a * value + b) % size

def invert(data, size, exp, value):
  a, b = parse(data, size)
  num = (value - (pow(a, exp, size) - 1) * pow(a - 1, -1, size) * b)
  return num * pow(a, -exp, size) % size

data = [line.strip() for line in sys.stdin]
aoc.cprint(apply(data, 10007, 2019))
aoc.cprint(invert(data, 119315717514047, 101741582076661, 2020))
