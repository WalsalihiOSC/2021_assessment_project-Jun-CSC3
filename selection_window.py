import tkinter as tk
from user_info import info
from start_window import start_window
bg_colour = "#FAE3C6"

class selection_window(tk.Frame):

    def click_easy(self):
        info("Easy")
    def click_hard(self):
        info("Hard")
    def test(self):
        
        start_window()

    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        tk.Label(text="Pick your Game Theme",font=("Arial",30),bg=bg_colour).place(x=510,y=147)
        

    def __init__(self, *args):
            easy_btn = tk.Button(text="Easy",command=self.test,font=("Arial",25))
            hard_btn = tk.Button(text="Hard",command=self.click_hard,font=("Arial",25))
            easy_btn.pack()
            hard_btn.pack()
    
################################################TEST
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    root["bg"] = "#FAE3C6"
    root.resizable(False, False)
    bruh = selection_window(root)


    root.mainloop()