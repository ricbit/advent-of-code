import sys
import re
import itertools
import math

ans = 0
for line in sys.stdin:
  numb = [int(i) for i in line.split()]
  mat = [numb]
  while True:
    d = [b - a for a, b in zip(numb, numb[1:])]
    numb = d
    mat.append(d)
    if len(set(d)) == 1:
      x = 0
      for m in reversed(mat):
        x = m[0] - x
      ans += x
      break
  #print(mat)
print(ans)
  
