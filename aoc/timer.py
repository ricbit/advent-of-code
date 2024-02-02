import tkinter as tk
import tkinter.font as tkFont
import socket
import threading

class ChronometerApp:
  def __init__(self, root):
    self.root = root
    root.title("AOC Goal")
    root.configure(bg="black")
    root.geometry("+3300+1900")
    root.attributes('-topmost', True)

    # Load leaderboard times.
    times = [list(map(int, line.split(":"))) 
      for line in open("leaderboard.txt", "rt").readlines()]
    self.leader = [times[100:], times[:100]]

    self.digital_font = tkFont.Font(family="Digital-7", size=30)

    # Initialize timers
    self.timer = [[0, 0, 0] for i in range(2)]  # hours, minutes, seconds

    # Create labels to display timers
    text = ["00:00:00"] * 2
    self.goal_label = list(self.create_labels(tk.Label, text))

    # Create labels to display timers
    self.timer_label = list(self.create_labels(tk.Label, text))

    # Create labels to display positions
    text = ["1", "1"]
    self.leader_label = list(self.create_labels(tk.Label, text))
        
    # Create buttons
    text = "p1 p2".split()
    cmds = [self.stop_timer1, self.stop_timer2]
    self.button = list(self.create_labels(tk.Button, text, cmds))
    self.timer_callback = [self.update_timer1, self.update_timer2]

    # Flags to control the timers
    self.running = [False] * 2

    # Start a thread to listen for start signal
    threading.Thread(target=self.listen_for_start_signal, daemon=True).start()

  def create_labels(self, widget, text, cmds=None):
    frame = tk.Frame(root, bg="black")
    frame.pack(pady=10)
    for i in range(2):
      label = widget(
          frame, text=text[i], font=self.digital_font, bg="black", fg="white")
      if cmds is not None:
        label['command'] = cmds[i]
      label.pack(side=tk.LEFT, padx=10)
      yield label

  def listen_for_start_signal(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind(('localhost', 12345))
      s.listen()

      while True:
        # Wait for a connection
        conn, addr = s.accept()
        with conn:
          data = conn.recv(1024)
          # Start timers if the received data is the start signal
          if data:
            match data.decode().strip().split():
              case "start", t1, t2:
                self.goal_label[0].config(text=t1)
                self.goal_label[1].config(text=t2)
                self.start_timers()
                conn.close()
              case "stop", "1":
                self.running[0] = False
                conn.close()
              case "stop", "2":
                self.running[1] = False
                conn.close()

  def start_timers(self):
    self.running[0] = True
    self.running[1] = True
    self.update_timer1()
    self.update_timer2()

  def inctimer(self, timer):
    timer[2] += 1
    if timer[2] >= 60:
      timer[2] = 0
      timer[1] += 1
    if timer[1] >= 60:
      timer[1] = 0
      timer[0] += 1

  def get_leader(self, timer, leader):
    for i, leader_time in enumerate(leader):
      if timer < leader_time:
        return str(i + 1)
    return "100+"

  def update_timer(self, t):
    if self.running[t]:
      self.inctimer(self.timer[t])
      time_string = f"{self.timer[t][0]:02d}:{self.timer[t][1]:02d}:{self.timer[t][2]:02d}"
      self.timer_label[t].config(text=time_string)
      self.leader_label[t].config(text=self.get_leader(self.timer[t], self.leader[t]))
      self.root.after(1000, self.timer_callback[t])

  def update_timer1(self):
    self.update_timer(0)

  def update_timer2(self):
    self.update_timer(1)

  def stop_timer1(self):
    self.running[0] = not self.running[0]
    self.update_timer1()

  def stop_timer2(self):
    self.running[1] = not self.running[1]
    self.update_timer2()

# Create the Tkinter window
root = tk.Tk()
app = ChronometerApp(root)
root.mainloop()

