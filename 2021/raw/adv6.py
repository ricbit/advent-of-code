import sys

fishes = [int(fish) for fish in sys.stdin.readline().strip().split(",")]
fishtypes = [0] * 9
for fish in fishes:
  fishtypes[fish] += 1

days = 256
for _ in range(days):
  newfish = fishtypes[1:] + [fishtypes[0]]
  newfish[6] += fishtypes[0]
  fishtypes = newfish
print(sum(fishtypes))

