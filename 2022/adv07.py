import sys

class Parser:
  def __init__(self):
    self.lines = sys.stdin.readlines()
    self.size = len(self.lines)
    self.root = []
    self.current = self.root
    self.pos = 0

  def process_commands(self):
    while self.pos < self.size:
      self.parse_command()

  def add_path(self, path):
    new_path = [("dir", "..", self.current)] 
    self.current.append(("dir", path, new_path))
    self.pos += 1
    self.current = new_path

  def find_path(self, path):
    for code, name, link in self.current:
      if code == "dir" and name == path:
        self.current = link
        self.pos += 1
        return True
    return False

  def parse_command(self):
    match self.lines[self.pos].split()[1:]:
      case ["cd", "/"]:
        self.current = self.root
        self.pos += 1
      case ["cd", path]:
        if not self.find_path(path):
          self.add_path(path)
      case ["ls"]:
        self.pos += 1
        while self.pos<self.size and not self.lines[self.pos].startswith("$"):
          file_size, file_name = self.lines[self.pos].strip().split()
          if file_size != "dir":
            self.current.append(("file", file_name, int(file_size)))
          self.pos += 1

  def collect_dir_size(self, current, func):
    total = 0
    for code, name, value in current:
      if code == "file":
        total += value
      elif code == "dir" and name != "..":
        value = self.collect_dir_size(value, func)
        total += value
    return func(total)

  def collect_all_sizes(self, func):
    return func(self.collect_dir_size(self.root, func))

first_ans = 0
def first(value):
  global first_ans
  if value <= 100000:
    first_ans += value
  return value

parser = Parser()
parser.process_commands()
total = parser.collect_all_sizes(first)
unused = 70000000 - total
missing = 30000000 - unused

second_ans = 1e10
def second(value):
  global second_ans
  if value >= missing and value < second_ans:
    second_ans = value
  return value

parser.collect_all_sizes(second)
print(first_ans, second_ans)

