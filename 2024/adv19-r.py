import aoc
import functools

class Solver:
  def __init__(self, data):
    colors, stripes = data
    self.colors = {color.strip() for color in colors[0].split(",")}
    self.stripes = [x.strip() for x in stripes]

  @functools.cache
  def search(self, line):
    ans = 0
    if line in self.colors:
      ans += 1
    for i in range(len(line)):
      if line[:i] in self.colors and (x := self.search(line[i:])):
        ans += x
    return ans

  def solve(self, counter):
    return sum(counter(self.search(line)) for line in self.stripes)

s = Solver(aoc.line_blocks())
aoc.cprint(s.solve(lambda x: x > 0))
aoc.cprint(s.solve(lambda x: x))
