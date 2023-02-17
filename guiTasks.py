import win
import guiDictionary
import dbTasks

tableArg = {'name':'Tasks','title':'Задания'}        

class frmTasks(guiDictionary.frmTable):
    def __init__(self) -> None:
        fldsArg = []
        fldsArg.append({'fld_name':'Id',   'title':'Id',       'visible':False, 'width':10})
        fldsArg.append({'fld_name':'Name', 'title':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg, readonly=True)
        self.btnNew.MouseClick += self.createNew

    def doEdit(self, sender, e):
        f1 = frmTask(guiDictionary.dummyId, '')
        f1.btnSave.MouseClick += self.doSaveNew
        f1.ShowDialog()
    
    def createNew(self, sender, e):
        f1 = frmTask(guiDictionary.dummyId, '', self)
        f1.ShowDialog()

class frmTask(guiDictionary.frmSimpleObject):
    def __init__(self, argId, argName, parent) -> None:
        super().__init__(tableArg['name'], argId, argName)
        self.parent = parent
        self.btnSave.MouseClick += self.doSave

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == guiDictionary.dummyId:
            err, newId = dbTasks.new(name)
        else:
            err = dbTasks.update(id, name)
        if err:
            win.SowErrorMessage(err)
        else:
            self.parent.getData()
            self.Close()


if __name__ == '__main__':
    # frm = frmDepartments() 
    # frm.Execute()

    f1 = frmTask(guiDictionary.dummyId, '')
    f1.ShowDialog()

