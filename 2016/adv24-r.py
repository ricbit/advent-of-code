import itertools
import aoc

def find_pos(m):
  pos = {}
  for j, i in m.iter_all():
    if m[j][i].isdigit():
      pos[m[j][i]] = (j, i)
  return pos

def find_short(m, start, goal):
  vnext = aoc.bq([(0, start[0], start[1])])
  visited = set()
  while vnext:
    score, y, x = vnext.pop()
    if (y, x) == goal:
      return score
    for jj, ii in m.iter_neigh4(y, x):
      if m[jj][ii] != "#":
        if (jj, ii) not in visited:
          visited.add((jj, ii))
          vnext.push((score + 1, jj, ii))

def find_all_short(m, pos):
  shorts = aoc.ddict(lambda: {})
  for a, b in itertools.combinations(pos.keys(), 2):
    shorts[a][b] = find_short(m, pos[a], pos[b])
    shorts[b][a] = shorts[a][b]
  return shorts

def best(m, pos, shorts, build_path):
  others = [i for i in pos.keys() if i != "0"]
  ans = []
  for path in itertools.permutations(others):
    apath = build_path(path)
    ans.append(sum(shorts[a][b] for a, b in zip(apath, apath[1:])))
  return min(ans)


m = aoc.Table.read()
pos = find_pos(m)
shorts = find_all_short(m, pos)
aoc.cprint(best(m, pos, shorts, lambda path: ('0',)  + path))
aoc.cprint(best(m, pos, shorts, lambda path: ('0',) + path + ('0',)))
