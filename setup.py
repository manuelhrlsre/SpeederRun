import tkinter as tk
from tkinter import *
import sys
from tkinter.tix import COLUMN, ROW
from tkinter import ttk
from tkinter import messagebox


def hacer_click():
    messagebox.showinfo("Alert", "Hello World")

def create_frame(container):
    frameUNO = ttk.Frame(container) # ,height=300, width=300, bg='#ccffcc')
    ttk.Label(frameUNO, text='Sing In',font=('Arial', 22, 'bold'),foreground=('white'), background=('#3498DB')).grid(column=0, row=0, sticky=tk.W)
    return frameUNO

def create_input_frame(container):

    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    ttk.Label(frame, text='').grid(column=0, row=1, sticky=tk.W)
    ttk.Label(frame, text='').grid(column=0, row=2, sticky=tk.W)
    ttk.Label(frame, text='').grid(column=0, row=6, sticky=tk.W)

    ttk.Label(frame, text='Username:  ').grid(column=0, row=3, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=3, sticky=tk.W)

    
    ttk.Label(frame, text='Password:  ').grid(column=0, row=4, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=4, sticky=tk.W)

    
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Remember me',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=1, row=5, sticky=tk.W)


    
    ttk.Button(frame, text='Login',command=hacer_click).grid(column=1, row=7)
    

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame

class WindowPpal:
    def __init__(self, tkWindow):
        self.wind = tkWindow
        self.wind.title('SpeederRun')
        self.wind.geometry('350x450+500+200')

        usernameLabel = Label(tkWindow, text="User Name").grid(row=2, column=0)
        username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=username).grid(row=2, column=1)  

        passwordLabel = Label(tkWindow,text="Password").grid(row=4, column=0)  
        password = StringVar()
        passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

        boton = Button(tkWindow, text="OK!", command=hacer_click, bg='palegreen2', font=('Arial', 11, 'bold')) 
        boton.grid(column=1, row=4)

class Window2:
    def __init__(self, tkWindow): #create buttons,entries,etc
        pass

    def button_method(self):
        #run this when button click to close window
        self.master.destroy()

def main(): #run mianloop 
    winmain = Tk()
    winmain.title('SpeederRun')
    # ok - winmain['background']='#E0E0EE'
    winmain.config(bg='#f7ef38')
    winmain.resizable(False, False)

    winmain.columnconfigure(0, weight=4)
    winmain.columnconfigure(1, weight=4)
    winmain.columnconfigure(2, weight=4)
    #winmain.columnconfigure(1, weight=1)


    winmain.geometry('320x350+500+200')

    input_frameUNO = create_frame(winmain)
    input_frameUNO.grid(column=0, row=0)

    input_frame = create_input_frame(winmain)
    input_frame.grid(column=0, row=1)

    winmain.mainloop()

if __name__ == '__main__':
    main()