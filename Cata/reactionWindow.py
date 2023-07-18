import random
import tkinter as tk
from Cata.mainWindow4 import MainWindowFour
from Cata.utils import left_click_count



class ReactionWindow:
    def __init__(self, root):
        self.root = root
        self.first_click = True
        self.timer_active = True

        self.score = 0
        self.root.geometry("400x300")

        self.countdown_label = tk.Label(self.root, text="")
        self.countdown_label.pack(pady=10, padx=10)

        self.button = tk.Button(self.root, text="Start Timer", command=self.start_countdown)
        self.button.pack(pady=10)

        self.countdown_seconds = 10
        self.result_text = ""

        self.root.bind("<Button-1>", left_click_count)

    def update_countdown_label(self):
        
        if self.countdown_seconds >= 4:
            self.countdown_label.config(text=f"Countdown: %s seconds"%int(self.countdown_seconds))
            self.countdown_seconds -= 1
            print(self.countdown_seconds)
            self.root.after(1000, self.update_countdown_label)

        elif self.countdown_seconds < 4 and self.countdown_seconds >= 0:
            self.countdown_label.config(text=f"Countdown: %.2f seconds"%self.countdown_seconds)
            self.countdown_seconds -= 0.1
            print(self.countdown_seconds)
            self.root.after(100, self.update_countdown_label)

        else:
            self.countdown_label.config(text=f"Time is up!")
            self.countdown_seconds = -1
            self.timer_completed()

    def start_countdown(self):
        
        if not self.timer_active:
            self.button.forget()

        if self.first_click:
            self.button.config(text="Happy")
            
            self.update_countdown_label()
            self.root.after(10000, self.timer_completed)
            self.first_click = False

        if not self.first_click and self.timer_active:
            if self.score % 2 == 0:
                self.button.config(text="Happy")
            else:
                self.button.config(text="Birthday")

            self.score += 1
            
            x = random.randint(0, max(10, int(self.root.winfo_width()-self.button.winfo_width()*1.1)))
            y = random.randint(0, max(10, int(self.root.winfo_height()-self.button.winfo_height()*1.1)))
            self.button.place(x=x, y=y)


    def timer_completed(self):
        if self.timer_active:
            self.timer_active = False
        
            self.score_label = tk.Label(self.root, text=f"You achieved a score of %s!"%self.score)
            self.score_label.pack()

            self.button.destroy()

            button2 = tk.Button(self.root, text="Next", command=self.b1_clicked)
            button2.pack(pady=20)


    def b1_clicked(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        
        # Open the prompt window
        prompt_window = MainWindowFour(root,
                                       "Yes",
                                       "No",
                                       "???")
