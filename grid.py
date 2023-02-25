from tkinter import *
from tkinter import ttk

class grid(ttk.Frame):
    # def __init__(self, master: tkinter.Misc | None = None, *, border: tkinter._ScreenUnits = ..., borderwidth: tkinter._ScreenUnits = ..., class_: str = ..., cursor: tkinter._Cursor = ..., height: tkinter._ScreenUnits = ..., name: str = ..., padding: _Padding = ..., relief: tkinter._Relief = ..., style: str = ..., takefocus: tkinter._TakeFocusValue = ..., width: tkinter._ScreenUnits = ...) -> None:
    #     super().__init__(master, border=border, borderwidth, class_, cursor, height, name, padding, relief, style, takefocus, width)
    def __init__(self, master, name='grid'):
        super().__init__(master, name=name)
        self.Name = name
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        self.tree = ttk.Treeview(self, column=("colId", "colName"), show='headings')
        self.tree.CurrentId = 0
        self.tree.column("colId", anchor=W, width=50, stretch=NO)
        self.tree.heading("colId", text="Id")
        self.tree.column("colName", anchor=W, width=100)
        self.tree.heading("colName", text="Название")
        self.tree.pack(fill=BOTH, expand=True, side=LEFT)

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)  
        self.tree.bind('<ButtonRelease-1>', self.gridClick)
        self.scrollbar.pack(anchor=E, expand=True, fill=Y)

    def gridClick(self, e):
        print('gridClick: to be replaced')

if __name__ == '__main__':
    root = Tk()
    root.title("grid test")
    root.geometry("300x600")
    root.grid = grid(root,'gridtest')
    root.grid.pack(fill=BOTH, expand=True)
    root.mainloop()
