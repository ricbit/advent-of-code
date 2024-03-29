import sys
import re
import functools
import aoc

def apply_hash(code):
  return functools.reduce(lambda acc, x: (acc + ord(x)) * 17 % 256, code, 0)

def initialize(codes):
  boxes = {n: {} for n in range(256)}
  for code in codes:
    match re.match(r"(\w+)[-=](\d+)?", code).groups():
      case (label, None):
        boxes[apply_hash(label)].pop(label, None)
      case (label, number):
        boxes[apply_hash(label)][label] = int(number)
  return boxes

codes = sys.stdin.read().strip().split(",")
aoc.cprint(sum(apply_hash(code) for code in codes))

boxes = initialize(codes)
ans = 0
for box, contents in boxes.items():
  for i, (label, focal) in enumerate(contents.items()):
    ans += (box + 1) * (i + 1) * focal
aoc.cprint(ans)
