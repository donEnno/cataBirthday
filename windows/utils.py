import tkinter as tk
import random


class PopupWindow:
    def __init__(self, text, geometry="600x200"):
        self.text = text
        self.geometry = geometry

    def run(self):
        # Create a pop-up window to show when the click count reaches 25
        popup_root = tk.Toplevel()
        popup_root.title("Popup Window")
        popup_root.geometry(self.geometry)
        
        center_window(popup_root, almost=True)

        popup_label = tk.Label(popup_root, text=self.text, font=("Arial", 16))
        popup_label.pack(pady=50)

        popup_root.mainloop()


class ClickCounter:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1


class Score:
    score = 0

    @classmethod
    def increment_score(cls, inc):
        cls.score += inc
   

class QuestionScore:
    score = 0

    @classmethod
    def increment_score(cls):
        cls.score += 1


def left_click_count(event):
    ClickCounter.increment_count()
    
    if ClickCounter.count == 250:
        # Open a pop-up window when the click count reaches 25
        popup_window = PopupWindow(text="Awesome! You clicked as many times as you're aged!!")
        popup_window.run()

    

def center_window(root, almost=False):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates for centering the window
    x = int((screen_width - root.winfo_reqwidth()) / 2)
    y = int((screen_height - root.winfo_reqheight()) / 2)

    if almost:
        x += 25
        y += 25

    # Set the window's position
    root.geometry(f"+{x}+{y}")


def generate_compliment():

    compliments = [
    "You are amazing!",
    "You make me smile every day.",
    "You have a heart of gold.",
    "You light up my world.",
    "You are a Süßmaus.",
    "You are beautiful!",
    "You make me feel special.",
    "You are my sunshine.",
    "Not just a pretty face!",
    "You can achieve anything!",
    "You deserve it all.",
    "You are loved <3",
    "You are just great.",
    "You mean the world to me.",
    "You're cute as an apple pie."
    ]

    return random.choice(compliments)
