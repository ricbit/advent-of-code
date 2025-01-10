import sys
import re
import aoc

lines = sys.stdin.readlines()
numbers = "one|two|three|four|five|six|seven|eight|nine"
values = {name: value + 1 for value, name in enumerate(numbers.split("|"))}
values.update({str(digit): digit for digit in range(10)})
build = lambda regexp: lambda line: values[re.search(regexp, line).group(1)]
first = build(fr"^.*?(\d|{numbers})")
last = build(fr"^.*(\d|{numbers}).*?$")
digits = lambda line: "".join(d for d in line if d.isdecimal())
compose = lambda line: first(line) * 10 + last(line)
aoc.cprint(sum(compose(digits(line)) for line in lines))
aoc.cprint(sum(compose(line) for line in lines))
