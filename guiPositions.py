from tkinter import *
from tkinter import ttk
import frameGrid
import frame4buttons
import dbPositions
from tkinter.messagebox import showerror, askyesno

def createMainFrame():
    mainFrame = ttk.Frame()
    mainFrame.Name = 'mainFrame'
    mainFrame.frame1 = createFramePositions(mainFrame)
    mainFrame.frame1.pack(fill=BOTH, expand=True)
    mainFrame.frame2 = createFrameButtons(mainFrame)
    mainFrame.frame2.pack(fill=X)
    return mainFrame

def createFramePositions(parent):
    frame1 = frameGrid.frameGrid(parent)
    frame1.addColumn(name='Id',text='Id',anchor=W,width=50,stretch=NO)
    frame1.addColumn(name='Name',text='Название',anchor=W,width=100,stretch=YES)
    frame1.buildGrid()    
    frame1.tree.bind('<ButtonRelease-1>', gridClick)
    idReset(frame1)
    frame1DataRefresh(frame1)
    return frame1

def createFrameButtons(parent):
    frame2 = frame4buttons.frame4Buttons(parent)
    frame2.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    frame2.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    frame2.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    frame2.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    return frame2

def gridClick(e):
    frame1 = e.widget.master
    idSet(frame1)

def idReset(frame1):
    frame1.itemId = None
    frame1.itemName = None

def idSet(frame1):
    curItem = frame1.tree.focus()
    if curItem:
        frame1.itemId = frame1.tree.item(curItem)['values'][0]
        frame1.itemName = frame1.tree.item(curItem)['values'][1]

def frame1DataRefresh(frame1):
    err, data = dbPositions.select()
    if not err:
        frame1.putData(data)
        idReset(frame1)

# ------- 4 buttons ----------
def btnAddPressed(e):
    mainFrame = e.widget.master.master
    idReset(mainFrame.frame1)
    openFrmNew("Новая позиция", mainFrame)

def btnEditPressed(e):
    frm = e.widget.master.master
    if frm.frame1.itemId != None:
        openFrmNew("Изменение позиции", frm)

def btnDeletePressed(e):
    frm = e.widget.master.master
    if frm.frame1.itemId != None:
        result = askyesno("Подтверждение действия", f"Удалить: {frm.frame1.itemName}?")
        if result:
            err = dbPositions.delete(frm.frame1.itemId)
            if err:
                showerror("Ошибка", err)
            else:
                frame1DataRefresh(frm.frame1)

def btnRefreshPressed(e):
    mainFrame = e.widget.master.master
    frame1DataRefresh(mainFrame.frame1)

# ------ edit form ----------
def openFrmNew(title, frmParent, id=None, name = None):
    frmNew = Toplevel()
    frmNew.title(title)
    frmNew.Name = 'frmNew'
    frmNew.geometry("400x300")
    frmNew.iconbitmap("nz.ico")
    frmNew.frmParent = frmParent

    frmNew.lbl = ttk.Label(frmNew, text="Название")
    frmNew.lbl.grid(row=0, column=0, padx=10, pady=10)

    frmNew.txtName = ttk.Entry(frmNew)
    frmNew.txtName.grid(row=0, column=1, padx=10, pady=10)
    if frmParent.frame1.itemName != None:
        frmNew.txtName.insert(0, frmParent.frame1.itemName)
    frmNew.txtName.focus()

    frmNew.btnSave = ttk.Button(frmNew, text="Сохранить")
    frmNew.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
    frmNew.btnSave.grid(row=1, column=1, padx=10, pady=10)

    frmNew.grab_set()

def btnSavePressed(e):
    frm = e.widget.master
    newName = frm.txtName.get()
    if frm.frmParent.frame1.itemId == None:
        err, newId = dbPositions.new(newName)
    else:
        err = dbPositions.update(frm.frmParent.frame1.itemId, newName)
    if err:
        showerror("Ошибка", err)
    else:
        frame1DataRefresh(frm.frmParent.frame1)
        frm.destroy()

# ------- test -------------
if __name__ == '__main__':
    root = Tk()
    root.Name = 'root'
    root.title("Position test")
    root.geometry("500x500")
    root.frameMain = createMainFrame()
    root.frameMain.pack(fill=BOTH, expand=True)
    root.mainloop()
