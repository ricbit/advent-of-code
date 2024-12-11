import sys
import re
import itertools
import aoc

splitter = lambda s: set("".join(field) for field in itertools.batched(s, 3))
required = splitter("byriyreyrhgthcleclpid")
colors = splitter("ambblubrngrygrnhzloth")

validators = {
  "byr": lambda x: x.isdigit() and len(x) == 4 and 1920 <= int(x) <= 2002,
  "iyr": lambda x: x.isdigit() and len(x) == 4 and 2010 <= int(x) <= 2020,
  "eyr": lambda x: x.isdigit() and len(x) == 4 and 2020 <= int(x) <= 2030,
  "hgt": lambda x: ((y := re.search(r"(\d+)(cm|in)$", x)) is not None and 
                    ((150 <= int(y.group(1)) <= 193 and y.group(2) == "cm") or
                    ((59 <= int(y.group(1)) <= 76 and y.group(2) == "in")))),
  "hcl": lambda x: re.match(r"#[0-9a-f]{6}", x) is not None,
  "ecl": lambda x: x in colors,
  "pid": lambda x: x.isdigit() and len(x) == 9,
  "cid": lambda x: True
}

def solve(passports, validator):
  ans = 0
  for raw in passports:
    passport = dict(re.findall(r"(\w{3}):(\S+)", " ".join(raw)))
    if (all(fields in passport for fields in required) and
        all(validator[field](value) for field, value in passport.items())):
      ans += 1
  return ans

data = aoc.line_blocks()
aoc.cprint(solve(data, aoc.ddict(lambda: lambda y: True)))
aoc.cprint(solve(data, validators))
