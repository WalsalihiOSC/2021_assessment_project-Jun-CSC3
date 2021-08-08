import tkinter as tk
from user_info import info

class game_window(tk.Frame):
    def __init__(self,*args,**kwargs):
        diff = info.getdiff()
        