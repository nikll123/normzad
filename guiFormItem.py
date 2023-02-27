from tkinter import *
from tkinter import ttk
import config

import guiCommon

class frmItem(guiCommon.formTopLevel):
    def __init__(self, master, title, table='', flds=[], id=config.dummyNum, frmName='frmItem'):
        super().__init__(master=master, title=title, frmName=frmName)
        self.frameEmpty1 = guiCommon.frameEmpty(self, height=30)
        self.frameEmpty1.pack()

        if table:
            for f in flds:
                pass


        self.txtName = guiCommon.frameLbltext(self, 'Нзвание')
        self.txtName.pack(side=TOP)

        self.frameEmpty2 = guiCommon.frameEmpty(self, height=30)
        self.frameEmpty2.pack()

        self.btnSave = Button(self, text='Сохранить')
        self.btnSave.bind('<ButtonRelease-1>', self.btnSaveClicked)
        self.btnSave.pack(side=TOP)
    
    def btnSaveClicked(self, e):
        print('btnSaveClicked')
    
    def setName(self, name):
        self.txtName.set(name)


if __name__ =='__main__' :
    root = Tk()
    frm = frmItem(root, 'item test', 'frmItemTest')
    frm.txtName.set('test data')
    frm.grab_set()
    frm.mainloop()
