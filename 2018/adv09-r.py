import sys
import aoc

def solve(players, goal):
  marbles = aoc.bidi([0], circular=True)
  pos = marbles.start
  score = [0] * players
  for i in range(1, 1 + goal):
    if i % 23 != 0:
      pos = marbles.insert(marbles.next(pos), i)
    else:
      for j in range(7):
        pos = marbles.prev(pos)
      npos = marbles.prev(pos)
      score[i % players] += i + marbles.value(pos)
      marbles.remove(pos)
      pos = marbles.next(npos)
  return max(score)

data = sys.stdin.read().strip()
q = aoc.retuple("players_ goal_", r"(\d+).*?(\d+)", data)
aoc.cprint(solve(q.players, q.goal))
aoc.cprint(solve(q.players, q.goal * 100))
