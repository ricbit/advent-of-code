import itertools
import aoc
import sys

def process(src):
  ans = []
  for k, v in itertools.groupby(src):
    ans.append(str(len(list(v))))
    ans.append(k)
  return "".join(ans)

def apply(src, times):
  for _ in range(times):
    src = process(src)
    yield len(src)

src = sys.stdin.read().strip()
for i, ans in enumerate(apply(src, 50)):
  if (i + 1) in [40, 50]:
    aoc.cprint(ans)
