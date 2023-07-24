import tkinter as tk
from windows.mainWindow5 import MainWindowFive
from windows.utils import center_window, left_click_count


class JanWindow:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1200x300")
        self.root.title("It's your birthday")

        center_window(root)

        # Configure the message box to span three columns and center the text
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)        

        # Create the message labelcd
        self.congrats = tk.Label(self.root, text='Frohe Ostern', font=("Arial", 16))
        self.congrats.grid(row=0, column=0, columnspan=3,  pady=0, padx=0, sticky="nsew")

        self.sub_congrats = tk.Label(self.root, text='Von JPL dem Unausdribbelbarendribbeldribbler', font=("Arial", 32))
        self.sub_congrats.grid(row=1, column=1)

        # Create the buttons
        self.button = tk.Button(self.root, text='Ok.', command=self.button_click)
        self.button.grid(row=2, column=1)

        self.root.bind("<Button-1>", left_click_count)

    def button_click(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        

        # Open the prompt window
        next_window = MainWindowFive(root, 
                                      "Okay.....",
                                      "Something unexpected happend there. \n Let's continue with a few quiz questions.",
                                      "Ok")
        