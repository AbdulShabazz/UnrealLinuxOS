import tkinter as TK

class MainWindow(TK.Tk):
    def IsChecked(self):
        param = self.cb.get()
        print ( f"Checkbutton is checked - {param}" )
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title( "Unreal Engine - Level Designer - v1.0.0.0" )
        self.minsize(1000,500)
        self.cb = TK.StringVar()
        fm = TK.Frame(self, width=900, height=400)
        fm.grid(rows=90, columns=40)
        c = TK.Checkbutton(fm, text="3D Library Call", onvalue="CheckBox_0000 - 1", offvalue="CheckBox_0000 - 0", variable=self.cb, command=self.IsChecked)
        c.grid(row=0, column=0)
        c.deselect()
        c.pack()

MWH = MainWindow()
MWH.mainloop()