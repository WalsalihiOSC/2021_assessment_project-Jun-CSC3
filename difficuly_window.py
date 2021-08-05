import tkinter as tk
from user_info import info

BG_colour = "#FAE3C6"

class difficultywindow(tk.Frame):
    # Functions that sets the difficulty of the program
    def click_easy(self):
        info(name="Easy")
    def click_hard(self):
        info("Hard")

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        # Frame within the window
        # This allows the background to be BG_colour otherwise the background colours
        # For the buttons will be white
        main_frame = tk.Frame(background=BG_colour)
        main_frame.grid(column=5,row=3)
        name_label = tk.Label(main_frame,text="What is your name",font=("Arial",30),bg=BG_colour)
        name_label.grid(row=2,column=2)
        name_entry = tk.Entry()
        name_entry.grid(row=2,column=3)
        name_difficulty = tk.Label(main_frame,text="Choose your difficulty",font=("Arial",30),bg=BG_colour)
        name_difficulty.grid(row=2,column=4)
        # Easy and Hard buttons 
        easy_btn = tk.Button(main_frame,text="Easy",command=self.click_easy,font=("Arial",25))
        hard_btn = tk.Button(main_frame,text="Hard",command=self.click_hard,font=("Arial",25))
        easy_btn.grid(row=1,column=5)
        hard_btn.grid(row=3,column=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    root.configure(bg=BG_colour)
    difficultywindow()
    root.mainloop()
