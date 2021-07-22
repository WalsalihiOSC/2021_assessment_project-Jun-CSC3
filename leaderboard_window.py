import tkinter as tk

colour = "#FAE3C6"
root = tk.Tk()


help = tk.Frame(root)
help.grid(column=3, row=3)
tk.Label(help,text="fart",bg=colour).grid(row=1,column=1)
help["bg"] = colour


root.mainloop()

