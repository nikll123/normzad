from tkinter import *
from tkinter import ttk

class frameGrid(ttk.Frame):
    """ grid class (parent class - frame)

    """
    def __init__(self, parent, columns, name='frameGrid'):
        super().__init__(master=parent, name=name)
        self.Name = name
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        
        self.fldNames = [c['name'] for c in columns]
        self.tree = ttk.Treeview(self, column=self.fldNames, show='headings')
        dispCols = []
        for c in columns:
            self.tree.column(c['name'], anchor=c['anchor'], width=c['width'], stretch=c['stretch'])
            if c['display']:
                dispCols.append(c['name'])
            self.tree.heading(c['name'], text=c['text'])
        # self.tree.bind('<<TreeviewSelect>>', self.rowSelected)
        self.tree['displaycolumns'] = dispCols
        self.tree.pack(fill=BOTH, expand=True, side=LEFT)

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)  
        self.scrollbar.pack(anchor=E, expand=True, fill=Y)

    def putData(self, data):
        for c in self.tree.get_children(""):
            self.tree.delete(c)
        for row in data:
            self.tree.insert("", END, values=row)        

    def getSelectedId(self):
        id = None
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            id = item["values"][0]
            break
        return id

if __name__ == '__main__':
    root = Tk()
    root.title("frameGrid test")
    root.geometry("300x600")
    cols = []
    cols.append({'name':"colId", 'text':"id", 'anchor':W, 'width':50, 'stretch':NO})
    cols.append({'name':"colName", 'text':"Name", 'anchor':W, 'width':100, 'stretch':YES})
    root.grid = frameGrid(root, cols)
    root.grid.pack(fill=BOTH, expand=True)
    root.mainloop()
