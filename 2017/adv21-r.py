import sys
import aoc

def apply(rules, pattern, size, before, after):
  final = []
  for j in range(size // before):
    line = []
    for i in range(size // before):
      k = []
      for jj in range(before):
        kk = []
        for ii in range(before):
          kk.append(pattern[j * before + jj][i * before + ii])
        k.append("".join(kk))
      dst = rules["/".join(k)].split("/")
      line.append(dst)
    final.append(line)
  newp = [[0] * (size // before * after) for _ in range(size // before * after)]
  for j in range(size // before):
    for i in range(size // before):
      for jj in range(after):
        for ii in range(after):
          newp[j * after + jj][i * after + ii] = final[j][i][jj][ii]
  return newp

def fractal(rules, n):
  pattern = [".#.", "..#", "###"]
  for _ in range(n):
    size = len(pattern)
    if len(pattern) % 2 == 0:
      pattern = apply(rules, pattern, size, 2, 3)
    else:
      pattern = apply(rules, pattern, size, 3, 4)
  return sum(sum(i == "#" for i in line) for line in pattern)
  
lines = [line.strip() for line in sys.stdin]
rules = {}
for line in lines:
  src, dst = line.strip().split(" => ")
  tsrc = aoc.Table([list(c) for c in src.split("/")])
  for i in range(4):
    nsrc = "/".join("".join(line) for line in tsrc)
    rules[nsrc] = dst
    ksrc = tsrc.flipx()
    nsrc = "/".join("".join(line) for line in ksrc)
    rules[nsrc] = dst
    tsrc = tsrc.clock90()
aoc.cprint(fractal(rules, 5))
aoc.cprint(fractal(rules, 18))
