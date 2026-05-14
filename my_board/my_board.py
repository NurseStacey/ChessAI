import tkinter as tk

class PlayingBoard(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.columnconfigure(0,weight=1)
        self.columnconfigure(9,weight=1) 
        self.rowconfigure(0,weight=1)      
        self.rowconfigure(9,weight=1)       

        tk.Label(self, text='hello').grid(row=5, column=5)

