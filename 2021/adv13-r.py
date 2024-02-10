import sys
import itertools
import re
import aoc

lines = sys.stdin.readlines()
nonempty = lambda s: s.strip()
points_src = itertools.takewhile(nonempty, lines)
points = [[int(y) for y in x.strip().split(",")] for x in points_src]
folds_src = itertools.islice(itertools.dropwhile(nonempty, lines), 1, None)
parse_fold = lambda s: re.findall(r"(\S+)=(\d+)\s*$", s) 
folds = itertools.chain.from_iterable(parse_fold(s) for s in folds_src)
unpack = lambda p, d: (p[0], p[1], int(d))
fold_y = lambda x, y, d: (x, y if y < d else d + d - y)
fold_x = lambda x, y, d: (x if x < d else d + d - x, y)
fold_fn = lambda f: fold_x if f == "x" else fold_y
all_folds = []
for fold in folds:
  points = [fold_fn(fold[0])(*unpack(s, fold[1])) for s in points]
  all_folds.append(points)
aoc.cprint(len(set(all_folds[0])))
w = 1 + max(x for x, y in points)
h = 1 + max(y for x, y in points)
paper = [["."] * w for _ in range(h)]
for x, y in points:
  paper[y][x] = "#"
for line in paper:
  print("".join(line))

