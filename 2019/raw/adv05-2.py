import sys
import itertools
import aoc

def decode(data, pos, opcode, size, decode_last=False):
  ans = []
  msize = size if decode_last else size - 1
  for i in range(msize):
    if opcode[::-1][2 + i] == "0":
      ans.append(data[data[pos + i]])
    else:
      ans.append(data[pos + i])
  if not decode_last:
    ans.append(data[pos + size - 1])
  return ans

def solve(data, input_value):
  data = data[:]
  pos = 0
  output = None
  while pos < len(data):
    opcode = "%05d" % data[pos]
    cmd = data[pos] % 100
    #print(pos, cmd)
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
      data[a] = input_value
      pos += 2
    elif cmd == 4:
      (a,) = decode(data, pos + 1, opcode, 1, True)
      output = a
      pos += 2
    elif cmd == 5:
      a, b = decode(data, pos + 1, opcode, 2, True)
      if a != 0:
        pos = b
      else:
        pos += 3
    elif cmd == 6:
      a, b = decode(data, pos + 1, opcode, 2, True)
      if a == 0:
        pos = b
      else:
        pos += 3
    elif cmd == 7:
      a, b, c = decode(data, pos + 1, opcode, 3)
      if a < b:        
        data[c] = 1
      else: 
        data[c] = 0
      pos += 4
    elif cmd == 8:
      a, b, c = decode(data, pos + 1, opcode, 3)
      if a == b:        
        data[c] = 1
      else: 
        data[c] = 0
      pos += 4
    elif cmd == 99:
      break
  return input_value, output

def part2(data):
  for a, b in itertools.product(range(50), repeat=2):
    data = original_data[:]
    data[1] = a
    data[2] = b
    solve(data)
    if data[0] == 19690720:
      return data[1] * 100 + data[2]

original_data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(solve(original_data, 5))
