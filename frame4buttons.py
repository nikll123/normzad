from tkinter import *
from tkinter import ttk

class frame4Buttons(ttk.Frame):
    def __init__(self, name='frame4Buttons'):
        super().__init__(name=name)

        self.Name=name

        self.btnNew = ttk.Button(self, text="Добавить")
        self.btnNew.bind('<ButtonRelease-1>', self.btnAddPressed)
        self.btnNew.pack(side=LEFT, padx=10, pady=10)

        self.btnEdit = ttk.Button(self, text="Изменить")
        self.btnEdit.bind('<ButtonRelease-1>', self.btnEditPressed)
        self.btnEdit.pack(side=LEFT, padx=10, pady=10)

        self.btnDelete = ttk.Button(self, text="Удалить")
        self.btnDelete.bind('<ButtonRelease-1>', self.btnDeletePressed)
        self.btnDelete.pack(side=LEFT, padx=10, pady=10)

        self.btnRefresh = ttk.Button(self, text="Обновить")
        self.btnRefresh.bind('<ButtonRelease-1>', self.btnRefreshPressed)
        self.btnRefresh.pack(side=LEFT, padx=10, pady=10)


    def btnAddPressed(self, e):
        print('btnAddPressed: to be replaced')

    def btnEditPressed(self, e):
        print('btnAddPressed: to be replaced')

    def btnDeletePressed(self, e):
        print('btnDeletePressed: to be replaced')
        
    def btnRefreshPressed(self, e):
        print('btnRefreshPressed: to be replaced')

if __name__ == '__main__':
    root = Tk()
    root.title("frame4Buttons test")
    root.geometry("400x200")
    root.but4 = frame4Buttons('frame4Buttons')
    root.but4.pack(fill=X)
    root.mainloop()

