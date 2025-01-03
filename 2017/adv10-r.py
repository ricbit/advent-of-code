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

raw_line = sys.stdin.read().strip()
line = aoc.ints(raw_line.split(","))
q = apply_rounds(line, 1)
aoc.cprint(q[0] * q[1])
line = [ord(i) for i in raw_line] + [17, 31, 73, 47, 23]
aoc.cprint(sparse_hash(apply_rounds(line, 64)))
