import sys
import math

ans = 0
for line in sys.stdin:
  games = line.split(":")
  gameid = int(games[0].strip().split(" ")[1])
  rounds = games[1].split(";")
  minrgb = {"r": 0, "g": 0, "b": 0}
  for contents in rounds:
    colors = contents.split(",")
    for color in colors:
      n, name = color.strip().split()
      minrgb[name[0]] = max(minrgb[name[0]], int(n))
  power = math.prod(minrgb.values())
  ans += power
print(ans)

