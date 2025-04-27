import customtkinter as ctk 
from tkinter import filedialog
from pathlib import Path
from .execute import build

class GUI(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(fg_color='transparent')
        self.pack(fill='both', expand=True)
        
        self.path = ''
        self.isNoconsole = ''
        self.name = ''
        
        self.label = ctk.CTkLabel(self, text='PyInstaller-GUI')
        self.label.pack(pady=10)
        
        noconsole_var = ctk.BooleanVar()
        name_var = ctk.BooleanVar()
        
        def checkboxes():
            def on():
                if noconsole_var.get():
                    # print('cheeky breeky iv danke')
                    self.isNoconsole = '--noconsole'
                else :
                    self.isNoconsole = ''   
            def name_on():
                if name_var.get():
                    print('Enter app name : \n')
                    self.name = '--name ' + input()
                    while self.name == '':
                        print('Please enter the app name: \n')
                        self.name = '--name ' + input() 
                else:
                    self.name = ''          
                
            noconsole = ctk.CTkCheckBox(self, text='No console', variable=noconsole_var, command=on)
            noconsole.pack(pady=23, padx=20)
            name = ctk.CTkCheckBox(self, text='Name', variable=name_var, command=name_on)
            name.pack(pady=0, padx=20)
            
        def select():
            path = filedialog.askopenfilename()
            ext = Path(path).suffix
            # print(ext)
            if path and ext == '.py' or ext == '.pyw':
                filelable.configure(text=path)
                buildbtn.pack(pady=30) # show btn
                checkboxes()
                self.path = path
            else:
                filelable.configure(text='This is not a python file...')
                buildbtn.grid_remove() # hide btn
                 
                
        buildbtn = ctk.CTkButton(self, text='Build' , command=lambda: build(self.path, self.isNoconsole, self.name)) # by default tk dosnt support func with parameters
                                                                                       
        filebtn = ctk.CTkButton(self, text='File', command=select)
        filebtn.pack(pady=20)
        
        filelable = ctk.CTkLabel(self, text='not selected')
        filelable.pack(pady=10)
        
