import frmDictionary

def frmPositions():
    table = {'name':'Positions','title':'Должнсти'}
    cols = []
    cols.append({'name':'Id',   'title':'Id',        'visible':False, 'width':10,  'readonly':True})
    cols.append({'name':'Name', 'title':'Название', 'visible':True,  'width':300, 'readonly':True})

    frm = frmDictionary.frmTable(table, cols) 
    return frm

if __name__ == '__main__':
    frm = frmPositions()
    frm.Execute()
