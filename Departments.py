# deparments stuff
import sqlite3
import config
import db

tableName = "Departments"

def New(name):
    name = name.strip()
    err = config.dummyErr
    newId = config.dummyNum
    if name:
        with sqlite3.connect(config.dbFileName) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {tableName} (Name) VALUES ("{name}")"""
            try:
                cursor.execute(sql)
                newId = db.getLastId(cursor)
                err = ''
            except sqlite3.IntegrityError:
                err = f"Дублирование данных: '{name}'"
                
    else:
        err = "Нет данных"
    return err, newId


if __name__ == '__main__':
    print (New("ttt3"))
