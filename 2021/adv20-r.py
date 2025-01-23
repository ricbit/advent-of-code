import sys
import aoc
import itertools

def binary(line):
  return [(0 if c == "." else 1) for c in line]

def enlarge(image, empty):
  return image.grow(empty).grow(empty)

def mask(image, y, x):
  address = 0
  for j, i in image.iter_quad(y, x, 3, 3):
    address = address * 2 + image[j][i]
  return address

def enhance(code, image):
  w = image.w
  enhanced = []
  for j in range(w - 2):
    line = [code[mask(image, j, i)] for i in range(w - 2)]
    enhanced.append(line)
  return aoc.Table(enhanced)

def draw(image):
  for line in image:
    print("".join("." if c == 0 else "#" for c in line))

def count(image):
  return sum(aoc.flatten(image))

def multiple_enhance(code, image, limit):
  empty = 0
  for i in range(limit):
    image = enhance(code, enlarge(image, empty))
    if code[0] == 1:
      empty = 1 - empty
  return image

code, raw_image = aoc.line_blocks()
code = binary(code[0])
image = aoc.Table([binary(line) for line in raw_image])

aoc.cprint(count(multiple_enhance(code, image, 2)))
aoc.cprint(count(multiple_enhance(code, image, 50)))



