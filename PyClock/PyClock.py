import datetime
import time
import tkinter as tk

class PyClock:
    def __init__(self):
        self.show_seconds = True
        self.root = tk.Tk()
        self.root.title("PyClock")
        self.label = tk.Label(self.root, font=('Helvetica', 48))
        self.label.pack(padx=20, pady=20)
        self.button = tk.Button(self.root, text="Másodperc BE", command=self.toggle_seconds)
        self.button.pack(padx=20, pady=20)
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = datetime.datetime.now()
        if self.show_seconds:
            formatted_time = now.strftime("%H:%M:%S")
        else:
            formatted_time = now.strftime("%H:%M")
        self.label.configure(text=formatted_time)
        self.root.after(1000, self.update_clock)

    def toggle_seconds(self):
        self.show_seconds = not self.show_seconds
        if self.show_seconds:
            self.button.configure(text="Másodperc KI")
        else:
            self.button.configure(text="Másodperc BE")

if __name__ == '__main__':
    PyClock()
