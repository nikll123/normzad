from tkinter import *
from tkinter import ttk
import guiFrameGrid
import guiFrame4buttons
import dbPositions
from tkinter.messagebox import showerror, askyesno
debugMode = False

class frameDictionary(ttk.Frame):

    def __init__(self, parent, cols, name='frameDictionary', border=False):
        super().__init__(master=parent)
        self.Name = name

        self.frameGrid = guiFrameGrid.frameGrid(self, cols)
        self.frameGrid.pack(fill=BOTH, expand=True)

        self.frame4buttons = guiFrame4buttons.frame4Buttons(self)
        self.frame4buttons.btnNew.bind('<ButtonRelease-1>', self.btnAddPressed)
        self.frame4buttons.btnEdit.bind('<ButtonRelease-1>', self.btnEditPressed)
        self.frame4buttons.btnDelete.bind('<ButtonRelease-1>', self.btnDeletePressed)
        self.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', self.btnRefreshPressed)
        self.frame4buttons.pack(fill=X)


    def getSelectedId(self):
        return self.frameGrid.getSelectedId()

    def dataPut(self, data):
        self.frameGrid.putData(data)

    # ------- 4 buttons ----------
    def btnAddPressed(self, e):
        print(".frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)")

    def btnEditPressed(self, e):
        print(".frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)")

    def btnDeletePressed(self, e):
        print(".frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)")

    def btnRefreshPressed(self, e):
        print(".frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)")

    def Refresh(self):
        pass

# ------- test -------------
if __name__ == '__main__':
    debugMode = True
    root = Tk()
    root.Name = 'root'
    root.title("Dictionary test")
    root.geometry("400x500")
    cols = []
    cols.append({'name':'Id','text':'Id','anchor':W,'width':50,'stretch':NO})
    cols.append({'name':'Name','text':'Название','anchor':W,'width':100,'stretch':YES})
    root.frameDict = frameDictionary(root, cols)
    root.frameDict.pack(fill=BOTH, expand=True)
    err, data = dbPositions.select()
    root.frameDict.dataRefresh(data)
    root.mainloop()
