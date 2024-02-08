import numpy

m = numpy.zeros(10000000)
for i in range(1, 1000000):
  m[i:51 * i:i] += 11 * i

print(numpy.argwhere(m >= 34000000))
