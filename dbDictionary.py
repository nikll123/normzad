# Базовая БД функциональность справочников
import db

def insert(tableName, newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        err, newId  = db.insert(tableName, fldList, [newName])
    else:
        newId = None
        err = "Нет данных"
    return err, newId

def delete(tableName, id):
    err = db.delete(tableName, id)
    return err

def update(tableName, id, newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        data = [newName]
        err = db.update(tableName, fldList, data, id)
    else:
        err = "Нет данных"
    return err

def select(tableName, flds, cond):
    err, data = db.select(tableName,flds,cond)
    return err, data

if __name__ == '__main__':
    err, idTest = insert("dept Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "dept Test new name")
        print (err)

        err = delete(idTest)
        print (err)


