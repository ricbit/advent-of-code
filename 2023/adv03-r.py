import sys
import re
import itertools

class Table:
  def __init__(self):
    self.table = [x.strip() for x in sys.stdin.readlines()]
    self.w = len(self.table[0])
    self.h = len(self.table)

  def iter_all(self, conditional=lambda x: True):
    for j, i in itertools.product(range(self.h), range(self.w)):
      if conditional(self.table[j][i]):
        yield j, i

  def valid(self, j, i):
    return 0 <= j < self.h and 0 <= i < self.w

  def iter_neigh8(self, j, i, conditional=lambda x: True):
    for dj, di in itertools.product(range(-1, 2), repeat=2):
      if dj == 0 and di == 0:
        continue
      jj, ii = j + dj, i + di
      if self.valid(jj, ii) and conditional(self.table[jj][ii]):
        yield jj, ii

  def __getitem__(self, j):
    return self.table[j]

def issymbol(c):
  return (not c.isnumeric()) and c != "."

def extract_max_number(s):
  return re.match(r"^(\d+)", s).group(1)

def search_backwards(table, j, i):
  return j, i + 1 - len(extract_max_number(table[j][i::-1]))

def extract_number(table, j, i):
  return int(extract_max_number(table[j][i:]))

def unique(j, i, visited):
  insert = (j, i) not in visited
  visited.add((j, i))
  return insert

table = Table()
parts_visited = set()
parts_total = 0
gears_total = 0
for j, i in table.iter_all(issymbol):
  gears_visited = set()
  gears_value = 1
  for jj, ii in table.iter_neigh8(j, i, lambda c: c.isnumeric()):
    nj, ni = search_backwards(table, jj, ii)

    if unique(nj, ni, parts_visited):
      parts_total += extract_number(table, nj, ni)

    if unique(nj, ni, gears_visited):
      gears_value *= extract_number(table, nj, ni)

  if len(gears_visited) == 2:
    gears_total += gears_value

print(parts_total)
print(gears_total)
      

