import sys
import itertools
import re
import hashlib
import unittest
import _md5
from collections import namedtuple, defaultdict, Counter
from dataclasses import dataclass
from io import StringIO

UNREACHABLE = None

try:
  import pyperclip
except ImportError:
  pyperclip = None

def integer_compositions(n):
  """Compositions of an integer (as an ordered sum of positive integers).
  Returns an iterator over the compositions of the given integer n.
  Example: n=3 -> 3 = 2+1 = 1+2 = 1+1+1.
  """
  if n < 0:
    raise ValueError("n must be non-negative")
  if n == 0:
    yield []
  else:
    yield [n]
    for i in range(n - 1, 0, -1):
      for composition in integer_compositions(n - i):
        yield [i] + composition

def to_binary(n, length):
  if n < 0:
    raise ValueError("n must be non-negative")
  if length < 0:
    raise ValueError("length must be non-negative")
  return ("0" * length + bin(n)[2:])[-length:]

def extrapolate(it, goal):
  seen, inv = {}, {}
  for time, key in enumerate(it, 1):
    if time == goal:
      return key
    if key in seen:
      period = time - seen[key]
      return inv[(goal - time) % period + seen[key]]
    else:
      seen[key] = time
      inv[time] = key

def invert(graph):
  inv = ddict(lambda: set())
  for key, values in graph.items():
    for value in values:
      inv[value].add(key)
  return inv

@dataclass(repr=True, init=False)
class Bounds:
  ymin: int
  ymax: int
  xmin: int
  xmax: int

def bounds(points):
  b = Bounds()
  b.ymin = min(point[0] for point in points)
  b.ymax = max(point[0] for point in points)
  b.xmin = min(point[1] for point in points)
  b.xmax = max(point[1] for point in points)
  return b

class bidi:
  def __init__(self, orig, circular=True):
    self.start = 0
    self.values = [[i - 1, i + 1, value] for i, value in enumerate(orig)]
    self.size = len(self.values)
    self.top = len(self.values)
    if self.size > 0:
      if circular:
        self.values[self.start][0] = self.top - 1
        self.values[self.top - 1][1] = 0
      else:
        self.values[self.start][0] = -1
        self.values[self.top - 1][1] = -1

  def valid(self, pos):
    return pos >= 0

  def __iter__(self):
    self.current = self.start
    self.stop = self.start
    self.loaded = False
    return self

  def __next__(self):
    if not self.size:
      raise StopIteration
    if self.current != -1:
      if self.loaded and self.current == self.stop:
        raise StopIteration
      value = self.values[self.current][2]
      self.current = self.next(self.current)
      self.loaded = True
      return value
    else:
      raise StopIteration

  def next(self, pos):
    return self.values[pos][1]

  def value(self, pos):
    return self.values[pos][2]

  def prev(self, pos):
    return self.values[pos][0]

  def remove(self, pos):
    if pos == self.start:
      self.start = self.values[pos][1]
    if self.values[pos][0] != -1:
      self.values[self.values[pos][0]][1] = self.values[pos][1]
    if self.values[pos][1] != -1:
      self.values[self.values[pos][1]][0] = self.values[pos][0]
    self.size -= 1

  def insert_after(self, pos, value):
    self.values.append([pos, self.values[pos][1], value])
    self.values[self.values[pos][1]][0] = self.top
    self.values[pos][1] = self.top
    self.size += 1
    self.top += 1
    return self.top - 1

  def __len__(self):
    return self.size


def maxindex(x):
  if isinstance(x, list):
    return max(range(len(x)), key=lambda q: x[q])
  else:
    return max(x.keys(), key=lambda q: x[q])

def minindex(x):
  if isinstance(x, list):
    return min(range(len(x)), key=lambda q: x[q])
  else:
    return min(x.keys(), key=lambda q: x[q])

ddict = defaultdict

def first(seq):
  return next(iter(seq))

def ifirst(seq):
  return itertools.islice(seq, 0, 1)

HEX = {
    'n': [0, -1], 's': [0, 1], 'ne': [1, -1], 
    'nw': [-1, 0], 'se': [1, 0], 'sw': [-1, 1]
}

