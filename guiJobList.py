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
    frm = guiEdit(parent=frameDict)

def btnEditPressed(e):
    frameDict = e.widget.master.master
    id = frameDict.getSelectedId()
    frm = guiEdit(parent=frameDict, rowId=id)
    
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

class guiEdit(guiCommon.subForm):
    Name='guiEditJob'
    def __init__(self, parent, rowId=None):
        super().__init__(parent, rowId)
        self.rowId = rowId

        self.txtDate = guiCommon.frametext(self, 'Дата')
        self.txtDate.pack()
        self.txtFio = guiCommon.frametext(self, 'Ф.И.О.')
        self.txtFio.pack()
        self.txtTabNom = guiCommon.frametext(self, 'Таб. №')
        self.txtTabNom.pack()
        self.txtTask = guiCommon.frametext(self, 'Задание')
        self.txtTask.pack()
        self.txtTime = guiCommon.frametext(self, 'Время')
        self.txtTime.pack()

        if self.rowId != None:
            err, name = dlModule.getName(self.rowId)
            if guiCommon.notError(err):
                pass
    
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
    root = guiCommon.form(title="joblist test")
    root.dictTasks = createFrame(root)
    root.dictTasks.pack(fill=BOTH, expand=True)
    root.mainloop()

