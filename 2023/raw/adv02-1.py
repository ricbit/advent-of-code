import sys

maxrgb = {"r": 12, "g": 13, "b": 14}
ans = 0
for line in sys.stdin:
  games = line.split(":")
  gameid = int(games[0].strip().split(" ")[1])
  rounds = games[1].split(";")
  allrounds = []
  for contents in rounds:
    colors = contents.split(",")
    rgb = {}
    for color in colors:
      n, name = color.strip().split()
      rgb[name[0]] = int(n)
    allrounds.append(all(maxrgb[k] >= v for k, v in rgb.items()))
  if all(allrounds):
    ans += gameid
print(ans)

