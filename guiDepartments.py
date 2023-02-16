import frmDictionary
import dbDepartments

class frmDepartments(frmDictionary.frmTable):
    def __init__(self) -> None:
        tableArg = {'name':'Departments','title':'Подразделения'}
        fldsArg = []
        fldsArg.append({'name':'Id',   'title':'Id',       'visible':False, 'width':10})
        fldsArg.append({'name':'Name', 'title':'Название', 'visible':True,  'width':300})
        super().__init__(tableArg, fldsArg)
        self.btnNew.MouseClick += self.doAppend
        

    def doAppend(self, sender, e):
        f1 = frmDepartment(1,'sss')
        f1.ShowDialog()

    def doEdit(self, sender, e):
        id = int(self.cntLblTxtId.txt_value.Text)
        name = int(self.cntLblTxtName.txt_value.Text)


class frmDepartment(frmDictionary.frmSimpleObject):
    def __init__(self, argId, argName) -> None:
        super().__init__('Departments', argId, argName)





if __name__ == '__main__':
    frm = frmDepartments() 
    frm.Execute()
