from tkinter import *
from tkinter import ttk
import guiDictionary
import guiCommon
import Positions
from tkinter.messagebox import showerror, askyesno

def createFrame(parent):
    cols = []
    cols.append({'name':'Id','text':'Id','anchor':W,'width':50,'stretch':NO})
    cols.append({'name':'Name','text':'Название','anchor':W,'width':100,'stretch':YES})
    dictPositions = guiDictionary.frameDictionary(parent, cols)
    dictPositions.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictPositions.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictPositions.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictPositions.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    fgridDataRefresh(dictPositions)    
    return dictPositions

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
        err, name = Positions.getName(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {name}?")
            if result:
                err = Positions.delete(id)
                if guiCommon.notError(err):
                    fgridDataRefresh(dictPositions)

def btnRefreshPressed(e):
    dictPositions = e.widget.master.master
    fgridDataRefresh(dictPositions)

def fgridDataRefresh(dictPositions):
    err, data = Positions.selectAll()
    if guiCommon.notError(err):
        dictPositions.dataRefresh(data)



# ------- test -------------
if __name__ == '__main__':
    root = Tk()
    root.Name = 'root'
    root.title("Position test")
    root.geometry("400x500")
    root.dictPositions = createFrame(root)
    root.dictPositions.pack(fill=BOTH, expand=True)
    root.mainloop()
