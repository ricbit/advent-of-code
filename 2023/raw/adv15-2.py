import sys
import re
import itertools
import math

codes = sys.stdin.read().strip().split(",")
print(codes)

def applyhash(code):
  ans = 0
  for c in code:
    ans = (ans + ord(c)) * 17 % 256
  return ans

ans = 0
print(sum(applyhash(code) for code in codes))

def search(box, label):
  x = [b for b, a in box]
  if label in x:
    return x.index(label)
  else:
    return None

boxes = {n:[] for n in range(256)}
for code in codes:
  if code.endswith("-"):
    label = code[:-1]
    box = applyhash(code[:-1])
    c = search(boxes[box], label)
    if c is not None:
      boxes[box].pop(c)
  else:
    label, number = re.match(r"(\w+)=(\d+)", code).groups()
    box = applyhash(label)
    c = search(boxes[box], label)
    if c is not None:
      boxes[box][c][1] = int(number)
    else:
      boxes[box].append([label, int(number)])

ans = 0
for box in boxes:
  if boxes[box]:
    for i, focal in enumerate(boxes[box]):
      ans += (box + 1) * (i + 1) * focal[1]
print(ans)

