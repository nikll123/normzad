import common
import guiBaseForm
import dbDepartments

tableArg = {'name':'Departments','header':'Подразделения'}
fldsArg = []
fldsArg.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
fldsArg.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})

class frmDepartmentTable(guiBaseForm.frmDictionary):
    def __init__(self):
        super().__init__(tableArg, fldsArg, readonly=True)

    def createItem(self, sender, e):
        id = guiBaseForm.dummyId
        name = ''
        frm = frmDepartment(id, name, self)
        frm.ShowDialog()

    def editItem(self, sender, e):
        if not self.grd.SelectedRows[0].IsNewRow:
            id, name = self.getSelectedRowValues(['id','Name'])
            frm = frmDepartment(id, name, self)
            frm.ShowDialog()

    def deleteItem(self, sender, e):
        if not self.grd.SelectedRows[0].IsNewRow:
            id, name = self.getSelectedRowValues(['id','Name'])
            if common.showQuestionMessage(f"Удалить подразделение: {name}?"):
                err = dbDepartments.delete(id)
                isError = common.checkIfError(err)
                if not isError:
                    self.getDataFromDb()

class frmDepartment(guiBaseForm.frmDictionaryItem):
    def __init__(self, argId, argName, parent):
        super().__init__(tableArg, argId, argName)
        self.parent = parent

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt.Text)
        name = self.cntLblTxtName.txt.Text
        if id == guiBaseForm.dummyId:
            err, newId = dbDepartments.new(name)
        else:
            err = dbDepartments.update(id, name)
        if err:
            common.checkIfError(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

