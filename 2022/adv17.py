import itertools
import more_itertools
import sys
from dataclasses import dataclass

rocks_original = [
  ["..####."],

  ["...#...",
   "..###..",
   "...#..."],

  ["....#..",
   "....#..",
   "..###.."],

  ["..#....",
   "..#....",
   "..#....",
   "..#...."],

  ["..##...",
   "..##..."]
]

def read_rocks():
  rocks = []
  for rock in rocks_original:
    lines = []
    for line in rock:
      bin_line = line.replace(".", "0").replace("#", "1")
      lines.append(int(bin_line, 2) * 2)
    rocks.append(lines)
  return rocks

@dataclass(init=False)
class State:
  well: list[int]
  y: int
  x: int

def collision(rock, well):
  return any((r & w) > 0 for r, w in zip(rock, well))

def move_rock(rock, x):
  if x < 0:
    rock <<= -x
  else:
    rock >>= x
  return rock

def apply_wind(iter_wind, rock, state):
  wind = more_itertools.first(iter_wind)
  delta = -1 if wind == "<" else 1
  moving_rock = [move_rock(line, state.x + delta) for line in rock]
  if not collision(moving_rock, state.well[state.y:state.y + len(rock)]):
    state.x += delta
  return False

def apply_gravity(iter_wind, rock, state):
  moving_rock = [move_rock(line, state.x) for line in rock]
  new_y = state.y + 1
  blocked = collision(moving_rock, state.well[new_y:new_y + len(rock)])
  if not blocked:
    state.y += 1
  return blocked

empty_wall = 257

def clean_well(state):
  while (state.well[0] & ~empty_wall) == 0:
    state.well.pop(0)
  return state

def trim_well(state, rock):
  clean_well(state)
  state.well = [empty_wall] * (3 + len(rock)) + state.well

def bin_to_wall(line):
  line = "".join("0" * 8 + bin(line)[2:])[-9:]
  line = line.replace("0", ".").replace("1", "#")
  return line

def rock_blit(rock_line, wall_line):
  line = bin_to_wall(rock_line).replace("#", "@")
  blitted = []
  for a, b in zip(line, wall_line):
    blitted.append(a if a == "@" else b)
  return "".join(blitted)

def dump_state(state, rock):
  lines = [bin_to_wall(line) for line in state.well]
  for j in range(len(rock)):
    moving_rock = move_rock(rock[j], state.x)
    lines[j + state.y] = rock_blit(moving_rock, lines[j + state.y])
  print("\n".join(lines))
  print()

def stamp_rock(state, rock):
  for j, line in enumerate(rock):
    state.well[state.y + j] |= move_rock(line, state.x)

class Wind:
  def __init__(self, patterns):
    self.patterns = patterns
    self.index = 0
  def iter_wind(self):
    for i in itertools.cycle(range(len(self.patterns))):
      self.index = i
      yield self.patterns[i]
  def query_position(self):
    return self.index

class CycleDetector:
  def __init__(self):
    self.values = {}
    self.start = None
    self.period = None
    self.index = 0
    self.heights = []
  def add(self, value, height):
    self.heights.append(height)
    if self.start is not None:
      return True
    if value in self.values:
      self.start = self.values[value][0]
      self.period = self.index - self.start
      return False
    else:
      self.values[value] = (self.index, height)
      self.index += 1
      return True
  def period_height(self, periods):
    top = self.heights[self.period + self.start]
    bottom = self.heights[self.start]
    return bottom + periods * (top - bottom)

def well_height(state):
  empty = 0
  while state.well[empty] & ~empty_wall == 0:
    empty += 1
  return len(state.well) - empty - 1

class RockManager:
  def __init__(self, rocks):
    self.rocks = len(rocks)
    self.left = -1
  def start_countdown(self, detector, state, limit):
    rocks_period = detector.period * self.rocks
    rocks_start = detector.start * self.rocks
    self.required = (limit - rocks_start) // rocks_period
    self.left = limit - self.required * rocks_period - rocks_start
  def check_countdown(self):
    self.left -= 1
    return self.left == -1

def simulate(wind_patterns, rocks, limit):
  state = State()
  state.well = [2 ** 9 - 1]
  state.x, state.y = 0, 0
  iter_rocks = itertools.cycle(rocks)
  wind = Wind(wind_patterns)
  iter_wind = wind.iter_wind()
  detector = CycleDetector()
  manager = RockManager(rocks)
  for rock_index, rock in enumerate(itertools.islice(iter_rocks, limit)):
    trim_well(state, rock)
    state.x, state.y = 0, 0
    if rock_index % len(rocks) == 0:
      if not detector.add(wind.query_position(), well_height(state)):
        manager.start_countdown(detector, state, limit)
        last_height = well_height(state)
    if manager.check_countdown():
      height_left = well_height(state) - last_height
      return height_left + detector.period_height(manager.required)
    for action in itertools.cycle([apply_wind, apply_gravity]):
      if action(iter_wind, rock, state):
        stamp_rock(state, rock)
        break
  return well_height(state)

wind_patterns = sys.stdin.readline().strip()
rocks = read_rocks()
print(simulate(wind_patterns, rocks, 2022))
print(simulate(wind_patterns, rocks, 1000000000000))
