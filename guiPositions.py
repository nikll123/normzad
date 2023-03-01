from tkinter import *
from tkinter import ttk
import blPositions, guiTable, guiCommon, guiEditName
from tkinter.messagebox import showerror, askyesno

def createFrame(parent):
    cols = []
    cols.append({'name':'Id','text':'Id','anchor':W,'width':50,'stretch':NO})
    cols.append({'name':'Name','text':'Название','anchor':W,'width':100,'stretch':YES})
    dictPositions = guiTable.frameDictionary(parent, cols)
    dictPositions.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictPositions.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictPositions.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictPositions.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictPositions.Refresh = funcDataRefresh
    dictPositions.Refresh(dictPositions)
    return dictPositions

def btnAddPressed(e):
    frameDict = e.widget.master.master
    guiEditPosition(parent=frameDict)

def btnEditPressed(e):
    frameDict = e.widget.master.master
    id = frameDict.getSelectedId()
    if id != None:
        guiEditPosition(parent=frameDict, rowId=id)
    
def btnDeletePressed(e):
    dictPositions = e.widget.master.master
    id = dictPositions.getSelectedId()
    if id != None:
        err, name = blPositions.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = blPositions.delete(id)
                if guiCommon.notError(err):
                    funcDataRefresh(dictPositions)

def btnRefreshPressed(e):
    dictPositions = e.widget.master.master
    funcDataRefresh(dictPositions)

def funcDataRefresh(dictPositions):
    err, data = blPositions.selectAll()
    if guiCommon.notError(err):
        dictPositions.dataPut(data)

class guiEditPosition(guiEditName.frmEditName):
    Name='guiEditPosition'
    def __init__(self, parent, rowId=None):
        super().__init__(parent, rowId)
        if self.rowId != None:
            err, name = blPositions.getName(self.rowId)
            if guiCommon.notError(err):
                self.setName(name)
    
    def btnSaveClicked(self, e):
        name = self.getName()
        if self.rowId ==None:
            err, newId = blPositions.insName(name)
        else:
            err = blPositions.updName(self.rowId, name)
        if guiCommon.notError(err):
            self.parent.Refresh(self.parent)
            self.destroy()


# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.form(title="Positions test")
    root.dictPositions = createFrame(root)
    root.dictPositions.pack(fill=BOTH, expand=True)
    root.mainloop()

