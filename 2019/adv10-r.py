import itertools
import math
import cmath
import aoc

def near(s):
  return abs(s) < 1e-4

def get_slopes(asteroids):
  slopes = aoc.ddict(lambda: [])
  for a, b in itertools.combinations(asteroids, 2):
    vec = (a[0] - b[0]) * 1j + (a[1] - b[1])
    angle = cmath.polar(vec)[1]
    slopes[int(angle * 10000)].append((a, b, near(vec.imag)))
  return slopes

def add_horizontal_lines(colinear, line, angle):
  for a, b, h in line:
    colinear[(angle, a[0])].add(a)
    colinear[(angle, a[0])].add(b)

def add_general_lines(colinear, line, angle):
  for p1, p2, h in line:
    b = int(10000 * (p1[1] - p1[0] * (p1[1] - p2[1]) / (p1[0] - p2[0])))
    colinear[(angle, b)].add(p1)
    colinear[(angle, b)].add(p2)

def get_colinear(slopes):
  colinear = aoc.ddict(lambda: set())
  for angle, line in slopes.items():
    if len(line) <= 2:
      continue
    if line[0][2]:
      add_horizontal_lines(colinear, line, angle)
    else:
      add_general_lines(colinear, line, angle)
  return colinear

def get_station(asteroids, colinear):
  blocked_sight = {a: 0 for a in asteroids}
  for line in colinear.values():
    for i, v in enumerate(sorted(line)):
      blocked_sight[v] += len(range(0, i - 1)) + len(range(i + 2, len(line)))
  max_detected = len(asteroids) - min(blocked_sight.values()) - 1
  station = min(blocked_sight.keys(), key=lambda x: blocked_sight[x])
  return max_detected, station

def spiral(asteroids):
  while True:
    for phase in sorted(asteroids.keys()):
      if asteroids[phase]:
        x, y = asteroids[phase].pop(0)
        yield x * 100 + y

def get_vaporized(station, asteroids, number):
  sy, sx = station
  rotate = cmath.exp(-1j * (math.pi / 2 - 0.01))
  goals = ((ay, ax) for ay, ax in asteroids if (ay, ax) != (sy, sx))
  polar = [(cmath.polar(((ax - sx) + (ay - sy) * 1j) * rotate), ax, ay) for ay, ax in goals]
  polar.sort(key=lambda c: (c[0][1], c[0][0]))
  sorted_asteroids = aoc.ddict(lambda: [])
  for ((r, phase), y, x) in polar:
    sorted_asteroids[int(phase * 10000)].append((y, x))
  return aoc.first(itertools.islice(spiral(sorted_asteroids), number - 1, number))

t = aoc.Table.read()
asteroids = [(j, i) for j, i in t.iter_all(lambda x: x in "#X")]
slopes = get_slopes(asteroids)
colinear = get_colinear(slopes)
max_detected, station = get_station(asteroids, colinear)
aoc.cprint(max_detected)
aoc.cprint(get_vaporized(station, asteroids, 200))

