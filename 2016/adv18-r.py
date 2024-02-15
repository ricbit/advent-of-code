import sys
import aoc

def get(line, i):
  if 0 <= i < len(line):
    return line[i]
  return "."

def search(line, rows):
  ans = line.count(".")
  for _ in range(rows - 1):
    new = []
    for i in range(len(line)):
      match (get(line, i - 1), get(line, i), get(line, i + 1)):
        case ("^", "^", ".") | (".", "^", "^") | (".", ".", "^") | ("^", ".", "."):
          new.append("^")
        case _:
          new.append(".")
    line = new
    ans += line.count(".")
  return ans

cline = sys.stdin.read().strip()
aoc.cprint(str(search(cline, 40)))
aoc.cprint(str(search(cline, 400000)))
