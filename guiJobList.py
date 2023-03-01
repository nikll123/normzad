from tkinter import *
from datetime import datetime
import blJobList as blModule, guiTable, guiCommon, blTasks, blWorkers
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
    dictTabel = guiTable.frameDictionary(parent, cols)
    dictTabel.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictTabel.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictTabel.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictTabel.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictTabel.Refresh = funcDataRefresh
    dictTabel.Refresh(dictTabel)
    return dictTabel

def btnAddPressed(e):
    frameDict = e.widget.master.master
    frm = guiEditTabel(parent=frameDict)

def btnEditPressed(e):
    frameDict = e.widget.master.master
    id = frameDict.getSelectedId()
    frm = guiEditTabel(parent=frameDict, rowId=id)
    
def btnDeletePressed(e):
    frameDict = e.widget.master.master
    id = frameDict.getSelectedId()
    if id != None:
        err, name = blModule.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = blModule.delete(id)
                if guiCommon.notError(err):
                    funcDataRefresh(frameDict)

def btnRefreshPressed(e):
    frameDict = e.widget.master.master
    funcDataRefresh(frameDict)

def funcDataRefresh(dictJobList):
    err, data = blModule.selectAll()
    if guiCommon.notError(err):
        dictJobList.dataPut(data)

class guiEditTabel(guiCommon.subForm):
    Name='guiEditTabel'
    def __init__(self, parent, rowId=None):
        super().__init__(parent, rowId)
        self.rowId = rowId

        self.txtDate = guiCommon.frametext(self, 'Дата')
        self.txtDate.pack()

        self.cmbFIO = guiCommon.frameCmb(self, 'Ф.И.О.')
        err, data = blWorkers.selectFioNumAll()
        if guiCommon.notError(err):
            self.cmbFIO.loadValues(data)
        self.cmbFIO.pack()

        self.cmbTask = guiCommon.frameCmb(self, 'Задание')
        err, data = blTasks.selectAll()
        if guiCommon.notError(err):
            self.cmbTask.loadValues(data)
        self.cmbTask.pack()

        self.txtTime = guiCommon.frametext(self, 'Время')
        self.txtTime.pack()

        if self.rowId != None:
            err, name = blModule.getName(self.rowId)
            if guiCommon.notError(err):
                pass
        
        if self.rowId==None:
            date = datetime.now()
            date = date.strftime("%d.%m.%Y")
            self.txtDate.set(date)
            self.txtTime.set('8')
        else:
            err, data = blModule.getJobListRow(self.rowId)
            # guiCommon.notError(err):
            #     data


        self.btnSave = Button(self, text='Сохранить')
        self.btnSave.bind('<ButtonRelease-1>', self.btnSaveClicked)
        self.btnSave.pack(side=TOP)

    
    def btnSaveClicked(self, e):
        name = self.getName()
        if self.rowId ==None:
            err, newId = blModule.insName(name)
        else:
            err = blModule.updName(self.rowId, name)
        if guiCommon.notError(err):
            self.parent.Refresh(self.parent)
            self.destroy()

# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.form(title="joblist test")
    root.dictTasks = createFrame(root)
    root.dictTasks.pack(fill=BOTH, expand=True)
    root.mainloop()

