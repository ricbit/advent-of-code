import aoc
import itertools
from multiprocessing import Pool

def append(m, tiles, visited, pos, vdir):
  pos += vdir
  if (pos, vdir) not in visited and m.cvalid(pos):
    tiles.append((pos, vdir))
    visited.add((pos, vdir))

def fast_track(m, pos, vdir):
  while m.cvalid(pos) and m.get(pos) == ".":
    yield pos
    pos += vdir

def count(packed):
  m, pos, vdir = packed
  tiles = [(pos, vdir)]
  visited = set(tiles)
  positions = set([pos])
  while tiles:
    pos, vdir = tiles.pop()
    positions.add(pos)
    match m.get(pos):
      case ".":
        for track in fast_track(m, pos, vdir):
          positions.add(track)
        append(m, tiles, visited, track, vdir)
      case "\\":
        append(m, tiles, visited, pos, vdir.conjugate() * 1J)
      case "/":
        append(m, tiles, visited, pos, (vdir * 1J).conjugate())
      case "|":
        if vdir.imag == 0:
          append(m, tiles, visited, pos, 1J)
          append(m, tiles, visited, pos, -1J)
        else:
          append(m, tiles, visited, pos, vdir)
      case "-":
        if vdir.real == 0:
          append(m, tiles, visited, pos, 1)
          append(m, tiles, visited, pos, -1)
        else:
          append(m, tiles, visited, pos, vdir)
  return len(positions)

def all_rays(m):
  for j in range(m.h):
    yield (m, j * 1J, 1)
    yield (m, m.w - 1 + j * 1J, -1)
  for i in range(m.w):
    yield (m, i, 1J)
    yield (m, (m.h - 1) * 1J + i, -1J)

def count_batched(batched):
  return max(count(task) for task in batched)

m = aoc.Table.read()
print(count((m, 0, 1)))
with Pool(8) as p:
  batched = itertools.batched(all_rays(m), 15)
  print(max(p.imap_unordered(count_batched, batched)))
