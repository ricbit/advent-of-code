import sys
import itertools
import aoc

def decode(data, pos, opcode, size):
  ans = []
  for i in range(size - 1):
    if opcode[::-1][2 + i] == "0":
      ans.append(data[data[pos + i]])
    else:
      ans.append(data[pos + i])
  ans.append(data[pos + size - 1])
  return ans

def solve(data):
  pos = 0
  output = None
  while pos < len(data):
    opcode = "%05d" % data[pos]
    cmd = data[pos] % 100
    if cmd == 1:
      a, b, c = decode(data, pos + 1, opcode, 3)
      data[c] = a + b
      pos += 4
    elif cmd == 2:
      a, b, c = decode(data, pos + 1, opcode, 3)
      data[c] = a * b
      pos += 4
    elif cmd == 3:
      (a,) = decode(data, pos + 1, opcode, 1)
      data[a] = 1
      pos += 2
    elif cmd == 4:
      (a,) = decode(data, pos + 1, opcode, 1)
      output = data[a]
      pos += 2
    elif cmd == 99:
      break
  return output

def part2(data):
  for a, b in itertools.product(range(50), repeat=2):
    data = original_data[:]
    data[1] = a
    data[2] = b
    solve(data)
    if data[0] == 19690720:
      return data[1] * 100 + data[2]

def part1(data):
  data = data[:]
  return solve(data)

original_data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(part1(original_data))
