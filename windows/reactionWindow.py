import random
import tkinter as tk
from windows.JanWindow import JanWindow
from windows.utils import center_window, left_click_count, Score



class ReactionWindow:
    def __init__(self, root):
        self.root = root
        self.first_click = True
        self.timer_active = True

        self.score = 0
        self.root.geometry("400x300")
        self.root.title("It's your birthday")

        center_window(root)

        self.countdown_label = tk.Label(self.root, text="")
        self.countdown_label.pack(pady=10, padx=10)

        self.explain_label = tk.Label(self.root, text="Try to click as many buttons as possible. \n You got 10 seconds.")
        self.explain_label.pack()

        self.button = tk.Button(self.root, text="Start Timer", command=self.start_countdown)
        self.button.pack(pady=10)

        self.countdown_seconds = 10
        self.result_text = ""

        self.root.bind("<Button-1>", left_click_count)

    def update_countdown_label(self):
        
        if self.countdown_seconds >= 4:
            self.countdown_label.config(text=f"Countdown: %s seconds"%int(self.countdown_seconds))
            self.countdown_seconds -= 1
            self.root.after(1000, self.update_countdown_label)

        elif self.countdown_seconds < 4 and self.countdown_seconds >= 0:
            self.countdown_label.config(text=f"Countdown: %.2f seconds"%self.countdown_seconds)
            self.countdown_seconds -= 0.1
            self.root.after(100, self.update_countdown_label)

        else:
            self.countdown_label.config(text=f"Time is up!")
            self.countdown_seconds = -1
            self.timer_completed()

    def start_countdown(self):
        
        if not self.timer_active:
            self.button.forget()

        if self.first_click:
            self.explain_label.destroy()

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

    
    def try_again(self):        
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        
        # Open the prompt window
        next_window = ReactionWindow(root)


    def timer_completed(self):
        ENNOS_HIGHSCORE = 19

        if self.timer_active:
            self.timer_active = False
        
            self.score_label = tk.Label(self.root, text=f"You achieved a score of %s!"%self.score)
            self.score_label.pack()

            if self.score < ENNOS_HIGHSCORE:
                self.message_label = tk.Label(self.root, text=f"That's %s less than Enno's highscore!"%(ENNOS_HIGHSCORE-self.score))
                self.message_label.pack()
            elif self.score == ENNOS_HIGHSCORE:
                self.message_label = tk.Label(self.root, text="You machted Enno's highscore. Maybe give it another go?")
                self.message_label.pack()
            else:
                self.message_label = tk.Label(self.root, text=f"You beat Enno's highscore by %s. \n That's awesome!"%(self.score-ENNOS_HIGHSCORE))
                self.message_label.pack()

            self.button.destroy()

            button2 = tk.Button(self.root, text="Next", command=self.button_click)
            button2.pack(pady=20)
            
            button3 = tk.Button(self.root, text="Try again", command=self.try_again)
            button3.pack()


    def button_click(self):
        Score.increment_score(self.score)
        
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        
        # Open the prompt window
        next_window = JanWindow(root)
