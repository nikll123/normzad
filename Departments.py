# deparments stuff
import sqlite3
import config
import db

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


def update(id, name):
    err = config.dummyErr
    with sqlite3.connect(config.dbFileName) as conn:
        cursor = conn.cursor()
        sql = f"""UPDATE {tableName} SET name=? WHERE ID=?"""
        try:
            cursor.execute(sql, [name, id])
            err = ''
        except Exception as ex: 
            err = f"SQL eror:\n   {sql}\n   {ex.args[0]}"
    return err


if __name__ == '__main__':
    while True:
        print ("выбирайте таблицу. departments - d, positions - p")
        x = input()
        x = x.strip()
        
        if x == 'd':
            while True:
                tableName = "Departments"
                print ('новая строка - n, удаленье - d, обновленье - u')
                y = input()
                y = y.strip()
                if y == 'n':
                    print (new("ttt"))
                elif y == 'd':    
                    print (delete(6))
                elif y == 'u':    
                    print (update(2, "new name"))

                break
        elif x == 'p':
            while True:
                tableName = "Positions"
                print (new("llooo"))

                print (delete(6))

                print (update(2, "new name"))

                break
        else:
            print('неправильный ввод')
            continue
              