import sys
import re

lines = sys.stdin.readlines()
numbers = "one|two|three|four|five|six|seven|eight|nine"
values = {name:value + 1 for value, name in enumerate(numbers.split("|"))}
values.update({str(digit):digit for digit in range(10)})
build = lambda regexp: lambda line: values[re.search(regexp, line).group(1)]
first = build(fr"^.*?(\d|{numbers})")
last = build(fr"^.*(\d|{numbers}).*?$")
digits = lambda line: "".join(d for d in line if d.isdecimal())
print(sum(first(digits(line)) * 10 + last(digits(line)) for line in lines))
print(sum(first(line) * 10 + last(line) for line in lines))
