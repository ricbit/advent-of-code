# This script/repo/tool does follow the automation guidelines
# on the /r/adventofcode community wiki

import requests
from bs4 import BeautifulSoup as BS
import sys
import os
import webbrowser
import shutil
import re
import libtmux
import socket
import datetime

cookies = {}
cookie_file = open("cookies.txt", "rt")
for line in cookie_file:
  key, value = line.strip().split("=")
  cookies[key] = value

session = libtmux.Server().sessions[0]
for pane in session.panes:
  if pane != session.attached_pane:
    pane.cmd('kill-pane')

year = re.match(r".*?(\d+)", os.getcwd()).group(1)
problem = sys.argv[1].strip()
url_problem = f"https://adventofcode.com/{year}/day/{problem}"
page = requests.get(url_problem, cookies=cookies)
soup = BS(page.text, "html.parser")
for i, pre in enumerate(soup.find_all("pre")):
  f = open("sample.%02d.%d.txt" % (int(problem), i + 1) , "wt")
  f.write(pre.find("code").text)
  f.close()

url_leaderboard = f"https://adventofcode.com/{year}/leaderboard/day/{problem}"
page = requests.get(url_leaderboard, cookies=cookies)
soup = BS(page.text, "html.parser")
times = []
for div in soup.find_all(class_="leaderboard-entry"):
  span = div.find(class_="leaderboard-position")
  if span.text.startswith("100"):
    timestr = div.find(class_="leaderboard-time").text
    time = datetime.datetime.strptime(timestr, "%b %d %H:%M:%S")
    times.append(time.strftime("%H:%M:%S"))

input_text = requests.get(url_problem + "/input", cookies=cookies)
f = open("input.%02d.txt" % int(problem), "wt")
f.write(input_text.text)
f.close()

session.attached_pane.cmd(
    'split-window', '-b', '-p', '20', '-d', 'vi', 'input.%02d.txt' % int(problem))
session.attached_pane.cmd(
    'split-window', '-b', '-p', '20', '-d', 'python')

filename_part1 = "adv%02d-1.py" % int(problem)
filename_part2 = "adv%02d-2.py" % int(problem)
part = 1
if not os.path.exists(filename_part1):
  webbrowser.open_new_tab(url_problem)
  shutil.copy("template.py", filename_part1)
elif not os.path.exists(filename_part2):
  shutil.copy(filename_part1, filename_part2)
  part = 2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(('localhost', 12345))
  s.sendall(bytes(f'start {times[0]} {times[1]}', encoding="ascii"))

session.attached_pane.send_keys("vi adv%02i-%d.py" % (int(problem), part))
