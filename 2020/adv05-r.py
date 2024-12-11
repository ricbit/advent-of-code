import sys
import itertools
import aoc

translation = {k:v for k,v in itertools.batched("F0B1L0R1", 2)}

def decode(lines):
  for line in lines:
    binary = "".join(translation[c] for c in line)
    yield (int(binary[:7], 2) * 8 + int(binary[7:], 2))

def find_missing(seats):
  all_seats = range(min(seats) + 1, max(seats) - 1)
  for seat in all_seats:
    if seat not in seats:
      return seat

data = sys.stdin.read().splitlines()
seats = list(decode(data))
aoc.cprint(max(seats))
aoc.cprint(find_missing(seats))

