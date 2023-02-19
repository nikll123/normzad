import common
import guiBaseForm
import dbTasks

tableArg = {'name':'Tasks','header':'Задания'}        

class frmTasks(guiBaseForm.frmDictionary):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
        fldsArg.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg, readonly=True)

    def editItem(self, sender, e):
        id = self.getSelectedFldValue('id')
        name = self.getSelectedFldValue('Name')
        frm = frmTask(id, name, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        positionId = guiBaseForm.dummyId
        positionName = ''
        frm = frmTask(positionId, positionName, self)
        frm.ShowDialog()
    
    def deleteItem(self, sender, e):
        id = self.getSelectedFldValue('id')
        name = self.getSelectedFldValue('Name')
        if id != None:
            if common.ShowQuestionMessage(f'Удалить задание: {name}?'):
                err = dbTasks.delete(id)
                if not common.checkIfError(err):
                    self.getDataFromDb()

class frmTask(guiBaseForm.frmDictionaryItem):
    def __init__(self, argId, argName, parent):
        super().__init__(tableArg, argId, argName)
        self.parent = parent

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.dummyId:
            err, newId = dbTasks.new(name)
        else:
            err = dbTasks.update(id, name)
        if err:
            common.checkIfError(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

