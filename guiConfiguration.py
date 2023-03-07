from tkinter import *
from tkinter import ttk
import guiCommon
import config
import blConfiguration
from tkinter.messagebox import showerror, askyesno
import os

def createFrame(parent):
    err, showId = blConfiguration.getShowId()
    if guiCommon.notError(err):
        pass
    else:
        showId = True

    frame = ttk.Frame()

    frame.confFrame = ttk.Frame(master=frame, borderwidth=1, relief=SOLID)
    frame.checked = IntVar()
    frame.checked.set(showId)
    frame.chkShowId = ttk.Checkbutton(master=frame.confFrame, text='Показывать id', variable=frame.checked)
    frame.chkShowId.pack(padx=10,pady=10)

    frame.btnSave = ttk.Button(master=frame.confFrame, text='Сохранить')
    frame.btnSave.bind('<ButtonRelease-1>', btnSavePressed)
    frame.btnSave.pack(padx=10, pady=10)
    frame.confFrame.pack(padx=10, pady=10)

    frame.btnCreateDb = ttk.Button(master=frame, text='Создать БВ')
    frame.btnCreateDb.bind('<ButtonRelease-1>', btnCreateDbPressed)
    frame.btnCreateDb.pack(padx=10,pady=10)

    frame.btnCreateTestData = ttk.Button(master=frame, text='Создать тестовый данные')
    frame.btnCreateTestData.bind('<ButtonRelease-1>', btnCreateTestDataPressed)
    frame.btnCreateTestData.pack(padx=10,pady=10)

    return frame

def btnSavePressed(e):
    newVal = e.widget.master.master.checked.get()
    err = blConfiguration.setShowId(newVal)
    guiCommon.notError(err)

def btnCreateDbPressed(e):
    if not os.path.exists(config.dbFileName):
        _res, txt = blConfiguration.createDB()
    else:
        txt = f'Файл {config.dbFileName} уже существует.'
    guiCommon.showMessage(txt)

def btnCreateTestDataPressed(e):
    blConfiguration.createTestData()

if __name__=='__main__':
    root = guiCommon.form(title="Departments test")
    root.formConfig = createFrame(root)
    root.formConfig.pack(fill=BOTH, expand=True)
    root.mainloop()

