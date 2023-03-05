# workers 

import dbCommon

tableName = "Workers"
viewName  = "vWorkers"

def insert(tn,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    flds = ['TabNum','LastName','Name','SecondName','Level','PositionId','DepartmentId']
    data = [tn, LastName, Name, SecondName, Level, PositionId, DepartmentId]
    err, newId = dbCommon.insert(tableName, flds, data)
    return err, newId

def delete(id):
    err = dbCommon.delete(tableName, id)
    return err

def update(id,tn,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    flds = ['TabNum','LastName','Name','SecondName','Level','PositionId','DepartmentId']
    data = [tn,LastName,Name,SecondName,Level,PositionId,DepartmentId]
    err = dbCommon.update(tableName, flds, data, id)
    return err

def select(flds=['*'], cond='', order=''):
    err, data = dbCommon.select(viewName, flds, cond, order)
    return err, data

# FIO = Фамилия и инициалы, например: Иванов И.И.
def selectFio(cond=''):
    err, data = select(['id','FIO'], cond=cond)
    return err, data

# FIO и табельный номер, например: Иванов И.И. (333)
def selectFioNum(cond=''):
    err, data = select(['id','FIO_Num'], cond=cond)
    return err, data


if __name__ == '__main__':
    print (insert(122,"ggggg","ffff","iiiii",1,8))

    print (delete(4))

    print (update(121,"g","ffff","iiiii",1,8 ))

    pass
