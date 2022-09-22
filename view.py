from tkinter import *
import tkinter as tk


class FrameTop(Frame):
    def __init__(self, ws):
        Frame.__init__(self, ws, bg="#3498DB")
        self.ws = ws
        self.objCreate()

    def objCreate(self):
        self.text =Label(self, 
                    text='Sing In', 
                    foreground=('white'),
                    background=('#3498DB'),
                    font=('Arial', 22, 'bold'),
                    anchor="w", width=25)
        self.text.grid(row=0, column=0,padx = 5)
        



class FrameCenter(Frame):
    def __init__(self, ws):
        Frame.__init__(self, ws, bg="#D8DFE3",padx=68, pady=112)
        self.ws = ws
        self.objCreate()

    def objCreate(self):
        tk.Label(self, text='Username:  ',background=('#D8DFE3')).grid(column=0, row=1, sticky=tk.W)
        keyword = tk.Entry(self, width=15)
        keyword.focus()
        keyword.grid(column=1, row=1, padx = 5,sticky=tk.W)

        #self.text = Label(self, text="This label is on the frame ")
        #self.text.grid(row=0, column=0, padx=20, pady=20) # margins


class Win(Tk):

    def __init__(self, ws):
        Tk.__init__(self, ws)
        self.ws = ws
        self.title('SpeederRun')
        self.geometry('320x350+500+200')
        self.main()

    def main(self):
        self.w = FrameTop(self)
        self.w.pack()
        self.w = FrameCenter(self)
        self.w.pack()

if __name__=="__main__":
    app = Win(None)
    app.mainloop()