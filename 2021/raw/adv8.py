import sys

instances = []
for line in sys.stdin:
  numbers, given = (x.strip().split() for x in line.split("|"))
  instances.append((numbers, given))

ans = 0
for numbers, given in instances:
  for shown in given:
    if len(shown) in [2,3,4,7]:
      ans += 1
print(ans)
