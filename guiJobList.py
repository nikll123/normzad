from tkinter import *
from tkinter import ttk
import blJobList as dlModule, guiTable, guiCommon, guiEditName
from tkinter.messagebox import showerror, askyesno

def createFrame(parent):
    cols = []
    cols.append({'name':'Id','text':'Id','anchor':W,'width':50,'stretch':NO})
    cols.append({'name':'Date','text':'Дата','anchor':W,'width':100,'stretch':YES})
    cols.append({'name':'TabNum','text':'Таб. №','anchor':W,'width':100,'stretch':YES})
    cols.append({'name':'FIO','text':'Ф.И.О.','anchor':W,'width':100,'stretch':YES})
    cols.append({'name':'Level','text':'Разряд','anchor':W,'width':100,'stretch':YES})
    cols.append({'name':'Position','text':'Должность','anchor':W,'width':100,'stretch':YES})
    cols.append({'name':'Task','text':'Задание','anchor':W,'width':100,'stretch':YES})
    cols.append({'name':'TimeJob','text':'Время','anchor':W,'width':100,'stretch':YES})
    dictJobList = guiTable.frameDictionary(parent, cols)
    dictJobList.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictJobList.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictJobList.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictJobList.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictJobList.Refresh = funcDataRefresh
    dictJobList.Refresh(dictJobList)
    return dictJobList

def btnAddPressed(e):
    frameDict = e.widget.master.master
    frm = guiEditTask(parent=frameDict)

def btnEditPressed(e):
    frameDict = e.widget.master.master
    id = frameDict.getSelectedId()
    frm = guiEditTask(parent=frameDict, rowId=id)
    
def btnDeletePressed(e):
    dictJobList = e.widget.master.master
    id = dictJobList.getSelectedId()
    if id != None:
        err, name = dlModule.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = dlModule.delete(id)
                if guiCommon.notError(err):
                    funcDataRefresh(dictJobList)

def btnRefreshPressed(e):
    dictJobList = e.widget.master.master
    funcDataRefresh(dictJobList)

def funcDataRefresh(dictJobList):
    err, data = dlModule.selectAll()
    if guiCommon.notError(err):
        dictJobList.dataPut(data)

class guiEditTask(guiEditName.frmEditName):
    Name='guiEditTask'
    def __init__(self, parent, rowId=None):
        super().__init__(parent, rowId)
        if self.rowId != None:
            err, name = dlModule.getName(self.rowId)
            if guiCommon.notError(err):
                self.setName(name)
    
    def btnSaveClicked(self, e):
        name = self.getName()
        if self.rowId ==None:
            err, newId = dlModule.insName(name)
        else:
            err = dlModule.updName(self.rowId, name)
        if guiCommon.notError(err):
            self.parent.Refresh(self.parent)
            self.destroy()

# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.formTk(title="joblist test")
    root.dictTasks = createFrame(root)
    root.dictTasks.pack(fill=BOTH, expand=True)
    root.mainloop()

