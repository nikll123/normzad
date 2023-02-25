from tkinter import *
from tkinter import ttk

class frameGrid(ttk.Frame):
    """ grid class (parent class - frame)

    """
    def __init__(self, parent, name='frameGrid'):
        super().__init__(master=parent, name=name)
        self.Name = name
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.Columns = []

    def addColumn(self, name, text, anchor=None, width=None, stretch=YES):
        self.Columns.append({'name':name, 'text':text, 'anchor':anchor, 'width':width, 'stretch':stretch})
    
    def buildGrid(self):
        names = [c['name'] for c in self.Columns]
        self.tree = ttk.Treeview(self, column=names, show='headings')
        for c in self.Columns:
            self.tree.column(c['name'], anchor=c['anchor'], width=c['width'], stretch=c['stretch'])
            self.tree.heading(c['name'], text=c['text'])
        self.tree.pack(fill=BOTH, expand=True, side=LEFT)

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)  
        self.tree.bind('<ButtonRelease-1>', gridClick)
        self.scrollbar.pack(anchor=E, expand=True, fill=Y)

    def putData(self, data):
        for c in self.tree.get_children(""):
            self.tree.delete(c)
        for row in data:
            self.tree.insert("", END, values=row)        

def gridClick(e):
    print("gridClick: to be replaced: frameGrid.tree.bind('<ButtonRelease-1>', gridClick)")


if __name__ == '__main__':
    root = Tk()
    root.title("frameGrid test")
    root.geometry("300x600")
    root.grid = frameGrid(root,'frameGrid')
    root.grid.addColumn(name="colId", text="id", anchor=W, width=50, stretch=NO)
    root.grid.addColumn(name="colName", text='Name', anchor=W, width=100)
    root.grid.buildGrid()
    root.grid.pack(fill=BOTH, expand=True)
    root.mainloop()
