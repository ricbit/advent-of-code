import sys

vectors = {
  "R": (0, 1),
  "L": (0, -1),
  "U": (1, 0),
  "D": (-1, 0)
}

search = [
  (1, 0), (-1, 0), (0, 1), (0, -1),
  (1, 1), (1, -1), (-1, -1), (-1, 1)
]

lines = sys.stdin.readlines()

def add(pos, delta):
  return (pos[0] + delta[0], pos[1] + delta[1])

def move_tail(head, tail):
  best = (100, None)
  for delta in search:
    next_tail = add(tail, delta)
    next_score = abs(head[0] - next_tail[0]) + abs(head[1] - next_tail[1])
    if next_score < best[0]:
      best = (next_score, next_tail)
  return best[1]

def too_far(head, tail):
  return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1

def get_rope(size):
  visited = set()
  rope = [(0, 0)] * size
  visited.add(rope[-1])
  for line in lines:
    direction, steps = line.strip().split()
    for step in range(int(steps)):
      rope[0] = add(rope[0], vectors[direction])
      for n in range(1, size):
        if too_far(rope[n - 1], rope[n]):
          rope[n] = move_tail(rope[n - 1], rope[n])
      visited.add(rope[-1])
  return len(visited)

print(get_rope(2))
print(get_rope(10))
      


