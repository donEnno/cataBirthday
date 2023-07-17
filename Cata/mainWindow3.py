import tkinter as tk
from tkinter import messagebox
from Cata.reactionWindow import ReactionWindow
from Cata.utils import ClickCounter, center_window, left_click_count


class MainWindowThree:
    def __init__(self, root, 
                 large_txt, 
                 sub_txt, 
                 button_txt):
        
        self.root = root
        self.root.geometry("400x150")

        center_window(root)

        # Configure the message box to span three columns and center the text
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)        

        # Create the message labelcd
        self.congrats = tk.Label(self.root, text=large_txt, font=("Arial", 16))
        self.congrats.grid(row=0, column=0, columnspan=3,  pady=0, padx=0, sticky="nsew")

        self.sub_congrats = tk.Label(self.root, text=sub_txt, font=("Arial", 12))
        self.sub_congrats.grid(row=1, column=1)

        # Create the buttons
        self.b1 = tk.Button(self.root, text=button_txt, command=self.b1_clicked)
        self.b1.grid(row=2, column=1)

        self.root.bind("<Button-1>", left_click_count)

    def b1_clicked(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        

        # Open the prompt window
        prompt_window = ReactionWindow(root)

    def b2_clicked(self):
        messagebox.showinfo("Button 2", "Button 2 clicked!")

    
