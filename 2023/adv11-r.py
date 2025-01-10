import itertools
import aoc

def empty_rows(lines):
  current = 0
  for line in lines.table:
    if "#" not in line:
      current += 1
    yield current

def find_galaxies(lines):
  for j, i in lines.iter_all():
    if lines[j][i] == "#":
      yield (j, i)

def shortest(sj, si, j, i, rows, cols, expand):
  dist = abs(j - sj) + abs(i - si)
  dist += (expand - 1) * (rows[max(j, sj)] - rows[min(j, sj)])
  dist += (expand - 1) * (cols[max(i, si)] - cols[min(i, si)])
  return dist

def all_distances(galaxies, rows, cols, expand):
  ans = 0
  for (j, i), (sj, si) in itertools.combinations(galaxies, 2):
    ans += shortest(j, i, sj, si, rows, cols, expand)
  return ans

lines = aoc.Table.read()
rows = list(empty_rows(lines))
cols = list(empty_rows(lines.transpose()))
galaxies = list(find_galaxies(lines))
aoc.cprint(all_distances(galaxies, rows, cols, 2))
aoc.cprint(all_distances(galaxies, rows, cols, 1000000))
