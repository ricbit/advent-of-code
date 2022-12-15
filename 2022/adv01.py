import sys

calories = [0]
for line in sys.stdin:
  if not line.strip():
    calories.append(0)
  else:
    calories[-1] += int(line)
calories.sort(reverse=True)
print(sum(calories[:3]))
