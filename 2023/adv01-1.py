import sys

ans = 0
for line in sys.stdin:
  line = "".join((c if c.isdecimal() else "") for c in line)
  n = int(line[0] + line[-1])
  ans += n
print(ans)

