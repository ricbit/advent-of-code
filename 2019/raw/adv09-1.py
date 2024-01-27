import sys
import itertools
import aoc
from collections import deque

class IntCode:
  def __init__(self, data, input_values):
    self.data = aoc.ddict(lambda: 0)
    self.data.update({i:value for i, value in enumerate(data)})
    self.input_values = deque(input_values)
    self.pos = 0
    self.output = []
    self.halted = False
    self.base = 0

  def decode(self, opcode, size, decode_last=False):
    ans = []
    msize = size if decode_last else size - 1
    for i in range(msize):
      addr = opcode[-1 - (2 + i)]
      if addr == "0":
        ans.append(self.data[self.data[self.pos + 1 + i]])
      elif addr == "1":
        ans.append(self.data[self.pos + 1 + i])
      elif addr == "2":
        ans.append(self.data[self.data[self.pos + 1 + i] + self.base])
    if not decode_last:
      ans.append(self.data[self.pos + size])
    return ans

  def write_args(self, opcode):
    args = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7:3, 8:3, 9:1, 99:0}
    ans = []
    for i in range(args[int(opcode[-2:])]):
      if opcode[-3-i] == "0":
        ans.append(f"[{self.data[self.pos + 1 + i]}]")
      if opcode[-3-i] == "1":
        ans.append(f"{self.data[self.pos + 1 + i]}")
      if opcode[-3-i] == "2":
        ans.append(f"[BP + {self.data[self.pos + 1 + i]}]")
    return " ".join(ans)

  def run(self):
    if self.halted:
      return True
    names = {1: "ADD", 2: "MUL", 3:"IN",4:"OUT",5:"JP NZ", 6:"JP Z",7:"SET LT",8:"SET EQ",9:"ADD BP"
        ,99:"halt"}

    while self.pos < len(self.data):
      opcode = "%05d" % self.data[self.pos]
      cmd = self.data[self.pos] % 100
      print(f"{self.pos} {opcode} {names[cmd]} {self.write_args(opcode)}")
      print(f"BP {self.base}")
      print(f"data[1000] {self.data[1000]}")
      if cmd == 1: # ADD
        a, b, c = self.decode(opcode, 3)
        if opcode[-5] == "0":
          self.data[c] = a + b
        elif opcode[-5] == "2":
          self.data[c + self.base] = a + b
        self.pos += 4
      elif cmd == 2: # MUL
        a, b, c = self.decode(opcode, 3)
        if opcode[-5] == "0":
          self.data[c] = a * b
        elif opcode[-5] == "2":
          self.data[c + self.base] = a * b
        self.pos += 4
      elif cmd == 3: # IN
        (a,) = self.decode(opcode, 1)
        print(opcode, a, self.base)
        if opcode[-3] == "0":
          self.data[a] = self.input_values.popleft()
        elif opcode[-3] == "2":
          print("here")
          self.data[a + self.base] = self.input_values.popleft()
          print(f"a {a} base{self.base}", a+self.base)
          print("sd1000 ",self.data[1000])
        self.pos += 2
      elif cmd == 4: # OUT
        (a,) = self.decode(opcode, 1, True)
        self.output.append(a)
        self.pos += 2
        #return False
      elif cmd == 5: # JP NZ
        a, b = self.decode(opcode, 2, True)
        self.pos = b if (a != 0) else self.pos + 3
      elif cmd == 6: # JP Z
        a, b = self.decode(opcode, 2, True)
        self.pos = b if (a == 0) else self.pos + 3
      elif cmd == 7: # SET LT
        a, b, c = self.decode(opcode, 3)
        if opcode[-5] == "0":
          self.data[c] = int(a < b)
        elif opcode[-5] == "2":
          self.data[c + self.base] = int(a < b)
        self.pos += 4
      elif cmd == 8: # SET EQ
        a, b, c = self.decode(opcode, 3)
        if opcode[-5] == "0":
          self.data[c] = int(a == b)
        elif opcode[-5] == "2":
          self.data[c + self.base] = int(a == b)
        self.pos += 4
      elif cmd == 9: # SET BP
        (a,) = self.decode(opcode, 1, True)
        self.base += a
        self.pos += 2
      elif cmd == 99: # HALT
        self.halted = True
        return True

data = [int(i) for i in sys.stdin.read().split(",")]
cpu = IntCode(data, [1])
cpu.run()
aoc.cprint(cpu.output)
