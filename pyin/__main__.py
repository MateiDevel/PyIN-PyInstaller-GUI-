import customtkinter as ctk
from .gui import GUI

app = ctk.CTk()
app.title('PyInstaller-GUI')
app.geometry('597x353')
app.resizable(False, False)
gui = GUI(master=app)
app.mainloop()

