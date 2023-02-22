# deparments stuff
import db

tableName = 'Departments'
pkField = 'id'

def new(newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        err, newId  = db.insert(tableName, fldList, [newName])
    else:
        newId = None
        err = "Нет данных"
    return err, newId

def delete(id):
    err = db.delete(tableName, id)
    return err

def update(id, newName):
    newName = newName.strip()
    if newName:
        fldList = ['Name']
        data = [newName]
        err = db.update(tableName, fldList, data, id)
    else:
        err = "Нет данных"
    return err


if __name__ == '__main__':
    err, idTest = new("dept Test")
    print (err, idTest)

    if idTest != None:
        err = update(idTest, "dept Test new name")
        print (err)

        err = delete(idTest)
        print (err)


