# This script/repo/tool does follow the automation guidelines
# on the /r/adventofcode community wiki

import requests
import sys
import os

cookies = {}
cookie_file = open("cookies.txt", "rt")
for line in cookie_file:
  key, value = line.strip().split("=")
  cookies[key] = value

os.makedirs("altinputs", exist_ok=True)
year = sys.argv[1].strip()
for problem in range(1, 26):
  print(f"Downloading problem {problem}")
  url_problem = "https://adventofcode.com/" + str(year) + "/day/" + str(problem)
  input_text = requests.get(url_problem + "/input", cookies=cookies)
  f = open("altinputs/input.%02d.txt" % problem, "wt")
  f.write(input_text.text)
  f.close()

