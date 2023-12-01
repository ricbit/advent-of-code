import sys
import re

numb = """
one, two, three, four, five, six, seven, eight, nine
""".split(",")
numb = [x.strip() for x in numb]
d = {n:i+1 for i, n in enumerate(numb)}
reg = "|".join(numb)

def value(n):
  if n.isdigit():
    return int(n)
  else:
    return d[n]

ans = 0
for line in sys.stdin:
  p = re.search("^.*?(\d|" + reg + ")", line)
  a = value(p.group(1))
  p = re.search("^.*(\d|" + reg + ").*?$", line)
  b = value(p.group(1))
  ans += a * 10 + b
print(ans)

