import sys
import aoc

def count(numbers, bit, pos, neg):
  length = len(numbers)
  ones = 0
  for number in numbers:
    if number[bit] == "1":
      ones += 1
  return pos if ones >= length // 2 else neg

def most(numbers, bit):
  return count(numbers, bit, "1", "0")

def least(numbers, bit):
  return count(numbers, bit, "0", "1")

def collect(numbers, func, length):
  for i in range(length):
    goal = func(numbers, i)
    numbers = set([v for v in numbers if v[i] == goal])
    if len(numbers) == 1:
      return int(list(numbers)[0], 2)

def rate(numbers, func, length):
  ans = 0
  for i in range(length):
    ans = ans * 2 + int(func(numbers, i))
  return ans

lines = [line.strip() for line in sys.stdin.readlines()]
length = len(lines[0])
size = len(lines)

start = set(lines)
oxy = collect(start, most, length)
co2 = collect(start, least, length)

aoc.cprint(rate(lines, most, length) * rate(lines, least, length))
aoc.cprint(oxy * co2)
