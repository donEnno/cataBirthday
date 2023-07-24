import tkinter as tk
from quiz.questionWindow2 import questionTwo
from windows.utils import QuestionScore, center_window, left_click_count


class questionOne:
    def __init__(self, root, 
                 question, header,
                 a, b, c):
        
        self.root = root
        self.root.geometry("500x300")
        self.root.title("It's your birthday")
        
        center_window(root)

        # Configure the message box to span three columns and center the text
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)        
        self.root.grid_rowconfigure(3, weight=1)        

        # Create the message labelcd
        self.header_label = tk.Label(self.root, text=header, font=("Arial", 24))
        self.header_label.grid(row=0, column=0, columnspan=3,  pady=0, padx=0, sticky="nsew")

        self.question_label = tk.Label(self.root, text=question, font=("Arial", 14))
        self.question_label.grid(row=1, column=0, columnspan=3,  pady=0, padx=0)

        # Create the buttons
        self.b1 = tk.Button(self.root, text=a, command=self.right_answer)
        self.b1.grid(row=2, column=0, padx=10, pady=10)

        self.b2 = tk.Button(self.root, text=b, command=self.wrong_answer)
        self.b2.grid(row=2, column=1, padx=10, pady=10)

        self.b3 = tk.Button(self.root, text=c, command=self.wrong_answer)
        self.b3.grid(row=2, column=2, padx=10, pady=10)

        
        self.root.bind("<Button-1>", left_click_count)

    def right_answer(self):
        self.b4 = tk.Button(self.root, text="Next question", command=self.button_click)
        self.b4.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        QuestionScore.increment_score()
        self.header_label.config(text="Correct!")

    def wrong_answer(self):
        self.b4 = tk.Button(self.root, text="Next question", command=self.button_click)
        self.b4.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        self.header_label.config(text="Wrong answer.")

    def button_click(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        

        # Open the prompt window
        next_window = questionTwo(root, 
                                      "How many syllables can S. bilineate sing?",
                                      "Biology",
                                      "23",
                                      "25",
                                      "29")
    
