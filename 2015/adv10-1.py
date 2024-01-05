import itertools

src = "3113322113"

def count(it):
  ans = 0
  for i in it:
    ans += 1
  return ans

def process(src):
  ans = []
  for k, v in itertools.groupby(src):
    ans.append(str(count(v)))
    ans.append(k)
  return "".join(ans)

for i in range(50):
  src = process(src)
print(len(src))


