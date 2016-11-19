from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):
        e=Entry(self)
        b1 = Button(self, text="1")
        b2 = Button(self, text="2")
        b3 = Button(self, text="3")
        b4 = Button(self, text="4")
        b5 = Button(self, text="5")
        b6 = Button(self, text="6")
        b7 = Button(self, text="7")
        b8 = Button(self, text="8")
        b9 = Button(self, text="9")

        e.grid(row=0, column=0, columnspan=4, sticky=W+E)
        b1.grid(row=1,column=0)
        b2.grid(row=1,column=1)
        b3.grid(row=1,column=2)
        b4.grid(row=2,column=0)
        b5.grid(row=2,column=1)
        b6.grid(row=2,column=2)
        b7.grid(row=3,column=0)
        b8.grid(row=3,column=1)
        b9.grid(row=3,column=2)

        self.pack()

def main():

    root = Tk()
    app = Example(root)
    root.mainloop()  

if __name__ == '__main__':
    main() 
