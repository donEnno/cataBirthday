import random
import tkinter as tk
from tkinter import messagebox
from windows.utils import center_window, left_click_count

class PromptWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Prompt Window")
        self.root.protocol("WM_DELETE_WINDOW", self.button_click)
        
        center_window(root)

        self.question_label = tk.Label(self.root, text="Question:")
        self.question_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.question_textbox = tk.Text(self.root, height=3, width=30)
        self.question_textbox.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.close_button = tk.Button(self.root, text="Close", command=self.button_click)
        self.close_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        
        self.answer_label = tk.Label(self.root, text="")
        self.answer_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.countdown_label = tk.Label(self.root, text="")
        self.countdown_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.countdown_seconds = 5.0

        self.start_countdown()

        self.root.bind("<Button-1>", left_click_count)

        self.root.mainloop()

    def start_countdown(self):
        if self.countdown_seconds >= 0:
            self.countdown_label.config(text=f"Countdown: {self.countdown_seconds} seconds")
            self.countdown_seconds -= 0.01
            self.root.after(1000, self.start_countdown)
        else:
            self.countdown_label.config(text="Countdown: Time's up!")

    def submit_answer(self):
        answer = self.question_textbox.get("1.0", tk.END).strip()
        self.answer_label.config(text=f"Answer: {answer}")

    def button_click(self):
        self.root.destroy()
        self.root.quit()  # Terminate the Tkinter event loop