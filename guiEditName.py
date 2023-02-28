from tkinter import *
from tkinter import ttk
import blDepartments

import guiCommon

class frmEditName(guiCommon.formTopLevel):
    Name = 'frmEditName'
    def __init__(self, parent, rowId):
        if rowId == None:
            title = 'Добавить'
        else:
            title = 'Изменить'
        super().__init__(master=parent, title=title)
        self.rowId = rowId
        self.parent=parent
        self.frameEmpty1 = guiCommon.frameEmpty(self, height=30)
        self.frameEmpty1.pack()

        self.txtName = guiCommon.frameLbltext(self, 'Название')
        self.txtName.pack(side=TOP)
                    
        self.frameEmpty2 = guiCommon.frameEmpty(self, height=30)
        self.frameEmpty2.pack()

        self.btnSave = Button(self, text='Сохранить')
        self.btnSave.bind('<ButtonRelease-1>', self.btnSaveClicked)
        self.btnSave.pack(side=TOP)
        self.grab_set()
    
    def btnSaveClicked(self, e):
        self.destroy()

    def setName(self, name):
        self.txtName.set(name)

    def getName(self):
        return self.txtName.get()



if __name__ =='__main__' :
    root = Tk()
    frm = frmEditName(root, 'item test')
    print(frm.Name)
    frm.mainloop()
