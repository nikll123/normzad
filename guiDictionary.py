from tkinter import *
from tkinter import ttk
import frameGrid
import frame4buttons
import dbPositions
from tkinter.messagebox import showerror, askyesno

class frameDictionary(ttk.Frame):

    def __init__(self, parent, name='frameDictionary',border=False):
        super().__init__(master=parent)
        self.Name = name
        # if border:
        #     self.
        self.frame1 = frameGrid.frameGrid(parent)
        self.frame1.tree.bind('<ButtonRelease-1>', self.gridClick)
        self.idReset(self.frame1)
        # self.frame1DataRefresh(parent, self.frame1)

        self.frame1.pack(fill=BOTH, expand=True)

        self.frame2 = frame4buttons.frame4Buttons(parent)
        # self.frame2.btnNew.bind('<ButtonRelease-1>', self.btnAddPressed)
        # self.frame2.btnEdit.bind('<ButtonRelease-1>', self.btnEditPressed)
        # self.frame2.btnDelete.bind('<ButtonRelease-1>', self.btnDeletePressed)
        # self.frame2.btnRefresh.bind('<ButtonRelease-1>', self.btnRefreshPressed)


        # self.frame2 = self.createFrameButtons(self)
        self.frame2.pack(fill=X)

    def gridClick(self, e):
        frame1 = e.widget.master
        self.idSet(frame1)

    def idReset(self, frame1):
        frame1.itemId = None
        frame1.itemName = None

    def idSet(frame1):
        curItem = frame1.tree.focus()
        if curItem:
            frame1.itemId = frame1.tree.item(curItem)['values'][0]
            frame1.itemName = frame1.tree.item(curItem)['values'][1]

    def frame1DataRefresh(self, frame1, data):
        self.frame1.putData(data)
        self.idReset(frame1)

    # ------- 4 buttons ----------
    def btnAddPressed(self, e):
        # mainFrame = e.widget.master.master
        # self.idReset(mainFrame.frame1)
        # openFrmNew("Создание", mainFrame)
        print("btnAddPressed: frame2.btnNew.bind('<ButtonRelease-1>', parent.btnAddPressed)")

    def btnEditPressed(self, e):
        # frm = e.widget.master.master
        # if frm.frame1.itemId != None:
        #     openFrmNew("Изменение", frm)
        print("btnEditPressed: frame2.btnEdit.bind('<ButtonRelease-1>', parent.btnEditPressed)")

    def btnDeletePressed(self, e):
        frm = e.widget.master.master
        if frm.frame1.itemId != None:
            result = askyesno("Подтверждение действия", f"Удалить: {frm.frame1.itemName}?")
            if result:
                err = dbPositions.delete(frm.frame1.itemId)
                if err:
                    showerror("Ошибка", err)
                else:
                    self.frame1DataRefresh(frm.frame1)

    def btnRefreshPressed(self, e):
        mainFrame = e.widget.master.master
        self.frame1DataRefresh(mainFrame.frame1)

# # ------ edit form ----------
# def openFrmNew(title, frmParent, id=None, name = None):
#     frmNew = Toplevel()
#     frmNew.title(title)
#     frmNew.Name = 'frmNew'
#     frmNew.geometry("400x300")
#     frmNew.iconbitmap("nz.ico")
#     frmNew.frmParent = frmParent

#     frmNew.lbl = ttk.Label(frmNew, text="Название")
#     frmNew.lbl.grid(row=0, column=0, padx=10, pady=10)

#     frmNew.txtName = ttk.Entry(frmNew)
#     frmNew.txtName.grid(row=0, column=1, padx=10, pady=10)
#     if frmParent.frame1.itemName != None:
#         frmNew.txtName.insert(0, frmParent.frame1.itemName)
#     frmNew.txtName.focus()

#     frmNew.btnSave = ttk.Button(frmNew, text="Сохранить")
#     frmNew.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
#     frmNew.btnSave.grid(row=1, column=1, padx=10, pady=10)

#     frmNew.grab_set()

# def btnSavePressed(e):
#     frm = e.widget.master
#     newName = frm.txtName.get()
#     if frm.frmParent.frame1.itemId == None:
#         err, newId = dbPositions.new(newName)
#     else:
#         err = dbPositions.update(frm.frmParent.frame1.itemId, newName)
#     if err:
#         showerror("Ошибка", err)
#     else:
#         frame1DataRefresh(frm.frmParent.frame1)
#         frm.destroy()

# ------- test -------------
if __name__ == '__main__':
    root = Tk()
    root.Name = 'root'
    root.title("Dictionary test")
    root.geometry("400x500")
    root.frameMain = frameDictionary(root)
    root.frameMain.frame1.addColumn(name='Id',text='Id',anchor=W,width=50,stretch=NO)
    root.frameMain.frame1.addColumn(name='Name',text='Название',anchor=W,width=100,stretch=YES)
    root.frameMain.frame1.buildGrid()    
    root.frameMain.pack(fill=BOTH, expand=True)
    err, data = dbPositions.select()
    root.frameMain.frame1DataRefresh(root.frameMain.frame1, data)
    root.mainloop()
