import sys
import aoc

def printbidi(bidi):
  pos = bidi[0][1]
  ans = []
  while True:
    ans.append(pos)
    pos = bidi[pos][1]
    if pos == 0:
      return "".join(str(i + 1) for i in ans)

def solve(data, moves):
  size = len(data)
  bidi = [[0, 0] for i in range(size)]
  for i in range(size):
    pos = data[i] - 1
    bidi[pos][0] = data[(i - 1) % size] - 1
    bidi[pos][1] = data[(i + 1) % size] - 1
  pos = data[0] - 1
  for _ in range(moves):
    dstvalue = (pos - 1) % size
    save = [bidi[pos][1]]
    for _ in range(3):
      save.append(bidi[save[-1]][1])
    *save, advance = save
    bidi[pos][1] = advance
    bidi[advance][0] = pos
    while dstvalue in save:
      dstvalue = (dstvalue - 1) % size
    advance = bidi[dstvalue][1]
    bidi[dstvalue][1] = save[0]
    bidi[save[0]][0] = dstvalue
    bidi[save[2]][1] = advance
    bidi[advance][0] = save[2]
    pos = bidi[pos][1]
  return bidi

data = aoc.ints(list(sys.stdin.read().strip()))
aoc.cprint(printbidi(solve(data, 100)))
data.extend(range(len(data) + 1, 1000001))
bidi = solve(data, 10000000)
val1 = bidi[0][1]
val2 = bidi[val1][1]
aoc.cprint((val1 + 1) * (val2 + 1))
