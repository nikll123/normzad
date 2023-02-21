import common
import guiBaseForm
import dbPositions

table = {'name':'Positions','header':'Должности'}
fldList = []
fldList.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
fldList.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})

class frmPositions(guiBaseForm.frmDictionary):
    def __init__(self):
        super().__init__(table, fldList, readonly=True)

    def createItem(self, sender, e):
        id = guiBaseForm.newId
        name = ''
        frm = frmPosition(id, name, self)
        frm.ShowDialog()

    def editItem(self, sender, e):
        if not self.grd.SelectedRows[0].IsNewRow:
            id, name = self.getSelectedRowValues(['id','Name'])
            frm = frmPosition(id, name, self)
            frm.ShowDialog()

    def deleteItem(self, sender, e):
        if not self.grd.SelectedRows[0].IsNewRow:
            id, name = self.getSelectedRowValues(['id','Name'])
            if common.showQuestionMessage(f"Удалить должность: {name}?"):
                err = dbPositions.delete(id)
                isError = common.checkIfError(err)
                if not isError:
                    self.getDataFromDb()
        
class frmPosition(guiBaseForm.frmDictionaryItem):
    def __init__(self, positionId, positionName, parent):
        super().__init__(table, positionId, positionName)
        self.parent = parent
        self.btnSave.MouseClick += self.doSave

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.newId:
            err, newId = dbPositions.new(name)
        else:
            err = dbPositions.update(id, name)
        if err:
            common.checkIfError(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

