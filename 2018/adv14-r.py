import sys
import itertools
import aoc

def criteria1(size):
  size = int(size)
  def criteria(recipes):
    if len(recipes) > size + 10:
      return "".join(str(i) for i in recipes[size: size + 10])
    return None
  return criteria

def criteria2(size):
  size = [int(i) for i in size]
  def criteria(recipes):
    for pos in range(max(0, len(recipes) - len(size) * 2), len(recipes) - len(size)):
      if recipes[pos:pos + len(size)] == size:
        return pos
    return None
  return criteria

def solve(criteria):
  recipes = [3, 7]
  pos1, pos2 = 0, 1
  for tick in itertools.count(0):
    new = recipes[pos1] + recipes[pos2]
    recipes.extend((int(i) for i in str(new)))
    pos1 = (pos1 + 1 + recipes[pos1]) % len(recipes)
    pos2 = (pos2 + 1 + recipes[pos2]) % len(recipes)
    if (result := criteria(recipes)) is not None:
      return result

data = sys.stdin.read().strip()
aoc.cprint(solve(criteria1(data)))
aoc.cprint(solve(criteria2(data)))
