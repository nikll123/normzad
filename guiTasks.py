import common
import guiBaseForm
import dbTasks

table = {'name':'Tasks','header':'Задания'}        
fldList = []
fldList.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
fldList.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})

class frmTasks(guiBaseForm.frmDictionary):
    def __init__(self):
        super().__init__(table, fldList, readonly=True)

    def editItem(self, sender, e):
        id = self.getSelectedRowValues('id')
        name = self.getSelectedRowValues('Name')
        frm = frmTask(id, name, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        positionId = guiBaseForm.newId
        positionName = ''
        frm = frmTask(positionId, positionName, self)
        frm.ShowDialog()
    
    def deleteItem(self, sender, e):
        id = self.getSelectedRowValues('id')
        name = self.getSelectedRowValues('Name')
        if id != None:
            if common.showQuestionMessage(f'Удалить задание: {name}?'):
                err = dbTasks.delete(id)
                if not common.checkIfError(err):
                    self.getDataFromDb()

class frmTask(guiBaseForm.frmDictionaryItem):
    def __init__(self, argId, argName, parent):
        super().__init__(table, argId, argName)
        self.parent = parent

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.newId:
            err, newId = dbTasks.new(name)
        else:
            err = dbTasks.update(id, name)
        if err:
            common.checkIfError(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

