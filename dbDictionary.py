# Базовая БД функциональность справочников
import dbCommon

def insert(tableName, newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        err, newId  = dbCommon.insert(tableName, fldList, [newName])
    else:
        newId = None
        err = "Нет данных"
    return err, newId

def delete(tableName, id):
    err = dbCommon.delete(tableName, id)
    return err

def update(tableName, id, newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        data = [newName]
        err = dbCommon.update(tableName, fldList, data, id)
    else:
        err = "Строка не найдена"
    return err

def select(tableName, flds, cond, order):
    err, data = dbCommon.select(tableName,flds,cond,order)
    return err, data

if __name__ == '__main__':
    err, idTest = insert("dept Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "dept Test new name")
        print (err)

        err = delete(idTest)
        print (err)


