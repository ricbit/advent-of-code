import itertools
import functools

def deterministic_dice():
  yield from itertools.cycle(range(1, 101))

def roll(dice, pos, score):
  move = sum(itertools.islice(dice, 3))
  pos = (pos - 1 + move) % 10 + 1
  score += pos
  return pos, score

def play(p1, p2):
  dice = deterministic_dice()
  s1, s2 = 0, 0
  throws = 0
  while True:
    p1, s1 = roll(dice, p1, s1)
    throws += 3
    if s1 >= 1000:
      return s2 * throws
    p2, s2 = roll(dice, p2, s2)
    throws += 3
    if s2 >= 1000:
      return s1 * throws

def add(score, diff):
  return (score[0] + diff[0], score[1] + diff[1])

@functools.cache
def manyworlds(state, pos1, pos2, dice1, dice2, score1, score2):
  worlds = (0, 0)
  match state:
    case 0 | 1 | 2:
      worlds = add(worlds, manyworlds(state + 1, pos1, pos2, dice1 + 1, 0, score1, score2))
      worlds = add(worlds, manyworlds(state + 1, pos1, pos2, dice1 + 2, 0, score1, score2))
      worlds = add(worlds, manyworlds(state + 1, pos1, pos2, dice1 + 3, 0, score1, score2))
    case 3:
      pos1 = (pos1 + dice1) % 10
      score1 += pos1 + 1
      if score1 >= 21:
        return (1, 0)
      worlds = add(worlds, manyworlds(4, pos1, pos2, 0, 0, score1, score2))
    case 4 | 5 | 6:
      worlds = add(worlds, manyworlds(state + 1, pos1, pos2, 0, dice2 + 1, score1, score2))
      worlds = add(worlds, manyworlds(state + 1, pos1, pos2, 0, dice2 + 2, score1, score2))
      worlds = add(worlds, manyworlds(state + 1, pos1, pos2, 0, dice2 + 3, score1, score2))
    case 7:
      pos2 = (pos2 + dice2) % 10
      score2 += pos2 + 1
      if score2 >= 21:
        return (0, 1)
      worlds = add(worlds, manyworlds(0, pos1, pos2, 0, 0, score1, score2))
  return worlds

p1 = int(input().split(":")[1])
p2 = int(input().split(":")[1])
print(play(p1, p2))
print(max(*manyworlds(0, p1 - 1, p2 - 1, 0, 0, 0, 0)))