HEX2 = {
    'e': [2, 0], 'w': [-2, 0], 'ne': [1, -1],
    'nw': [-1, -1], 'se': [1, 1], 'sw': [-1, 1]
}

def hex_dist(y, x):
  return (abs(x) + abs(y) + abs(x + y)) // 2

def spiral(visitor=lambda m, j, i, cur: cur):
  m = ddict(lambda: 0, {(0, 0): 1})
  cur, vdir = 1, -1j
  yield 0, 0, 1
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

def ints_read(src=sys.stdin):
  ans = []
  for line in src:
    ans.append(ints(line.strip().split()))
  return ans

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

# Intervals are inclusive
@dataclass(repr=True, init=True, order=True)
class Interval:
  begin: int
  end: int

  def inter(self, b):
    m = Interval(max(self.begin, b.begin), min(self.end, b.end))
    if m.begin <= m.end:
      yield m

  def sub(self, b):
    m = Interval(max(self.begin, b.begin), min(self.end, b.end))
    if m.begin <= m.end:
      if self.begin < m.begin:
        yield Interval(self.begin, m.begin - 1)
      if self.end > m.end:
        yield Interval(m.end + 1, self.end)
    else:
      yield self 

  def union(self, b):
    if max(self.begin, b.begin) <= min(self.end, b.end):
      yield Interval(min(self.begin, b.begin), max(self.end, b.end))
  
  def __len__(self):
    return self.end - self.begin + 1

def md5(text):
  m = _md5.md5()
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

def retuple_read(fields, regexp, src=sys.stdin):
  out = []
  for line in src:
    out.append(retuple(fields, regexp, line.strip()))
  return out

def flatten(composite):
  return itertools.chain.from_iterable(composite)

def shoelace(points):
  # points in (y, x) format, counterclockwise is negative
  area = 0
  pairs = zip(points, itertools.islice(itertools.cycle(points), 1, None))
  for (y1, x1), (y2, x2) in pairs:
    area += x1 * y2 - x2 * y1
  return area / 2

CDIRECTIONS = {"R": 1, "L": -1, "U": -1j, "D": 1j}
CDIRECTIONS2 = {">": 1, "<": -1, "^": -1j, "v": 1j}
CDIRECTIONS3 = {"E": 1, "W": -1, "N": -1j, "S": 1j}

def get_cdir(vdir):
  for i in [CDIRECTIONS, CDIRECTIONS2, CDIRECTIONS3]:
    if vdir in i.keys():
      return i

def get_dir(vdir):
  vmap = {}
  for k, v in get_cdir(vdir).items():
    vmap[k] = (int(v.imag), int(v.real))
  return vmap

def get_diagonals():
  return [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]

def iter_neigh4(y, x):
  for dj, di in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
    yield y + dj, x + di

def iter_neigh8(y, x):
  for dj, di in itertools.product(range(-1, 2), repeat=2):
    if dj == 0 and di == 0:
      continue
    yield y + dj, x + di

def line_blocks():
  return [line.splitlines() for line in sys.stdin.read().rstrip().split("\n\n")]

def transpose(table):
  return [list(t) for t in zip(*table)]
  

