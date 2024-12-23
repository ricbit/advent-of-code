import aoc
import itertools

def walk(t, start):
  vdir = -1j
  visited, prevmap, pos = set(), {}, start
  while t.cvalid(pos) and (pos, vdir) not in visited:
    visited.add((pos, vdir))
    prev = (pos, vdir)
    while t.cvalid(pos + vdir) and t.get(pos + vdir) == "#":
      vdir *= 1j
    if t.cvalid(pos + vdir):
      pos += vdir
    if pos not in prevmap:
      prevmap[pos] = prev
  return pos, visited, prevmap

def run(t, start, skipmap, cpos):
  pos, vdir = start
  visited = set()
  while t.cvalid(pos) and (pos, vdir) not in visited:
    visited.add((pos, vdir))
    while t.cvalid(pos + vdir) and t.get(pos + vdir) == "#":
      vdir *= 1j
    if (t.cvalid(pos + vdir) and not
        ((pos+vdir).real == cpos.real or (pos+vdir).imag == cpos.imag)):
      pos = skipmap[vdir][pos]
    else:
      pos += vdir
  return pos

def original_path(t):
  sy, sx = t.find("^")
  t[sy][sx] = "."
  start = sy * 1j + sx
  pos, visited, prevmap = walk(t, start)
  return visited, start, prevmap

def is_loop(t, start, skipmap, cpos):
  return t.cvalid(run(t, start, skipmap, cpos))

def build_skipmap(t):
  dirs = [1, -1, 1j, -1j]
  limits = [t.w, -1, 1j * t.h, -1j]
  axis = [1j, 1j, 1, 1]
  skipmap = {k: {} for k in dirs}
  for vdir, hdir, limit in zip(dirs, axis, limits):
    for col in itertools.count(0):
      pos = col * hdir + limit - vdir      
      last = col * hdir + limit
      if not t.cvalid(pos):
        break
      while t.cvalid(pos):
        skipmap[vdir][pos] = last
        if t.get(pos) == "#":
          last = pos - vdir
        pos -= vdir
  return skipmap

def find_blockers(t, visited, start, prevmap):
  skipmap = build_skipmap(t)
  ans = 0
  for cpos in set(cpos for cpos, vdir in visited):
    t.put(cpos, "#")
    if is_loop(t, prevmap.get(cpos, (start, -1j)), skipmap, cpos):
      ans += 1
    t.put(cpos, ".")
  return ans

t = aoc.Table.read()
visited, start, prevmap = original_path(t)
aoc.cprint(len(set(cpos for cpos, vdir in visited)))
aoc.cprint(find_blockers(t, visited, start, prevmap))
