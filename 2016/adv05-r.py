import sys
import aoc
import _md5
import itertools
from multiprocessing import Pool

def direct_search(pwd):
  with Pool() as pool:
    out = sorted(pool.starmap(direct_encode, ((pwd, offset) for offset in range(1100))))
    all_chars = aoc.flatten(chars for _, chars in out)
    return "".join(itertools.islice(all_chars, 8))

def direct_encode(pwd, offset):
  out = []
  for i in range(offset * 10000, offset * 10000 + 10000):
    md5 = _md5.md5((pwd + str(i)).encode("ascii")).hexdigest()
    if md5[:5] == "00000":
      out.append(md5[5])
  return offset, out

def search(pwd):
  with Pool() as pool:
    out = pool.starmap(merge, ((pwd, offset) for offset in range(2700)))
    yield from (encoded for _, encoded in sorted(out))

def encode(pwd, offset):
  for i in range(offset * 10000, offset * 10000 + 10000):
    md5 = _md5.md5((pwd + str(i)).encode("ascii")).hexdigest()
    if md5[:5] == "00000":
      if (pos := int(md5[5], 16)) < 8:
        yield (i, pos, md5[6])

def reduce(ic_list):
  new_pwd = ["_"] * 8
  for i, c in ic_list: 
    if new_pwd[i] == "_":
      new_pwd[i] = c
  return "".join(new_pwd)

def merge(pwd, offset):
  return offset, reduce((i, c) for _, i, c in encode(pwd,offset))

def join(pwd_list):
  return reduce(aoc.flatten(enumerate(pwd) for pwd in pwd_list))

pwd = sys.stdin.read().strip()
aoc.cprint(direct_search(pwd))
aoc.cprint(join(search(pwd)))
