from tkinter import *
from tkinter import ttk

class frame4Buttons(ttk.Frame):
    def __init__(self, parent, name='frame4Buttons'):
        super().__init__(master=parent, name=name)
        self.Name=name

        self.btnNew = ttk.Button(self, text="Добавить")
        self.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
        self.btnNew.pack(side=LEFT, padx=10, pady=10)

        self.btnEdit = ttk.Button(self, text="Изменить")
        self.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
        self.btnEdit.pack(side=LEFT, padx=10, pady=10)

        self.btnDelete = ttk.Button(self, text="Удалить")
        self.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
        self.btnDelete.pack(side=LEFT, padx=10, pady=10)

        self.btnRefresh = ttk.Button(self, text="Обновить")
        self.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
        self.btnRefresh.pack(side=LEFT, padx=10, pady=10)

def btnAddPressed(e):
    print("to be replaced: frame4Buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)")

def btnEditPressed(e):
    print("to be replaced: frame4Buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)")

def btnDeletePressed(e):
    print("to be replaced: frame4Buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)")
    
def btnRefreshPressed(e):
    print("to be replaced: frame4Buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)")


if __name__ == '__main__':
    root = Tk()
    root.title("frame4Buttons test")
    root.geometry("400x200")
    root.but4 = frame4Buttons('frame4Buttons')
    root.but4.pack(fill=X)
    root.mainloop()

