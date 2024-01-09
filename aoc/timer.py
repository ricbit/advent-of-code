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

        self.digital_font = tkFont.Font(family="Digital-7", size=30)

        # Initialize timers
        self.timer1 = [0, 0, 0]  # hours, minutes, seconds
        self.timer2 = [0, 0, 0]

        # Create labels to display timers
        self.original_frame = tk.Frame(root, bg="black")
        self.original_frame.pack(pady=20)
        self.original1_label = tk.Label(
            self.original_frame, text="00:00:00", font=self.digital_font, bg="black", fg="white")
        self.original1_label.pack(side=tk.LEFT, padx=10)
        self.original2_label = tk.Label(
            self.original_frame, text="00:00:00", font=self.digital_font, bg="black", fg="white")
        self.original2_label.pack(side=tk.LEFT, padx=10)

        # Create labels to display timers
        self.timer_frame = tk.Frame(root, bg="black")
        self.timer_frame.pack()
        self.timer1_label = tk.Label(
            self.timer_frame, text="00:00:00", font=self.digital_font, bg="black", fg="white")
        self.timer1_label.pack(side=tk.LEFT, padx=10)
        self.timer2_label = tk.Label(
            self.timer_frame, text="00:00:00", font=self.digital_font, bg="black", fg="white")
        self.timer2_label.pack(side=tk.LEFT, padx=10)

        # Create buttons
        self.button_frame = tk.Frame(root, bg="black")
        self.button_frame.pack(pady=20)
        self.p1_button = tk.Button(self.button_frame, text="P1", command=self.stop_timer1)
        self.p1_button.pack(side=tk.LEFT, padx=10)
        self.p2_button = tk.Button(self.button_frame, text="P2", command=self.stop_timer2)
        self.p2_button.pack(side=tk.LEFT, padx=10)

        # Flags to control the timers
        self.running1 = False
        self.running2 = False

        # Start a thread to listen for start signal
        threading.Thread(target=self.listen_for_start_signal, daemon=True).start()

    def listen_for_start_signal(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Bind to localhost on a specific port, e.g., 12345
            s.bind(('localhost', 12345))
            s.listen()

            while True:
                # Wait for a connection
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    # Start timers if the received data is the start signal
                    if data and data.decode().startswith('start'):
                        _, t1, t2 = data.decode().split()
                        self.original1_label.config(text=t2)
                        self.original2_label.config(text=t1)
                        self.start_timers()
                        conn.close()

    def start_timers(self):
        self.running1 = True
        self.running2 = True
        self.update_timer1()
        self.update_timer2()

    def update_timer1(self):
        if self.running1:
            self.timer1[2] += 1
            if self.timer1[2] >= 60:
                self.timer1[2] = 0
                self.timer1[1] += 1
            if self.timer1[1] >= 60:
                self.timer1[1] = 0
                self.timer1[0] += 1
            time_string = f"{self.timer1[0]:02d}:{self.timer1[1]:02d}:{self.timer1[2]:02d}"
            self.timer1_label.config(text=time_string)
            self.root.after(1000, self.update_timer1)

    def update_timer2(self):
        if self.running2:
            self.timer2[2] += 1
            if self.timer2[2] >= 60:
                self.timer2[2] = 0
                self.timer2[1] += 1
            if self.timer2[1] >= 60:
                self.timer2[1] = 0
                self.timer2[0] += 1
            time_string = f"{self.timer2[0]:02d}:{self.timer2[1]:02d}:{self.timer2[2]:02d}"
            self.timer2_label.config(text=time_string)
            self.root.after(1000, self.update_timer2)

    def stop_timer1(self):
        self.running1 = False

    def stop_timer2(self):
        self.running2 = False

# Create the Tkinter window
root = tk.Tk()
app = ChronometerApp(root)
root.mainloop()

