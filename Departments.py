# deparments stuff
import sqlite3
import config
import db

tableName = "Departments"

def new(name):
    name = name.strip()
    err = config.dummyErr
    newId = None
    if name:
        with sqlite3.connect(config.dbFileName) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {tableName} (Name) VALUES (?)"""
            try:
                cursor.execute(sql, [name])
                newId = db.getLastId(cursor)
                err = ''
            except sqlite3.IntegrityError:
                err = f"Дублирование данных: '{name}'"
            except Exception as ex: 
                err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    else:
        err = "Нет данных"
    return err, newId

def delete(id):
    err = config.dummyErr
    with sqlite3.connect(config.dbFileName) as conn:
        cursor = conn.cursor()
        sql = f"""DELETE FROM {tableName} WHERE ID=?"""
        try:
            cursor.execute(sql, [id])
            err = ''
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    return err


if __name__ == '__main__':
    print (new("ttt4"))

    print (delete(6))

    pass
