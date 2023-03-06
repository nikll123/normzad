from tkinter import *
from tkinter import ttk
from datetime import datetime
import blJobs, guiGridButtons, guiCommon, blTasks, blWorkers, blReports
from tkinter.messagebox import askyesno

def createFrame(parent, showId):
    cols = []
    cols.append({'name':'Id',       'text':'Id',            'anchor':W,'width':50, 'stretch':NO, 'display':showId})
    cols.append({'name':'Date',     'text':'Дата',          'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'TabNum',   'text':'Таб. №',        'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'FIO',      'text':'Ф.И.О.',        'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Level',    'text':'Разряд',        'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Position', 'text':'Должность',     'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Task',     'text':'Задание',       'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'TimeJob',  'text':'Время',         'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Comment',  'text':'Комментарий',   'anchor':W,'width':100,'stretch':YES,'display':1})
    dictJobs = guiGridButtons.frameDictionary(parent, cols)
    dictJobs.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictJobs.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictJobs.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictJobs.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictJobs.Refresh = dataRefresh
    dictJobs.Refresh(dictJobs)
    dictJobs.btnNormZad = ttk.Button(master=dictJobs.frame4buttons, text='Задание')
    dictJobs.btnNormZad.bind('<ButtonRelease-1>', btnNormZadPressed)
    dictJobs.btnNormZad.pack(side=LEFT, padx=10, pady=10)
    return dictJobs

def btnNormZadPressed(e):
    dictJobs = e.widget.master.master
    id = dictJobs.getSelectedId()
    err, filename = blReports.repNormZad(id)
    if guiCommon.notError(err):
        blReports.openExcelFile(filename)

def btnAddPressed(e):
    dictJobs = e.widget.master.master
    frm = frmOneRow(parent=dictJobs,title='Новое заданиё')

def btnEditPressed(e):
    dictJobs = e.widget.master.master
    id = dictJobs.getSelectedId()
    if id is not None:
        frm = frmOneRow(parent=dictJobs, rowId=id, title='Редактированиё задания')
    
def btnDeletePressed(e):
    dictJobs = e.widget.master.master
    id = dictJobs.getSelectedId()
    if id != None:
        err, data = blJobs.get(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {data.Date}, {data.FIO}?")
            if result:
                err = blJobs.delete(id)
                if guiCommon.notError(err):
                    dataRefresh(dictJobs)

def btnRefreshPressed(e):
    dictJobs = e.widget.master.master
    dataRefresh(dictJobs)

def dataRefresh(dictJobs):
    err, data = blJobs.select(dictJobs.frameGrid.fldNames)
    if guiCommon.notError(err):
        dictJobs.dataPut(data)

class frmOneRow(guiCommon.subForm):
    Name='frmOneRow'
    def __init__(self, parent, title, rowId=None):
        super().__init__(parent, title)
        self.rowId = rowId
        self.parent = parent

        self.txtDate = guiCommon.frameText(self, 'Дата')
        self.txtDate.pack()

        self.cmbFIO = guiCommon.frameCmb(self, 'Ф.И.О.')
        err, data = blWorkers.selectFioNumAll()
        if guiCommon.notError(err):
            self.cmbFIO.loadValues(data)
        self.cmbFIO.pack()

        self.cmbTask = guiCommon.frameCmb(self, 'Задание')
        err, data = blTasks.selectAll()
        if guiCommon.notError(err):
            self.cmbTask.loadValues(data)
        self.cmbTask.pack()

        self.txtTime = guiCommon.frameText(self, 'Время')
        self.txtTime.pack()
        
        self.txtComment = guiCommon.frameText(self, 'Комментарий')
        self.txtComment.pack()

        if self.rowId==None:   # new data
            date = datetime.now()
            date = date.strftime("%d.%m.%Y")
            self.txtDate.set(date)
            self.txtTime.set('8')
        else:
            err, row = blJobs.get(self.rowId)
            if guiCommon.notError(err):
                self.txtDate.set(row.Date)
                self.txtTime.set(row.TimeJob)
                self.cmbTask.setCurrentId(row.TaskId)
                self.cmbFIO.setCurrentId(row.WorkerId)
                self.txtComment.set(row.Comment)

        self.btnSave = Button(self, text='Сохранить', command=self.btnSaveClicked)
        self.btnSave.pack(side=TOP)

    def btnSaveClicked(self):
        date = self.txtDate.get()
        if date != None:
            timeJob = self.txtTime.get()
            taskId = self.cmbTask.getCurrentId()
            workerId = self.cmbFIO.getCurrentId()
            comment = self.txtComment.get()
            if self.rowId==None:   # new data
                err, _newId = blJobs.add(date=date, timeJob=timeJob, taskId=taskId, workerId=workerId, comment=comment)
            else:
                err = blJobs.save(id=self.rowId, date=date, timeJob=timeJob, taskId=taskId, workerId=workerId, comment=comment)
            if guiCommon.notError(err):
                self.parent.Refresh(self.parent)
                self.destroy()
        else:
            guiCommon.showerror('Ошибка', 'Неправильный формат даты')

# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.form(title="vJobs test")
    root.dictTasks = createFrame(root, 1)
    root.dictTasks.pack(fill=BOTH, expand=True)
    root.mainloop()

