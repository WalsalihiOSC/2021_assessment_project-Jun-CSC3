import tkinter as tk
#from start_window import start_window
#from selection_window import selection_window

class StartPage(tk.Frame):
    def __init__(self,*args, **kwargs):
        self.title("MathLearn")
        self.geometry("1024x600")
    def Showpage(self,Frame):
        pass

class NextPage(tk):
    pass

if __name__ == "__main__":
    root = tk.Tk()
    StartPage(root)
    root.mainloop()