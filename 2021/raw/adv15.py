import sys
import heapq

cave = [[int(i) for i in line.strip()] for line in sys.stdin]
h, w = len(cave), len(cave[0])
heap = [(0, 0, 0)]
visited = [[False] * w for i in range(h)]
smallest = [[100 * w * h] * w for i in range(h)]

def neigh(y, x):
  if x > 0: yield y, x - 1
  if x < w - 1: yield y, x + 1
  if y > 0: yield y - 1, x
  if y < h - 1: yield y + 1, x

while heap:
  value, j, i = heapq.heappop(heap)
  visited[j][i] = True
  if j == h - 1 and i == w - 1:
    print(value)
    break
  for jj, ii in neigh(j, i):
    nextvalue = value + cave[jj][ii]
    if not visited[jj][ii] and nextvalue < smallest[jj][ii]:
      heapq.heappush(heap, (nextvalue, jj, ii))
      smallest[jj][ii] = nextvalue




