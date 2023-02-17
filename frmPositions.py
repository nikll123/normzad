import win
import frmDictionary
import dbPositions

tableArg = {'name':'Positions','title':'Должнсти'}

class frmPositions(frmDictionary.frmTable):
    def __init__(self) -> None:
        fldsArg = []
        fldsArg.append({'fld_name':'Id',   'title':'Id',       'visible':False, 'width':10})
        fldsArg.append({'fld_name':'Name', 'title':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg, readonly=True)
        self.btnNew.MouseClick += self.createNew

    def doEdit(self, sender, e):
        f1 = frmPosition(frmDictionary.dummyId, '')
        f1.btnSave.MouseClick += self.doSaveNew
        f1.ShowDialog()
    
    def createNew(self, sender, e):
        f1 = frmPosition(frmDictionary.dummyId, '', self)
        f1.ShowDialog()

class frmPosition(frmDictionary.frmSimpleObject):
    def __init__(self, argId, argName, parent) -> None:
        super().__init__(tableArg['name'], argId, argName)
        self.parent = parent
        self.btnSave.MouseClick += self.doSave

    def doSave(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = self.cntLblTxtName.txt_value.Text
        if id == frmDictionary.dummyId:
            err, newId = dbPositions.new(name)
        else:
            err = dbPositions.update(id, name)
        if err:
            win.SowErrorMessage(err)
        else:
            self.parent.getData()
            self.Close()


if __name__ == '__main__':
    f1 = frmPosition(frmDictionary.dummyId, '')
    f1.ShowDialog()
