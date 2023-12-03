import sys
import re

class Table:
  def __init__(self):
    self.table = [x.strip() for x in sys.stdin.readlines()]
    self.w = len(self.table[0])
    self.h = len(self.table)

  def iter_all(self, conditional=lambda x: True):
    for j in range(self.h):
      for i in range(self.w):
        if conditional(table[j][i]):
          yield j, i

  def iter8(self, j, i, conditional=lambda x: True):
    for dj in range(-1, 2):
      for di in range(-1, 2):
        jj, ii = j + dj, i + di
        if 0 <= jj < self.h and 0 <= ii < self.w:
          if conditional(table[jj][ii]):
            yield jj, ii

  def __getitem__(self, j):
    return self.table[j]

def issymbol(c):
  return (not c.isnumeric()) and c != "."

def search(table, j, i):
  return j, i + 1 - len(re.match(r"^(\d+)", table[j][i::-1]).group(1))

def number(table, j, i):
  return int(re.match(r"^(\d+)", table[j][i:]).group(1))

table = Table()
parts_visited = set()
parts_total = 0
gears_total = 0
for j, i in table.iter_all(issymbol):
  gears_visited = set()
  gears_value = 1
  for jj, ii in table.iter8(j, i, lambda c: c.isnumeric()):
    nj, ni = search(table, jj, ii)

    if (nj, ni) not in parts_visited:
      parts_visited.add((nj, ni))
      parts_total += number(table, nj, ni)

    if (nj, ni) not in gears_visited:
      gears_visited.add((nj, ni))
      gears_value *= number(table, nj, ni)

  if len(gears_visited) == 2:
    gears_total += gears_value

print(parts_total)
print(gears_total)
      

