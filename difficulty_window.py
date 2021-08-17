import tkinter as tk
from user_info import info

BG_colour = "#FAE3C6"

class difficultywindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        # Variable set to represent if the difficulty buttons have been pressed
        # 0 = no , 1 = yes
        self.click = 0

        # Frame within the window
        # This allows the background to be BG_colour otherwise the background colours
        # For the buttons will be white
        self.main_frame = tk.Frame(background=BG_colour)
        self.main_frame.grid(row=5,column=3)

        # Label for name and Entry 
        name_label = tk.Label(self.main_frame,text="What is your name",font=("Arial",30),bg=BG_colour)
        name_label.grid(row=2,column=2)
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.grid(row=3,column=2)

        #Difficulty label
        name_difficulty = tk.Label(self.main_frame,text="Choose your difficulty",font=("Arial",30),bg=BG_colour)
        name_difficulty.grid(row=4,column=2)
        # Easy and Hard buttons 
        easy_btn = tk.Button(self.main_frame,text="Easy",command=(self.click_easy),font=("Arial",25))
        hard_btn = tk.Button(self.main_frame,text="Hard",command=(self.click_hard),font=("Arial",25))
        easy_btn.grid(row=5,column=1)
        hard_btn.grid(row=5,column=3)
    # Name warning
    def error(self):
        self.error_label = tk.Label(self.main_frame,text="broo",bg=BG_colour,fg="#ff0000",font=("Arial",22))
        self.error_label.grid(row=3,column=3)

    def entryget(self):
        # Grabs any input from entry
        self.entry_text = self.name_entry.get()

    def entrycheck(self):
        self.entryget()
        if self.entry_text == "":
            # Checks if the input gathered from the entry is empty
            # If its an error, calls for the error function
            self.error()
        
        else:
            self.name_entry.delete(0,"end") 
            # Forgets/ Removes the error label beside the entry
            self.error_label.grid_forget()
            

 
    # Functions that sets the difficulty of the program
    def click_easy(self):
        info(difficulty="Easy")
        self.click = 1
        self.entrycheck()
    def click_hard(self):
        info(difficulty="Hard")
        self.click = 1
        self.entrycheck()

    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1440x900")
    root.configure(bg=BG_colour)
    root.resizable(False, False)

    difficultywindow()
    root.mainloop()
