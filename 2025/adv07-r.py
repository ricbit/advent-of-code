import aoc
import functools

class Search:
  def __init__(self, table):
    self.table = table
    self.splits = set()

  @functools.cache
  def search(self, j, i):
    while j < self.table.h - 1 and self.table[j][i] != "^":
      j += 1
    if self.table[j][i] != "^":
      return 1
    self.splits.add((j, i))
    return self.search(j, i - 1) + self.search(j, i + 1)

def solve(table):
  j, i = table.find("S")
  s = Search(table)
  universes = s.search(j, i)
  return len(s.splits), universes

table = aoc.Table.read()
part1, part2 = solve(table)
aoc.cprint(part1)
aoc.cprint(part2)
