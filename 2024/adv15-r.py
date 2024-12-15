import aoc

def get_initial_pos(t):
  py, px = t.find("@")
  t[py][px] = "."
  pos = py * 1j + px
  return pos

def score(t, value):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == value:
      ans += j * 100 + i
  return ans

def part1(data):
  maze, moves = data
  moves = "".join(s.strip() for s in moves)
  t = aoc.Table([list(p.strip()) for p in maze])
  cdir = aoc.get_cdir(">")
  pos = get_initial_pos(t)
  for move in moves:
    pdir = cdir[move]
    if t.get(pos + pdir) == ".":
      pos += pdir
    elif t.get(pos + pdir) == "O":
      walk = pos + pdir
      while t.get(walk) == "O":
        walk += pdir
      if t.get(walk) != "#":
        t.put(pos, ".")
        t.put(walk, "O")
        pos += pdir
      t.put(pos, ".")
  return score(t, "O")

class Maze:
  def __init__(self, data):
    wide = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    maze, moves = data
    maze = ["".join(wide[k] for k in s.strip()) for s in maze]
    self.moves = "".join(s.strip() for s in moves)
    self.t = aoc.Table([list(p) for p in maze])

  def canon(self, pos):
    if self.get(pos) == "]":
      pos -= 1
    return pos

  def put(self, pos, value):
    self.t.put(pos, value)

  def get(self, pos):
    return self.t.get(pos)

  def move_h(self, pos, pdir):
    self.put(pos, self.get(pos - pdir))
    self.put(pos - pdir, self.get(pos - 2 * pdir))
    self.put(pos - 2 * pdir, ".")

  def move_v(self, pos, pdir):
    self.put(pos + pdir, self.get(pos))
    self.put(pos + pdir + 1, self.get(pos + 1))
    self.put(pos, ".")
    self.put(pos + 1, ".")

  def move(self, pos, pdir, dry=False):
    pos = self.canon(pos)
    if self.get(pos) == "#":
      return False
    if self.get(pos) == ".":
      return True
    if pdir.imag == 0:
      start = pos + 2 if pdir == 1 else pos - 1
      if (check := self.move(start, pdir, dry)) and not dry:
        self.move_h(start, pdir)
    else:
      check_a = self.move(pos + pdir, pdir, dry)
      check_b = self.move(pos + pdir + 1, pdir, dry)
      if (check := check_a and check_b) and not dry:
        self.move_v(pos, pdir)
    return check

  def solve(self, data):
    cdir = aoc.get_cdir(">")
    pos = get_initial_pos(self.t)
    for move in self.moves:
      pdir = cdir[move]
      if self.get(pos + pdir) == ".":
        pos += pdir
      elif self.get(pos + pdir) in "[]":
        if self.move(pos + pdir, pdir, dry=True):
          self.move(pos + pdir, pdir)
          pos += pdir
    return score(self.t, "[")

data = aoc.line_blocks()
aoc.cprint(part1(data))
maze = Maze(data)
aoc.cprint(maze.solve(data))
