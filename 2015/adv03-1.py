import itertools

dirs = {">": (0, 1), "<": (0, -1), "^": (1, 0), "v": (-1, 0)}
visited = set([(0, 0)])
j, i = 0, 0
rj, ri = 0, 0
for c, rc in itertools.batched(input().strip(), 2):
  dj, di = dirs[c]
  j += dj
  i += di
  visited.add((j, i))
  dj, di = dirs[rc]
  rj += dj
  ri += di
  visited.add((rj, ri))
print(len(visited))
  
