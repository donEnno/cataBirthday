import tkinter as tk
from windows.lastWindow import LastWindow
from windows.utils import QuestionScore, center_window, left_click_count


class QuestionSummary:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("650x200")
        self.root.title("It's your birthday")
        
        self.clicked = False

        center_window(root)

        # Create the message label
        self.summary_label = tk.Label(self.root, text="Result", font=("Arial", 16))
        self.summary_label.pack(pady=15)

        self.result_label = tk.Label(self.root, text=f"You answered %s out of 7 questions correctly. \n You are clearly awesome!"%QuestionScore.score, 
                                     font=("Arial", 14))
        self.result_label.pack(pady=15)

        # Create the buttons
        self.b1 = tk.Button(self.root, text="Go on", command=self.button_click)
        self.b1.pack(pady=15)

        self.root.bind("<Button-1>", left_click_count)

    def button_click(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        

        # Open the prompt window
        next_window = LastWindow(root)
    
    
