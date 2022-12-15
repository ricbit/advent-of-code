import sys

def get_range(encoded):
  a, b = encoded.split("-")
  return int(a), int(b)

def simple_contains(inter1, inter2):
  return inter1[0] <= inter2[0] and inter1[1] >= inter2[1]

def fully_contains(inter1, inter2):
  return simple_contains(inter1, inter2) or simple_contains(inter2, inter1)

def point_inside(inter, point):
  return point >= inter[0] and point <= inter[1]

def iter_elfs():
  for line in sys.stdin:
    yield [get_range(encoded) for encoded in line.strip().split(",")]

def first():
  contained_pairs = 0
  for elfs in iter_elfs():
    if fully_contains(*elfs):
      contained_pairs += 1
  print(contained_pairs)

def second():
  contained_pairs = 0
  for inter1, inter2 in iter_elfs():
    conditions = [
      point_inside(inter1, inter2[0]),
      point_inside(inter1, inter2[1]),
      point_inside(inter2, inter1[0]),
      point_inside(inter2, inter1[1]),
    ]
    if any(conditions):
      contained_pairs += 1
  print(contained_pairs)
  
second()
