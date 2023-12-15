import sys
import re

def apply_hash(code):
  ans = 0
  for c in code:
    ans = (ans + ord(c)) * 17 % 256
  return ans

def initialize(codes):
  boxes = {n:{} for n in range(256)}
  for code in codes:
    if code.endswith("-"):
      label = code[:-1]
      box = apply_hash(label)
      if label in boxes[box]:
        del boxes[box][label]
    else:
      label, number = re.match(r"(\w+)=(\d+)", code).groups()
      box = apply_hash(label)
      boxes[box][label] = int(number)
  return boxes

codes = sys.stdin.read().strip().split(",")
print(sum(apply_hash(code) for code in codes))

boxes = initialize(codes)
ans = 0
for box in boxes:
  for i, (label, focal) in enumerate(boxes[box].items()):
    ans += (box + 1) * (i + 1) * focal
print(ans)

