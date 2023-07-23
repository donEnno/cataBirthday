import tkinter as tk
from Cata.mainWindow import MainWindow
from Cata.utils import ClickCounter, center_window

def on_left_click(event):
    ClickCounter.increment_count()


def main():
    print("Check check")

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("My Application")

    # Create an instance of the MainWindow class
    main_window = MainWindow(root,
                             large_txt="Happy Birthday Cata!",
                             sub_txt="Are you happy it's your special day?",
                             button_txt="Yes!!")
    
    center_window(root)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()