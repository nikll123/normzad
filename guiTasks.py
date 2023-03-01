from tkinter import *
from tkinter import ttk
import blTasks, guiTable, guiCommon, guiEditName
from tkinter.messagebox import showerror, askyesno

def createFrame(parent):
    cols = []
    cols.append({'name':'Id','text':'Id','anchor':W,'width':50,'stretch':NO})
    cols.append({'name':'Name','text':'Название','anchor':W,'width':100,'stretch':YES})
    dictTasks = guiTable.frameDictionary(parent, cols)
    dictTasks.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictTasks.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictTasks.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictTasks.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictTasks.Refresh = funcDataRefresh
    dictTasks.Refresh(dictTasks)
    return dictTasks

def btnAddPressed(e):
    frameDict = e.widget.master.master
    frm = guiEditTask(parent=frameDict)

def btnEditPressed(e):
    frameDict = e.widget.master.master
    id = frameDict.getSelectedId()
    frm = guiEditTask(parent=frameDict, rowId=id)
    
def btnDeletePressed(e):
    dictTasks = e.widget.master.master
    id = dictTasks.getSelectedId()
    if id != None:
        err, name = blTasks.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = blTasks.delete(id)
                if guiCommon.notError(err):
                    funcDataRefresh(dictTasks)

def btnRefreshPressed(e):
    dictTasks = e.widget.master.master
    funcDataRefresh(dictTasks)

def funcDataRefresh(dictTasks):
    err, data = blTasks.selectAll()
    if guiCommon.notError(err):
        dictTasks.dataPut(data)

class guiEditTask(guiEditName.frmEditName):
    Name='guiEditTask'
    def __init__(self, parent, rowId=None):
        super().__init__(parent, rowId)
        if self.rowId != None:
            err, name = blTasks.getName(self.rowId)
            if guiCommon.notError(err):
                self.setName(name)
    
    def btnSaveClicked(self, e):
        name = self.getName()
        if self.rowId ==None:
            err, newId = blTasks.insName(name)
        else:
            err = blTasks.updName(self.rowId, name)
        if guiCommon.notError(err):
            self.parent.Refresh(self.parent)
            self.destroy()

# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.formTk(title="Tasks test")
    root.dictTasks = createFrame(root)
    root.dictTasks.pack(fill=BOTH, expand=True)
    root.mainloop()

