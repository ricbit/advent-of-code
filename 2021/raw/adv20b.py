import sys
import itertools

lines = [line.strip() for line in sys.stdin]

def binary(line):
  return [(0 if c == "." else 1) for c in line]

code = binary(lines[0])
image = [binary(line) for line in lines[2:]]
print(len(image))
print(len(image[0]))

def enlarge(image, empty):
  w = len(image[0]) + 4
  enlarged = [[empty] * w for i in range(2)]
  for line in image:
    enlarged.append([empty, empty] + line + [empty, empty])
  enlarged.extend([[empty] * w for i in range(2)])
  return enlarged

def offset():
  for j in range(3):
    for i in range(3):
      yield j, i

def mask(image, y, x):
  address = 0
  for j, i in offset():
    address = address * 2 + image[y + j][x + i]
  return code[address]

def enhance(image):
  w = len(image)
  enhanced = []
  for j in range(w - 2):
    line = []
    for i in range(w - 2):
      line.append(mask(image, j, i))
    enhanced.append(line)
  return enhanced

def draw(image):
  for line in image:
    print("".join("." if c == 0 else "#" for c in line))

def count(image):
  return sum(sum(line) for line in image)

empty = 0
for i in range(50):
  image = enhance(enlarge(image, empty))
  if code[0] == 1:
    empty = 1 - empty

print(count(image))


