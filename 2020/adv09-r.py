import sys
import aoc

def check(window, value):
  for x in window:
    if value - x in window and value != 2 * x:
      return True
  return False

def find_number(data, preamble):
  window = set(data[:preamble])
  for i in range(preamble, len(data)):
    if not check(window, data[i]):
      return data[i]
    window.remove(data[i - preamble])
    window.add(data[i])
  return None

def part2(data, number):
  csum = []
  acc = 0
  for x in data:
    csum.append(acc + x)
    acc += x
  indices = {x: index for index, x in enumerate(csum)}
  for i, x in enumerate(csum):
    if x - number in csum:
      seq = data[indices[x - number] + 1:i + 1]
      return min(seq) + max(seq)
  return None

data = aoc.ints(sys.stdin.read().splitlines())
preamble = 25
number = find_number(data, preamble)
aoc.cprint(number)
aoc.cprint(part2(data, number))
