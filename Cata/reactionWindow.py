import tkinter as tk
from Cata.mainWindow4 import MainWindowFour
from Cata.utils import left_click_count



class ReactionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Click the button to start the timer", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Start Timer", command=self.start_timer)
        self.button.pack(pady=10)

        self.timer_count = 0
        self.result_text = ""

        self.root.bind("<Button-1>", left_click_count)


    def start_timer(self):
        self.button.pack_forget()  # Hide the button
        self.timer_count += 1
        self.label.config(text=f"Timer {self.timer_count}: Running...")

        self.root.after(5000, self.timer_completed)

    def timer_completed(self):
        self.label.config(text=f"Timer {self.timer_count}: Completed")
        self.button.pack()  # Show the button again

        if self.timer_count < 5:
            self.button.place(x=150, y=150)  # Reposition the button
        else:
            self.show_result()

    def show_result(self):
        self.result_text = "All timers completed!"
        result_label = tk.Label(self.root, text=self.result_text, font=("Arial", 16))
        result_label.pack(pady=20)

        button2 = tk.Button(self.root, text="Next", command=self.b1_clicked)
        button2.pack(pady=20)

    def b1_clicked(self):
        # Close the current window
        self.root.withdraw()
        root = tk.Toplevel(self.root)
        

        # Open the prompt window
        prompt_window = MainWindowFour(root,
                                       "Yes",
                                       "No",
                                       "???")
