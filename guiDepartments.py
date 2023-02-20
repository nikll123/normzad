import common
import guiBaseForm
import dbDepartments

tableArg = {'name':'Departments','header':'Подразделения'}

class frmDepartmentTable(guiBaseForm.frmDictionary):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
        fldsArg.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg, readonly=True)

    def editItem(self, sender, e):
        id = self.getSelectedFldValue('id')
        name = self.getSelectedFldValue('Name')
        frm = frmDepartment(id, name, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        id = guiBaseForm.newId
        name = ''
        frm = frmDepartment(id, name, self)
        frm.ShowDialog()

    def deleteItem(self, sender, e):
        id = self.getSelectedFldValue('id')
        name = self.getSelectedFldValue('Name')
        if id != None:
            if common.ShowQuestionMessage(f'Удалить подразделение: {name}?'):
                err = dbDepartments.delete(id)
                if not common.checkIfError(err):
                    self.getDataFromDb()

class frmDepartment(guiBaseForm.frmDictionaryItem):
    def __init__(self, argId, argName, parent):
        super().__init__(tableArg, argId, argName)
        self.parent = parent

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.newId:
            err, newId = dbDepartments.new(name)
        else:
            err = dbDepartments.update(id, name)
        if err:
            common.checkIfError(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

