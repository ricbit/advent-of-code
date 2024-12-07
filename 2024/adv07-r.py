import multiprocessing
import sys
import aoc

class Line:
  def __init__(self, line, concat=False):
    goal, values = line.split(":")
    self.values = aoc.ints(values.split())
    self.goal = int(goal)
    self.concat = concat

  def search(self, current, pos):
    if pos == len(self.values):
      return current == self.goal
    if current > self.goal:
      return False
    if self.search(current + self.values[pos], pos + 1):
      return True
    if self.search(current * self.values[pos], pos + 1):
      return True
    if self.concat and self.search(int(str(current) + str(self.values[pos])), pos + 1):
      return True
    return False

  def check(self):
    return self.search(self.values[0], 1)

def process_line(packed):
  line, done, concat = packed
  line = Line(line, concat)
  return line.goal if (done > 0 or line.check()) else 0

def solve(data):
  with multiprocessing.Pool() as pool:
    part1 = list(pool.imap(process_line,
        ((line, 0, False) for line in data)))
    part2 = list(pool.imap(process_line, 
        ((line, done, True) for line, done in zip(data, part1))))
  return sum(part1), sum(part2)

data = sys.stdin.readlines()
part1, part2 = solve(data)
aoc.cprint(part1)
aoc.cprint(part2)