class Table:
  def __init__(self, lines):
    self.table = lines
    self.w = len(self.table[0])
    self.h = len(self.table)

  def __repr__(self):
    return "\n".join(str(line) for line in self.table)

  @staticmethod
  def read():
    return Table([list(line.rstrip()) for line in sys.stdin])

  def iter_all(self, conditional=lambda x: True):
    for j, i in itertools.product(range(self.h), range(self.w)):
      if conditional(self.table[j][i]):
        yield j, i

  def grow(self, empty=" "):
    empty_line = [empty] * (self.w + 2)
    new_table = [empty_line] + [[empty] + line + [empty] for line in self.table] + [empty_line]
    return Table(new_table)

  def find(self, value):
    for j, i in self.iter_all():
      if self.table[j][i] == value:
        return (j, i)
 
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

  def iter_neigh4(self, j, i):
    if j > 0:
      yield j - 1, i
    if j < self.h - 1:
      yield j + 1, i
    if i > 0:
      yield j, i - 1
    if i < self.w - 1:
      yield j, i + 1

  def iter_diamond(self, y, x, d):
    for j in range(max(0, y - d), min(self.h, y + d + 1)):
      dj = abs(j - y)
      for i in range(max(0, x - d + dj), min(self.w, x + d - dj + 1)):
        dist = dj + abs(x - i)
        yield j, i, dist

  def __getitem__(self, j):
    return self.table[j]

  def get(self, complex_position):
    return self.table[int(complex_position.imag)][int(complex_position.real)]

  def put(self, complex_position, value):
    self.table[int(complex_position.imag)][int(complex_position.real)] = value

  def transpose(self):
    return Table([list(t) for t in zip(*self.table)])
  
  def clock90(self):
    return Table([list(reversed(col)) for col in zip(*self.table)])

  def copy(self):
    return Table([line.copy() for line in self.table])

  def flipx(self):
    return Table([list(reversed(t)) for t in self.table])

  def iter_quad(self, y, x, h, w):
    for j in range(h):
      for i in range(w):
        yield y + j, x + i

# unit tests

class TestMaxindex(unittest.TestCase):
    def test_maxindex_with_list(self):
        self.assertEqual(maxindex([1, 3, 2]), 1)

    def test_maxindex_with_dict(self):
        self.assertEqual(maxindex({0: 1, 1: 3, 2: 2}), 1)


class TestMd5(unittest.TestCase):
    def test_md5(self):
        self.assertEqual(md5("hello"), "5d41402abc4b2a76b9719d911017c592")


class TestInterval(unittest.TestCase):
    def test_sub_no_overlap(self):
        interval = Interval(1, 5)
        result = list(interval.sub(Interval(6, 10)))
        self.assertEqual(result, [interval])

    def test_sub_overlap(self):
        interval = Interval(1, 10)
        result = list(interval.sub(Interval(5, 7)))
        self.assertEqual(result, [Interval(1, 4), Interval(8, 10)])


class TestHexDist(unittest.TestCase):
    def test_hex_dist(self):
        # Test cases for hex_dist function
        self.assertEqual(hex_dist(0, 0), 0)
        self.assertEqual(hex_dist(1, -1), 1)
        self.assertEqual(hex_dist(2, -1), 2)
        self.assertEqual(hex_dist(-3, 2), 3)


class TestSpiral(unittest.TestCase):
    def test_spiral(self):
        # Test cases for spiral function
        result = list(itertools.islice(spiral(), 5))
        expected = [(0, 0, 1), (0, 1, 2), (-1, 1, 3), (-1, 0, 4), (-1, -1, 5)]
        self.assertEqual(result, expected)


class TestRetuple(unittest.TestCase):
    def test_retuple(self):
        # Test the retuple function
        fields = "x_ y_ label"
        regexp = r"(\d+) (\d+) (\w+)"
        line = "123 456 label123"
        result = retuple(fields, regexp, line)
        self.assertEqual(result.x, 123)
        self.assertEqual(result.y, 456)
        self.assertEqual(result.label, "label123")


