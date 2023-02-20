import common
import guiBaseForm
import dbWorkers

tableArg = {'name':'workerList','header':'Сотрудники'}

class frmWorkers(guiBaseForm.frmDictionary):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',          'header':'Id',            'visible':False, 'width':10})
        fldsArg.append({'fld_name':'LastName',    'header':'Фамилия',       'visible':True,  'width':200})
        fldsArg.append({'fld_name':'Name',        'header':'Имя',           'visible':True,  'width':200})
        fldsArg.append({'fld_name':'SecondName',  'header':'Отчество',      'visible':True,  'width':200})
        fldsArg.append({'fld_name':'Level',       'header':'Разряд',        'visible':True,  'width':100})
        fldsArg.append({'fld_name':'Department',  'header':'Подразделение', 'visible':True,  'width':100})
        fldsArg.append({'fld_name':'Position',    'header':'Должность',     'visible':True,  'width':100})
        fldsArg.append({'fld_name':'DepartmentId','header':'DepartmentId',  'visible':False, 'width':100})
        fldsArg.append({'fld_name':'PositionId',  'header':'PositionId',    'visible':False, 'width':100})
        super().__init__(tableArg, fldsArg, readonly=True)

    def editItem(self, sender, e):
        id = self.getSelectedFldValue('id')
        name = self.getSelectedFldValue('Name')
        secondName = self.getSelectedFldValue('SecondName')
        lastName = self.getSelectedFldValue('LastName')
        level = self.getSelectedFldValue('Level')
        departmentId = self.getSelectedFldValue('DepartmentId')
        positionId = self.getSelectedFldValue('PositionId')
        frm = frmWorker(id, name, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        id = guiBaseForm.newId
        name = ''
        frm = frmWorkers(id, name, self)
        frm.ShowDialog()

    def deleteItem(self, sender, e):
        pass
        

class frmWorker(guiBaseForm.frmDictionaryItem):
    def __init__(self, id,LastName,Name,SecondName,PositionId,Level, parent):
        super().__init__(tableArg, argId, argName)
        self.parent = parent

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.newId:
            err, newId = dbWorkers.new(id,LastName,Name,SecondName,PositionId,Level)
        else:
            err = dbWorkers.update(id, name)
        if err:
            common.checkIfError(err)
        else:
            self.parent.getDataFromDb()
            self.Close()
