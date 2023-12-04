import sys
import re
import itertools
import math

ans = 0
lines = sys.stdin.readlines()
total = len(lines)
copies = [1] * total
for pos, line in enumerate(lines):
  card, numbers = line.split(":")
  win, maybe = numbers.split("|")
  win = set([int(i) for i in win.split()])
  maybe = [int(i) for i in maybe.split()]
  a = 0
  for n in maybe:
    if n in win:
      a += 1
  if a > 0:
    for i in range(a):
      copies[pos + i + 1] += copies[pos]
print(sum(copies))
    
  
