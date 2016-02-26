from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def call_second_window(Frame):
        two = SecondWindow(master=root)
        two.mainloop()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello"

        self.hi_there["command"] = self.say_hi
        self.hi_there["command"] = self
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


class SecondWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.layout()


    def layout(self):
        self.Enter = Button(self)
        self.Enter["text"] = "OK"
        self.Enter.pack({"side": "left"})
        #self.hi_there["command"] = self.say_hi
        #self.hi_there["command"] = self
        #self.hi_there.pack({"side": "left"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})





root = Tk()


# tkinter has to initialize this way.
app = Application(master=root)
app.mainloop()

#two = SecondWindow()
#two.mainloop()

root.destroy()
#root2.destroy()






