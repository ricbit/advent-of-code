import sys
import itertools
import re
import hashlib
from collections import namedtuple, defaultdict
from dataclasses import dataclass
try:
  import pyperclip
except ImportError:
  pyperclip = None

ddict = defaultdict

def first(seq):
  return next(iter(seq))

HEX = {
    'n': [0, -1], 's': [0, 1], 'ne': [1, -1], 
    'nw': [-1, 0], 'se': [1, 0], 'sw': [-1, 1]
}

def hex_dist(y, x):
  return (abs(x) + abs(y) + abs(x + y)) // 2

def spiral(visitor=lambda m, j, i, cur: cur):
  m = ddict(lambda: 0, {(0, 0): 1})
  cur, vdir = 1, -1j
  for stride in itertools.count(1):
    pos = stride * (1 + 1j)
    for side in range(4):
      for w in range(2 * stride):
        cur, pos = cur + 1, pos + vdir
        j, i = int(pos.imag), int(pos.real)
        m[(j, i)] = visitor(m, j, i, cur)
        yield j, i, m[(j, i)]
      vdir *= -1j

def ints(seq):
  return [int(i) for i in seq]

def cls():
  print("\033c", end="")

def goto0():
  print("\033[H", end="")

class bq:
  def __init__(self, start, size=300):
    self.buckets = [[] for i in range(size)]
    self.size = 0
    self.minkey = 0
    for item in start:
      self.push(item)

  def push(self, item):
    i = item[0]
    self.buckets[i].append(item)
    self.size += 1
    if i < self.minkey:
      self.minkey = i

  def pop(self):
    i = self.minkey
    while True:
      self.minkey = i
      bucket = self.buckets[i]
      if bucket:
        self.size -= 1
        if len(bucket) == 1:
          self.minkey += 1
        return bucket.pop()
      i += 1

  def __bool__(self):
    return self.size > 0

  def __len__(self):
    return self.size

@dataclass(repr=True, init=True)
class Interval:
  begin: int
  end: int

  def sub(self, b):
    m = Interval(max(self.begin, b.begin), min(self.end, b.end))
    if m.begin <= m.end:
      if self.begin < m.begin:
        yield Interval(self.begin, m.begin - 1)
      if self.end > m.end:
        yield Interval(m.end + 1, self.end)
    else:
      yield self 
  
  def __len__(self):
    return self.end - self.begin + 1

def md5(text):
  m = hashlib.md5()
  m.update(bytes(text, "ascii"))
  return m.hexdigest()

def cprint(s):
  print(s)
  if s is not None and pyperclip is not None:
    pyperclip.copy(str(s))

def retuple(fields, regexp, line):
  field_names = "".join(c for c in fields if c != "_")
  values = re.match(regexp, line).groups()
  integers = [(int(v) if "_" in n and v is not None else v) for v, n in
          zip(values, fields.split())]
  return namedtuple("autogen", field_names)(*integers)

def flatten(composite):
  return itertools.chain.from_iterable(composite)

def shoelace(points):
  area = 0
  pairs = zip(points, itertools.islice(itertools.cycle(points), 1, None))
  for (y1, x1), (y2, x2) in pairs:
    area += x1 * y2 - x2 * y1
  return area / 2

DIRECTIONS = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
DIRECTIONS2 = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

def iter_neigh4(y, x):
  for dj, di in DIRECTIONS.values():
    yield y + dj, x + di

def iter_neigh8(y, x):
  for dj, di in itertools.product(range(-1, 2), repeat=2):
    if dj == 0 and di == 0:
      continue
    yield y + dj, x + di

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
    for dj, di in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
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

  def flipx(self):
    return Table([list(reversed(t)) for t in self.table])
