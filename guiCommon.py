from tkinter.messagebox import showerror, askyesno
from tkinter import *
from tkinter import ttk

class formTk(Tk):
    Name='formTk'
    def __init__(self,  title):
        super().__init__()
        _frmInit(self,  title)
        self.geometry("800x400")

class formTopLevel(Toplevel):
    Name='formTopLevel'
    def __init__(self, master, title):
        super().__init__(master=master)
        _frmInit(self,  title)
        self.geometry("400x300")

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
    def __init__(self, master, width=100, height=100, relief=FLAT):
        super().__init__(master, relief=relief, width=width, height=height)

class frameLbltext(ttk.Frame):
    def __init__(self, master, title='lbl', relief=FLAT):
        super().__init__(master, relief=relief, width=500, height=100)
        self.lbl = Label(self, text=title, width=20)
        pad = 5
        self.lbl.pack(side=LEFT, padx=pad, pady=pad)
        self.tetx = Entry(self, width=30)
        self.tetx.pack(side=LEFT, fill=X, expand=True, padx=pad, pady=pad)
    
    def set(self, txt):
        self.tetx.insert(0, txt)

    def get(self):
        return self.tetx.get()

class cmbField(ttk.Combobox):
    def __init__(self, master, tabName, fldName):
        super().__init__(master)
        


if __name__ == '__main__':
    root = formTk('Test')
    subform = formTopLevel(root, 'subform', 'subformTitle')
    subform.frameEmpty = frameEmpty(subform, height=30)
    subform.frameEmpty.pack()
    subform.frameLbltext = frameLbltext(subform)
    subform.frameLbltext.pack()
    subform.frameLbltext.set('test')
    root.mainloop()
