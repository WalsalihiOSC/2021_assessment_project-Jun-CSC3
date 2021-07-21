import tkinter as tk

class start_window(tk.Frame):
    def __init__(self, *args, **kwargs):
        Frame = tk.Frame.__init__(self)
        Frame.__init__(self)
        title_frame = tk.Frame()
        title = tk.Label( text="Welcome to MathLearn",font=("Arial",30))
        title.pack(fill="none")
        header = tk.Label(text="Press start to begin",font=("Arial",25))
        header.pack(fill="none")
        start_btn = tk.Button(text="Start")
        start_btn.pack()

################################################TEST
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    start_window()

    root.mainloop()