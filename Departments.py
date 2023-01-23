# deparments stuff
import db

tableName = 'Departments'

def new(name):
    newId = None
    err = "Нет данных"
    name = name.strip()
    if name:
        sql = f"""INSERT INTO {tableName} (Name) VALUES (?)"""
        err, newId = db.executeTry(sql, [name])
    return err, newId


def delete(id):
    sql = f"""DELETE FROM {tableName} WHERE ID=?"""
    err, _notUsed = db.executeTry(sql, [id])
    return err


def update(id, name):
    err = "Нет данных"
    name = name.strip()
    if name:
        sql = f"""UPDATE {tableName} SET name=? WHERE ID=?"""
        err, _notUsed = db.executeTry(sql, [name, id])
    return err


if __name__ == '__main__':
    err, idTest = new("dept Test")
    print (err, idTest)

    err = update(idTest, "dept Test new name")
    print (err)

    err = delete(idTest)
    print (err)


