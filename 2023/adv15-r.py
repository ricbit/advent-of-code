import sys
import re
import functools

def apply_hash(code):
  return functools.reduce(lambda acc, x: (acc + ord(x)) * 17 % 256, code, 0)

def initialize(codes):
  boxes = {n:{} for n in range(256)}
  for code in codes:
    match re.match(r"(\w+)-|(\w+)=(\d+)", code).groups():
      case (label, None, None):
        boxes[apply_hash(label)].pop(label, None)
      case (None, label, number):
        boxes[apply_hash(label)][label] = int(number)
  return boxes

codes = sys.stdin.read().strip().split(",")
print(sum(apply_hash(code) for code in codes))

boxes = initialize(codes)
ans = 0
for box in boxes:
  for i, (label, focal) in enumerate(boxes[box].items()):
    ans += (box + 1) * (i + 1) * focal
print(ans)

