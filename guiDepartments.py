from tkinter import *
from tkinter import ttk
import Departments, guiDictionary, guiCommon
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
    pass

def btnEditPressed(e):
    dictPositions = e.widget.master.master
    id = dictPositions.getSelectedId()
    if id != None:
        # openFrmNew("Изменение позиции", frm)
        print('openFrmNew')

def btnDeletePressed(e):
    dictPositions = e.widget.master.master
    id = dictPositions.getSelectedId()
    if id != None:
        err, name = Departments.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = Departments.delete(id)
                if guiCommon.notError(err):
                    fgridDataRefresh(dictPositions)

def btnRefreshPressed(e):
    dictPositions = e.widget.master.master
    fgridDataRefresh(dictPositions)

def fgridDataRefresh(dictPositions):
    err, data = Departments.selectAll()
    if guiCommon.notError(err):
        dictPositions.dataRefresh(data)



def openFrmNew(title, mainFrame, id=None, name = None):
    frmNew = Toplevel()
    frmNew.title(title)
    frmNew.Name = 'frmNew'
    frmNew.geometry("400x300")
    frmNew.iconbitmap("nz.ico")
    frmNew.mainFrame = mainFrame
    frmNew.id = mainFrame.itemId
    name = mainFrame.itemName

    frmNew.lbl = ttk.Label(frmNew, text="Название")
    frmNew.lbl.grid(row=0, column=0, padx=10, pady=10)

    frmNew.txtName = ttk.Entry(frmNew)
    frmNew.txtName.grid(row=0, column=1, padx=10, pady=10)
    if name != None:
        frmNew.txtName.insert(0, name)
    frmNew.txtName.focus()

    frmNew.btnSave = ttk.Button(frmNew, text="Сохранить")
    frmNew.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
    frmNew.btnSave.grid(row=1, column=1, padx=10, pady=10)

    frmNew.grab_set()

def btnSavePressed(e):
    frm = e.widget.master
    newName = frm.txtName.get()
    if frm.id == None:
        err, newId = dbDepartments.new(newName)
    else:
        err = dbDepartments.update(frm.id, newName)
    if err:
        showerror("Ошибка", err)
    else:
        frmDataRefresh(frm.mainFrame)
        frm.destroy()

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
    root = Tk()
    root.Name = 'root'
    root.title("Departments test")
    root.geometry("400x500")
    root.dictDepartments = createFrame(root)
    root.dictDepartments.pack(fill=BOTH, expand=True)
    root.mainloop()

