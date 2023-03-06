from tkinter import *
from datetime import datetime
import blWorkers, guiGridButtons, guiCommon, blDepartments, blPositions
from tkinter.messagebox import askyesno

def createFrame(parent, showId):
    cols = []
    cols.append({'name':'Id',           'text':'Id',            'anchor':W,'width':50, 'stretch':NO, 'display':showId})
    cols.append({'name':'TabNum',       'text':'Таб.№',         'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'LastName',     'text':'Фамилия',       'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Name',         'text':'Имя',           'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'SecondName',   'text':'Отчество',      'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Level',        'text':'Разряд',        'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Department',   'text':'Подразделение', 'anchor':W,'width':100,'stretch':YES,'display':1})
    cols.append({'name':'Position',     'text':'Должность',     'anchor':W,'width':100,'stretch':YES,'display':1})
    dictWorkers = guiGridButtons.frameDictionary(parent, cols)
    dictWorkers.frame4buttons.btnNew.bind('<ButtonRelease-1>', btnAddPressed)
    dictWorkers.frame4buttons.btnEdit.bind('<ButtonRelease-1>', btnEditPressed)
    dictWorkers.frame4buttons.btnDelete.bind('<ButtonRelease-1>', btnDeletePressed)
    dictWorkers.frame4buttons.btnRefresh.bind('<ButtonRelease-1>', btnRefreshPressed)
    dictWorkers.Refresh = dataRefresh
    dictWorkers.Refresh(dictWorkers)
    return dictWorkers

def btnAddPressed(e):
    dictWorkers = e.widget.master.master
    frm = frmOneRow(parent=dictWorkers,title='Новый сотрудник')

def btnEditPressed(e):
    dictWorkers = e.widget.master.master
    id = dictWorkers.getSelectedId()
    if id is not None:
        frm = frmOneRow(parent=dictWorkers, rowId=id, title='Редактирование сотрудника')
    
def btnDeletePressed(e):
    dictWorkers = e.widget.master.master
    id = dictWorkers.getSelectedId()
    if id != None:
        err, data = blWorkers.get(id)
        if guiCommon.notError(err):
            result = askyesno("Подтверждение действия", f"Удалить: {data.TabNum}, {data.FIO}?")
            if result:
                err = blWorkers.delete(id)
                if guiCommon.notError(err):
                    dataRefresh(dictWorkers)

def btnRefreshPressed(e):
    dictWorkers = e.widget.master.master
    dataRefresh(dictWorkers)

def dataRefresh(dictWorkers):
    err, data = blWorkers.select(dictWorkers.frameGrid.fldNames)
    if guiCommon.notError(err):
        dictWorkers.dataPut(data)

class frmOneRow(guiCommon.subForm):
    Name='frmOneRow'
    def __init__(self, parent, title, rowId=None):
        super().__init__(parent, title)
        self.geometry("400x400")
        self.rowId = rowId
        self.parent = parent

        self.txtTabNum = guiCommon.frameText(self, 'Табельный номер')
        self.txtTabNum.pack()

        self.txtLastName = guiCommon.frameText(self, 'Фамилия')
        self.txtLastName.pack()

        self.txtName = guiCommon.frameText(self, 'Имя')
        self.txtName.pack()

        self.txtSecondName = guiCommon.frameText(self, 'Отчество')
        self.txtSecondName.pack()

        self.txtLevel = guiCommon.frameText(self, 'Разряд')
        self.txtLevel.pack()

        self.cmbDepartment = guiCommon.frameCmb(self, 'Подразделение')
        err, data = blDepartments.selectAll()
        if guiCommon.notError(err):
            self.cmbDepartment.loadValues(data)
        self.cmbDepartment.pack()

        self.cmbPosition = guiCommon.frameCmb(self, 'Должность')
        err, data = blPositions.selectAll()
        if guiCommon.notError(err):
            self.cmbPosition.loadValues(data)
        self.cmbPosition.pack()

        if self.rowId==None:   # new data
            pass
        else:
            err, row = blWorkers.get(self.rowId)
            if guiCommon.notError(err):
                self.txtTabNum.set(row.TabNum)
                self.txtLastName.set(row.LastName)
                self.txtName.set(row.Name)
                self.txtSecondName.set(row.SecondName)
                self.txtLevel.set(row.Level)
                self.cmbDepartment.setCurrentId(row.DepartmentId)
                self.cmbPosition.setCurrentId(row.PositionId)

        self.btnSave = Button(self, text='Сохранить', command=self.btnSaveClicked)
        self.btnSave.pack(side=TOP)

    def btnSaveClicked(self):
        tn = self.txtTabNum.get()
        lastName = self.txtLastName.get()
        name = self.txtName.get()
        secondName = self.txtSecondName.get()
        level = self.txtLevel.get()
        departmentId = self.cmbDepartment.getCurrentId()
        positionId = self.cmbPosition.getCurrentId()

        if self.rowId==None:   # new data
            err, _newId = blWorkers.add(tn=tn,LastName=lastName,
                                        Name=name, SecondName=secondName, Level=level, 
                                        DepartmentId=departmentId, PositionId=positionId)
        else:
            err = blWorkers.save(id=self.rowId, tn=tn,LastName=lastName,
                                        Name=name, SecondName=secondName, Level=level, 
                                        DepartmentId=departmentId, PositionId=positionId)
        if guiCommon.notError(err):
            self.parent.Refresh(self.parent)
            self.destroy()

# ------- test -------------
if __name__ == '__main__':
    root = guiCommon.form(title="vWorkers test")
    root.dictWorkers = createFrame(root, 1)
    root.dictWorkers.pack(fill=BOTH, expand=True)
    root.mainloop()

