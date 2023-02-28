from tkinter import *
from tkinter import ttk
import blDepartments, guiDictionary, guiCommon, guiEditName
from tkinter.messagebox import showerror, askyesno

def createFrame(parent):
    cols = []
    cols.append({'name':'Id','text':'Id','anchor':W,'width':50,'stretch':NO})
    cols.append({'name':'Name','text':'Название','anchor':W,'width':100,'stretch':YES})
    dictDepartatmens = guiDictionary.frameDictionary(parent, cols)
    dictDepartatmens.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictDepartatmens.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictDepartatmens.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictDepartatmens.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictDepartatmens.Refresh = funcDataRefresh
    dictDepartatmens.Refresh(dictDepartatmens)
    return dictDepartatmens

def btnAddPressed(e):
    parent = e.widget.master.master.master
    frm = guiEditDepartment(parent=parent)

def btnEditPressed(e):
    dictDepartatmens = e.widget.master.master
    id = dictDepartatmens.getSelectedId()
    parent = e.widget.master.master.master
    frm = guiEditDepartment(parent=parent, rowId=id)
    
def btnDeletePressed(e):
    dictDepartatmens = e.widget.master.master
    id = dictDepartatmens.getSelectedId()
    if id != None:
        err, name = blDepartments.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = blDepartments.delete(id)
                if guiCommon.notError(err):
                    funcDataRefresh(dictDepartatmens)

def btnRefreshPressed(e):
    dictDepartatmens = e.widget.master.master
    funcDataRefresh(dictDepartatmens)

def funcDataRefresh(dictDepartatmens):
    err, data = blDepartments.selectAll()
    if guiCommon.notError(err):
        dictDepartatmens.dataPut(data)

class guiEditDepartment(guiEditName.frmEditName):
    Name='guiEditDepartment'
    def __init__(self, parent, rowId=None):
        super().__init__(parent, rowId)
        if self.rowId != None:
            err, name = blDepartments.getName(self.rowId)
            if guiCommon.notError(err):
                self.setName(name)
    
    def btnSaveClicked(self, e):
        name = self.getName()
        if self.rowId ==None:
            err, newId = blDepartments.insName(name)
        else:
            err = blDepartments.updName(self.rowId, name)
        if guiCommon.notError(err):
            self.parent.dictDepartments.Refresh(self.parent.dictDepartments)
            self.destroy()


# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.formTk(title="Departments test")
    root.dictDepartments = createFrame(root)
    root.dictDepartments.pack(fill=BOTH, expand=True)
    root.mainloop()

