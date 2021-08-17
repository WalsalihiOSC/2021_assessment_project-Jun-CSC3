import tkinter as tk
from user_info import info
from start_window import start_window


BG_colour = "#FAE3C6"

class selection_window(tk.Frame):
    pass

    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    root.configure(bg=BG_colour)
    root.resizable(False, False)


    root.mainloop()