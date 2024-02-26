import itertools
import aoc

def gen_frac():
  ans = {}
  INNER = {1: 0, 3: 4}
  OUTER_Y = {0: (1, 2), 4: (3, 2)}
  OUTER_X = {0: (2, 1), 4: (2, 3)}
  for j, i in itertools.product(range(5), repeat=2):
    if j == i == 2:
      continue
    nn = aoc.ddict(lambda: [])
    for jj, ii in aoc.iter_neigh4(j, i):
      if 0 <= jj < 5 and 0 <= ii < 5:
        if jj == ii == 2:
          if j in [1, 3]:
            nn[-1].extend([(INNER[j], k) for k in range(5)])
          if i in [1, 3]:
            nn[-1].extend([(k, INNER[i]) for k in range(5)])
        else:
          nn[0].append((jj, ii))
    if j in [0, 4]:
      nn[1].append(OUTER_Y[j])
    if i in [0, 4]:
      nn[1].append(OUTER_X[i])
    ans[(j, i)] = nn.items()
  return ans

FRAC = gen_frac()

def single_neigh(level, j, i):
  for head, tail in FRAC[(j, i)]:
    for jj, ii in tail:
      yield (level + head, jj, ii)

def flat_neigh(level, j, i):
  for jj, ii in aoc.iter_neigh4(j, i):
    if 0 <= jj < 5 and 0 <= ii < 5:
      yield (level, jj, ii)

def neigh(bugs, t, callback):
  ans = set()
  for level, j, i in bugs:
    for n in callback(level, j, i):
      ans.add(n)
  return ans

def extract_bugs(t):
  bugs = set()
  for j, i in t.iter_all():
    if t[j][i] == "#":
      bugs.add((0, j, i))
  return bugs

def bug_iterator(t, callback):
  bugs = extract_bugs(t)
  while True:
    newbugs = set()
    for level, j, i in neigh(bugs, t, callback):
      n = sum((l2, jj, ii) in bugs for l2, jj, ii in callback(level, j, i))
      if (level, j, i) in bugs:
        if n == 1:
          newbugs.add((level, j, i))
      else:
        if 1 <= n <= 2:
          newbugs.add((level, j, i))
    bugs = newbugs
    yield bugs

def solve1(t):
  visited = set()
  for bugs in bug_iterator(t, flat_neigh):
    t = tuple(bugs)
    if t in visited:
      return sum(2 ** (j * 5 + i) for level, j, i in bugs)
    visited.add(t)

def solve2(t):
  it = bug_iterator(t, single_neigh)
  return len(aoc.first(itertools.islice(it, 199, 200)))

t = aoc.Table.read()
aoc.cprint(solve1(t))
aoc.cprint(solve2(t))
