import customtkinter as ctk 
from tkinter import filedialog
from pathlib import Path
from .execute import build

class GUI(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(fg_color='transparent')
        self.pack(fill='both', expand=True)
        
        self.path = None

        self.label = ctk.CTkLabel(self, text='PyInstaller-GUI')
        self.label.pack(pady=10)
        
        def select():
            path = filedialog.askopenfilename()
            ext = Path(path).suffix
            # print(ext)
            if path and ext == '.py':
                filelable.configure(text=path)
                buildbtn.pack(pady=30) # show btn
                self.path = path
            else:
                filelable.configure(text='This is not a python file...')
                buildbtn.grid_remove() # hide btn
                
        buildbtn = ctk.CTkButton(self, text='Build' , command=lambda: build(self.path)) # by default tk dosnt support func with parameters
                                                                                       
        filebtn = ctk.CTkButton(self, text='File', command=select)
        filebtn.pack(pady=20)
        
        filelable = ctk.CTkLabel(self, text='not selected')
        filelable.pack(pady=10)
        
