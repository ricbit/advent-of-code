import sys
import itertools

def direct(lines, func):
  ans = 0
  for line in lines:
    mat = [func([int(i) for i in line.split()])]
    while True:
      mat.append([b - a for a, b in itertools.pairwise(mat[-1])])
      if len(set(mat[-1])) == 1:
        ans += sum(row[-1] for row in mat)
        break
  return ans

lines = sys.stdin.readlines()
print(direct(lines, lambda x: x))
print(direct(lines, lambda x: x[::-1]))
