import sys
import re

ans = 0
for w in sys.stdin:
  if re.search(r"(..).*\1", w) is not None:
    if re.search(r"(.).\1", w) is not None:
      ans += 1
print(ans)
