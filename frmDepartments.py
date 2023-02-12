import FormDictionary

def frmDepartments():
    table = {'name':'Departments','title':'Подразделения'}
    cols = []
    cols.append({'name':'Id',   'title':'Id',        'visible':False, 'width':10,  'readonly':True})
    cols.append({'name':'Name', 'title':'Название', 'visible':True,  'width':300, 'readonly':True})

    frm = FormDictionary.frmDictionary(table, cols) 
    return frm

if __name__ == '__main__':
    frm = frmDepartments()
    frm.Execute()
    