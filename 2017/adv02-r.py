import sys
import itertools
import aoc

lines = [line.strip() for line in sys.stdin]
checksum, sum_divisors = 0, 0
for line in lines:
  numbers = [int(i) for i in line.split()]
  checksum += max(numbers) - min(numbers)
  for a in itertools.combinations(numbers, 2):
    if max(a) % min(a) == 0:
      sum_divisors += max(a) // min(a)
aoc.cprint(checksum)
aoc.cprint(sum_divisors)
