import aoc

def remove_layer(table):
  visited = []
  for j, i in table:
    count = 0
    for jj, ii in aoc.iter_neigh8(j, i):
      if (jj, ii) in table:
        count += 1
        if count >= 4:
          break
    else:
      visited.append((j, i))
  for j, i in visited:
    table.remove((j, i))
  return len(visited)

def remove_all(table):
  ans = 0
  while (incr := remove_layer(table)) > 0:
    ans += incr
  return ans

table = aoc.Table.read()
tableset = set((j, i) for j, i in table.iter_all(lambda x: x == "@"))
first_layer = remove_layer(tableset)
aoc.cprint(first_layer)
aoc.cprint(first_layer + remove_all(tableset))
