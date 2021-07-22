import tkinter as tk


bg_colour = "#FAE3C6"

class selection_window(tk.Frame):

    def click_easy():
        return("Easy")
    def hard():
        return("Hard")

    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        self.columnconfigure(0, weight=1)
        tk.Label(text="Pick your Game Theme",font=("Arial",30),bg=bg_colour).place(x=510,y=147)
        

    def __init__(self, *args):
            easy_btn = tk.Button(text="Easy",command=click_easy,font=("Arial",25))


    
################################################TEST
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    root["bg"] = "#FAE3C6"
    root.resizable(False, False)
    bruh = selection_window(root)
    print(bruh)
    root.mainloop()