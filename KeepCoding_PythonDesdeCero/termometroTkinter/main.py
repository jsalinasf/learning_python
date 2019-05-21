from tkinter import *
from tkinter import ttk

class mainApp():

    def __init__(self):
        self.root = Tk()   
        self.root.geometry('640x480')
        self.root.title('Mi Ventana')
        self.root.configure(bg = 'lightgreen')

if __name__ == '__main__':
    app = mainApp()
    app.root.mainloop()


