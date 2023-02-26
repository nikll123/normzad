from tkinter import *
from tkinter import ttk
import Departments, guiDictionary, guiCommon, guiFormItem
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
    fgridDataRefresh(dictDepartatmens)    
    return dictDepartatmens

def btnAddPressed(e):
    parent = e.widget.master.master.master
    frm = guiFormItem.frmItem(parent, 'добавить', 'frmDepItem')
    frm.grab_set()

def btnEditPressed(e):
    dictDepartatmens = e.widget.master.master
    id = dictDepartatmens.getSelectedId()
    if id != None:
        err, name = Departments.getName(id)
        if guiCommon.notError(err):
            parent = e.widget.master.master.master
            frm = guiFormItem.frmItem(parent, 'Измененить', 'frmDepItem')
            frm.setName(name)
            frm.grab_set()

def btnDeletePressed(e):
    dictDepartatmens = e.widget.master.master
    id = dictDepartatmens.getSelectedId()
    if id != None:
        err, name = Departments.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = Departments.delete(id)
                if guiCommon.notError(err):
                    fgridDataRefresh(dictDepartatmens)

def btnRefreshPressed(e):
    dictDepartatmens = e.widget.master.master
    fgridDataRefresh(dictDepartatmens)

def fgridDataRefresh(dictDepartatmens):
    err, data = Departments.selectAll()
    if guiCommon.notError(err):
        dictDepartatmens.dataRefresh(data)

def openFrmNew(title, parent, id=None):
    frmNew = guiCommon.formTopLevel(parent, title=title, frmName='frmNewDep')
    frmNew.id = parent.itemId
    if id != None:
        err, name = Departments.getName(id)
        if guiCommon.notError(err):
            frmNew.txtName = name
    frmNew.grab_set()

# def btnSavePressed(e):
#     frm = e.widget.master
#     newName = frm.txtName.get()
#     if frm.id == None:
#         err, newId = dbDepartments.new(newName)
#     else:
#         err = dbDepartments.update(frm.id, newName)
#     if err:
#         showerror("Ошибка", err)
#     else:
#         frmDataRefresh(frm.mainFrame)
#         frm.destroy()

# def btnAddPressed(e):
#     mainFrame = e.widget.master.master
#     idReset(mainFrame)
#     openFrmNew("Новое подразделение", mainFrame)

# def btnEditPressed(e):
#     mainFrame = e.widget.master.master
#     if mainFrame.itemId != None:
#         openFrmNew("Изменение подразделения", mainFrame)

# def btnDeletePressed(e):
#     mainFrame = e.widget.master.master
#     if mainFrame.itemId != None:
#         result = askyesno("Подтверждение действия", f"Удалить: {mainFrame.itemName}?")
#         if result:
#             err = dbDepartments.delete(mainFrame.itemId)
#             if err:
#                 showerror("Ошибка", err)
#             else:
#                 frmDataRefresh(mainFrame)

# def idReset(mainFrame):
#     mainFrame.itemId = None
#     mainFrame.itemName = None

# def btnRefreshPressed(e):
#     frm = e.widget.master.master
#     frmDataRefresh(frm)


# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.formTk(frmName='root', title="Departments test")
    root.dictDepartments = createFrame(root)
    root.dictDepartments.pack(fill=BOTH, expand=True)
    root.mainloop()

