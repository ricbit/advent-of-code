import sys

def count(lines):
  ans = 0
  for line in lines:
    inside = line[1:-1]
    chars = 0
    pos = 0
    while pos < len(inside):
      chars += 1
      if inside[pos] == "\\":
        if inside[pos + 1] == "x":
          pos += 4
        else:
          pos += 2
      else:
        pos += 1
    ans += len(line) - chars
  return ans

def count2(lines):
  ans = 0
  for line in lines:
    ans += line.count("\\") + line.count("\"") + 2
  return ans

lines = sys.stdin.readlines()
print(count(lines))
print(count2(lines))
