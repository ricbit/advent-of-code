import sys
import itertools
import more_itertools

lines = [line.strip() for line in sys.stdin]
scanners = []
while lines:
  scanlines = list(itertools.takewhile(lambda x: x, lines))[1:]
  scanners.append([[int(i) for i in line.split(",")] for line in scanlines])
  lines = list(itertools.dropwhile(lambda x: x, lines))[1:]

def orientations(x, y, z):
  for i, j, k in itertools.permutations([x, y, z]):
    for ii, jj, kk in itertools.product([1, -1], repeat=3):
      yield i * ii, j * jj, k * kk

def scanner_orientations(scanner):
  original = []
  for x, y, z in scanner:
    original.append(list(orientations(x, y, z)))


def match_beacons(a, b):
  

for a in range(len(scanners)):
  for b in range(a + 1, len(scanners)):
    print(a, b, match_beacons(a, b))

