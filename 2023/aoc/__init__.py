import sys
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

