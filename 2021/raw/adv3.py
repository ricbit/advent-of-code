import sys

lines = [line.strip() for line in sys.stdin.readlines()]
length = len(lines[0])
size = len(lines)
ones = [0] * length
for line in lines:
  for n, v in enumerate(line):
    if v == "1":
      ones[n] += 1
most, least = 0, 0
for i in range(length):
  if ones[i] > size // 2:
    most = most * 2 + 1
    least = least * 2
  else:
    least = least * 2 + 1
    most = most * 2
print(least * most)

