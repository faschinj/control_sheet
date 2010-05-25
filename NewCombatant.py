from Tkinter import *
     
class NewCombatant(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.data = {}
        self.makeWidgets()           # else only usable one way
        self.pack()
    def makeWidgets(self):
        Label(self, text='Character Name:')
        self.data['cname'] = Entry(self, relief=RIDGE)

        Label(self, text='Player Name:')
        self.data['pname'] = Entry(self, relief=RIDGE)

        Label(self, text='Reaction Modifier:')
        self.data['pname'] = Entry(self, relief=RIDGE)

        statFrame = Frame(self, bd=2, relief=SUNKEN)

        Label(statFrame, text='ST:').grid(row=0, column=0)
        def test_int(input):
            return input.isdigit() or len(input) == 0
        
        vcmd = (self.register(test_int), '%P')
        self.data['st'] = Entry(statFrame, validate="key", vcmd=vcmd, relief=RIDGE)
        self.data['st'].grid(row=0, column=1)

        Label(statFrame, text='DX:').grid(row=1, column=0)
        self.data['dx'] = Entry(statFrame, validate="key",vcmd=vcmd, relief=RIDGE)
        self.data['dx'].grid(row=1, column=1)

        Label(statFrame, text='IQ:').grid(row=2, column=0)
        self.data['iq'] = Entry(statFrame, validate="key",vcmd=vcmd, relief=RIDGE)
        self.data['iq'].grid(row=2, column=1)

        Label(statFrame, text='HT:').grid(row=3, column=0)
        self.data['ht'] = Entry(statFrame, validate="key",vcmd=vcmd, relief=RIDGE)
        self.data['ht'].grid(row=3, column=1)

        Label(statFrame, text='Will:').grid(row=1, column=2)
        self.data['will'] = Entry(statFrame, validate="key",vcmd=vcmd, relief=RIDGE)
        self.data['will'].grid(row=1, column=3)

        Label(statFrame, text='Per:').grid(row=2, column=2)
        self.data['per'] = Entry(statFrame, validate="key",vcmd=vcmd, relief=RIDGE)
        self.data['per'].grid(row=2, column=3)


        Label(statFrame, text='Basic Speed:').grid(row=4, column=0)
        self.data['spd'] = Entry(statFrame, relief=RIDGE)
        self.data['spd'].grid(row=4, column=1)

        Label(statFrame, text='Basic Move:').grid(row=4, column=2)
        self.data['mov'] = Entry(statFrame, relief=RIDGE)
        self.data['mov'].grid(row=4,column=3)
        Label(self, text='DR:')
        self.data['dr'] = Entry(statFrame, relief=RIDGE)

        Label(self, text='HP:')
        self.data['pname'] = Entry(self, relief=RIDGE)

        Button(self, text='Add')
        Button(self, text='Clear')
        Button(self, text='Cancel')
        statFrame.pack()
     
     
if __name__ == '__main__':NewCombatant().mainloop()
