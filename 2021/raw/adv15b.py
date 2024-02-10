import sys
import heapq

smallcave = [[int(i) for i in line.strip()] for line in sys.stdin]
smallh, smallw = len(smallcave), len(smallcave[0])
h, w = 5 * smallh, 5 * smallw
cave = [[(smallcave[j % smallh][i % smallw] - 1 + j // smallh + i // smallw) % 9 + 1
        for i in range(w)] for j in range(h)]
heap = [(0, 0, 0)]
smallest = [[100 * w * h] * w for i in range(h)]

def neigh(y, x):
  if x > 0: yield y, x - 1
  if x < w - 1: yield y, x + 1
  if y > 0: yield y - 1, x
  if y < h - 1: yield y + 1, x

while heap:
  value, j, i = heapq.heappop(heap)
  if j == h - 1 and i == w - 1:
    print(value)
    break
  for jj, ii in neigh(j, i):
    nextvalue = value + cave[jj][ii]
    if nextvalue < smallest[jj][ii]:
      heapq.heappush(heap, (nextvalue, jj, ii))
      smallest[jj][ii] = nextvalue




