import sys
import re

def apply_hash(code):
  ans = 0
  for c in code:
    ans = (ans + ord(c)) * 17 % 256
  return ans

def search(box, label):
  names = [name for name, focal in box]
  if label in names:
    return names.index(label)
  else:
    return None

def initialize(codes):
  boxes = {n:[] for n in range(256)}
  for code in codes:
    if code.endswith("-"):
      label = code[:-1]
      box = apply_hash(label)
      index = search(boxes[box], label)
      if index is not None:
        boxes[box].pop(index)
    else:
      label, number = re.match(r"(\w+)=(\d+)", code).groups()
      box = apply_hash(label)
      index = search(boxes[box], label)
      if index is not None:
        boxes[box][index][1] = int(number)
      else:
        boxes[box].append([label, int(number)])
  return boxes

codes = sys.stdin.read().strip().split(",")
print(sum(apply_hash(code) for code in codes))

boxes = initialize(codes)
ans = 0
for box in boxes:
  if boxes[box]:
    for i, focal in enumerate(boxes[box]):
      ans += (box + 1) * (i + 1) * focal[1]
print(ans)

