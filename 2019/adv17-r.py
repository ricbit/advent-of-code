import sys
import itertools
import aoc
from aoc.refintcode import IntCode

def alignment(t):
  ans = 0
  for j, i in t.iter_all():
    if t[j][i] == "#":
      count = 0
      for jj, ii in t.iter_neigh4(j, i):
        if t[jj][ii] == "#":
          count += 1
      if count == 4:
        ans += (j - 1) * (i - 1)
  return ans

def read_table(data):
  cpu = IntCode(data[:])
  table = []
  line = []
  while cpu.run():
    match cpu.state:
      case cpu.OUTPUT:
        if cpu.output == 10:
          table.append(line)
          line = []
        else:
          line.append(chr(cpu.output))
  return aoc.Table(table[:-1]).grow(".")

def get_pos(t):
  for j, i in t.iter_all():
    if t[j][i] == "^":
      return i + j * 1j

def get_full_path(t):
  pos = get_pos(t)
  vdir = -1
  cmd = ["L"]
  dirs = {"R": 1j, "L": -1j}
  while True:
    if t.get(pos + vdir) == "#":
      pos += vdir
      cmd.append("w")
    else:
      for c, d in dirs.items():
        if t.get(pos + vdir * d) == "#":
          vdir *= d
          pos += vdir
          cmd.append(c)
          cmd.append("w")
          break
      else:
        return cmd

def get_short_path(t):
  full_path = get_full_path(t)
  path = []
  for k, v in itertools.groupby(full_path):
    if k == "w":
      path.append(str(len(list(v))))
    else:
      path.append(k)
  return path

def get_functions(path, asize, bsize, csize):
  a, b = path[:asize], path[asize: asize + bsize]
  c, pos, cmd = None, 0, []
  while pos < len(path):
    if path[pos:pos + asize] == a:
      cmd.append("A")
      pos += asize
    elif path[pos:pos + bsize] == b:
      cmd.append("B")
      pos += bsize
    elif c is None:
      c = path[pos:pos + csize]
      cmd.append("C")
      pos += csize
    elif path[pos:pos + csize] == c:
      cmd.append("C")
      pos += csize
    else:
      return None
  return (cmd, a, b, c) if pos == len(path) else None

def encode_input(functions):
  cmd = []
  for sub in functions:
    cmd.append(",".join(sub) + chr(10))
  return "".join(cmd) + "n" + chr(10)

def find_parts(path):
  path = list(a + "," + b for a, b in itertools.batched(path, 2))
  for a, b, c in itertools.product(range(1, 10), repeat=3):
    if (functions := get_functions(path, a, b, c)) is not None:
      return functions

def collect_dust(data, robot_cmds):
  data[0] = 2
  cpu = IntCode(data)
  pos, output = 0, 0
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        cpu.input = ord(robot_cmds[pos])
        pos += 1
      case cpu.OUTPUT:
        output = cpu.output
  return output

data = aoc.ints(sys.stdin.read().split(","))
table = read_table(data)
aoc.cprint(alignment(table))
path = get_short_path(table)
robot_cmds = encode_input(find_parts(path))
aoc.cprint(collect_dust(data, robot_cmds))
