from tkinter.messagebox import showerror, askyesno
from tkinter import *
from tkinter import ttk
import blDepartments
import blPositions

class form(Tk):
    Name='formTk'
    def __init__(self,  title):
        super().__init__()
        _frmInit(self,  title)
        self.geometry("800x400")

class subForm(Toplevel):
    Name='subForm'
    def __init__(self, master, title):
        super().__init__(master=master)
        _frmInit(self,  title)
        self.geometry("400x300")
        self.grab_set()

def _frmInit(self,title):
    self.title(title)
    self.iconbitmap("nz.ico")

def notError(err):
    """проверка наличия ошибки 

    если err не пустая строка - значит есть ошибка, 
    выдатеся сообщение об ошибке и возвращается True, иначе False."""
    isError = err != ''
    if isError:
        showerror(title="Ошибка", message=err)
    return not isError

class frameEmpty(ttk.Frame):
    Name='frameEmpty'
    def __init__(self, master, relief=FLAT):
        super().__init__(master, relief=relief, width=350, height=40, padding=5)

class frameText(ttk.Frame):
    Name='frameText'
    def __init__(self, master, title='lbl', relief=FLAT):
        super().__init__(master, relief=relief, width=350, height=40, padding=5)
        self.pack_propagate(False)
        self.lbl = Label(self, text=title, width=20)
        self.lbl.pack(side=LEFT)
        
        self.tetx = Entry(self, width=30)
        self.tetx.pack(side=LEFT, fill=X, expand=True)
    
    def set(self, txt):
        self.tetx.insert(0, txt)

    def get(self):
        return self.tetx.get()

class frameCmb(ttk.Frame):
    Name='frameCmb'
    def __init__(self, master, title='cmb', relief=FLAT):
        super().__init__(master, relief=relief, width=350, height=40, padding=5)
        self.pack_propagate(False)
        self.lbl = Label(self, text=title, width=20)
        self.lbl.pack(side=LEFT)
        self.id = None
        self.data = None

        self.cmb = ttk.Combobox(self)
        self.cmb.pack(side=LEFT, fill=X, expand=True)
        self.cmb.bind('<KeyRelease>', self.search)    # autoincrement search
        # self.cmb.bind("<<ComboboxSelected>>", self.selected)
    
    def setCurrentId(self, id):
        self.id = None
        self.cmb.set("")
        if self.data != None and id != None:
            for row in self.data:
                if row[0] == id:
                    self.id = id
                    self.cmb.set(row[1])
                    break

    def getCurrentId(self):
        id = None
        ix = self.cmb.current()
        if ix != -1:
            id = self.data[ix][0]
        return id

    def loadValues(self, data):
        self.data = data
        self.setListValues('')

    def setListValues(self, txt):
        valuesAll = [r[1] for r in self.data]
        if txt == '':
            values = valuesAll
        else:
            values=[]
            for v in valuesAll:
                if txt.lower() in v.lower():
                    values.append(v)
        self.cmb['value'] = values
    
    def search(self, e):
        txt = e.widget.get()
        self.setListValues(txt)
        self.event_generate('<Down>')

    # def selected(self, e):
    #     print(self.cmb.current(), self.cmb.get(), self.getCurrentId())


if __name__ == '__main__':
    root = form('Test')
    subform = subForm(root, 'subformTitle')
    relief=FLAT
    subform.frameEmpty = frameEmpty(subform, relief=relief)
    subform.frameEmpty.pack()
    subform.frameLbltext = frameText(subform, 'test txt', relief=relief)
    subform.frameLbltext.pack()
    subform.frameLbltext.set('test data')
    subform.cmb=frameCmb(subform, 'test cmb', relief=relief)
    subform.cmb.pack()

    err, data = blPositions.selectAll()
    if notError(err):
        subform.cmb.loadValues(data)
        subform.cmb.setCurrentId(4)


    root.mainloop()

