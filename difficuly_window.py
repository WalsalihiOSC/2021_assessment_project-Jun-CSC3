import tkinter as tk
from user_info import info

BG_colour = "#FAE3C6"

class difficultywindow(tk.Frame):
    def click_easy(self):
        info("Easy")
    def click_hard(self):
        info("Hard")

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        main_frame = tk.Frame()
        main_frame.pack()
        tk.Label(main_frame,text="Pick your Game Theme",font=("Arial",30),bg=BG_colour).pack()
        easy_btn = tk.Button(main_frame,text="Easy",command=self.click_easy,font=("Arial",25))
        hard_btn = tk.Button(main_frame,text="Hard",command=self.click_hard,font=("Arial",25))
        easy_btn.pack()
        hard_btn.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    difficultywindow()
    root.mainloop()
