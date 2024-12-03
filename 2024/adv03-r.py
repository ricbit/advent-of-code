import sys
import re
import aoc

def parse(data, switch):
  opcodes = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data)
  ans, on = 0, True
  for opcode, a, b in opcodes:
    if opcode.startswith("mul") and on:
      ans += int(a) * int(b)
    elif opcode == "don't()" and switch:
      on = False
    elif opcode == "do()" and switch:
      on = True
  return ans

data = sys.stdin.read()
aoc.cprint(parse(data, switch=False))
aoc.cprint(parse(data, switch=True))
