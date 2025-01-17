import sys
import itertools
import aoc
import multiprocessing

def action(pwd):
  for line in lines:
    match line:
      case "move", _, p0, _, _, p1:
        a = pwd.pop(int(p0))
        pwd.insert(int(p1), a)
      case "swap", "position", p0, _, _, p1:
        pwd[int(p0)], pwd[int(p1)] = pwd[int(p1)], pwd[int(p0)]
      case "swap", "letter", a, _, _, b:
        for i, p in enumerate(pwd):
          if p == a:
            pwd[i] = b
          elif p == b:
            pwd[i] = a
      case "reverse", _, p0, _, p1:
        pwd[int(p0):int(p1) + 1] = pwd[int(p0):int(p1) + 1][::-1]
      case "rotate", "left", a, _:
        for i in range(int(a)):
          pwd = pwd[1:] + [pwd[0]]
      case "rotate", "right", a, _:
        for i in range(int(a)):
          pwd = [pwd[-1]] + pwd[:-1]
      case "rotate", "based", _, _, _, _, x:
        i = pwd.index(x)
        size = i + 1 + (1 if i >= 4 else 0)
        for _ in range(int(size)):
          pwd = [pwd[-1]] + pwd[:-1]
  return "".join(pwd)

def search(src, goal):
  return (src, action(list(src)) == goal)

def decode(goal):
  with multiprocessing.Pool() as pool:
    perms = itertools.permutations(goal, len(goal))
    ans = pool.starmap(search, ((p, goal) for p in perms))
  for perm, found in ans:
    if found:
      return "".join(perm)
  return None

lines = [line.strip().split() for line in sys.stdin]
aoc.cprint(action(list("abcdefgh")))
aoc.cprint(decode("fbgdceah"))