class TestRetupleRead(unittest.TestCase):
    def test_retuple_read(self):
        # Test the retuple_read function
        fields = "x_ y_ label"
        regexp = r"(\d+) (\d+) (\w+)"
        input_data = "123 456 label123\n789 1011 label456"
        src = StringIO(input_data)
        result = retuple_read(fields, regexp, src)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].x, 123)
        self.assertEqual(result[1].label, "label456")


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        # Test the flatten function
        composite = [[1, 2, 3], [4, 5], [6]]
        result = list(flatten(composite))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table([
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ])

    def test_iter_all(self):
        result = list(self.table.iter_all())
        expected = [(j, i) for j, i in itertools.product(range(3), range(3))]
        self.assertEqual(result, expected)

    def test_valid(self):
        self.assertTrue(self.table.valid(0, 0))
        self.assertFalse(self.table.valid(-1, 0))
        self.assertFalse(self.table.valid(3, 3))

    def test_cvalid(self):
        self.assertTrue(self.table.cvalid(complex(0, 0)))
        self.assertFalse(self.table.cvalid(complex(-1, 0)))
        self.assertFalse(self.table.cvalid(complex(3, 3)))

    def test_iter_neigh8(self):
        neighbors = list(self.table.iter_neigh8(1, 1))
        expected = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertEqual(sorted(neighbors), expected)

    def test_iter_neigh4(self):
        neighbors = list(self.table.iter_neigh4(1, 1))
        expected = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertEqual(sorted(neighbors), expected)

    def test_transpose(self):
        transposed = self.table.transpose()
        expected = Table([
            ['1', '4', '7'],
            ['2', '5', '8'],
            ['3', '6', '9']
        ])
        self.assertEqual(transposed.table, expected.table)

    def test_clock90(self):
        rotated = self.table.clock90()
        expected = Table([
            ['7', '4', '1'],
            ['8', '5', '2'],
            ['9', '6', '3']
        ])
        self.assertEqual(rotated.table, expected.table)

    def test_copy(self):
        copy_table = self.table.copy()
        self.assertEqual(copy_table.table, self.table.table)
        self.assertIsNot(copy_table, self.table)

    def test_flipx(self):
        flipped = self.table.flipx()
        expected = Table([
            ['3', '2', '1'],
            ['6', '5', '4'],
            ['9', '8', '7']
        ])
        self.assertEqual(flipped.table, expected.table)

    def test_iter_quad(self):
        quad = list(self.table.iter_quad(1, 1, 2, 2))
        expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
        self.assertEqual(quad, expected)


class TestShoelace(unittest.TestCase):
    def test_shoelace(self):
        # Testing the shoelace formula for area calculation
        points = [(1, 6), (3, 1), (7, 2), (4, 4), (8, 5)]
        self.assertAlmostEqual(shoelace(points), -16.5)


class TestIterNeigh4(unittest.TestCase):
    def test_iter_neigh4(self):
        # Testing 4-neighbor iteration
        neighbors = list(iter_neigh4(1, 1))
        expected = [(0, 1), (1, 2), (2, 1), (1, 0)]
        self.assertEqual(sorted(neighbors), sorted(expected))


class TestIterNeigh8(unittest.TestCase):
    def test_iter_neigh8(self):
        # Testing 8-neighbor iteration
        neighbors = list(iter_neigh8(1, 1))
        expected = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertEqual(sorted(neighbors), expected)


class TestLineBlocks(unittest.TestCase):
    def test_line_blocks(self):
        # Mocking stdin for testing line_blocks function
        test_input = 'line1\nline2\n\nline3\nline4'
        sys.stdin = StringIO(test_input)
        result = line_blocks()
        expected = [['line1', 'line2'], ['line3', 'line4']]
        self.assertEqual(result, expected)
        sys.stdin = sys.__stdin__  # Reset stdin


class TestBq(unittest.TestCase):

    def test_negative_keys(self):
        queue = bq(start=[(-2, 'a'), (-1, 'b')])
        self.assertEqual(queue.pop(), (-2, 'a'))
        self.assertEqual(queue.pop(), (-1, 'b'))

    def test_large_keys(self):
        queue = bq(start=[(305, 'a'), (400, 'b')], size=500)
        self.assertEqual(queue.pop(), (305, 'a'))
        self.assertEqual(queue.pop(), (400, 'b'))

    def test_sporadic_keys(self):
        queue = bq(start=[(10, 'a'), (1, 'b'), (50, 'c')])
        self.assertEqual(queue.pop(), (1, 'b'))
        self.assertEqual(queue.pop(), (10, 'a'))
        self.assertEqual(queue.pop(), (50, 'c'))

    def test_repeated_push_pop(self):
        queue = bq(start=[(1, 'a')])
        queue.push((2, 'b'))
        self.assertEqual(queue.pop(), (1, 'a'))
        self.assertEqual(queue.pop(), (2, 'b'))

    def test_pop_empty_queue(self):
        queue = bq(start=[])
        self.assertFalse(queue)

    def test_same_key_items(self):
        original = [(1, 'a'), (1, 'b')]
        queue = bq(start=original)
        items = set([queue.pop(), queue.pop()])
        self.assertEqual(items, set(original))

    def test_descending_order_push(self):
        queue = bq(start=[(3, 'c'), (2, 'b'), (1, 'a')])
        self.assertEqual(queue.pop(), (1, 'a'))
        self.assertEqual(queue.pop(), (2, 'b'))
        self.assertEqual(queue.pop(), (3, 'c'))

    def test_complex_items(self):
        queue = bq(start=[(1, {'key': 'value'}), (2, [1, 2, 3])])
        self.assertEqual(queue.pop(), (1, {'key': 'value'}))
        self.assertEqual(queue.pop(), (2, [1, 2, 3]))

    def test_large_number_of_items(self):
        queue = bq(start=[(i, i) for i in range(1000)], size=2000)
        for i in range(1000):
            self.assertEqual(queue.pop(), (i, i))


class TestFirstFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(first([1, 2, 3]), 1)

    def test_empty_sequence(self):
        with self.assertRaises(StopIteration):
            first([])

    def test_different_types(self):
        self.assertEqual(first("hello"), 'h')
        self.assertEqual(first({1, 2, 3}), 1)


class TestIntsFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(ints(["1", "2", "3"]), [1, 2, 3])

    def test_mixed_input(self):
        self.assertEqual(ints([1, "2", 3.0]), [1, 2, 3])

    def test_empty_sequence(self):
        self.assertEqual(ints([]), [])

    def test_non_numeric_strings(self):
        with self.assertRaises(ValueError):
            ints(["a", "b", "c"])

class TestBidi(unittest.TestCase):

    def setUp(self):
        self.sequence = bidi("abc")

    def test_initial_length(self):
        self.assertEqual(len(self.sequence), 3)

    def test_remove(self):
        self.sequence.remove(1)  # remove 'b'
        self.assertEqual(len(self.sequence), 2)
        self.assertEqual(['a', 'c'], list(self.sequence))

    def test_simple_iteration(self):
        values = list(self.sequence)
        self.assertEqual(values, ['a', 'b', 'c'])

    def test_init(self):
        # Empty list
        bd = bidi([])
        self.assertEqual(len(bd), 0)

        # Non-empty list
        bd = bidi([1, 2, 3])
        self.assertEqual(len(bd), 3)

        # Circular list
        bd = bidi([1, 2, 3], circular=True)
        self.assertEqual(bd.next(2), 0)
        self.assertEqual(bd.prev(0), 2)

        # Non-circular list
        bd = bidi([1, 2, 3], circular=False)
        self.assertEqual(bd.next(2), -1)
        self.assertEqual(bd.prev(0), -1)

    def test_valid(self):
        bd = bidi([1, 2, 3])
        self.assertTrue(bd.valid(1))
        self.assertFalse(bd.valid(-1))

    def test_iteration(self):
        bd = bidi([])
        self.assertEqual(list(bd), [])

        bd = bidi([1, 2, 3])
        self.assertEqual(list(bd), [1, 2, 3])

    def test_navigation(self):
        bd = bidi([1, 2, 3])
        self.assertEqual(bd.next(0), 1)
        self.assertEqual(bd.prev(1), 0)
        self.assertEqual(bd.value(1), 2)

    def test_modification(self):
        bd = bidi([1, 2, 3])

        # Remove
        bd.remove(1)
        self.assertEqual(list(bd), [1, 3])

        # Insert
        bd.insert_after(0, 2)
        self.assertEqual(list(bd), [1, 2, 3])

    def test_length(self):
        bd = bidi([])
        self.assertEqual(len(bd), 0)

        bd = bidi([1, 2, 3])
        self.assertEqual(len(bd), 3)

        bd.remove(1)
        self.assertEqual(len(bd), 2)

        bd.insert_after(1, 4)
        self.assertEqual(len(bd), 3)

if __name__ == '__main__':
    unittest.main()
