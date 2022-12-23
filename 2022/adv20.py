import sys

encrypted = [int(i) for i in sys.stdin]

def bruteforce(circ, encrypted):
  for index, value in enumerate(encrypted):
    pos = circ.index(index)
    circ.pop(pos)
    npos = (pos + value) % len(circ)
    if npos == 0 and value < 0:
      npos = len(circ)
    circ.insert(npos, index)
  return circ

def score(encrypted, circ):
  zero_index = encrypted.index(0)
  for index, value in enumerate(circ):
    if value == zero_index:
      zero = index
  total = sum(encrypted[circ[(zero + v * 1000) % len(circ)]] for v in [1, 2, 3])
  return total

def first():
  indexes = list(range(len(encrypted)))
  return score(encrypted, bruteforce(indexes, encrypted))

def second():
  decrypted = [i * 811589153 for i in encrypted]
  indexes = list(range(len(decrypted)))
  for _ in range(10):
    indexes = bruteforce(indexes, decrypted)
  return score(decrypted, indexes)

print(first())
print(second())
