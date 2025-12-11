import aoc
import functools

class Solver:
  def __init__(self, g):
    self.g = g

  @functools.cache
  def count(self, src, cur, skip):
    if cur in skip:
      return 0
    if src == cur:
      return 1
    return sum(self.count(src, node, skip) for node in self.g[cur])

def build_solver(data):
  g = aoc.ddict(lambda: [])
  for line in data:
    for node in line.dst.split():
      g[node].append(line.src)
  return Solver(g)

def part1(solver):
  return solver.count("you", "out", tuple())

def part2(solver):
  svr_fft = solver.count("svr", "fft", ("out", "dac"))
  svr_dac = solver.count("svr", "dac", ("out", "fft"))
  dac_fft = solver.count("dac", "fft", ("out"))
  fft_dac = solver.count("fft", "dac", ("out"))
  dac_out = solver.count("dac", "out", ("fft"))
  fft_out = solver.count("fft", "out", ("dac"))
  return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out

data = aoc.retuple_read("src dst", r"(\w+): (.*)$")
solver = build_solver(data)
aoc.cprint(part1(solver))
aoc.cprint(part2(solver))
