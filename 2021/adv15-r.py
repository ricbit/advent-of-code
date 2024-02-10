import sys
import heapq
import aoc

small = aoc.Table([[int(i) for i in line.strip()] for line in sys.stdin])
h, w = 5 * small.h, 5 * small.w
cave = aoc.Table([[(small[j % small.h][i % small.w] - 1 + j // small.h + i // small.w) % 9 + 1
        for i in range(w)] for j in range(h)])

def search(cave):
  h, w = cave.h, cave.w
  heap = [(0, 0, 0)]
  smallest = [[100 * w * h] * w for i in range(h)]
  while heap:
    value, j, i = heapq.heappop(heap)
    if j == h - 1 and i == w - 1:
      return value
    for jj, ii in cave.iter_neigh4(j, i):
      nextvalue = value + cave[jj][ii]
      if nextvalue < smallest[jj][ii]:
        heapq.heappush(heap, (nextvalue, jj, ii))
        smallest[jj][ii] = nextvalue

aoc.cprint(search(small))
aoc.cprint(search(cave))


