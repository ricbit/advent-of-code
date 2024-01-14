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
import subprocess
import time
import asyncio

def get_cookies():
  cookies = {}
  cookie_file = open("cookies.txt", "rt")
  for line in cookie_file:
    key, value = line.strip().split("=")
    cookies[key] = value
  return cookies

def get_tmux_session():
  session = libtmux.Server().sessions[0]
  for pane in session.panes:
    if pane != session.attached_pane:
      pane.cmd('kill-pane')
  return session

def get_problem():
  year = re.match(r".*?(\d+)", os.getcwd()).group(1)
  if len(sys.argv) >= 2:
    problem = sys.argv[1].strip()
  else:
    problem = open("advcurrent.txt").read().split()[0]
  return year, problem

def get_url_problem(year, problem):
  return f"https://adventofcode.com/{year}/day/{problem}"

def get_samples(year, problem, cookies):
  url_problem = get_url_problem(year, problem)
  page = requests.get(url_problem, cookies=cookies)
  soup = BS(page.text, "html.parser")
  for i, code in enumerate(soup.find_all("code")):
    f = open("sample.%02d.%d.txt" % (int(problem), i + 1) , "wt")
    f.write(code.text)
    f.close()

def get_times(year, problem, cookies):
  url_leaderboard = f"https://adventofcode.com/{year}/leaderboard/day/{problem}"
  page = requests.get(url_leaderboard, cookies=cookies)
  soup = BS(page.text, "html.parser")
  times = []
  for div in soup.find_all(class_="leaderboard-entry"):
    span = div.find(class_="leaderboard-position")
    if span.text.startswith("100"):
      timestr = div.find(class_="leaderboard-time").text
      leader_time = datetime.datetime.strptime(timestr, "%b %d %H:%M:%S")
      times.append(leader_time.strftime("%H:%M:%S"))
  return times

def get_input(year, problem, cookies):
  url_problem = get_url_problem(year, problem)
  input_text = requests.get(url_problem + "/input", cookies=cookies)
  f = open("input.%02d.txt" % int(problem), "wt")
  f.write(input_text.text)
  f.close()

def open_panes(problem, session):
  session.attached_pane.cmd(
      'split-window', '-b', '-p', '20', '-d', 'vi', 'input.%02d.txt' % int(problem))
  session.attached_pane.cmd(
      'split-window', '-b', '-p', '20', '-d', 'python')

def open_browser(year, problem):
  url_problem = get_url_problem(year, problem)
  filename_part1 = "adv%02d-1.py" % int(problem)
  filename_part2 = "adv%02d-2.py" % int(problem)
  part = 1
  if not os.path.exists(filename_part1):
    webbrowser.open_new_tab(f"{url_problem}#part{part}")
    shutil.copy("template.py", filename_part1)
  elif not os.path.exists(filename_part2):
    part = 2
    webbrowser.open_new_tab(f"{url_problem}#part{part}")
    shutil.copy(filename_part1, filename_part2)
  return part

def write_current(problem, part):
  f = open("advcurrent.txt", "wt")
  f.write("%02d %d" % (int(problem), part))
  f.close()

def send_command(cmd):
  while True:
    try: 
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(bytes(cmd, encoding="ascii"))
        break
    except socket.error:
      time.sleep(1)

def start_timer(times, part):
  match part:
    case 1:
      subprocess.Popen(['python', 'timer.py'])
      send_command(f"start {times[0]} {times[1]}")
    case 2:
      send_command("stop 1")

def open_vi(problem, part, session):
  session.attached_pane.send_keys("vi adv%02i-%d.py" % (int(problem), part))

def main():
  cookies = get_cookies()
  session = get_tmux_session()
  year, problem = get_problem()
  get_samples(year, problem, cookies)
  times = get_times(year, problem, cookies)
  get_input(year, problem, cookies)
  open_panes(problem, session)
  part = open_browser(year, problem)
  write_current(problem, part)
  start_timer(times, part)
  open_vi(problem, part, session)

main()
