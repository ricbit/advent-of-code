import aoc

def remove_layer(table):
  visited = []
  for j, i in table.iter_all():
    if table[j][i] != "@":
      continue
    count = 0
    for jj, ii in table.iter_neigh8(j, i):
      if table[jj][ii] == "@":
        count += 1
        if count >= 4:
          break
    else:
      visited.append((j, i))
  for j, i in visited:
    table[j][i] = "."
  return len(visited)

def remove_all(table):
  ans = 0
  while (incr := remove_layer(table)) > 0:
    ans += incr
  return ans

table = aoc.Table.read()
table2 = table.copy()
aoc.cprint(remove_layer(table))
aoc.cprint(remove_all(table2))
