from tkinter import *
from tkinter import ttk
import frameGrid
import frame4buttons
import dbPositions
from tkinter.messagebox import showerror, askyesno

def createFramePositions(parent):
    grid1 = frameGrid.frameGrid('grdPos')
    grid1.addColumn(name='Id',text='Id',anchor=W,width=50,stretch=NO)
    grid1.addColumn(name='Name',text='Название',anchor=W,width=100,stretch=YES)
    grid1.buildGrid()    
    frmDataRefresh(grid1)
    return grid1

def createFrameButtons():
    frame2 = frame4buttons()
    frame2.Name='subFrameBottom'
    # frame2.pack(pady=5, fill=X)

    frame2.btnNew = ttk.Button(frame2, text="Добавить")
    frame2.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    frame2.btnNew.pack(side=LEFT, padx=10, pady=10)

    frame2.btnEdit = ttk.Button(frame2, text="Изменить")
    frame2.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    frame2.btnEdit.pack(side=LEFT, padx=10, pady=10)

    frame2.btnDelete = ttk.Button(frame2, text="Удалить")
    frame2.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    frame2.btnDelete.pack(side=LEFT, padx=10, pady=10)

    frame2.btnRefresh = ttk.Button(frame2, text="Обновить")
    frame2.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    frame2.btnRefresh.pack(side=LEFT, padx=10, pady=10)

    return frame2



def selectItem(e):
    frame = e.widget.master.master
    curItem = frame.tree.focus()
    if curItem:
        frame.itemId = frame.tree.item(curItem)['values'][0]
        frame.itemName = frame.tree.item(curItem)['values'][1]

def frmDataRefresh(grid):
    err, data = dbPositions.select()
    if not err:
        grid.putData(data)

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
        err, newId = dbPositions.new(newName)
    else:
        err = dbPositions.update(frm.id, newName)
    if err:
        showerror("Ошибка", err)
    else:
        frmDataRefresh(frm.mainFrame)
        frm.destroy()

def btnAddPressed(e):
    mainFrame = e.widget.master.master
    idReset(mainFrame)
    openFrmNew("Новая позиция", mainFrame)

def btnEditPressed(e):
    mainFrame = e.widget.master.master
    if mainFrame.itemId != None:
        openFrmNew("Изменение позиции", mainFrame)

def btnDeletePressed(e):
    mainFrame = e.widget.master.master
    if mainFrame.itemId != None:
        result = askyesno("Подтверждение действия", f"Удалить: {mainFrame.itemName}?")
        if result:
            err = dbPositions.delete(mainFrame.itemId)
            if err:
                showerror("Ошибка", err)
            else:
                frmDataRefresh(mainFrame)

def idReset(mainFrame):
    mainFrame.itemId = None
    mainFrame.itemName = None

def btnRefreshPressed(e):
    frm = e.widget.master.master
    frmDataRefresh(frm)


if __name__ == '__main__':
    root = Tk()
    root.title("Position test")
    root.geometry("400x500")
    root.frame1 = createFramePositions(root)
    root.frame1.pack(fill=BOTH, expand=True)
    # root.frame2 = createFrameButtons()
    # root.frame2.pack(fill=X)
    root.mainloop()
