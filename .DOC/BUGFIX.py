
SYMP:   print ( f"Checkbutton is checked - {param}" ) # Error Fail to convert params 
SOLU:   print ( "Checkbutton is checked - {param}" )

SYMP:   #Checkbox (c) fails to render
SYMP:   #Checkbox (c) Centered, not Left Justify

        fm = Frame(self, width=900, height=400)
        c = Checkbutton(fm, text="3D Library Call", onvalue="CheckBox_0 - Checked", offvalue="CheckBox_0 - Unchecked", variable=self.cb, command=self.IsChecked)
SOLU:
        fm = Frame(self, width=900, height=400)
        fm.grid(rows=90, columns=40)
        c = Checkbutton(fm, text="3D Library Call", onvalue="CheckBox_0 - Checked", offvalue="CheckBox_0 - Unchecked", variable=self.cb, command=self.IsChecked)
