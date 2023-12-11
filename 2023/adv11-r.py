import sys
import itertools

lines = [line.strip() for line in sys.stdin]

def empty_rows(lines):
  current = 0
  for i, line in enumerate(lines):
    if "#" not in line:
      current += 1
    yield current

def transpose(lines):
  return list(zip(*lines))

def find_galaxies(lines):
  for j, row in enumerate(lines):
    for i, c in enumerate(row):
      if c == "#":
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

rows = list(empty_rows(lines))
cols = list(empty_rows(transpose(lines)))
galaxies = list(find_galaxies(lines))
print(all_distances(galaxies, rows, cols, 2))
print(all_distances(galaxies, rows, cols, 1000000))

