import sys
import itertools
import re

nonempty = lambda s: s.strip()
lines = sys.stdin.readlines()
points_src = itertools.takewhile(nonempty, lines)
points = [[int(y) for y in x.strip().split(",")] for x in points_src]
folds_src = itertools.islice(itertools.dropwhile(nonempty, lines), 1, None)
parse_fold = lambda s: re.findall(r"(\S+)=(\d+)\s*$", s) 
folds = list(itertools.chain.from_iterable(parse_fold(s) for s in folds_src))
unpack = lambda p, d: (p[0], p[1], int(d))
fold_y = lambda x, y, d: (x, y if y < d else d + d - y)
fold_x = lambda x, y, d: (x if x < d else d + d - x, y)
first = folds[0]
p = [fold_x(*unpack(s, first[1])) for s in points]
print(len(set(p)))

