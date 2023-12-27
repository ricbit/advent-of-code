import sys
import numpy

numbers = [line.strip() for line in sys.stdin]
translate = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
tosnafu = {v:k for k, v in translate.items()}

def convert(snafu):
  total = 0
  for digit in snafu:
    total = total * 5 + translate[digit]
  return total

def snafu(decimal):
  number = [0] + [int(d) for d in numpy.base_repr(decimal, 5)]
  while True:
    for i, digit in enumerate(number):
      if digit >= 3:
        number[i] -= 5
        number[i - 1] += 1
        break
    else:
      break
  while number[0] == 0:
    number.pop(0)
  return "".join(tosnafu[d] for d in number)
      

def first():
  print(snafu(sum(convert(x) for x in numbers)))

first()
  
