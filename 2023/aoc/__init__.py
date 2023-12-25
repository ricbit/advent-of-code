import sys
import itertools

def flatten(composite):
  return itertools.chain.from_iterable(composite)

def shoelace(points):
  area = 0
  pairs = zip(points, itertools.islice(itertools.cycle(points), 1, None))
  for (y1, x1), (y2, x2) in pairs:
    area += x1 * y2 - x2 * y1
  return area / 2

DIRECTIONS = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

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
    for dj, di in [(0,1), (1,0), (0,-1), (-1,0)]:
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


