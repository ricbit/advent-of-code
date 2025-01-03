import sys
import aoc

def parser(chars):
  pos = 0
  copen = 0
  state = True
  score = 0
  garbage = 0
  while pos < len(chars):
    match chars[pos], state:
      case "{", True:
        copen += 1
        score += copen
      case "}", True:
        copen -= 1
      case "<", True:
        state = False
      case ">", False:
        state = True
      case "!", False:
        pos += 1
      case _, False:
        garbage += 1
    pos += 1
  return score, garbage

line = sys.stdin.read().strip()
score, garbage = parser(line)
aoc.cprint(score)
aoc.cprint(garbage)
