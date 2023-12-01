import sys
import re

numbers = "one|two|three|four|five|six|seven|eight|nine"
values = {name:value + 1 for value, name in enumerate(numbers.split("|"))}
values.update({str(digit):digit for digit in range(10)})
build = lambda regexp: lambda line: values[re.search(regexp, line).group(1)]
first = build(f"^.*?(\d|{numbers})")
last = build(f"^.*(\d|{numbers}).*?$")
ans = sum(first(line) * 10 + last(line) for line in sys.stdin)
print(ans)

