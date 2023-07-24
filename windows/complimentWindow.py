import tkinter as tk
from windows.mainWindow4 import MainWindowFour
from windows.utils import center_window, generate_compliment


class ComplimentWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x180")
        self.root.title("It's your birthday")

        self.packed = False
        self.n_compliments = 0

        center_window(root)

        self.compliment_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.compliment_label.pack(pady=20)

        self.generate_button = tk.Button(self.root, text="Try me", command=self.show_compliment)
        self.generate_button.pack(pady=10)

    
    def show_compliment(self):
        
        self.n_compliments += 1

        if self.n_compliments == 1:
            self.generate_button.config(text='Another one!')

        if self.n_compliments == 2:
            self.generate_button.config(text="And another one")

        if self.n_compliments > 2:
            self.generate_button.config(text="Go on")

            if not self.packed:
                self.packed = True

                self.next_button = tk.Button(self.root, text="Next", command=self.button_click)
                self.next_button.pack()


        compliment = generate_compliment()
        self.compliment_label.config(text=compliment)
    
    def button_click(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        
        # Open the prompt window
        next_window = MainWindowFour(root,
                                     'Okay the fun part is over.',
                                     'Are you ready for some birthday challenges?',
                                     'Do I have a choice?')
