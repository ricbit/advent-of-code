import sys
import aoc
import heapq

class Defrag:
  def __init__(self, data):
    self.blocks = []
    pos = 0
    self.spaceheap = aoc.ddict(list)
    for i, size in enumerate(data):
      if i % 2 == 0:
        self.blocks.append([i // 2, size, pos])
      else:
        heapq.heappush(self.spaceheap[size], pos)
      pos += size

  def first_space(self, space_size):
    return self.spaceheap[space_size][0]

  def get_valid_space(self, block_pos, block_size):
    best_size, best_pos = block_size, block_pos
    for space_size in range(block_size, 10):
      if (space_pos := self.first_space(space_size)) < best_pos:
        best_pos, best_size = space_pos, space_size
    return best_pos, best_size

  def checksum(self, pos, size, uid):
    return sum((pos + i) * uid for i in range(size))

  def part2(self):
    ans = 0
    for uid, block_size, block_pos in reversed(self.blocks):
      if block_size == 0:
        continue
      if uid == 0:
        ans += self.checksum(block_pos, block_size, uid)
        break
      space_pos, space_size = self.get_valid_space(block_pos, block_size)
      if space_pos == block_pos:
        ans += self.checksum(block_pos, block_size, uid)
        continue
      heapq.heappop(self.spaceheap[space_size])
      ans += self.checksum(space_pos, block_size, uid)
      if (space_left := space_size - block_size) > 0:
        heapq.heappush(self.spaceheap[space_left], (space_pos + block_size))
    return ans

def part1(data):
  fsys = []
  for i, v in enumerate(data):
    if i % 2 == 0:
      fsys.extend([i // 2] * v)
    else:
      fsys.extend([-1] * v)
  free = fsys.index(-1)
  used = len(fsys) - 1
  while fsys[used] == -1:
    used -= 1
  while free < used:
    fsys[used], fsys[free] = fsys[free], fsys[used]
    used -= 1
    while fsys[used] == -1:
      used -= 1
    free += 1
    while fsys[free] != -1:
      free += 1
  return sum(i * y for i, y in enumerate(x for x in fsys if x != -1))

data = aoc.ints(list(sys.stdin.read().strip()))
aoc.cprint(part1(data))
defrag = Defrag(data)
aoc.cprint(defrag.part2())
