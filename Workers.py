# workers 

import sqlite3
import config
import db

tableName = "Workers"

def new(TabelNom,LastName,Name,SecondName,PositionId,Level):
    LastName = LastName.strip()
    Name = Name.strip()
    SecondName = SecondName.strip()
    err = config.dummyErr
    
    if LastName and Name and SecondName:
        with sqlite3.connect(config.dbFileName) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {tableName} (TabelNom,LastName,Name,SecondName,PositionId,Level) VALUES (?,?,?,?,?,?)"""
            try:
                cursor.execute(sql, [TabelNom,LastName,Name,SecondName,PositionId,Level])
                err = ''
            except Exception as ex: 
                err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    else:
        err = "Нет данных"
    return err


def delete(TabelNom):
    err = config.dummyErr
    with sqlite3.connect(config.dbFileName) as conn:
        cursor = conn.cursor()
        sql = f"""DELETE FROM {tableName} WHERE TabelNom=?"""
        try:
            cursor.execute(sql, [TabelNom])
            err = ''
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    return err


def update(TabelNom,LastName,Name,SecondName,PositionId,Level):
    err = config.dummyErr
    with sqlite3.connect(config.dbFileName) as conn:
        cursor = conn.cursor()
        sql = f"""UPDATE {tableName} SET LastName = ?,Name = ?,SecondName = ?,PositionId = ?,Level = ? WHERE TabelNom = ?"""
        try:
            cursor.execute(sql, [LastName,Name,SecondName,PositionId,Level,TabelNom])
            err = ''
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    return err


if __name__ == '__main__':
    print (new(122,"ggggg","ffff","iiiii",1,8))

    print (delete(4))

    print (update(121,"g","ffff","iiiii",1,8 ))

    pass
