import numpy
import sys
import re

def part1(lines):
  m = numpy.zeros((1000, 1000)) - 1
  for command in lines:
    parse = r"^((?:\w+|\s+)*?)\s+(\d+),(\d+).*?(\d+),(\d+)$"
    match re.match(parse, command).groups():
      case ("turn on", a, b, c, d):
        m[int(a):int(c)+1,int(b):int(d)+1] = 1
      case ("turn off", a, b, c, d):
        m[int(a):int(c)+1,int(b):int(d)+1] = -1
      case ("toggle", a, b, c, d):
        m[int(a):int(c)+1,int(b):int(d)+1] *= -1
  return numpy.count_nonzero(m == 1)

def part2(lines):
  m = numpy.zeros((1000, 1000))
  for command in lines:
    parse = r"^((?:\w+|\s+)*?)\s+(\d+),(\d+).*?(\d+),(\d+)$"
    match re.match(parse, command).groups():
      case ("turn on", a, b, c, d):
        m[int(a):int(c)+1,int(b):int(d)+1] += 1
      case ("turn off", a, b, c, d):
        m[int(a):int(c)+1,int(b):int(d)+1] -= 1
        numpy.clip(m[int(a):int(c)+1,int(b):int(d)+1], 0, 1e8,
           m[int(a):int(c)+1,int(b):int(d)+1])                
      case ("toggle", a, b, c, d):
        m[int(a):int(c)+1,int(b):int(d)+1] += 2
  return numpy.sum(m)

lines = sys.stdin.readlines()
print(part1(lines))
print(part2(lines))
