import requests
from bs4 import BeautifulSoup as BS
import sys

cookies = {}
cookie_file = open("cookies.txt", "rt")
for line in cookie_file:
  key, value = line.strip().split("=")
  cookies[key] = value

problem = sys.argv[1].strip()
url_problem = "https://adventofcode.com/2023/day/" + problem
page = requests.get(url_problem, cookies=cookies)
soup = BS(page.text, "html.parser")
for i, pre in enumerate(soup.find_all("pre")):
  f = open("sample.%02d.%d.txt" % (int(problem), i + 1) , "wt")
  f.write(pre.find("code").text)
  f.close()

input_text = requests.get(url_problem + "/input", cookies=cookies)
f = open("input.%02d.txt" % int(problem), "wt")
f.write(input_text.text)
f.close()

