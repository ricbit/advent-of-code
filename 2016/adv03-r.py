import sys
import itertools
import aoc

def count_triangles(it):
  ans = 0
  for a, b, c in it:
    if a < b + c and b < a + c and c < a + b:
      ans += 1
  return ans

numbers = [aoc.ints(line.split()) for line in sys.stdin]
aoc.cprint(count_triangles(numbers))
tnumbers = zip(*numbers)
aoc.cprint(count_triangles(itertools.batched(aoc.flatten(tnumbers), 3)))
  
