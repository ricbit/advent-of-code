ops = input().strip()
level = 0
for i, c in enumerate(ops):
  if c == "(":
    level += 1
  elif c == ")":
    level -= 1
  if level == -1:
    print(i + 1)
    break
