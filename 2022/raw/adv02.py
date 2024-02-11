import sys

outcomes = {
  "A X": 3,
  "A Y": 6,
  "A Z": 0,
  "B X": 0,
  "B Y": 3,
  "B Z": 6,
  "C X": 6,
  "C Y": 0,
  "C Z": 3
}

lines = sys.stdin.readlines()

def first():
  score = 0
  for line in lines:
    a = outcomes[line.strip()] 
    b = ord(line.split()[1]) - ord('X') + 1
    score += a + b
  return score

def second():
  score = 0
  for line in lines:
    p1, result = line.strip().split()
    desired = (ord(result) - ord('X')) * 3
    for j in range(3):
      if outcomes[" ".join([p1, chr(ord('X') + j)])] == desired:
        score += desired + j + 1
  return score

print(first())
print(second())


