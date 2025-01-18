import sys
import math
import aoc

def babystep(alpha, beta, n):
  m = math.ceil(n ** 0.5)
  lookup = {}
  apow = 1
  for j in range(m):
    lookup[apow] = j
    apow = apow * alpha % n
  ainv = pow(alpha, -m, n)
  gamma = beta
  for i in range(m):
    if gamma in lookup:
      return i * m + lookup[gamma]
    gamma = (gamma * ainv) % n
  return None

def execute(subject, loop):
  return pow(subject, loop, 20201227)

def solve(data):
  card, door = data
  doorloop = babystep(7, door, 20201227)
  return execute(card, doorloop)

data = aoc.ints(sys.stdin.read().splitlines())
aoc.cprint(solve(data))
