import sys
import re
import itertools
import math
import multiprocessing

lines = sys.stdin.readlines()
time = lines[0].split(":")[1].split()
distance = lines[1].split(":")[1].split()
stride = 1000

def check_win(star):
  time, distance, i = star
  wins = 0
  for j in range(0, stride):
    ii = i * stride + j
    if (time - ii) * ii > distance:
      wins += 1
  return wins

def count_wins(time, distance):
  with multiprocessing.Pool(8) as p:
    star = ((time, distance, i) for i in range(0, time // stride + 1))
    return sum(p.imap_unordered(check_win, star, chunksize=100))

print(math.prod(count_wins(int(t), int(d)) for t, d in zip(time, distance)))
print(count_wins(int("".join(time)), int("".join(distance))))

  
