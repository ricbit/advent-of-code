import sys
import copy

state = [list(line.strip()) for line in sys.stdin]
w, h = len(state[0]), len(state)

def step(state):
  newstate = [["."] * w for i in range(h)]
  for j in range(h):
    for i in range(w):
      ni = (i + 1) % w
      if state[j][i] == ">" and state[j][ni] == ".":
        newstate[j][ni] = ">"
      elif state[j][i] == ">" or state[j][i] == "v":
        newstate[j][i] = state[j][i]
  finalstate = [["."] * w for i in range(h)]
  for j in range(h):
    for i in range(w):
      nj = (j + 1) % h
      if newstate[j][i] == "v" and newstate[nj][i] == ".":
        finalstate[nj][i] = "v"
      elif newstate[j][i] == ">" or newstate[j][i] == "v":
        finalstate[j][i] = newstate[j][i]
  return finalstate

ans = 0
while True:
  newstate = step(state)
  ans += 1
  if newstate == state:
    break
  state = newstate

print(ans)

