import tkinter as tk

import pygame
from windows.utils import QuestionScore, center_window, left_click_count


class LastWindow:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("650x200")
        self.root.title("It's your birthday")
        
        self.clicked = False

        center_window(root)

        # Create the message label
        self.summary_label = tk.Label(self.root, text="Happy Birthday Cata <3", font=("Arial", 16))
        self.summary_label.pack(pady=15)

        self.result_label = tk.Label(self.root, text=f"You are my sunshine and \n I love you a lot!", 
                                     font=("Arial", 14))
        self.result_label.pack(pady=15)

        # Create the buttons
        self.b1 = tk.Button(self.root, text="Thank you!", command=self.play_happy_birthday)
        self.b1.pack(pady=15)

        self.root.bind("<Button-1>", left_click_count)

    def play_happy_birthday(self):
        
        pygame.mixer.init()
        audio_file = "media/luisi_und_enno.mp3"  # Replace this with the actual file path
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    
    def button_click(self):
        self.root.destroy()
    
