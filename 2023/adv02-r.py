import sys
import re
import math

games = {}
for line in sys.stdin:
  gameid = int(re.match(r"^.*?(\d+)", line).group(1))
  colors = re.findall(r"(\d+) ([rgb])", line)
  rgb = {}
  for value, color in colors:
    rgb[color] = max(rgb.get(color, 0), int(value))
  games[gameid] = rgb

def first(games):
  maxrgb = {"r": 12, "g": 13, "b": 14}
  ans = 0
  for gameid, rgb in games.items():
    if all(maxrgb[key] >= value for key, value in rgb.items()):
      ans += gameid
  return ans

def second(games):
  ans = 0
  for gameid, rgb in games.items():
    ans += math.prod(rgb.values())
  return ans

print(first(games))
print(second(games))

