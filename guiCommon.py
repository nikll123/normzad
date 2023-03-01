from tkinter.messagebox import showerror, askyesno
from tkinter import *
from tkinter import ttk
import blDepartments

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

class frameLbltext(ttk.Frame):
    Name='frameLbltext'
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
    def __init__(self, master, title='cmb', relief=FLAT):
        super().__init__(master, relief=relief, width=350, height=40, padding=5)
        self.pack_propagate(False)
        self.lbl = Label(self, text=title, width=20)
        self.lbl.pack(side=LEFT)
        
        self.cmb = ttk.Combobox(self)
        self.cmb.pack(side=LEFT, fill=X, expand=True)

        # err, data = blDepartments.selectAll()
        # if notError(err):
        #     self.values=data
        


if __name__ == '__main__':
    root = form('Test')
    subform = subForm(root, 'subformTitle')
    subform.frameEmpty = frameEmpty(subform, relief=SOLID)
    subform.frameEmpty.pack()
    subform.frameLbltext = frameLbltext(subform, 'test txt', relief=SOLID)
    subform.frameLbltext.pack()
    subform.frameLbltext.set('test data')
    subform.cmb=frameCmb(subform, 'test cmb', relief=SOLID)
    subform.cmb.pack()
    root.mainloop()

