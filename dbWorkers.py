# workers 

import sqlite3
import config
import dbCommon

tableName = "Workers"

def new(tn,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    err, LastName, Name, SecondName= _checkNames(LastName,Name,SecondName)
    if not err:
        flds = ['TabNum','LastName','Name','SecondName','Level','PositionId','DepartmentId']
        data = [tn, LastName, Name, SecondName, Level, PositionId, DepartmentId]
        err, newId = dbCommon.insert(tableName, flds, data)
    return err

def delete(id):
    err = dbCommon.delete(tableName, id)
    return err

def update(id,tn,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    err, LastName, Name, SecondName= _checkNames(LastName,Name,SecondName)
    if not err:
        flds = ['TabNum','LastName','Name','SecondName','Level','PositionId','DepartmentId']
        data = [tn,LastName,Name,SecondName,Level,PositionId,DepartmentId]
        err = dbCommon.update(tableName, flds, data, id)
    return err

def _checkNames(LastName,Name,SecondName):
    LastName = LastName.strip()
    Name = Name.strip()
    SecondName = SecondName.strip()
    if LastName and Name and SecondName:
        err = ''
    else:
        err = "Нет полного имени"
    return err, LastName, Name, SecondName


if __name__ == '__main__':
    print (new(122,"ggggg","ffff","iiiii",1,8))

    print (delete(4))

    print (update(121,"g","ffff","iiiii",1,8 ))

    pass
