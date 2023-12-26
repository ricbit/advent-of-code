import sys
from numpy.polynomial.polynomial import Polynomial
import math

after, before = 0, 0
for line in sys.stdin:
  numbers = [int(i) for i in line.split()]
  poly = Polynomial.fit(list(range(len(numbers))), numbers, len(numbers) - 1)
  after += poly(len(numbers))
  before += poly(-1)

print(math.floor(0.5 + after))
print(math.floor(0.5 + before))
