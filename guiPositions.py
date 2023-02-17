import common
import guiBaseForm
import dbPositions

tableArg = {'name':'Positions','header':'Должности'}

class frmPositions(guiBaseForm.frmBaseTable):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
        fldsArg.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg, readonly=True)
        self.btnNew.MouseClick += self.createItem
        self.btnEdit.MouseClick += self.editItem
        self.btnDelete.MouseClick += self.deleteItem

    def editItem(self, sender, e):
        id = self.getSelectedRowFldValue('id')
        name = self.getSelectedRowFldValue('Name')
        frm = frmPosition(id, name, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        id = guiBaseForm.dummyId
        name = ''
        frm = frmPosition(id, name, self)
        frm.ShowDialog()

    def deleteItem(self, sender, e):
        id = self.getSelectedRowFldValue('id')
        if id is not None:
            name = self.getSelectedRowFldValue('Name')
            if common.ShowQuestionMessage(f"Удалить должность: {name}?"):
                err = dbPositions.delete(id)
                isError = common.ShowErrorIfNotEmpty(err)
                if not isError:
                    self.getDataFromDb()
        
class frmPosition(guiBaseForm.frmSimpleEditData):
    def __init__(self, positionId, positionName, parent):
        super().__init__(tableArg, positionId, positionName)
        self.parent = parent
        self.btnSave.MouseClick += self.doSave

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.dummyId:
            err, newId = dbPositions.new(name)
        else:
            err = dbPositions.update(id, name)
        if err:
            common.ShowErrorIfNotEmpty(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

