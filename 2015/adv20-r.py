import numpy
import aoc
import sys

goal = int(sys.stdin.read())

m = numpy.zeros(1000000, dtype=numpy.float64)
for i in range(1, 1000000):
  m[i:1000000:i] += 10 * i
aoc.cprint(numpy.argwhere(m >= goal)[0][0])

m = numpy.zeros(1000000, dtype=numpy.float64)
for i in range(1, 1000000):
  m[i:51 * i:i] += 11 * i
aoc.cprint(numpy.argwhere(m >= goal)[0][0])
