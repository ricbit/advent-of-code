import hashlib

for i in range(3 * 10 ** 7):
  m = hashlib.md5()
  m.update(b"ckczppom" + bytes(str(i), "ascii"))
  ans = m.hexdigest()
  if ans.startswith("000000"):
    print(i)
    break
