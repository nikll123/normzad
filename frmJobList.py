import frmDictionary


def frmJobList():
    table = {'name':'JobList','title':'Табель'}
    cols = []
    cols.append({'name':'Id',        'title':'Id',          'visible':False, 'width':10,  'readonly':True})
    cols.append({'name':'Date',      'title':'Дата',        'visible':True,  'width':100, 'readonly':False})
    cols.append({'name':'TabelNom',  'title':'Табельный №', 'visible':True,  'width':100, 'readonly':False})
    cols.append({'name':'ShortName', 'title':'Ф.И.О.',      'visible':True,  'width':300, 'readonly':False})
    cols.append({'name':'Level',     'title':'Разряд',      'visible':True,  'width':100, 'readonly':False})
    cols.append({'name':'Position',  'title':'Должность',   'visible':True,  'width':150, 'readonly':False})
    cols.append({'name':'Task',      'title':'Задание',     'visible':True,  'width':200, 'readonly':False})
    cols.append({'name':'TimeJob',   'title':'Время',       'visible':True,  'width':100, 'readonly':False})

    frm = frmDictionary.frmDictionary(table, cols, frmDictionary.Size(1200,600), readonly=False) 
    return frm

if __name__ == '__main__':
    frm = frmJobList()
    # frm.Show()
    # frm.Refresh()
    frm.Execute()
