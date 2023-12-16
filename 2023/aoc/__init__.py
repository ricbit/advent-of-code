import sys
import itertools

def batched(iterable, n):
  it = iter(iterable)
  while batch := tuple(itertools.islice(it, n)):
    yield batch

def line_blocks():
  return [line.strip().split("\n") for line in sys.stdin.read().split("\n\n")]

class Table:
  def __init__(self, lines):
    self.table = lines
    self.w = len(self.table[0])
    self.h = len(self.table)

  @staticmethod
  def read():
    return Table([list(line.strip()) for line in sys.stdin])

  def iter_all(self, conditional=lambda x: True):
    for j, i in itertools.product(range(self.h), range(self.w)):
      if conditional(self.table[j][i]):
        yield j, i

  def valid(self, j, i):
    return 0 <= j < self.h and 0 <= i < self.w

  def cvalid(self, complex_pos):
    return 0 <= complex_pos.imag < self.h and 0 <= complex_pos.real < self.w

  def iter_neigh8(self, j, i, conditional=lambda x: True):
    for dj, di in itertools.product(range(-1, 2), repeat=2):
      if dj == 0 and di == 0:
        continue
      jj, ii = j + dj, i + di
      if self.valid(jj, ii) and conditional(self.table[jj][ii]):
        yield jj, ii

  def iter_neigh4(self, j, i, conditional=lambda x: True):
    for dj, di in itertools.product([-1, 1], repeat=2):
      jj, ii = j + dj, i + di
      if self.valid(jj, ii) and conditional(self.table[jj][ii]):
        yield jj, ii

  def __getitem__(self, j):
    return self.table[j]

  def get(self, complex_position):
    return self.table[int(complex_position.imag)][int(complex_position.real)]

  def transpose(self):
    return Table(["".join(t) for t in zip(*self.table)])
  
  def clock90(self):
    return Table([list(reversed(col)) for col in zip(*self.table)])

  def copy(self):
    return Table([line.copy() for line in self.table])


