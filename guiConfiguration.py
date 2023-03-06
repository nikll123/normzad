from tkinter import *
from tkinter import ttk
import guiCommon
import blConfiguration
from tkinter.messagebox import showerror, askyesno

def createFrame(parent):
    err, showId = blConfiguration.getShowId()
    if guiCommon.notError(err):
        pass
    else:
        showId = True

    frame = ttk.Frame()
    frame.checked = IntVar()
    frame.checked.set(showId)
    frame.chkShowId = ttk.Checkbutton(master=frame, text='Показывать id', variable=frame.checked)
    frame.chkShowId.pack(padx=10,pady=10)

    frame.btnSave = ttk.Button(master=frame, text='Сохранить')
    frame.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
    frame.btnSave.pack(padx=10,pady=10)

    return frame

def btnSavePressed(e):
    newVal = e.widget.master.checked.get()
    err = blConfiguration.setShowId(newVal)
    guiCommon.notError(err)

if __name__=='__main__':
    root = guiCommon.form(title="Departments test")
    root.formConfig = createFrame(root)
    root.formConfig.pack(fill=BOTH, expand=True)
    root.mainloop()
