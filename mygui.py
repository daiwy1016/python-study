from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.hellolabel=Label(self,text='hello world!')
        self.hellolabel.pack()
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.quitbutton=Button(self,text='quit',command=self.hello)
        self.quitbutton.pack()
        self.quitbutton2=Button(self,text='quit',command=self.quit)
        self.quitbutton2.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('M','HELLO %s'%name)

app=Application()
app.master.title('hello')

app.mainloop()
        
    