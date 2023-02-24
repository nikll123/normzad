from tkinter import *
from tkinter import ttk
import dbPositions
from tkinter.messagebox import showerror, askyesno

def mainFrame(notebook):
    mainFrame = ttk.Frame(notebook)
    mainFrame.Name = 'mainFrame'
    idReset(mainFrame)
    notebook.add(mainFrame, text="Должности")

    mainFrame.subFrameTop = ttk.Frame(master=mainFrame, borderwidth=1, relief=SOLID)
    mainFrame.subFrameTop.Name = 'subFrameTop'
    mainFrame.subFrameTop.pack(fill=BOTH, expand=True)
    mainFrame.subFrameTop.columnconfigure(index=0, weight=1)
    mainFrame.subFrameTop.rowconfigure(index=0, weight=1)

    mainFrame.tree = ttk.Treeview(mainFrame.subFrameTop, column=("colId", "colName"), show='headings')
    mainFrame.tree.CurrentId = 0
    mainFrame.tree.column("colId", anchor=W, width=50, stretch=NO)
    mainFrame.tree.heading("colId", text="Id")
    mainFrame.tree.column("colName", anchor=W, width=100)
    mainFrame.tree.heading("colName", text="Название")
    mainFrame.tree.pack(fill=BOTH, expand=True, side=LEFT)

    mainFrame.scrollbar = ttk.Scrollbar(mainFrame.subFrameTop, orient=VERTICAL, command=mainFrame.tree.yview)
    mainFrame.tree.configure(yscroll=mainFrame.scrollbar.set)  
    mainFrame.tree.bind('<ButtonRelease-1>', selectItem)
    mainFrame.scrollbar.pack(anchor=E, expand=True, fill=Y)
        
    subFrameBottom = ttk.Frame(master=mainFrame)
    subFrameBottom.Name='subFrameBottom'
    subFrameBottom.pack(pady=5, fill=X)

    mainFrame.btnNew = ttk.Button(subFrameBottom, text="Добавить")
    mainFrame.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    mainFrame.btnNew.pack(side=LEFT)

    mainFrame.btnEdit = ttk.Button(subFrameBottom, text="Изменить")
    mainFrame.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    mainFrame.btnEdit.pack(side=LEFT)

    mainFrame.btnDelete = ttk.Button(subFrameBottom, text="Удалить")
    mainFrame.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    mainFrame.btnDelete.pack(side=LEFT)

    mainFrame.btnRefresh = ttk.Button(subFrameBottom, text="Обновить")
    mainFrame.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    mainFrame.btnRefresh.pack(side=LEFT)

    frmDataRefresh(mainFrame)

def selectItem(e):
    frame = e.widget.master.master
    curItem = frame.tree.focus()
    if curItem:
        frame.itemId = frame.tree.item(curItem)['values'][0]
        frame.itemName = frame.tree.item(curItem)['values'][1]

def frmDataRefresh(mainFrame):
    for c in mainFrame.tree.get_children(""):
        mainFrame.tree.delete(c)
    err, data = dbPositions.select()
    if not err:
        for row in data:
            mainFrame.tree.insert("", END, values=row)        
    idReset(mainFrame)
    

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

