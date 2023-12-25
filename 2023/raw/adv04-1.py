import sys
import re
import itertools
import math

ans = 0
for line in sys.stdin:
  card, numbers = line.split(":")
  win, maybe = numbers.split("|")
  win = set([int(i) for i in win.split()])
  maybe = [int(i) for i in maybe.split()]
  a = 0
  for n in maybe:
    if n in win:
      a += 1
  if a > 0:
    ans += 2 ** (a - 1)
print(ans)
    
  
