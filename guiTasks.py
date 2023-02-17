import common
import guiBaseForm
import dbTasks

tableArg = {'name':'Tasks','header':'Задания'}        

class frmTasks(guiBaseForm.frmBaseTable):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',   'header':'Id',       'visible':False, 'width':10})
        fldsArg.append({'fld_name':'Name', 'header':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg, readonly=True)
        self.btnNew.MouseClick += self.createNew
        self.btnEdit.MouseClick += self.editItem

    def editItem(self, sender, e):
        id = self.getSelectedRowFldValue('id')
        name = self.getSelectedRowFldValue('Name')
        frm = frmTask(id, name, self)
        frm.ShowDialog()
    
    def createNew(self, sender, e):
        positionId = guiBaseForm.dummyId
        positionName = ''
        frm = frmTask(positionId, positionName, self)
        frm.ShowDialog()

class frmTask(guiBaseForm.frmSimpleEditData):
    def __init__(self, argId, argName, parent):
        super().__init__(tableArg, argId, argName)
        self.parent = parent
        self.btnSave.MouseClick += self.doSave

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiBaseForm.dummyId:
            err, newId = dbTasks.new(name)
        else:
            err = dbTasks.update(id, name)
        if err:
            common.SowErrorMessage(err)
        else:
            self.parent.getDataFromDb()
            self.Close()

