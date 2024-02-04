import sys
import aoc
from collections import Counter

def decode(name, shift):
  ans = []
  for c in name:
    if c.islower():
      ans.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
    else:
      ans.append(" ")
  return "".join(ans)

def search(lines):
  ans = 0
  for line in sys.stdin:
    t = aoc.retuple("name number_ check", r"(.*)-(\d+)\[(.*)\]", line)
    h = Counter()
    for c in t.name:
      if c.islower():
        h[c] += 1
    chars = list(h.keys())
    chars.sort(key=lambda c: (-h[c], c))
    if "".join(chars[:5]) == t.check:
      ans += t.number
      decoded = decode(t.name, t.number)
      if "storage" in decoded and "northpole" in decoded:
        found = t.number
  return ans, found

ans, found = search(sys.stdin)
aoc.cprint(ans)
aoc.cprint(found)
