# workers 

import sqlite3
import config
import db

tableName = "Workers"

def new(id,LastName,Name,SecondName,Level,PositionId,DepartmentId):
    LastName = LastName.strip()
    Name = Name.strip()
    SecondName = SecondName.strip()
   
    if LastName and Name and SecondName:
        flds = ['id','LastName','Name','SecondName','Level','PositionId','DepartmentId']
        data = [id, LastName, Name, SecondName, Level, PositionId, DepartmentId]
        err, newId = db.insert(tableName, flds, data)
    else:
        err = "Нет полных имен"
    return err


def delete(id):
    err = db.delete(tableName, id)
    return err

def update(id,LastName,Name,SecondName,PositionId,Level):
    err = config.dummyErr
    with sqlite3.connect(config.dbFileName) as conn:
        cursor = conn.cursor()
        sql = f"""UPDATE {tableName} SET LastName = ?,Name = ?,SecondName = ?,PositionId = ?,Level = ? WHERE id = ?"""
        try:
            cursor.execute(sql, [LastName,Name,SecondName,PositionId,Level,id])
            err = ''
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    return err


if __name__ == '__main__':
    print (new(122,"ggggg","ffff","iiiii",1,8))

    print (delete(4))

    print (update(121,"g","ffff","iiiii",1,8 ))

    pass
