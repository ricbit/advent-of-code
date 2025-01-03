import sys
import aoc

def apply_rounds(line, nrounds):
  pos = 0
  skip = 0
  q = list(range(256))
  for _ in range(nrounds):
    for n in line:
      qq = q[:]
      for i in range(0, n):
        qq[(pos + i) % len(q)] = q[(pos + n - 1 - i + len(q)) % len(q)]
      q = qq
      pos += n + skip
      skip += 1
  return q

def sparse_hash(q):
  sparse = [0] * 16
  for i in range(16):
    for j in range(16):
      sparse[i] ^= q[j + i * 16]
  return "".join("%02x" % i for i in sparse)

def floodfill(m):
  t = aoc.Table(m)
  g = 0
  for j, i in t.iter_all():
    if t[j][i] == "1":
      g += 1
      vnext = [(j, i)]
      while vnext:
        y, x = vnext.pop()
        if isinstance(t[y][x], int):
          continue
        t[y][x] = g
        for jj, ii in t.iter_neigh4(y, x):
          if isinstance(t[jj][ii], str) and t[jj][ii] == "1":
            vnext.append((jj, ii))
  return g

raw_line = sys.stdin.read().strip()
ans = 0
m = []
for i in range(128):
  h = [ord(i) for i in f"{raw_line}-{i}"] + [17, 31, 73, 47, 23]
  h = sparse_hash(apply_rounds(h, 64))
  m.append(list("".join(format(int(d, 16), '04b') for d in h)))
aoc.cprint(sum(line.count("1") for line in m))
aoc.cprint(floodfill(m))
