from tkinter import *
from tkinter import ttk
import dbDepartments
from tkinter.messagebox import showerror, askyesno

def frameDepartments(notebook):
    frameDep = ttk.Frame(notebook)
    notebook.add(frameDep, text="Подразделения")

    subFrameTop = ttk.Frame(frameDep, borderwidth=1, relief=SOLID)
    subFrameBottom = ttk.Frame(frameDep)
    subFrameTop.pack()
    subFrameBottom.pack()

    subFrameTop.pack(fill=BOTH, expand=True)
    subFrameTop.columnconfigure(index=0, weight=1)
    subFrameTop.rowconfigure(index=0, weight=1)

    subFrameTop.tree = ttk.Treeview(subFrameTop, column=("colId", "colName"), show='headings')
    subFrameTop.tree.CurrentId = 0
    subFrameTop.tree.column("colId", anchor=W, width=40)
    subFrameTop.tree.heading("colId", text="Id")
    subFrameTop.tree.column("colName", anchor=W, width=100)
    subFrameTop.tree.heading("colName", text="Название")
    # frameDep.tree.grid(row=0, column=0)
    subFrameTop.tree.pack(fill=BOTH, expand=True, side=LEFT)

    subFrameTop.scrollbar = ttk.Scrollbar(subFrameTop, orient=VERTICAL, command=subFrameTop.tree.yview)
    subFrameTop.tree.configure(yscroll=subFrameTop.scrollbar.set)  
    # scrollbar.grid(row=0, column=1, sticky="ns")
    # frameDep.scrollbar.pack(fill=Y, expand=True, anchor=E)
    subFrameTop.scrollbar.pack(anchor=E, expand=True, fill=Y)

    subFrameTop.btnSave = ttk.Button(subFrameBottom, text="Сохранить")
    # frameDep.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
    subFrameTop.btnSave.pack()

    

    frmDataRefresh(subFrameTop)

def frmDataRefresh(frame):
    for c in frame.tree.get_children(""):
        frame.tree.delete(c)
    err, data = dbDepartments.select()
    if not err:
        for row in data:
            frame.tree.insert("", END, values=row)        


# def btnAddPressed(e):
#     parent = e.widget.master
#     showFormItem("Новое подразделение", parent)

# def showFormItem(title, parent, id=None, name = None):
#     frmNewDepartment = Toplevel()
#     frmNewDepartment.title(title)
#     frmNewDepartment.geometry("400x300")
#     frmNewDepartment.iconbitmap("nz.ico")
#     frmNewDepartment.parent = parent
#     frmNewDepartment.id = id

#     frmNewDepartment.lbl = ttk.Label(frmNewDepartment, text="Название")
#     frmNewDepartment.lbl.grid(row=0,column=0,padx=10,pady=10)

#     frmNewDepartment.txtName = ttk.Entry(frmNewDepartment)
#     frmNewDepartment.txtName.grid(row=0,column=1,padx=10,pady=10)
#     if name != None:
#         frmNewDepartment.txtName.insert(0, name)
#     frmNewDepartment.txtName.focus()

#     frmNewDepartment.btnSave = ttk.Button(frmNewDepartment, text="Сохранить")
#     frmNewDepartment.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
#     frmNewDepartment.btnSave.grid(row=1, column=1, padx=10, pady=10)

#     # frmNewDepartment.wm_transient(root)
#     # frmNewDepartment.attributes('-topmost',True)
#     frmNewDepartment.grab_set()

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
#         frmDataRefresh(frm.parent)
#         frm.destroy()

# def btnEditPressed(e):
#     frm = e.widget.master
#     id = frmGetTreeCurrentId(frm)
#     if id != None:
#         name = frmGetTreeCurrentName(frm)
#         showFormItem("Изменение подразделения", frm, id, name)

# def btnDelPressed(e):
#     frm = e.widget.master
#     id = frmGetTreeCurrentId(frm)
#     if id != None:
#         name = frmGetTreeCurrentName(frm)
#         result = askyesno("Подтверждение действия", f"Удалить: {name}?")
#         if result:
#             err = dbDepartments.delete(id)
#             if err:
#                 showerror("Ошибка", err)
#             else:
#                 frmDataRefresh(frm)

# def frmGetTreeCurrentId(frm):
#     return _frmGetTreeCurrentData(frm, 0)

# def frmGetTreeCurrentName(frm):
#     return _frmGetTreeCurrentData(frm, 1)

# def _frmGetTreeCurrentData(frm, index):
#     val = None
#     curItem = frm.tree.focus()
#     if curItem:
#         val = frm.tree.item(curItem)['values'][index]
#     # print(val)
#     return val

# def btnRefreshPressed(e):
#     frm = e.widget.master
#     frmDataRefresh(frm)


# def openFormDepartments():
#     # frmMain = e.widget.master
#     frmDepartments = Tk()
#     frmDepartments.title("Подразделения")
#     frmDepartments.geometry("400x350")
#     frmDepartments.iconbitmap("nz.ico")
#     # frmDepartments.datarefresh = frmRefresh
#     frmDepartments.resizable(False, False)
#     # x = frmMain.winfo_x()
#     # y = frmMain.winfo_y()
#     # frmDepartments.geometry("+%d+%d" %(x+50,y+50))
#     # frmDepartments.wm_transient(frmMain)
#     frmDepartments.attributes('-topmost',True)

#     frmDepartments.tree = ttk.Treeview(frmDepartments, column=("colId", "colName"), show='headings')
#     frmDepartments.tree.CurrentId = 0
#     frmDepartments.tree.column("colId", anchor=W, width=40)
#     frmDepartments.tree.heading("colId", text="Id")
#     frmDepartments.tree.column("colName", anchor=W, width=100)
#     frmDepartments.tree.heading("colName", text="Название")
#     frmDepartments.scrollbar = ttk.Scrollbar(orient=VERTICAL, command=frmDepartments.tree.yview)
#     # frmDepartments.tree.configure(yscroll=scrollbar.set)  
#     frmDepartments.scrollbar.grid(in_=frmDepartments, row=0, column=1, sticky="ns")
  
#     # frmDepartments.tree.pack()
#     frmDepartments.tree.grid(row=0, column=0)

#     # frmDepartments.tree.bind('<ButtonRelease-1>', selectItem)

#     # frmDepartments.btnAdd = ttk.Button(frmDepartments, text="Добавить")
#     # frmDepartments.btnAdd.bind('<ButtonRelease-1>', btnAddPressed)
#     # frmDepartments.btnAdd.pack()

#     # frmDepartments.btnEdit = ttk.Button(frmDepartments, text="Изменить")
#     # frmDepartments.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
#     # frmDepartments.btnEdit.pack()

#     # frmDepartments.btnDelete = ttk.Button(frmDepartments, text="Удалить")
#     # frmDepartments.btnDelete.bind('<ButtonRelease-1>', btnDelPressed)
#     # frmDepartments.btnDelete.pack()

#     # frmDepartments.btnRefresh = ttk.Button(frmDepartments, text="Обновить")
#     # frmDepartments.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
#     # frmDepartments.btnRefresh.pack()

#     frmDataRefresh(frmDepartments)
    

# if __name__ == '__main__':
#     openFormDepartments()
#     frmDepartments.mainloop()
