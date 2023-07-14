import tkinter as tk

class PopupWindow:
    def run(self):
        # Create a pop-up window to show when the click count reaches 25
        popup_root = tk.Toplevel()
        popup_root.title("Popup Window")
        popup_root.geometry("300x200")
        
        center_window(popup_root, almost=True)

        popup_label = tk.Label(popup_root, text="Click Count Reached 25!", font=("Arial", 16))
        popup_label.pack(pady=50)

        popup_root.mainloop()

class ClickCounter:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

def left_click_count(event):
    ClickCounter.increment_count()
    print(ClickCounter.count)

    if ClickCounter.count == 25:
        # Open a pop-up window when the click count reaches 25
        popup_window = PopupWindow()
        popup_window.run()

def center_window(root, almost=False):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates for centering the window
    x = int((screen_width - root.winfo_reqwidth()) / 2)
    y = int((screen_height - root.winfo_reqheight()) / 2)

    if almost:
        x += 25
        y += 25

    # Set the window's position
    root.geometry(f"+{x}+{y}")
