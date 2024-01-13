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
ans = 0
for i in range(128):
  h = [ord(i) for i in f"{raw_line}-{i}"] + [17,31,73,47,23]
  h = sparse_hash(apply_rounds(h, 64))
  #print(h)
  #print(list(int(c, 16).bit_count() for c in h))
  ans += sum(int(c, 16).bit_count() for c in h)
aoc.cprint(ans)
