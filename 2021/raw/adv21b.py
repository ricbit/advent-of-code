import sys
import itertools
import heapq
import collections
import heapq

p1 = int(input().split(":")[1]) - 1
p2 = int(input().split(":")[1]) - 1
M = 32

def make_dp_matrix():
  mat = [[[[0] * 10 for i in range(10)] for j in range(M)] for k in range(M)]
  return mat

def r(x):
  return x % 10

def moves():
  dice = collections.Counter()
  for a,b,c in itertools.product(range(1, 4), repeat=3):
    dice[a + b + c] += 1
  return dice

# mat[s1][s2][p1][p2]
mat1 = make_dp_matrix()
mat2 = make_dp_matrix()
mat2[0][0][p1][p2] = 1
dice = moves()
heap = [(0, 0, 0, p1, p2)]

while heap:
  step, s1, s2, p1, p2 = heapq.heappop(heap)
  if step % 2 == 0:
    mat2[s1][s2][p1][2] = 
    for d, value in dice.items():
      p1 = (p1 + d) % 10
      s1 += p1 + 1

print(444356092776315, 341960390180808)    
