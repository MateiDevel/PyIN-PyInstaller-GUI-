import customtkinter as ctk
from .gui import GUI

def main():
    app = ctk.CTk()
    app.title('PyInstaller-GUI')
    app.geometry('597x353')
    app.resizable(False, False)
    gui = GUI(master=app)
    app.mainloop()

if __name__ == '__main__':
    main()