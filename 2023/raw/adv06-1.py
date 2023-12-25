import sys
import re
import itertools
import math

lines = sys.stdin.readlines()
time = list(map(int, lines[0].split(":")[1].split()))
distance = list(map(int, lines[1].split(":")[1].split()))
size = len(time)
m = max(time)
wins = [0] * size
for i in range(1, m + 1):
  for k in range(size):
    timeleft = time[k] - i
    d = timeleft * i
    if d > distance[k]:
      wins[k] += 1
print(math.prod(wins))


  
