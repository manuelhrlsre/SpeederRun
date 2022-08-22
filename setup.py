import tkinter as tk
from tkinter import *
import sys
from tkinter.tix import COLUMN, ROW


def hacer_click():
    try:
       pass
    except ValueError:
       pass



class WindowPpal:
    def __init__(self, tkWindow):
        self.wind = tkWindow
        self.wind.title('SpeederRun')
        self.wind.geometry('350x450+500+200')

        usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

        passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

        boton = Button(tkWindow, text="OK!", command=hacer_click)
        boton.grid(column=1, row=4)

class Window2:
    def __init__(self, tkWindow): #create buttons,entries,etc
        pass

    def button_method(self):
        #run this when button click to close window
        self.master.destroy()

def main(): #run mianloop 
    winmain = Tk()
    winmain.resizable(False, False)  
    app = WindowPpal(winmain)
    winmain.mainloop()

if __name__ == '__main__':
    main()