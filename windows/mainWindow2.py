import tkinter as tk

import pygame
from windows.mainWindow3 import MainWindowThree
from windows.utils import center_window, left_click_count


class MainWindowTwo:
    def __init__(self, root, 
                 large_txt, 
                 sub_txt, 
                 button_txt):
        
        self.root = root
        self.root.geometry("400x150")
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
        self.congrats = tk.Label(self.root, text=large_txt, font=("Arial", 16))
        self.congrats.grid(row=0, column=0, columnspan=3,  pady=0, padx=0, sticky="nsew")

        self.sub_congrats = tk.Label(self.root, text=sub_txt, font=("Arial", 12))
        self.sub_congrats.grid(row=1, column=1)

        # Create the buttons
        self.song_button = tk.Button(self.root, text=button_txt, command=self.play_happy_birthday)
        self.song_button.grid(row=2, column=1)

        self.root.bind("<Button-1>", left_click_count)

    def play_happy_birthday(self):
        
        pygame.mixer.init()
        audio_file = "media/happy-birthday-155461.mp3"  # Replace this with the actual file path
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        self.next_button = tk.Button(self.root, text="That was so sweet.", command=self.button_click)
        self.next_button.grid(row=2, column=1)


    def button_click(self):
        pygame.mixer.music.stop()
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        

        # Open the prompt window
        next_window = MainWindowThree(root,
                                      "Did anyone tell you already that",
                                      "you are a special person?",
                                      "Not yet.")

